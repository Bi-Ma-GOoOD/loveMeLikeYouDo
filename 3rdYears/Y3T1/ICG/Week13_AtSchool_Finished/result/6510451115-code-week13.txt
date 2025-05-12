import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
from numpy.linalg import norm
from PIL import Image
from ctypes import c_void_p
import imgui
from imgui.integrations.glfw import GlfwRenderer
import pandas as pd
from gl_helpers_exercise import *

mouse_status = {'x': 0, 'y': 0, 
                GLFW_MOUSE_BUTTON_LEFT: GLFW_RELEASE, 
                GLFW_MOUSE_BUTTON_MIDDLE: GLFW_RELEASE,
                GLFW_MOUSE_BUTTON_RIGHT: GLFW_RELEASE}
special_keys = { GLFW_MOD_SHIFT: False, GLFW_MOD_CONTROL: False,
                 GLFW_MOD_ALT: False }
view_translate, view_rotate = [0, 0, 0], [0, 0, 0]
model_rotate, clear_color = [0, 0, 0], [0.1, 0.6, 0.6]
proj_mat, model_mat, view_mat = Identity(), Identity(), Identity()
type_selections = ("Reflection", "Refraction", "Fresnel")
type_selected, refract_index = 0, 1.00
impl, vao = None, None

def draw_gui():
    global clear_color, type_selected, refract_index
    
    impl.process_inputs()
    imgui.new_frame()                    # Start the Dear ImGui frame   
    imgui.begin("Control")               # Create a window
    imgui.push_item_width(300)
    imgui.text("View Translate")
    imgui.push_item_width(100)
    _, view_translate[0] = imgui.slider_float("X###vt_x", view_translate[0], -50, 50)
    imgui.same_line()
    _, view_translate[1] = imgui.slider_float("Y###vt_y", view_translate[1], -50, 50)
    imgui.same_line()
    _, view_translate[2] = imgui.slider_float("Z###vt_z", view_translate[2], -50, 50)
    imgui.text("View Rotate")
    _, view_rotate[0] = imgui.slider_float("X###vr_x", view_rotate[0], -360, 360)
    imgui.same_line()
    _, view_rotate[1] = imgui.slider_float("Y###vr_y", view_rotate[1], -360, 360)
    imgui.same_line()
    _, view_rotate[2] = imgui.slider_float("Z###vr_z", view_rotate[2], -360, 360)
    imgui.text("Model Rotation")
    _, model_rotate[0] = imgui.slider_float("X###mr_x", model_rotate[0], -180, 180)
    imgui.same_line()
    _, model_rotate[1] = imgui.slider_float("Y###mr_y", model_rotate[1], -180, 180)
    imgui.same_line()
    _, model_rotate[2] = imgui.slider_float("Z###mr_z", model_rotate[2], -180, 180)    
    imgui.pop_item_width()
    imgui.text("Mapping Types")
    imgui.push_item_width(60)
    for n, name in enumerate(type_selections):
        if imgui.radio_button(name, type_selected == n):
            type_selected = n
        if n < len(type_selections)-1: imgui.same_line()
    # print(type_selected)
    imgui.pop_item_width()
    imgui.push_item_width(100)
    _, refract_index = imgui.slider_float("Refraction Index", refract_index, 0.8, 3)
    imgui.pop_item_width()
    imgui.text("Background Color")
    _, clear_color = imgui.color_edit3("Clear Color", *clear_color)

    imgui.text("Application average %.3f ms/frame (%.1f FPS)" % \
        (1000 / imgui.get_io().framerate, imgui.get_io().framerate))
    imgui.pop_item_width()
    imgui.end()

def drawCube():
    cube_size = 150
    cube = [[ 1, -1, -1], [1, 1, -1], [1, 1, 1], [1, -1, 1],
            [-1, -1, -1], [-1, 1, -1], [-1, 1, 1], [-1, -1, 1],
            [-1, 1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1],
            [-1, -1, -1], [1, -1, -1], [1, -1, 1], [-1, -1, 1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1]]
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixf(proj_mat.T)
    glMatrixMode(GL_MODELVIEW)
    cubeview_mat = view_mat @ Scale(cube_size, cube_size, cube_size)
    glLoadMatrixf(cubeview_mat.T)
    glBegin(GL_QUADS)
    for i in range(24):
        glTexCoord3fv(cube[i])
        glVertex3fv(cube[i])
    glEnd()

