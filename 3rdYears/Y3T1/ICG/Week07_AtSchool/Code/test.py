import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
from PIL import Image


def resize(window, w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()


def refresh(window):
    glColor3f(1.0, 1.0, 1.0)

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    
    # Top - Right
    glTexCoord2f(3.0, 3.0)  # Repeat texture 3 times horizontally and vertically
    glVertex3f(3.0, 3.0, 0.0)
    # Top - Left
    glTexCoord2f(0.0, 3.0)
    glVertex3f(-3.0, 3.0, 0.0)
    # Bottom - Left
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-3.0, -3.0, 0.0)
    # Bottom - Right
    glTexCoord2f(3.0, 0.0)
    glVertex3f(3.0, -3.0, 0.0)

    glEnd()
    glfwSwapBuffers(window)


def gl_init():
    global tex_id  # Make tex_id global to use it in refresh function
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    filename = "D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\Week07_AtSchool\\Texture\\dolphin.jpg"
    tex_id = load_texture(filename)


def load_texture(filename):
    try:
        im = Image.open(filename)
    except:
        print("Error:", sys.exc_info()[0])
        return 0

    w, h = im.size
    image = im.tobytes("raw", "RGB", 0, -1)

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)

    return tex_id


def main():
    if not glfwInit():
        print("Failed to initialize GLFW")
        return

    window = glfwCreateWindow(800, 800, "Texture Mapping Exercise", None, None)
    if not window:
        print("Failed to create GLFW window")
        glfwTerminate()
        return

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
