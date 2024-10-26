import os
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import imgui
from imgui.integrations.glfw import GlfwRenderer
from gl_helpers_exercise import *
from ctypes import c_void_p

impl, vao = None, None
win_w, win_h = 1280, 800
shininess = 50
Ka, Kd, Ks, clear_color = [0.05, 0.05, 0.05], [0.5, 1.0, 0.2], [0.9, 0.9, 0.9], [0.1, 0.6, 0.6]
light_intensity, light_pos, eye_pos, eye_at = [1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0]
model_rotation = [0, 0, 0]
specular_on, selection = True, False

def draw_gui():
    global selection, light_intensity, Ka, Kd, Ks, shininess, specular_on, clear_color
    impl.process_inputs()
    imgui.new_frame()                    # Start the Dear ImGui frame   
    imgui.begin("Control")               # Create a window
    imgui.push_item_width(300)
    _, light_intensity = imgui.color_edit3("Light Intensity", *light_intensity)
    _, Ka = imgui.color_edit3("Ka", *Ka)
    _, Kd = imgui.color_edit3("Kd", *Kd)
    _, Ks = imgui.color_edit3("Ks", *Ks)
    _, shininess = imgui.slider_float("Shininess", shininess, 0.1, 180)
    if imgui.radio_button("Per-Vertex (Gouraud Shading)", not selection): 
        selection = False
    if imgui.radio_button("Per-Fragment (Phong Shading)", selection): 
        selection = True    
    imgui.text("Light Position")
    imgui.push_item_width(100)
    _, light_pos[0] = imgui.slider_float("X###light_pos_x", light_pos[0], -10, 10)
    imgui.same_line()
    _, light_pos[1] = imgui.slider_float("Y###light_pos_y", light_pos[1], -10, 10)
    imgui.same_line()
    _, light_pos[2] = imgui.slider_float("Z###light_pos_z", light_pos[2], -10, 10)
    imgui.text("Eye Position")
    _, eye_pos[0] = imgui.slider_float("X###eye_pos_x", eye_pos[0], -3, 3)
    imgui.same_line()
    _, eye_pos[1] = imgui.slider_float("Y###eye_pos_y", eye_pos[1], -3, 3)
    imgui.same_line()
    _, eye_pos[2] = imgui.slider_float("Z###eye_pos_z", eye_pos[2], -3, 3)
    imgui.text("Eye At")
    _, eye_at[0] = imgui.slider_float("X###eye_at_x", eye_at[0], -3, 3)
    imgui.same_line()
    _, eye_at[1] = imgui.slider_float("Y###eye_at_y", eye_at[1], -3, 3)
    imgui.same_line()
    _, eye_at[2] = imgui.slider_float("Z###eye_at_z", eye_at[2], -3, 3)
    imgui.text("Model Rotation about (X, Y, Z) Axis")
    _, model_rotation[0] = imgui.slider_float("X###about X", model_rotation[0], -180, 180)
    imgui.same_line()
    _, model_rotation[1] = imgui.slider_float("Y###about Y", model_rotation[1], -180, 180)
    imgui.same_line()
    _, model_rotation[2] = imgui.slider_float("Z###about Z", model_rotation[2], -180, 180)    
    imgui.pop_item_width()
    imgui.text("Background Color")
    _, clear_color = imgui.color_edit3("Clear Color", *clear_color)

    imgui.text("Application average %.3f ms/frame (%.1f FPS)" % \
        (1000 / imgui.get_io().framerate, imgui.get_io().framerate))
    imgui.pop_item_width()
    imgui.end()

def resize(window, w, h):
    global win_w, win_h, proj_mat

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    proj_mat = Perspective(60, w/h, 0.1, 10)
    
def refresh(window):
    glClearColor(*clear_color, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    model_mat = Rotate(model_rotation[0], 1, 0, 0) @ \
                Rotate(model_rotation[1], 0, 1, 0) @ \
                Rotate(model_rotation[2], 0, 0, 1)
    view_mat = LookAt(*eye_pos, *eye_at, 0, 1, 0)

    if selection == False:
        prog_id = g_prog_id
    else:
        prog_id = p_prog_id

    glUseProgram(prog_id)        
    glUniformMatrix4fv(glGetUniformLocation(prog_id, 'model_mat'), 1, GL_TRUE, model_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, 'view_mat'), 1, GL_TRUE, view_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, 'proj_mat'), 1, GL_TRUE, proj_mat)
    glUniform3fv(glGetUniformLocation(prog_id, 'light_intensity'), 1, light_intensity)
    glUniform3fv(glGetUniformLocation(prog_id, 'light_pos'), 1, light_pos)
    glUniform3fv(glGetUniformLocation(prog_id, 'eye_pos'), 1, eye_pos)
    glUniform3fv(glGetUniformLocation(prog_id, 'Ka'), 1, Ka)
    glUniform3fv(glGetUniformLocation(prog_id, 'Kd'), 1, Kd)
    glUniform3fv(glGetUniformLocation(prog_id, 'Ks'), 1, Ks)
    glUniform1f(glGetUniformLocation(prog_id, 'shininess'), shininess) 

    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)

    draw_gui()
    imgui.render()
    impl.render(imgui.get_draw_data())

    glfwSwapBuffers(window)

wireframe_on = False
def keyboard(window, key, scancode, action, mods):
    global wireframe_on

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)
    glfwPostEmptyEvent()

