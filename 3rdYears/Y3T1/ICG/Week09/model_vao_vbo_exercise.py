import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import time
from ctypes import c_void_p
import imgui
from imgui.integrations.glfw import GlfwRenderer

win_w, win_h = 1024, 768
impl = None
Kd1 = [0.86, 0.86, 0.4]
Kd2 = [0.5, 0.25, 0.38]
light_pos = [0.0, 0.0, 0.0]

def print_shader_info_log(shader, prompt=""):
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetShaderInfoLog(shader).decode("utf-8")))
        os._exit(1)

def print_program_info_log(shader, prompt=""):
    result = glGetProgramiv(shader, GL_LINK_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetProgramInfoLog(shader).decode("utf-8")))
        os._exit(1)

def create_shaders():
    global prog_id
    global vao, vbo

    vert_code = '''
#version 130
uniform vec3 light_position;
uniform vec3 Kd1, Kd2;

in vec3 position, normal;
in vec2 uv;

out vec3 sent_position, sent_normal;
out vec2 sent_uv;
out vec3 smooth_color;

void main()
{
    mat4 MVP = mat4(1.81,    0,    0,    0,      
                       0,  2.41,    0,    0,      
                       0,     0,   -1,   -1,    
                    -1.0, -6.34, 8.14, 8.15);

   gl_Position = MVP * vec4(position,1);
   sent_normal = normal;
   sent_uv = uv;

   vec3 L = normalize(light_position - position);
   if (position.x < 0){
        smooth_color = Kd1 * max(dot(L, normal), 0);
   }else {
        smooth_color = Kd2 * max(dot(L, normal), 0);
   }
}'''
    frag_code = '''
#version 130
in vec3 sent_position, sent_normal;
in vec2 sent_uv;
in vec3 smooth_color;

out vec4 fragment_color;

void main()
{
   fragment_color = vec4(smooth_color,1);
}'''
    prog_id = glCreateProgram()

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vert_code)
    glShaderSource(frag_id, frag_code)

    glCompileShader(vert_id)
    glCompileShader(frag_id)
    print_shader_info_log(vert_id, "Vertex Shader")
    print_shader_info_log(frag_id, "Fragment Shader")

    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    print_program_info_log(prog_id, "Link error")

    # Fix me!
    # Implement VAO and VBO here.
    glUseProgram(prog_id)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    vbo = glGenBuffers(3)

    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    position_loc = glGetAttribLocation(prog_id, "position")
    if position_loc != -1:
        glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(position_loc)

    normal_loc = glGetAttribLocation(prog_id, "normal")
    glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
    glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
    if normal_loc != -1:
        glVertexAttribPointer(normal_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(normal_loc)

    uv_loc = glGetAttribLocation(prog_id, "uv")
    glBindBuffer(GL_ARRAY_BUFFER, vbo[2])
    glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
    if uv_loc != -1:
        glVertexAttribPointer(uv_loc, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(uv_loc)


def draw_gui():
    global Kd1, Kd2, light_position

    impl.process_inputs()
    imgui.new_frame()                 # Start the Dear ImGui frame 
    imgui.begin("Control")            # Create a window
    _, Kd1 = imgui.color_edit3("Kd1", *Kd1)
    _, Kd2 = imgui.color_edit3("Kd2", *Kd2)
    imgui.text("Light Position")
    imgui.push_item_width(100)
    _, light_pos[0] = imgui.slider_float("X###light_pos_x", light_pos[0], -10, 10)
    imgui.same_line()
    _, light_pos[1] = imgui.slider_float("Y###light_pos_y", light_pos[1], -10, 10)
    imgui.same_line()
    _, light_pos[2] = imgui.slider_float("Z###light_pos_z", light_pos[2], -10, 10)

    imgui.text("Application average %.3f ms/frame (%.1f FPS)" % \
        (1000 / imgui.get_io().framerate, imgui.get_io().framerate))
    imgui.end()

wireframe_on, animation_on = False, True
def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on, texture_func

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on        
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)
    glfwPostEmptyEvent()

def resize(window, w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w/win_h, 0.01, 20)

def refresh(window):
    global start_time, frame_cnt
    if frame_cnt == 20:
        print("%.2f fps" % (frame_cnt/(time.time()-start_time)), end='\r')
        start_time = time.time()
        frame_cnt = 0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*eye_pos, *centroid, 0, 1, 0)

    glUseProgram(prog_id)

    Kd1_location = glGetUniformLocation(prog_id, "Kd1")
    Kd2_location = glGetUniformLocation(prog_id, "Kd2")
    light_location = glGetUniformLocation(prog_id, "light_position")

    glUniform3fv(Kd1_location, 1, Kd1)
    glUniform3fv(Kd2_location, 1, Kd2)
    glUniform3fv(light_location, 1, light_pos)
    
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)
    draw_gui()
    imgui.render()
    impl.render(imgui.get_draw_data())
        
    glfwSwapBuffers(window)

frame_cnt = 0
def animation(window):
    global frame_cnt

    frame_cnt += 1

def init_model():
    global n_vertices, positions, normals, uvs, centroid, bbox, eye_pos
    global impl, start_time

    glClearColor(0.01, 0.01, 0.2, 1)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    imgui.create_context()
    imgui.style_colors_dark()
    impl = GlfwRenderer(window, attach_callbacks=False)
    imgui.set_next_window_position(500, 10)
    imgui.set_next_window_collapsed(True)

    df = pd.read_csv("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\models\\armadillo.tri", sep='\s+',   
                     comment='#', header=None, dtype=np.float32)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)
    centroid = df.values[:, 0:3].min(axis=0) + 0.5*bbox + (0.5, 0, 0)
    eye_pos = centroid + (0, 0, 8)

    positions = df.values[:, 0:3]
    normals = df.values[:, 3:6]
    uvs = df.values[:, 6:8]

    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % 
          (n_vertices, n_vertices//3))
    print("Centroid:", centroid)
    print("BBox:", bbox)
    start_time = time.time() - 1e-4
    # create_shaders()

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "VAO and VBO Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    init_model()
    create_shaders()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        glfwWaitEvents()
        refresh(window)
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()