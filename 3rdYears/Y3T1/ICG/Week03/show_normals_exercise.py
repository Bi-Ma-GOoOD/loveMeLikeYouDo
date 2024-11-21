import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd

def buildFill():
    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(0.5 * (normals[i] + 1))
        glVertex3fv(positions[i])
    glEnd()

def buildBorder():
    for i in range(0, n_vertices, 3):
        glBegin(GL_LINE_LOOP)
        glColor3f(1.0, 1.0, 1.0)
        v0 = positions[i]
        v1 = positions[i+1]
        v2 = positions[i+2]
        glVertex3fv(v0)
        glVertex3fv(v1)
        glVertex3fv(v2)
        glEnd()

def vector():
    global d_vector
    for i in range(0, n_vertices, 3):
        v0 = positions[i]
        v1 = positions[i+1]
        v2 = positions[i+2]
    #     glBegin(GL_LINE_LOOP)
    #     glColor3f(1.0, 1.0, 1.0)
    #     glVertex3fv(v0)
    #     glVertex3fv(v1)
    #     glVertex3fv(v2)
    #     glEnd()
        #for vector
        c = (v0 + v1 + v2)/3
        n = np.cross(v1 - v0, v2 - v0)
        if(press_o == True):
            d_vector = c + (n*0.5)
        elif(press_p == True):
            d_vector = c + n
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3fv(c)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3fv(d_vector)
        glEnd()
        
def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*(centroid+(0, 10, max(bbox))), *centroid, 0, 1, 0)
    glRotatef(degree, 0, 1, 0)
    buildFill()
    if triangle_border == True: buildBorder()
    if see_vector == True: vector()
    glfwSwapBuffers(window)

def reshape(window, w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 50)

degree = 0
def animation(window):
    global degree
    degree = degree + 1
    glfwPostEmptyEvent()

wireframe_on, animation_on = False, False
#For triangle_border
triangle_border = False
#For normal vectors
see_vector = False
#Pree o for decrease vector and p for increase vector
press_o, press_p = False, False
def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on, triangle_border, see_vector, press_o, press_p

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key == GLFW_KEY_Q:
            glfwSetWindowShouldClose(window, GLFW_TRUE)
        elif key == GLFW_KEY_T:
            triangle_border = not triangle_border
        elif key == GLFW_KEY_N:
            see_vector = not see_vector
        elif key == GLFW_KEY_O:
            press_o = not press_o
        elif key == GLFW_KEY_P:
            press_p = not press_p
    glfwPostEmptyEvent()

def my_init():
    global n_vertices, positions, colors, normals, uvs
    global centroid, bbox

    glClearColor(0.2, 0.8, 0.8, 1)
    df = pd.read_csv("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\Week03\\ashtray.tri", sep='\s+', comment='#',
                     header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % 
          (n_vertices, n_vertices//3))    
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glLineWidth(1)

def show_versions():
    lists = [['Vendor', GL_VENDOR], ['Renderer',GL_RENDERER],
            ['OpenGL Version', GL_VERSION],
            ['GLSL Version', GL_SHADING_LANGUAGE_VERSION]]
    for x in lists:
        print("%s: %s" % (x[0], glGetString(x[1]).decode("utf-8")))

def main():
    global window, win_w, win_h

    if not glfwInit():
        glfwTerminate()
        return

    win_w, win_h = 1024, 768
    window = glfwCreateWindow(1, 1, "Show Normals Exercise", None, None)
    glfwMakeContextCurrent(window)
    show_versions()
    
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowRefreshCallback(window, display)
    glfwSetWindowSizeCallback(window, reshape)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    my_init()   
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        display(window)
        glfwWaitEvents()
        # glfwPollEvents()
    glfwDestroyWindow(window)
    glfwTerminate()   

if __name__ == "__main__":
    main()