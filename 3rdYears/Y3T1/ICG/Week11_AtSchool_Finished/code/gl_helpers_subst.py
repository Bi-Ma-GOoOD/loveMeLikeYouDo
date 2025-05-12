from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import array, ndarray, zeros, dot, cross
from numpy import float32, identity, matrix
from numpy.linalg import norm
from math import sqrt, sin, cos, tan, acos, pi
from PIL import Image

mat_map = {5888: GL_MODELVIEW_MATRIX, 5889: GL_PROJECTION_MATRIX}

def Identity():
    return array(((1, 0, 0, 0),
                  (0, 1, 0, 0),
                  (0, 0, 1, 0),
                  (0, 0, 0, 1)), dtype=float32)

def normalize(v):
    l = norm(v)
    if l == 0:
        return v
    else:
        return v/l

def Translate(tx, ty, tz):
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(tx, ty, tz)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T

def Scale(sx, sy, sz):
    glPushMatrix()
    glLoadIdentity()
    glScalef(sx, sy, sz)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T

def Rotate(angle, x, y, z):
    glPushMatrix()
    glLoadIdentity()
    glRotatef(angle, x, y, z)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T

def LookAt(eyex, eyey, eyez, atx, aty, atz, upx, upy, upz):
    glPushMatrix()
    glLoadIdentity()
    gluLookAt(eyex, eyey, eyez, atx, aty, atz, upx, upy, upz)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T

def Perspective(fovy, aspect, zNear, zFar):
    glPushMatrix()
    glLoadIdentity()
    gluPerspective(fovy, aspect, zNear, zFar)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T

def Frustum(left, right, bottom, top, near, far):
    glPushMatrix()
    glLoadIdentity()
    glFrustum(left, right, bottom, top, near, far)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T

def Ortho(left, right, bottom, top, near, far):
    glPushMatrix()
    glLoadIdentity()
    glOrtho(left, right, bottom, top, near, far)
    mat = glGetFloatv(mat_map[glGetIntegerv(GL_MATRIX_MODE)])
    glPopMatrix()
    return mat.T