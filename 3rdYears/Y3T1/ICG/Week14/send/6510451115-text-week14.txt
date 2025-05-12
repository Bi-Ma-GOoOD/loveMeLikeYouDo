import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import math as m
from PIL import Image
from ctypes import c_void_p
from gl_helpers_exercise import *

win_w, win_h, clear_color = 1280, 800, [0.1, 0.6, 0.6]
Ka, Kd, Ks = [0.15, 0.15, 0.15], [0.86, 0.65, 0.13], [0.8, 0.8, 0.0]
I, shininess, up_dir = [1, 1, 1], 80, np.array((0, 1, 0))
light_fovy, light_near, light_far = 45, 15, 40
wireframe_on, animation_on, t_value = False, False, 0
shadow_map_size = 1024  # Fix me!
# view_mat = Identity()

def print_shader_info_log(shader, prompt=""):
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetShaderInfoLog(shader).decode("utf-8")))
        os._exit(0)

def print_program_info_log(shader, prompt=""):
    result = glGetProgramiv(shader, GL_LINK_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetProgramInfoLog(shader).decode("utf-8")))
        os._exit(0)

def save_depth_map():
    data = glReadPixels(0, 0, shadow_map_size, shadow_map_size, GL_DEPTH_COMPONENT, GL_FLOAT)
    data3 = np.zeros((data.shape[0], data.shape[1], 3), dtype=np.uint8)
    data3[:,:,0] = 255*data[:]
    data3[:,:,1] = 255*data[:]
    data3[:,:,2] = 255*data[:]
    image = Image.frombytes(mode="RGB", size=(shadow_map_size, shadow_map_size), data=data3)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save("depth_map.jpg")

def compileProgram(vert_code, frag_code):
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
    return prog_id

def resize(window, w, h):
    global win_w, win_h, proj_mat

    win_w, win_h = w, h
    glViewport(0, 0, w, h)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    proj_mat = Perspective(60, win_w/win_h, 0.01, 100)

def refresh(window):
    glClear(GL_DEPTH_BUFFER_BIT)
    model_mat = Rotate(t_value, 0, 1, 0)
    view_mat = LookAt(*eye_pos, *eye_at, 0, 1, 0)

    # First pass: create shadow map 
    # Fix me!
    # Create shadow map into FBO.
    glUseProgram(shadow_prog_id)
    glActiveTexture(GL_TEXTURE0)
    glUseProgram(shadow_prog_id)
    light_position = [2, 8, 20]
    light_at = [-3.5, 2.3, -0.2]
    light_proj_mat = Perspective(60, 1, 20, 60)
    light_view_mat = LookAt(*light_position, *light_at, 0, 1, 0)
    MVP = light_proj_mat @ light_view_mat @ model_mat
    glUniformMatrix4fv(glGetUniformLocation(shadow_prog_id, "MVP"), 1, True, MVP)

    glDrawBuffer(GL_NONE)
    glBindTexture(GL_TEXTURE_2D, 0)
    glViewport(0, 0, shadow_map_size, shadow_map_size)
    glBindFramebuffer(GL_FRAMEBUFFER, shadow_FBO)
    glClear(GL_DEPTH_BUFFER_BIT)
    glBindVertexArray(shadow_vao)
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)
    # Test shadow map
    save_depth_map()

    # Second pass: render scene
    # Fix me!
    # Render the scene (The information of the pass appears in Week 7).
    glUseProgram(render_prog_id)

    B = np.array(((0.5, 0, 0, 0.5),
                  (0, 0.5, 0, 0.5),
                  (0, 0, 0.5, 0.5),
                  (0, 0, 0, 1)), dtype=np.float32)

    shadow_mat = B @ light_proj_mat @ light_view_mat @ model_mat    
    glUniformMatrix4fv(glGetUniformLocation(render_prog_id, "model_mat"), 1, True, model_mat)
    glUniformMatrix4fv(glGetUniformLocation(render_prog_id, "view_mat"), 1, True, view_mat)
    glUniformMatrix4fv(glGetUniformLocation(render_prog_id, "proj_mat"), 1, True, proj_mat)
    glUniformMatrix4fv(glGetUniformLocation(render_prog_id, "shadow_mat"), 1, True, shadow_mat)
    glUniform3fv(glGetUniformLocation(render_prog_id, "light_position"), 1, light_position)
    glUniform3fv(glGetUniformLocation(render_prog_id, "light_intensity"), 1, [1.0, 1.0, 1.0])
    glUniform3fv(glGetUniformLocation(render_prog_id, "eye_pos"), 1, eye_pos)
    # glUniform3fv(glGetUniformLocation(render_prog_id, "Ka"), 1, [0.05, 0.05, 0.05])
    # glUniform3fv(glGetUniformLocation(render_prog_id, "Kd"), 1, [0.25, 0.25, 0.25])
    glUniform3fv(glGetUniformLocation(render_prog_id, "Ks"), 1, [1.0, 1.0, 1.0])
    glUniform1f(glGetUniformLocation(render_prog_id, "shininess"), 50.0)

    glBindFramebuffer(GL_FRAMEBUFFER, 0)
    glDrawBuffer(GL_BACK)
    glViewport(0, 0, win_w, win_h)
    glBindTexture(GL_TEXTURE_2D, shadow_tex_id)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBindVertexArray(render_vao)
    glDrawArrays(GL_TRIANGLES, 0, n_vertices)
    glfwSwapBuffers(window)

def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
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

def animation(window):
    global t_value

    t_value += 0.1

