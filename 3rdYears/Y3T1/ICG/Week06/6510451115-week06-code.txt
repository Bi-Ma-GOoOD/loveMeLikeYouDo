import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import time, math as m
import imgui
from imgui.integrations.glfw import GlfwRenderer

impl, angle = None, 0
win_w, win_h = 1280, 800
I, light_pos, eye_pos, eye_at = [1, 1, 1], [0, 0, 10], [0, 0, 0], [0, 0, 0]
rot_x, rot_y = 0, 30
clear_color = [0.5, 0.85, 0.85]
mouse_status = {'x': 0, 'y': 0, 
                GLFW_MOUSE_BUTTON_LEFT: GLFW_RELEASE, 
                GLFW_MOUSE_BUTTON_MIDDLE: GLFW_RELEASE,
                GLFW_MOUSE_BUTTON_RIGHT: GLFW_RELEASE}

Ka = (0.35, 0.69, 1)
Kd_front = (1, 0, 0)
Kd_back = (0, 1, 0)
Ks = (0, 0, 1)
Shininess = 10.0
two_side = True
specular_on = False

def normalize(u):
    return u / (np.linalg.norm(u) + 1e-5)

def draw_gui():
    global I, Ka, Kd_front, Kd_back, Ks, clear_color
    global Shininess
    global rot_x, rot_y, specular_on
    global two_side

    impl.process_inputs()
    imgui.new_frame()                 # Start the Dear ImGui frame 
    imgui.set_next_window_position(800, 10, imgui.ALWAYS)
    imgui.set_next_window_collapsed(False, imgui.FIRST_USE_EVER)    
    imgui.begin("Control")            # Create a window
    imgui.push_item_width(220)
    #Intensity of light
    _, I = imgui.color_edit3("Light Intensity", *I)
    #Coefficient = Ambient, Diffuse, Specular
    _, Ka = imgui.color_edit3("Ambient(Ka)", *Ka)
    _, Kd_front = imgui.color_edit3("Diffuse - Front(Kd-front)", *Kd_front)
    _, Kd_back = imgui.color_edit3("Diffuse - Back(Kd-back)", *Kd_back)
    _, Ks = imgui.color_edit3("Specular(Ks)", *Ks)
    #Shinniness
    _, Shininess = imgui.slider_float("Shininess", Shininess, 1.0, 100.0)
    #Enable Specular
    _, specular_on = imgui.checkbox("Specular Enabled", specular_on)
    imgui.same_line()
    _, two_side = imgui.checkbox("Two Sided Enabled", two_side)
    #Light Position
    imgui.text("Light Position")
    imgui.push_item_width(100)
    _, light_pos[0] = imgui.slider_float("X###light_pos_x", light_pos[0], -10, 10)
    imgui.same_line()
    _, light_pos[1] = imgui.slider_float("Y###light_pos_y", light_pos[1], -10, 10)
    imgui.same_line()
    _, light_pos[2] = imgui.slider_float("Z###light_pos_z", light_pos[2], -10, 10)
    #Eye Position
    imgui.text("Eye Position")
    _, eye_pos[0] = imgui.slider_float("X###eye_pos_x", eye_pos[0], -10, 10)
    imgui.same_line()
    _, eye_pos[1] = imgui.slider_float("Y###eye_pos_y", eye_pos[1], -10, 10)
    imgui.same_line()
    _, eye_pos[2] = imgui.slider_float("Z###eye_pos_z", eye_pos[2], -10, 10)
    imgui.text("Eye At")
    _, eye_at[0] = imgui.slider_float("X###eye_at_x", eye_at[0], -10, 10)
    imgui.same_line()
    _, eye_at[1] = imgui.slider_float("Y###eye_at_y", eye_at[1], -10, 10)
    imgui.same_line()
    _, eye_at[2] = imgui.slider_float("Z###eye_at_z", eye_at[2], -10, 10)
    imgui.pop_item_width()
    #Model Rotations
    imgui.text("Model Rotation")
    imgui.push_item_width(120)    
    _, rot_x = imgui.slider_float("Rotate X", rot_x, -180, 180)
    imgui.same_line()        
    _, rot_y = imgui.slider_float("Rotate Y", rot_y, -180, 180)
    imgui.pop_item_width()        
    _, clear_color = imgui.color_edit3("Clear Color", *clear_color)
    #Show frames
    imgui.text("Application average %.3f ms/frame (%.1f FPS)" % \
        (1000 / imgui.get_io().framerate, imgui.get_io().framerate))
    imgui.pop_item_width()
    imgui.end()

def resize(window, w, h):
    glViewport(0, 0, w, h)	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 0.1, 50)


