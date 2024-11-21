import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import time, math as m

win_w, win_h = 1024, 768

def resize(window, w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w/win_h, 0.01, 30)

wireframe_on, animation_on = False, False
def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)
    glfwPostEmptyEvent()

ticks, frame_cnt = 0, 0
def animation(window):
    global ticks, frame_cnt

    ticks += 1
    frame_cnt += 1
    glfwPostEmptyEvent()

def refresh(window):
    global start_time, frame_cnt
    if frame_cnt == 20:
        print("%.2f fps" % (frame_cnt/(time.time()-start_time)), ticks, end='\r')
        start_time = time.time()
        frame_cnt = 0
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    eye_pos = centroid + (0, 0, 1.5*max(bbox))
    gluLookAt(*eye_pos, *centroid, 0, 1, 0)

    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(colors[i])
        glVertex3fv(positions[i])
    glEnd()
    glfwSwapBuffers(window)

def gl_init_models():
    global start_time
    global n_vertices, positions, colors, normals, uvs, centroid, bbox

    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    df = pd.read_csv("C:\\b6510451115\\models\\bunny_uv.tri", sep='\s+', 
                     comment='#', header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    n_vertices = len(df.values)
    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    start_time = time.time() - 0.0001

    light_pos = np.array((3, 4, 20))
    eye_pos = np.array((0, 3, 3))
    #Light L_a or L_l
    Intensity_light = np.array((1, 1, 1))
    #Coefficient
    K_a = np.array((0.1, 0.1, 0.1))
    K_d = np.array((1, 0, 0))
    K_s = np.array((1, 1, 0))
    #Shininess
    n = 100
    for i in range(n_vertices) :
        P = positions[i]
        N = normals[i]
        L = normalize(light_pos - P)
        V = normalize(eye_pos - P)
        R = (2 * max(0, np.dot(N, L)) * N) - L
        NdotL = max(0, np.dot(N, L))
        VdotR = np.power(max(0, np.dot(V, R)), n)
        ambient = K_a * Intensity_light
        diffuse = K_d * Intensity_light * NdotL
        specular = K_s * Intensity_light * VdotR
        if NdotL <= 0:
            specular = np.array((0, 0, 0))
        colors[i] = ambient + diffuse + specular

def normalize(a):
    return a / (np.linalg.norm(a) + 1e-5)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Illumination Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    gl_init_models()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        refresh(window)
        glfwWaitEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()