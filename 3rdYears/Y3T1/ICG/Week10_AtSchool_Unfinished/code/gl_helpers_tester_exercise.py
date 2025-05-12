import os
import sys, time
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
from pywavefront import Wavefront, visualization as vis
# check the correct results
# from gl_helpers_subst import *

# test
from gl_helpers_exercise import *

model = Wavefront("3rdYears\\Y3T1\\ICG\\models\\bunny.obj")
prog_id = 0
win_w, win_h = 1024, 768

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

    vert_code = '''
#version 130
uniform mat4 proj_mat, view_mat, model_mat;
out vec3 smooth_color;
void main()
{
   gl_Position = proj_mat * view_mat * model_mat * gl_Vertex;
   smooth_color = abs(gl_Normal);
}'''
    frag_code = '''
#version 130
in vec3 smooth_color;
void main()
{
   gl_FragColor = vec4(smooth_color, 1);
}'''

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vert_code)
    glShaderSource(frag_id, frag_code)

    glCompileShader(vert_id)
    glCompileShader(frag_id)
    print_shader_info_log(vert_id, "Vertex Shader")
    print_shader_info_log(frag_id, "Fragment Shader")

    prog_id = glCreateProgram()
    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    print_program_info_log(prog_id, "Link error")

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
    global win_w, win_h, proj_mat

    win_w, win_h = w, h
    glViewport(0, 0, w, h)  
    proj_mat = Perspective(60, win_w/win_h, 0.01, 10)

def refresh(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    view_mat = LookAt(*eye_pos, *centroid, 0, 1, 0)
    model_mat = Rotate(angle, 0, 1, 0)

    glUseProgram(prog_id)
    # Fix me!
    # Model matrix
    model_mat_loc = glGetUniformLocation(prog_id, "model_mat")
    glUniformMatrix4fv(model_mat_loc, 1, GL_TRUE, model_mat)
    # Viewing matrix
    view_mat_loc = glGetUniformLocation(prog_id, "view_mat")
    glUniformMatrix4fv(view_mat_loc, 1, GL_TRUE, view_mat)
    # Projection matrix
    prog_mat_loc = glGetUniformLocation(prog_id, "proj_mat")
    glUniformMatrix4fv(prog_mat_loc, 1, GL_TRUE, proj_mat)
    
    vis.draw(model)
    glfwSwapBuffers(window)

angle = 0
def animation(window):
    global angle

    angle += 1
    glfwPostEmptyEvent()

def init_model():
    global centroid, eye_pos

    glClearColor(0.4, 0.95, 0.95, 1)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    centroid = np.array((0, 0, 0))
    eye_pos = centroid + (0, 0, 2.5)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "gl_helpers Tester Exercise", None, None)
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
        refresh(window)
        glfwWaitEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()