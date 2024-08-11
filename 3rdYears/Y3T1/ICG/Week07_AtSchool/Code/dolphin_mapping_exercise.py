import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
from PIL import Image

def resize(window, w, h):
    glViewport(0, 0, w, h)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def refresh(window):
    glColor3f(1.0, 1.0, 0.0)

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    """ONE-LEFT-BOTTOM"""
    # Top - Right
    glTexCoord2f(0.0, 0.0)
    glVertex3f( 1.0, 1.0, 0.0)
    # Top - Left
    glTexCoord2f(3.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    # Bottom - Left
    glTexCoord2f(3.0, 3.0)
    glVertex3f(-1.0,-1.0, 0.0)
    # Bottom - Right
    glTexCoord2f(0.0, 3.0)
    glVertex3f( 1.0,-1.0, 0.0)
        
    glEnd()

    glfwSwapBuffers(window)

def gl_init():
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    filename = "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\Week07_AtSchool\\Texture\\dolphin.jpg"
    # Insert code for texture mapping here!
    load_texture(filename)

def load_texture(filename):

    try:
        im = Image.open(filename)
    except:
        print("Error:", sys.exc_info()[0])
    
    w = im.size[0]
    h = im.size[1]
    image = im.tobytes("raw", "RGB", 0)
    tex_id = glGenTextures(1)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexEnvf(GL_TEXTURE_2D, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    
def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(800, 800, "Texture Mapping Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)

    gl_init()
    while not glfwWindowShouldClose(window):
        refresh(window)
        glfwWaitEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()