def resize(window, w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    proj_mat[:] = Perspective(45., w/h, 0.01, 500.0)

def refresh(window):
    view_mat[:] = Translate(*view_translate)
    view_mat[:] = view_mat @ LookAt(*eye_pos, *eye_at, 0, 1, 0)
    view_mat[:] = view_mat @ Translate(*eye_at) @ \
                  Rotate(view_rotate[0], 1, 0, 0) @ \
                  Rotate(view_rotate[1], 0, 1, 0) @ \
                  Rotate(view_rotate[2], 0, 0, 1) @ \
                  Translate(*(-eye_at))
    model_mat[:] = Rotate(model_rotate[0], 1, 0, 0) @ \
                   Rotate(model_rotate[1], 0, 1, 0) @ \
                   Rotate(model_rotate[2], 0, 0, 1)

    glClearColor(*clear_color, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUseProgram(prog_id)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "model_mat"), 1, True, model_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "view_mat"), 1, True, view_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "proj_mat"), 1, True, proj_mat)
    glUniform1f(glGetUniformLocation(prog_id, "refract_index"), refract_index)
    glUniform1i(glGetUniformLocation(prog_id, "type_selected"), type_selected)
    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)

    glUseProgram(0)
    glDisable(GL_TEXTURE_2D)
    drawCube()
    glEnable(GL_TEXTURE_2D)

    draw_gui()
    imgui.render()
    impl.render(imgui.get_draw_data())

    glfwSwapBuffers(window)

def keyboard(window, key, scancode, action, mods):
    global wireframe, multisample, show_normals, culling, spinning, gui
    
    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)

def mouse_func(window, button, action, mods):
    mouse_status['x'], mouse_status['y'] = glfwGetCursorPos(window)
    mouse_status[button] = action
    for k in special_keys.keys():
        special_keys[k] = (mods & k) == k

def cursor_func(window, x, y):
    if impl.io.want_capture_mouse:
        return
        
    dx, dy = x-mouse_status['x'], mouse_status['y']-y 
    pass

def scroll_func(window, dx, dy):
    view_translate[2] += 5.0*dy

def printShaderInfoLog(shader, prompt=""):
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetShaderInfoLog(shader).decode("utf-8")))
        return -1
    else:
        return 0

def printProgramInfoLog(program, prompt=""):
    result = glGetProgramiv(program, GL_LINK_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetProgramInfoLog(program).decode("utf-8")))
        return -1
    else:
        return 0

