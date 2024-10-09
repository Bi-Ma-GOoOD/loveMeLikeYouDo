from numpy import array, ndarray, zeros, dot, cross, float32, identity
from numpy.linalg import norm
from math import sqrt, sin, cos, tan, acos, pi, radians

def Identity():
    return array(((1, 0, 0, 0),
                  (0, 1, 0, 0),
                  (0, 0, 1, 0),
                  (0, 0, 0, 1)), dtype=float32)

def normalize(v, eps=1e-5):
    l = norm(v)
    if l == 0:
        return v
    else:
        return v/l

def Translate(tx, ty, tz):
    # Fix me!
    return array(((1, 0, 0, tx),
                  (0, 1, 0, ty),
                  (0, 0, 1, tz),
                  (0, 0, 0, 1)), dtype=float32)

def Scale(sx, sy, sz):
    # Fix me!
    return array(((sx, 0, 0, 0),
                  (0, sy, 0, 0),
                  (0, 0, sz, 0),
                  (0, 0, 0, 1)), dtype=float32)

def Rotate(angle, x, y, z):
    # Fix me!
    C = cos(radians(angle))
    S = sin(radians(angle))
    return array((((x*x)*(1-C)+C,       (x*y)*(1-C)-(z*S),      (x*z)*(1-C)+(y*S),  0),
                  ((y*x)*(1-C)+(z*S),   (y*y)*(1-C)+C,          (y*z)*(1-C)-(x*S),  0),
                  ((z*x)*(1-C)-(y*S),   (z*y)*(1-C)+(x*S),      (z*z)*(1-C)+C,      0),
                  (0,                   0,                      0,                  1)), dtype=float32)

def LookAt(eyex, eyey, eyez, atx, aty, atz, upx, upy, upz):
    # Fix me!
    Eye = array((eyex, eyey, eyez))
    At = array((atx, aty, atz))
    Up = array((upx, upy, upz))
    Z = normalize(Eye - At)
    Y = normalize(Up)
    X = normalize(cross(Y, Z))
    Y = normalize(cross(Z, X))
    return array(((X[0], X[1], X[2], -1 * (dot(X, Eye))),
                  (Y[0], Y[1], Y[2], -1 * (dot(Y, Eye))),
                  (Z[0], Z[1], Z[2], -1 * (dot(Z, Eye))),
                  (0, 0, 0, 1)), dtype=float32)

def Perspective(fovy, aspect, zNear, zFar):
    # Fix me!
    cot = 1/tan(radians(fovy)/2)
    return array(((cot/aspect,          0,             0,                                                                           0),
                  (0,                   cot,           0,                                                                           0),
                  (0,                   0,             (-1 * (zFar + zNear))/(zFar - zNear),        (-2 * zNear * zFar)/(zFar - zNear)),
                  (0,                   0,              -1,                                         0)), dtype=float32)

def Frustum(left, right, bottom, top, near, far):
    # Fix me!
    return array((((2 * near)/(right - left),  0,                           (right + left)/(right - left),                                      0),
                  (0,                          (2 * near)/(top - bottom),   (top + bottom)/(top - bottom),                                      0),
                  (0,                          0,                           ((far + near)/(far - near))*(-1),    ((2*far*near)/(far - near))*(-1)),
                  (0,                          0,                           -1,                                                                 0)), dtype=float32)

def Ortho(left, right, bottom, top, near, far):
    # Fix me!
    return array(((2/right-left,    0,                  0,              ((right+left)/(right-left))*(-1)),
                  (0,               2/top - bottom,     0,              ((top + bottom)/(top - bottom))*(-1)),
                  (0,               0,                  -2/far - near,  ((far + near)/(far - near)) * (-1)),
                  (0,               0,                  0,              1)), dtype=float32)