def refresh(window):
    glClearColor(*clear_color, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(*eye_pos, *eye_at, 0, 1, 0)

    glRotate(angle, 0.8, 0.8, 0.2)
    glRotate(rot_x, 1, 0, 0)
    glRotate(rot_y, 0, 1, 0)

    # colors[:] = 0.2*normals + Ka

    glVertexPointer(3, GL_FLOAT, 0, positions)
    glColorPointer(3, GL_FLOAT, 0, colors)
    glNormalPointer(GL_FLOAT, 0, normals)
    glTexCoordPointer(2, GL_FLOAT, 0, uvs)
    turnLight()
    callMat()
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)      
    
    draw_gui()
    imgui.render()
    impl.render(imgui.get_draw_data())    

    glfwSwapBuffers(window)

wireframe_on, animation_on = False, False
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
            dx, dy, key_scale = 0, 0, 0.1
            if key == GLFW_KEY_LEFT:
                dx = -1
            elif key == GLFW_KEY_RIGHT:
                dx = 1
            elif key == GLFW_KEY_UP:
                dy = 1
            elif key == GLFW_KEY_DOWN:
                dy = -1           
            eye_dir = normalize(eye_at - eye_pos)
            up_dir = np.array((0, 1, 0))
            left_dir = np.cross(eye_dir, up_dir)
            up_dir = np.cross(left_dir, eye_dir)
            if mods & GLFW_MOD_CONTROL:
                eye_pos[:] += dy * key_scale * eye_dir
                eye_at[:] += dy * key_scale * eye_dir
            else:
                eye_pos[:] += dx * key_scale * left_dir
                eye_at[:] += dx * key_scale * left_dir
                eye_pos[:] += dy * key_scale * up_dir
                eye_at[:] += dy * key_scale * up_dir            
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)

def mouse_func(window, button, action, mods):
    mouse_status['x'], mouse_status['y'] = glfwGetCursorPos(window)
    mouse_status[button] = action

def cursor_func(window, x, y):
    global light_rotation

    if impl.io.want_capture_mouse:
        return
    dx, dy = x-mouse_status['x'], mouse_status['y']-y 
    mouse_status['x'], mouse_status['y'] = x, y
    if mouse_status[GLFW_MOUSE_BUTTON_LEFT] == GLFW_PRESS:
        pass

def scroll_func(window, dx, dy):
    scroll_scale = 0.2
    eye_dir = normalize(eye_at - eye_pos)    
    eye_pos[:] += dy * scroll_scale * eye_dir
    eye_at[:] += dy * scroll_scale * eye_dir

def animation(window):
    global angle

    angle += 1




def gl_init():
    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global impl, eye_pos, eye_at

    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    imgui.create_context()
    imgui.style_colors_light()
    impl = GlfwRenderer(window, attach_callbacks=False)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)


    df = pd.read_csv("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\models\\teapot_uv.tri", sep='\s+',
                     comment='#', header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    n_vertices = len(df.values)
    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    print("no. of vertices: %d, no. of triangles: %d" % 
          (n_vertices, n_vertices//3))
    print("Centroid:", centroid)
    print("BBox:", bbox)
    eye_pos = centroid + (0.5, 1.5, 1.5)
    eye_at = centroid + (0.5, 0, 0)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(win_w, win_h, "imGui Lighting Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetMouseButtonCallback(window, mouse_func)
    glfwSetCursorPosCallback(window, cursor_func)
    glfwSetScrollCallback(window, scroll_func)     
    glfwSetWindowPos(window, 20, 50)

    gl_init()
    resize(window, win_w, win_h)
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        glfwPollEvents()
        refresh(window)
    impl.shutdown()        
    glfwDestroyWindow(window)
    glfwTerminate()

def turnLight():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, I)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, I)
    glLightfv(GL_LIGHT0, GL_SPECULAR, I)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

def callMat():
    mat_a = Ka
    mat_d_front = Kd_front
    mat_d_back = Kd_back
    mat_s = Ks
    n = Shininess
   
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_a)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_d_front)
    glMaterialfv(GL_BACK, GL_DIFFUSE, mat_d_back)
    
    #Default of checkbox is true
    #true is mean checkbox is checked
    #false is mean checkbox is unchecked
    if two_side == True:
        # glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, mat_d_back)
        glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    else:
        # mat_d_back = (0, 0, 0)
        glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, GL_FALSE)
        # glMaterialfv(GL_BACK, GL_DIFFUSE, mat_d_front)
        # glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_d_front)
    # print(specular_on)
    #Default of specular's checkbox is false
    #False is mean checkbox is unchecked
    #True is mean checkbox is checked
    if specular_on == True:
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_d_front)
    else:
        mat_s = (0, 0, 0)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_s)
        
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_s)
    glMaterialf(GL_FRONT, GL_SHININESS, n)


if __name__ == "__main__":
    main()