def create_program():
    global prog_id, vao, n_vertices, bbox, eye_pos, eye_at

    vertex_code = '''
#version 330 core
in vec3 position, normal, color;
in vec2 uv;

uniform mat4 model_mat, view_mat, proj_mat;

out vec3 smooth_position, smooth_normal;

void main() 
{   
    mat4 MVP = proj_mat * view_mat * model_mat;
    gl_Position = MVP * vec4(position, 1);
    smooth_position = (model_mat * vec4(position, 1)).xyz;
    smooth_normal = (transpose(inverse(model_mat)) * vec4(normal, 0)).xyz;
}
'''
    fragment_code = '''
#version 150
in vec3 smooth_position, smooth_normal;

uniform mat4 model_mat, view_mat;
uniform float refract_index;
uniform samplerCube cube_map;
uniform int type_selected;

out vec4 frag_color;

vec3 result = vec3(0, 0, 0);
float bias = 0.1;
float scale = 2.0;
float power = 3.0;

void main()
{
    vec3 eye_pos = (inverse(view_mat) * vec4(0, 0, 0, 1)).xyz;
    vec3 N = normalize(smooth_normal);
    mat4 normal_mat = transpose(inverse(model_mat));
    N = normalize((normal_mat * vec4(N, 0)).xyz);
    vec3 I = normalize(smooth_position - eye_pos);
    
    // Calculate reflection direction
    vec3 reflect_dir = reflect(I, N);
    vec3 reflect_color = texture(cube_map, reflect_dir).rgb;
    
    // Calculate refract direction
    float eta = 1/refract_index;
    vec3 refract_dir = refract(I, N, eta);
    vec3 refract_color = texture(cube_map, refract_dir).rgb;

    // Calculate fresnel
    float reflectionCoef = max(0, min(1, bias + scale * pow(1 + dot(I, N), power)));
    vec3 fresnel_color = reflectionCoef * reflect_color + ((1 - reflectionCoef) * refract_color);

    if(type_selected == 0){
        frag_color.rgb = reflect_color;
    }else if(type_selected == 1){
        frag_color.rgb = refract_color;
    }else if(type_selected == 2){
        frag_color.rgb = fresnel_color;
    }
}
'''
    prog_id = glCreateProgram()

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vert_id, vertex_code)
    glCompileShader(vert_id)
    printShaderInfoLog(vert_id, "Vertex Shader")

    frag_id = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(frag_id, fragment_code)
    glCompileShader(frag_id)
    printShaderInfoLog(frag_id, "Fragment Shader")

    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    printProgramInfoLog(prog_id, "Link Error")

    df = pd.read_csv("C:\\6510451115-ICG\\models\\alien.tri", sep='\s+',
                     comment='#', header=None, dtype=np.float32)
    if df.values.shape[1] == 11:
        positions = df.values[:, 0:3]
        colors = df.values[:, 3:6]
        normals = df.values[:, 6:9]
        uvs = df.values[:, 9:11]
    else:
        positions = df.values[:, 0:3]
        colors = normals = df.values[:, 3:6]
        uvs = df.values[:, 6:8]
    n_vertices = len(positions)

    bbox = positions.max(axis=0) - positions.min(axis=0)
    centroid = positions.min(axis=0) + 0.5*bbox
    eye_pos = centroid + (0, 0, 1.5*max(bbox)) + (0.5, 0, 0)
    eye_at = centroid + (0.5, 0, 0)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    vbo = glGenBuffers(4)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    position_loc = glGetAttribLocation(prog_id, "position")
    glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, 
        c_void_p(0))
    glEnableVertexAttribArray(position_loc)
    color_loc = glGetAttribLocation(prog_id, "color")
    if color_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
        glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)
        glVertexAttribPointer(color_loc, 3, GL_FLOAT, GL_FALSE, 0, 
            c_void_p(0))
        glEnableVertexAttribArray(color_loc)    
    normal_loc = glGetAttribLocation(prog_id, "normal")
    if normal_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[2])
        glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
        glVertexAttribPointer(normal_loc, 3, GL_FLOAT, GL_FALSE, 0, 
            c_void_p(0))
        glEnableVertexAttribArray(normal_loc)
    uv_loc = glGetAttribLocation(prog_id, "uv")
    if uv_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[3])
        glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
        glVertexAttribPointer(uv_loc, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(uv_loc)

    glUseProgram(prog_id)
    glUniform1i(glGetUniformLocation(prog_id, "cube_map"), 0)
    glUniform1i(glGetUniformLocation(prog_id, "normal_map"), 1)

def initialize():
    global impl

    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)

    imgui.create_context()
    imgui.style_colors_dark()
    impl = GlfwRenderer(window, attach_callbacks=False)
    imgui.set_next_window_position(500, 10)
    imgui.set_next_window_collapsed(True)

def load_texture_map(filename, active_texture_unit):
    im = Image.open(filename)
    w, h = im.size
    image = im.tobytes("raw", im.mode, 0)
    tex_id = glGenTextures(1)
    glActiveTexture(active_texture_unit)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glGenerateMipmap(GL_TEXTURE_2D)
    glTextureParameteri(tex_id, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTextureParameteri(tex_id, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTextureParameteri(tex_id, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTextureParameteri(tex_id, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return active_texture_unit - GL_TEXTURE0

def load_cube_map(filename=None, active_texture_unit=GL_TEXTURE0):
    im = Image.open(filename)
    # Fix me!
    w, h = im.size
    sub_w = w//4
    sub_h = h//3
    box = [[2,1], [0,1], [1,0], [1,2], [1,1], [3,1]]
    tex_id = glGenTextures(1)
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    for i in range(6):
        image = im.crop((box[i][0] * sub_w, box[i][1] * sub_h, (box[i][0] + 1) * sub_w, (box[i][1] + 1) * sub_h)).tobytes("raw", "RGB", 0)
        glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGB, sub_h, sub_w, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
               
    glGenerateMipmap(GL_TEXTURE_CUBE_MAP)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glEnable(GL_TEXTURE_CUBE_MAP)
    return active_texture_unit-GL_TEXTURE0
 
def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Cube Mapping Exercise",
                              None, None)
    glfwMakeContextCurrent(window)
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetMouseButtonCallback(window, mouse_func)
    glfwSetCursorPosCallback(window, cursor_func)
    glfwSetScrollCallback(window, scroll_func)    
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, 1024, 768)

    initialize()
    load_cube_map("C:\\6510451115-ICG\\Week13\\cube_map\\roundabout_HCmap.jpg", GL_TEXTURE0)    
    load_texture_map("C:\\6510451115-ICG\\Week13\\normal_map\\normal_map5.jpg", GL_TEXTURE1)
    create_program()

    while not glfwWindowShouldClose(window):
        glfwPollEvents()
        refresh(window)

    impl.shutdown()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()