
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
from pywavefront import Wavefront, visualization as vis

model = Wavefront("3rdYears\\Y3T1\\ICG\\models\\teapot.obj")
prog_id = 0
win_w, win_h = 800, 600

def printShaderInfoLog(shader, prompt=""):

    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetShaderInfoLog(shader).decode("utf-8")))
        exit()



def printProgramInfoLog(program, prompt=""):

    result = glGetProgramiv(program, GL_LINK_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetProgramInfoLog(program).decode("utf-8")))
        exit()

def compileProgram(vertex_code, fragment_code):
        pass

def gl_init():
    global prog_id

    glViewport(0, 0, win_w, win_h)
    glEnable(GL_DEPTH_TEST)

    vert_code = '''
#version 120
out vec3 sentNormal;
void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    sentNormal = gl_Normal;
}
                '''
    frag_code = ''' 
#version 120
in vec3 sentNormal;
void main()
{
    gl_FragColor = vec4(0.5 * (sentNormal + 1), 0);
}
                '''                
    # prog_id = compileProgram(vert_code, frag_code)
    prog_id = glCreateProgram()

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vert_code)
    glShaderSource(frag_id, frag_code)

    glCompileShader(vert_id)
    printShaderInfoLog(vert_id, "Vertex Shader")
    glCompileShader(frag_id)
    printShaderInfoLog(frag_id, "Fragment Shader")

    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    printProgramInfoLog(prog_id, "Link Program")

def refresh(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w/win_h, 0.01, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0.5, 2, 0, 0.5, 0, 0, 1, 0)

    glUseProgram(prog_id)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glColor3f(1, 1, 0)
    vis.draw(model)
    glfwSwapBuffers(window)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "GLSL Shaders Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    gl_init()
    while not glfwWindowShouldClose(window):
        refresh(window)
        glfwWaitEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()    