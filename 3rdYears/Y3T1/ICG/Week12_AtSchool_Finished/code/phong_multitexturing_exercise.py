from ctypes import c_void_p
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
from PIL import Image

win_w, win_h = 1024, 768
Ka, Kd, Ks = [0.01, 0.01, 0.01], [0.86, 0.65, 0.13], [0.8, 0.8, 0.0]
light_intensity = [1, 1, 1]
shininess = 80
blend_factor, clear_color = 0.5, [0.0, 0.1, 0.1]
rot_x, rot_y = 0, 0
uv_translate, uv_rotate, uv_scale = [0, 0], 0, 1

def draw_gui():
    global blend_factor, clear_color, rot_x, rot_y, uv_rotate, uv_scale
    # Adding light_intensity, Ka, Kd, Ks and shininess
    global selection, light_intensity, Ka, Kd, Ks, shininess
    impl.process_inputs()
    imgui.new_frame()                 # Start the Dear ImGui frame 
    imgui.set_next_window_position(win_w-300, 10, imgui.FIRST_USE_EVER)
    imgui.begin("Control")            # Create a window
    imgui.push_item_width(200)
    _, blend_factor = imgui.slider_float("Blend Factor", blend_factor, 0, 1)
    imgui.pop_item_width()
    imgui.text("Control Light-Ambient-Diffuse and Shininess")
    # Adding light_intensity, Ka, Kd, Ks and shininess
    _, light_intensity = imgui.color_edit3("Light Intensity", *light_intensity)
    _, Ka = imgui.color_edit3("Ka", *Ka)
    _, Kd = imgui.color_edit3("Kd", *Kd)
    _, Ks = imgui.color_edit3("Ks", *Ks)
    _, shininess = imgui.slider_float("Shininess", shininess, 0.1, 180)
    imgui.text("Texture Coordinate Transform")
    imgui.push_item_width(100)
    _, uv_translate[0] = imgui.slider_float("Translate S###uv_translate_x", uv_translate[0], -1, 1)
    imgui.same_line()
    _, uv_translate[1] = imgui.slider_float("Translate T###uv_translate_y", uv_translate[1], -1, 1)
    _, uv_rotate = imgui.slider_float("Angle Rotation###uv_rotate_x", uv_rotate, -180, 180)
    _, uv_scale = imgui.slider_float("Scale###uv_scale_x", uv_scale, 0.01, 10)
    imgui.pop_item_width()
    imgui.text("Model Rotation")
    imgui.push_item_width(100)
    _, rot_x = imgui.slider_float("Rotate X", rot_x, -180, 180)      
    imgui.same_line()  
    _, rot_y = imgui.slider_float("Rotate Y", rot_y, -180, 180)
    imgui.pop_item_width()
    imgui.text("")      
    _, clear_color = imgui.color_edit3("Clear Color", *clear_color)    
    imgui.text("Application average %.3f ms/frame (%.1f FPS)" % \
        (1000 / imgui.get_io().framerate, imgui.get_io().framerate))
    
    imgui.end()

def resize(window, w, h):
    global win_w, win_h, proj_mat

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    proj_mat = Perspective(45, w / h, 0.1, 30)
    
def refresh(window):
    glClearColor(*clear_color, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    model_mat = Rotate(rot_x, 1, 0, 0) @ Rotate(rot_y, 0, 1, 0)
    view_mat = LookAt(*eye_pos, *centroid, 0, 1, 0)

    glUseProgram(prog_id)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "model_mat"), 1, GL_TRUE, model_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "view_mat"), 1, GL_TRUE, view_mat)
    glUniformMatrix4fv(glGetUniformLocation(prog_id, "proj_mat"), 1, GL_TRUE, proj_mat)
    glUniform3fv(glGetUniformLocation(prog_id, "Ka"), 1, Ka)
    glUniform3fv(glGetUniformLocation(prog_id, "Kd"), 1, Kd)
    glUniform3fv(glGetUniformLocation(prog_id, "Ks"), 1, Ks)
    glUniform3fv(glGetUniformLocation(prog_id, "light_intensity"), 1, light_intensity)
    glUniform1f(glGetUniformLocation(prog_id, "shininess"), shininess)
    glUniform3fv(glGetUniformLocation(prog_id, "light_pos"), 1, light_pos)
    glUniform3fv(glGetUniformLocation(prog_id, "eye_pos"), 1, eye_pos)
    glUniform1f(glGetUniformLocation(prog_id, "blend_factor"), blend_factor)
    glUniform2fv(glGetUniformLocation(prog_id, "uv_translate"), 1, uv_translate)
    glUniform1f(glGetUniformLocation(prog_id, "uv_rotate"), uv_rotate)
    glUniform1f(glGetUniformLocation(prog_id, "uv_scale"), uv_scale)
    
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

