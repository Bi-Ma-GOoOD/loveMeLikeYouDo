from ctypes import c_void_p
import os
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import math as m
import imgui
from imgui.integrations.glfw import GlfwRenderer
from gl_helpers_exercise import *

model_rotate, up_dir = [0, 0, 0], np.array((0, 1, 0))
I, light_pos, eye_pos, eye_at = [1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]
fog_on, fog_start, fog_end, fog_color = False, 1, 30, [0.95, 0.95, 0.95]
Kd1, Kd2, Ks = [0.85, 0.7, 0.13], [0.45, 0.35, 0.05], [0.9, 0.6, 0.2]
edge_color = [0, 0, 0.5]
diffuse_threshold, specular_threshold, edge_threshold = 0.5, 0.3, 0.3
scene_vao, shininess, clear_color = None, 50, [0.8, 1.0, 1.0]
wireframe_on, animation_on, gui_on = False, False, True

def draw_gui():
    global clear_color, I, Kd1, Kd2, Ks, edge_color, shininess
    global diffuse_threshold, specular_threshold, edge_threshold
    global fog_on, fog_start, fog_end, fog_color

    impl.process_inputs()
    imgui.new_frame()                 # Start the Dear ImGui frame 
    imgui.set_next_window_position(win_w-300, 10, imgui.FIRST_USE_EVER)
    imgui.begin("Control")            # Create a window
    imgui.push_item_width(100)
    imgui.text("Linear Fog")
    _, fog_on = imgui.checkbox("Enabled", fog_on)
    imgui.same_line()
    _, fog_start = imgui.slider_float("Start", fog_start, 0.0, 10)
    imgui.same_line()
    _, fog_end = imgui.slider_float("End", fog_end, 0.0, 50)
    if fog_start > fog_end: fog_end = fog_start + 1
    imgui.pop_item_width()
    imgui.push_item_width(200)
    _, fog_color = imgui.color_edit3("Fog Color", *fog_color)    
    _, I = imgui.color_edit3("Light Intensity", *I)
    _, Kd1 = imgui.color_edit3("Kd1", *Kd1)
    _, Kd2 = imgui.color_edit3("Kd2", *Kd2)    
    _, Ks = imgui.color_edit3("Ks", *Ks) 
    _, edge_color = imgui.color_edit3("Edge Color", *edge_color) 
    _, diffuse_threshold = imgui.slider_float("Diffuse Threshold", diffuse_threshold, 
                                              0.0, 1.0)
    _, specular_threshold = imgui.slider_float("Specular Threshold", specular_threshold, 
                                              0.0, 1.0)
    _, edge_threshold = imgui.slider_float("Edge Threshold", edge_threshold, 
                                              0.0, 1.0)
    _, clear_color = imgui.color_edit3("Clear Color", *clear_color)    
    imgui.pop_item_width()

    imgui.text("Application average %.3f ms/frame (%.1f FPS)" % \
        (1000 / imgui.get_io().framerate, imgui.get_io().framerate))
    imgui.end()

def resize(window, w, h):
    global win_w, win_h, proj_mat

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    proj_mat = Perspective(45, w/h, 0.01, 40)