def create_program():
    global shadow_prog_id, render_prog_id
    global shadow_vao, render_vao

    # First pass: create shadow map
    shadow_vert_code = '''
#version 120
attribute vec3 position;

uniform mat4 MVP;

void main()
{
    gl_Position = MVP * vec4(position, 1);
}
'''
    shadow_frag_code = '''
#version 110
void main()
{
}
'''
    shadow_prog_id = compileProgram(shadow_vert_code, shadow_frag_code)
    glUseProgram(shadow_prog_id)

    shadow_vao = glGenVertexArrays(1)
    glBindVertexArray(shadow_vao)
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    position_loc = glGetAttribLocation(shadow_prog_id, "position")
    if position_loc != -1:
        glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(position_loc)

    # Second pass: render scene
    render_vert_code = '''
#version 140
in vec3 position, color, normal;
in vec2 uv;

uniform mat4 model_mat, view_mat, proj_mat, shadow_mat;

out vec3 smooth_position, smooth_normal, smooth_color;
out vec4 ss_pos;   // Shadow-space (Light-space) position

void main()
{
    gl_Position = proj_mat * view_mat * model_mat * vec4(position, 1);
    smooth_position = (model_mat * vec4(position, 1)).xyz;
    mat4 normal_mat = transpose(inverse(model_mat));
    smooth_normal = (normal_mat * vec4(normal, 0)).xyz;
    ss_pos = shadow_mat * vec4(position, 1);
    smooth_color = color;
}
'''
    render_frag_code = '''
#version 140
in vec3 smooth_position, smooth_normal, smooth_color;
in vec4 ss_pos;

uniform vec3 light_pos, light_intensity, Ks, eye_pos;
uniform float shininess;
uniform mat4 view_mat;
uniform sampler2D shadow_map;

out vec4 frag_color;

void main()
{
    vec3 shadow_color = vec3(0.15, 0.15, 0.15);
    vec3 Ka = shadow_color;

    vec3 Kd = smooth_color;
    
    vec3 L = normalize(light_pos - smooth_position);
    vec3 V = normalize(eye_pos - smooth_position);
    vec3 N = normalize(smooth_normal);
    vec3 R = 2 * dot(L, N) * N - L;

    vec3 ambient = Ka * light_intensity;
    vec3 diffuse = Kd * max(dot(N, L), 0) * light_intensity;
    vec3 specular = Ks * pow(max(dot(V, R), 0), shininess) * light_intensity;

    vec3 color = ambient + diffuse + specular;

    //Fix acne and alias
    float visibility = 1.0;
    float bias = max(0.005 * (1.0 - dot(N, L)), 0.1);
    for(int i=-1; i <= 1; i++)
        for(int j=-1; j <= 1; j++)
            if (ss_pos.z/ss_pos.w < 1.0 && textureOffset(shadow_map, ss_pos.st/ss_pos.w, ivec2(i, j)).r < ss_pos.z/ss_pos.w - bias)
                visibility -= 0.1; 

    frag_color = vec4(visibility * color + shadow_color, 1.0);  
}
'''
    render_prog_id = compileProgram(render_vert_code, render_frag_code)
    glUseProgram(render_prog_id)

    render_vao = glGenVertexArrays(1)
    glBindVertexArray(render_vao)
    vbo = glGenBuffers(4)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    position_loc = glGetAttribLocation(render_prog_id, "position")
    if position_loc != -1:
        glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(position_loc)

    color_loc = glGetAttribLocation(render_prog_id, "color")
    glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
    glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)
    if color_loc != -1:
        glVertexAttribPointer(color_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(color_loc)

    normal_loc = glGetAttribLocation(render_prog_id, "normal")
    glBindBuffer(GL_ARRAY_BUFFER, vbo[2])
    glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
    if normal_loc != -1:
        glVertexAttribPointer(normal_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(normal_loc)

    uv_loc = glGetAttribLocation(render_prog_id, "uv")
    glBindBuffer(GL_ARRAY_BUFFER, vbo[3])
    glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
    if uv_loc != -1:
        glVertexAttribPointer(uv_loc, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(uv_loc)

    # Fix me!
    # นำโค้ดในการเตรียม FBO และเพื่อใช้สำหรับเก็บ shadow map มาใส่ด้านล่างนี้
    global shadow_tex_id, shadow_FBO
    glActiveTexture(GL_TEXTURE0)
    shadow_tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, shadow_tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT, shadow_map_size, shadow_map_size,
        0, GL_DEPTH_COMPONENT, GL_FLOAT, None)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_COMPARE_MODE, GL_NONE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
    glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, [1, 1, 1, 1])
    glBindTexture(GL_TEXTURE_2D, 0)
    if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
        exit(1)

    shadow_FBO = glGenFramebuffers(1)   # FBO setup
    glBindFramebuffer(GL_FRAMEBUFFER, shadow_FBO)
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT,
        GL_TEXTURE_2D, shadow_tex_id, 0)
    glBindFramebuffer(GL_FRAMEBUFFER, 0)   # Revert to default buffer

def initialize():
    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global eye_pos, eye_at, light_pos, light_at

    glClearColor(0.01, 0.01, 0.2, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    df = pd.read_csv("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\models\\objects_and_walls.tri",sep='\s+', 
                     comment='#', header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]

    eye_pos = centroid + (0.5*max(bbox), 0.2*max(bbox), 0.2*max(bbox))
    eye_at = centroid + (0.2*max(bbox), 0.1*max(bbox), 0)
    light_pos = [2, 8, 20]
    light_at = [-3.5, 2.3, -0.2]

    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % 
          (n_vertices, n_vertices//3))
    print("Centroid:", centroid)
    print("BBox:", bbox)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Shadow Mapping Exercise", None, None)
    glfwMakeContextCurrent(window)  
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    initialize()
    create_program()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        refresh(window)
        glfwPollEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()