def initialize():
    global impl

    glEnable(GL_DEPTH_TEST)
    imgui.create_context()
    imgui.style_colors_dark()
    impl = GlfwRenderer(window, attach_callbacks=False)
    imgui.set_next_window_position(500, 10)
    imgui.set_next_window_collapsed(True)

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

def compile_shaders(vert_code, frag_code, program_prompt=""):
    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vert_code)
    glShaderSource(frag_id, frag_code)

    glCompileShader(vert_id)
    glCompileShader(frag_id)
    print_shader_info_log(vert_id, program_prompt + " Vertex Shader")
    print_shader_info_log(frag_id, program_prompt + " Fragment Shader")

    prog_id = glCreateProgram()
    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    print_program_info_log(prog_id, program_prompt + " Link Error")
    return prog_id

def create_shaders():
    global g_prog_id, p_prog_id, vao

    g_vert_code = '''
#version 330
layout(location = 0) in vec3 position; 
layout(location = 1) in vec3 normal;
layout(location = 2) in vec3 color; 
layout(location = 3) in vec2 uv;

uniform mat4 model_mat, view_mat, proj_mat;
uniform vec3 light_intensity;
uniform vec3 light_pos;
uniform vec3 Ka, Kd, Ks;
uniform float shininess;
uniform vec3 eye_pos;

out vec3 vertex_color;

void main()
{
    gl_Position = proj_mat * view_mat * model_mat * vec4(position, 1);

    vec3 P = (model_mat * vec4(position, 1)).xyz;
    vec3 L = normalize(light_pos - P);
    vec3 V = normalize(eye_pos - P);
    vec3 N = (transpose(inverse(model_mat)) * vec4(normal, 0)).xyz;
    vec3 R = 2 * dot(L, N) * N - L;

    vec3 ambient = Ka * light_intensity;
    vec3 diffuse = Kd * max(dot(N, L), 0) * light_intensity;
    vec3 specular = Ks * pow(max(dot(V, R), 0), shininess) * light_intensity;

    if (dot(N, L) < 0){
        specular = vec3(0, 0, 0);    
    }

    vertex_color = ambient + diffuse + specular;
}'''
    g_frag_code = '''
#version 140
in vec3 vertex_color;

void main()
{
    gl_FragColor.rgb = vertex_color;
}'''

    g_prog_id = compile_shaders(g_vert_code, g_frag_code, "Gouraud")

    p_vert_code = '''
#version 330
layout(location = 0) in vec3 position; 
layout(location = 1) in vec3 normal;
layout(location = 2) in vec3 color; 
layout(location = 3) in vec2 uv;

uniform mat4 model_mat, view_mat, proj_mat;
uniform vec3 eye_pos;
uniform vec3 light_intensity;

out vec3 smooth_position;
out vec3 smooth_normal, smooth_light_intensity, smooth_eye_pos;

void main()
{
    gl_Position = proj_mat * view_mat * model_mat * vec4(position, 1);
    smooth_position = (model_mat * vec4(position, 1)).xyz;
    smooth_normal = (transpose(inverse(model_mat)) * vec4(normal, 0)).xyz;
    smooth_light_intensity = (model_mat * vec4(light_intensity, 1)).xyz;
    smooth_eye_pos = (model_mat * vec4(eye_pos, 1)).xyz;
}'''
    p_frag_code = '''
#version 140
uniform vec3 light_intensity;
uniform vec3 light_pos;
uniform vec3 Ka, Kd, Ks;
uniform float shininess;
uniform vec3 eye_pos;

in vec3 smooth_position, smooth_normal, smooth_eye_pos, smooth_light_intensity;

void main()
{
    vec3 L = normalize(light_pos - smooth_position);
    vec3 V = normalize(smooth_eye_pos - smooth_position);
    vec3 N = normalize(smooth_normal);
    vec3 R = 2 * dot(L, N) * N - L;

    vec3 ambient = Ka * smooth_light_intensity;
    vec3 diffuse = Kd * max(dot(N, L), 0) * smooth_light_intensity;
    vec3 specular = Ks * pow(max(dot(V, R), 0), shininess) * smooth_light_intensity;

    if (dot(N, L) < 0){
        specular = vec3(0, 0, 0);    
    }

    gl_FragColor.rgb = ambient + diffuse + specular;
}'''
    p_prog_id = compile_shaders(p_vert_code, p_frag_code, "Phong")

    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global light_pos, eye_pos, eye_at

    df = pd.read_csv("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\models\\teapot.tri", sep='\s+',
                     comment='#', header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)
    light_pos = centroid + (0, 0, 5)
    eye_pos = centroid + (0, 0, 0.8*max(bbox)) + (0.5, 0, 0)
    eye_at = centroid + (0.5, 0, 0)

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    vbo = glGenBuffers(4)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
    glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
    glEnableVertexAttribArray(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[2])
    glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
    glEnableVertexAttribArray(2)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[3])
    glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
    glVertexAttribPointer(3, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
    glEnableVertexAttribArray(3)

def show_versions():
    lists = [['Vendor', GL_VENDOR], ['Renderer',GL_RENDERER],
            ['OpenGL Version', GL_VERSION],
            ['GLSL Version', GL_SHADING_LANGUAGE_VERSION]]
    for x in lists:
        print("%s: %s" % (x[0], glGetString(x[1]).decode("utf-8")))

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Per-Vertex and Per-Fragment Lighting Exercise",
                              None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    initialize()
    create_shaders()
    while not glfwWindowShouldClose(window):
        glfwPollEvents()
        refresh(window)
    impl.shutdown()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()