def refresh(window):
    glClearColor(*clear_color, 0)    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view_mat = LookAt(*eye_pos, *eye_at, 0, 1, 0)
    model_mat = Rotate(model_rotate[0], 1, 0, 0) @ Rotate(model_rotate[1], 0, 1, 0)

    glUseProgram(prog_id)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "model_mat"), 1, GL_TRUE, model_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "view_mat"), 1, GL_TRUE, view_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "proj_mat"), 1, GL_TRUE, proj_mat)
    glUniform3fv(glGetUniformLocation(prog_id, "Kd1"), 1, Kd1)
    glUniform3fv(glGetUniformLocation(prog_id, "Kd2"), 1, Kd2)
    glUniform3fv(glGetUniformLocation(prog_id, "Ks"), 1, Ks)
    glUniform3fv(glGetUniformLocation(prog_id, "edge_color"), 1, edge_color)    
    glUniform3fv(glGetUniformLocation(prog_id, "I"), 1, I)
    glUniform1f(glGetUniformLocation(prog_id, "shininess"), shininess)
    glUniform3fv(glGetUniformLocation(prog_id, "light_pos"), 1, light_pos)
    glUniform3fv(glGetUniformLocation(prog_id, "eye_pos"), 1, eye_pos)
    glUniform1f(glGetUniformLocation(prog_id, "diffuse_threshold"), diffuse_threshold)
    glUniform1f(glGetUniformLocation(prog_id, "specular_threshold"), specular_threshold)
    glUniform1f(glGetUniformLocation(prog_id, "edge_threshold"), edge_threshold)
    glUniform1i(glGetUniformLocation(prog_id, "fog_on"), fog_on)    
    glUniform1f(glGetUniformLocation(prog_id, "fog_start"), fog_start)
    glUniform1f(glGetUniformLocation(prog_id, "fog_end"), fog_end)        
    glUniform3fv(glGetUniformLocation(prog_id, "fog_color"), 1, fog_color)     

    glBindVertexArray(scene_vao)
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)

    if gui_on:
        draw_gui()
        imgui.render()
        impl.render(imgui.get_draw_data())

    glfwSwapBuffers(window)

def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on, gui_on

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
        elif key == GLFW_KEY_G:
            gui_on = not gui_on            
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key in (GLFW_KEY_UP, GLFW_KEY_DOWN, GLFW_KEY_LEFT, GLFW_KEY_RIGHT):
            dx, dy, key_scale = 0, 0, 0.25
            if key == GLFW_KEY_LEFT:
                dx = -1
            elif key == GLFW_KEY_RIGHT:
                dx = 1
            elif key == GLFW_KEY_UP:
                dy = 1
            elif key == GLFW_KEY_DOWN:
                dy = -1
            eye_dir = normalize(eye_at - eye_pos)
            left_dir = np.cross(eye_dir, up_dir)
            if mods & GLFW_MOD_CONTROL:
                eye_pos[:] += dy*key_scale*eye_dir
                eye_at[:] += dy*key_scale*eye_dir
            else:
                eye_pos[:] += dx*key_scale*left_dir
                eye_at[:] += dx*key_scale*left_dir
                eye_pos[:] += dy*key_scale*up_dir
                eye_at[:] += dy*key_scale*up_dir            
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)
    glfwPostEmptyEvent()

def animation(window):
    model_rotate[1] += 0.1

mouse_x, mouse_y, mouse_button, mouse_action = 0, 0, 0, 0
def mouse_func(window, button, action, mods):
    global mouse_x, mouse_y, mouse_button, mouse_action

    mouse_x, mouse_y = glfwGetCursorPos(window)
    mouse_button, mouse_action = button, action
        