def load_texture(filename, active_texture_unit):
    im = Image.open(filename)
    w, h = im.size
    image = im.tobytes("raw", im.mode, 0)
    tex_id = glGenTextures(1)
    glActiveTexture(active_texture_unit)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    
    if im.mode == 'RGBA':
        n_channels = GL_RGBA
        format = GL_RGBA
    else:
        n_channels = GL_RGB
        format = GL_RGB
    glTexImage2D(GL_TEXTURE_2D, 0, n_channels, w, h, 0, format, GL_UNSIGNED_BYTE, image)
    glGenerateMipmap(GL_TEXTURE_2D)
    glTextureParameteri(tex_id, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE if format == GL_RGBA else GL_REPEAT)
    glTextureParameteri(tex_id, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE if format == GL_RGBA else GL_REPEAT)
    glTextureParameteri(tex_id, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTextureParameteri(tex_id, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return active_texture_unit - GL_TEXTURE0

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
    global prog_id, vao, vbo
    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global eye_pos, light_pos

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    vert_code = '''
#version 140
in vec3 position, color, normal;
in vec2 uv;

uniform mat4 model_mat, view_mat, proj_mat;
uniform vec2 uv_translate;
uniform float uv_rotate, uv_scale;

out vec3 smooth_position, smooth_normal;
out vec2 bunny_uv, brick_uv;

void main()
{
    gl_Position = proj_mat * view_mat * model_mat * vec4(position, 1);

    smooth_position = (model_mat *  vec4(position, 1)).xyz;
    smooth_normal = (transpose(inverse(model_mat)) * vec4(normal, 0)).xyz;

    float theta = uv_rotate/180*3.141593;
    mat2 rot_mat = mat2(cos(theta), -sin(theta), sin(theta), cos(theta));
    brick_uv = rot_mat * (uv_scale * uv + uv_translate);
    bunny_uv = uv;
}'''

    frag_code = '''
#version 140
uniform vec3 Ka, Kd, Ks, light_intensity, light_pos, eye_pos;
uniform float shininess, blend_factor;
uniform sampler2D bunny_hair, brick;

smooth in vec3 smooth_position, smooth_normal;
smooth in vec2 bunny_uv, brick_uv;

out vec4 frag_color;

void main()
{
    vec3 Kd_bunny = texture(bunny_hair, bunny_uv).rgb;
    vec3 Kd_brick = texture(brick, brick_uv).rgb;
    vec3 Kd_mix = mix(Kd_bunny, Kd_brick, blend_factor);
    vec3 Kd_tex_and_user = mix(Kd_mix, Kd, 0.2);

    vec3 L = normalize(light_pos - smooth_position);
    vec3 V = normalize(eye_pos - smooth_position);
    vec3 N = normalize(smooth_normal);
    vec3 R = 2 * dot(L, N) * N - L;

    vec3 ambient = Ka * light_intensity;
    vec3 diffuse = Kd_tex_and_user * max(dot(N, L), 0) * light_intensity;
    vec3 specular = Ks * pow(max(dot(V, R), 0), shininess) * light_intensity;

    if (dot(N, L) < 0){
        specular = vec3(0, 0, 0);    
    }

    gl_FragColor.rgb = ambient + diffuse + specular;
}'''
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
    glUseProgram(prog_id)

    global n_vertices, positions, colors, normals, uvs, centroid, bbox
    global light_pos, eye_pos

    df = pd.read_csv("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\models\\bunny_uv.tri", sep='\s+', comment='#',
                     header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)
    eye_pos = centroid + (0, 0, 1.5*bbox[0])
    light_pos = eye_pos

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)

    glUseProgram(prog_id)
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    vbo = glGenBuffers(4)
    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])
    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)
    position_loc = glGetAttribLocation(prog_id, "position")
    glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, 
        c_void_p(0))
    glEnableVertexAttribArray(position_loc)
    color_loc = glGetAttribLocation(prog_id, "color")
    if color_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[1])
        glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)
        glVertexAttribPointer(color_loc, 3, GL_FLOAT, GL_FALSE, 0, 
            c_void_p(0))
        glEnableVertexAttribArray(color_loc)
    normal_loc = glGetAttribLocation(prog_id, "normal")
    if normal_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[2])
        glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)
        glVertexAttribPointer(normal_loc, 3, GL_FLOAT, GL_FALSE, 0, 
            c_void_p(0))
        glEnableVertexAttribArray(normal_loc)
    uv_loc = glGetAttribLocation(prog_id, "uv")
    if uv_loc != -1:
        glBindBuffer(GL_ARRAY_BUFFER, vbo[3])
        glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)
        glVertexAttribPointer(uv_loc, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))
        glEnableVertexAttribArray(uv_loc)
        
    bunny_unit = load_texture("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\Week12_AtSchool_Finished\\texture\\bunny_hair.jpg", GL_TEXTURE1)
    brick_unit = load_texture("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T1\\ICG\\Week12_AtSchool_Finished\\texture\\brick_wall_small.jpg", GL_TEXTURE2)

    bunny_texture_location = glGetUniformLocation(prog_id, "bunny_hair")
    glUniform1i(bunny_texture_location, bunny_unit)
    brick_texture_location = glGetUniformLocation(prog_id, "brick")
    glUniform1i(brick_texture_location, brick_unit)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Multitexturing with Lighting Exercise", None, None)
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