def cursor_func(window, x, y):
    global mouse_x, mouse_y

    if impl.io.want_capture_mouse:
        return      
    dx, dy = x - mouse_x, mouse_y - y 
    if mouse_button == GLFW_MOUSE_BUTTON_LEFT and mouse_action == GLFW_PRESS:
        model_rotate[1] += 0.05*dx
        model_rotate[0] -= 0.05*dy
    mouse_x, mouse_y = x, y

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
    global prog_id, scene_vao, n_vertices
    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global eye_pos, light_pos

    vert_code = '''
#version 140
in vec3 position, color, normal;
in vec2 uv;

uniform mat4 model_mat, view_mat, proj_mat;

out vec3 smooth_position, smooth_color, smooth_normal;
out float smooth_distance;

void main() 
{
    gl_Position = proj_mat* view_mat * model_mat * vec4(position, 1);
    smooth_position = (model_mat * vec4(position, 1)).xyz;
    mat4 normal_mat = transpose(inverse(model_mat));
    smooth_normal = (normal_mat * vec4(normal, 0)).xyz;
    smooth_color = color;
    smooth_distance = abs((view_mat * model_mat * vec4(position, 1)).z);
}
'''
    frag_code = '''
#version 130
in vec3 smooth_position, smooth_color, smooth_normal;
in float smooth_distance;

uniform vec3 Kd1, Kd2, Ks, edge_color, fog_color, I, light_pos, eye_pos;
uniform float shininess, fog_start, fog_end;
uniform float diffuse_threshold, specular_threshold, edge_threshold;
uniform bool fog_on;

out vec4 frag_color;

void main() 
{
    vec3 L = normalize(light_pos - smooth_position);
    vec3 V = normalize(eye_pos - smooth_position);
    vec3 N = normalize(smooth_normal);
    vec3 R = 2 * dot(L, N) * N - L;
    
    float diffuse = max(dot(N, L), 0);
    float specular = pow(max(dot(R, V), 0), shininess);
    float edge = max(dot(N, V), 0);
    
    vec3 diffuse_color = (diffuse > diffuse_threshold) ? Kd1 : Kd2;
    vec3 specular_color = (specular > specular_threshold) ? Ks : vec3(0);
    
    edge = (edge < edge_threshold) ? 1.0 : 0.0;
    
    vec3 shade_toon_color = vec4(mix(diffuse_color + specular_color, edge_color, edge), 1).xyz;
    
    if (fog_on){
        float fog_scale = 1.0 - (fog_end - smooth_distance)/(fog_end - fog_start);
        fog_scale = clamp(fog_scale, 0.0, 0.95);
        frag_color = mix(vec4(shade_toon_color, 1), vec4(fog_color, 1), fog_scale);
    }else{
        frag_color = vec4(shade_toon_color, 1);
    }
}
'''
    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vert_code)
    glShaderSource(frag_id, frag_code)

    glCompileShader(vert_id)
    print_shader_info_log(vert_id, "Vertex Shader")
    glCompileShader(frag_id)
    print_shader_info_log(frag_id, "Fragment Shader")

    prog_id = glCreateProgram()
    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    print_program_info_log(prog_id, "Link Error")

    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global light_pos, eye_pos

    df = pd.read_csv("3rdYears\\Y3T1\\ICG\\models\\objects_and_floor.tri", sep='\s+', comment='#',
                     header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)
    eye_pos = centroid + (0, 2, 10)
    light_pos = eye_pos

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)

    glUseProgram(prog_id)
    scene_vao = glGenVertexArrays(1)
    glBindVertexArray(scene_vao)
    vbo = glGenBuffers(4)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    position_loc = glGetAttribLocation(prog_id, "position")
    glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
    glEnableVertexAttribArray(position_loc)
    
    color_loc = glGetAttribLocation(prog_id, "color")
    if color_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
        glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)
        glVertexAttribPointer(color_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(color_loc)
    
    normal_loc = glGetAttribLocation(prog_id, "normal")
    if normal_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[2])
        glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
        glVertexAttribPointer(normal_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(normal_loc)
    
    uv_loc = glGetAttribLocation(prog_id, "uv")
    if uv_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[3])
        glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
        glVertexAttribPointer(uv_loc, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(uv_loc)      

def initialize():
    global impl

    glEnable(GL_DEPTH_TEST)
    imgui.create_context()
    imgui.style_colors_dark()
    impl = GlfwRenderer(window, attach_callbacks=False)
    imgui.set_next_window_position(500, 10)
    imgui.set_next_window_collapsed(True)
    
def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Toon Shading in Fog Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetMouseButtonCallback(window, mouse_func)
    glfwSetCursorPosCallback(window, cursor_func)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, 1024, 768)

    initialize()
    create_shaders()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        glfwPollEvents()
        refresh(window)
    impl.shutdown()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()    