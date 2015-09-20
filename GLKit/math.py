# coding: utf-8
import ctypes
from objc_util import *


class xyzw(ctypes.Structure):
    _fields_ = [
                ('x', ctypes.c_float),
                ('y', ctypes.c_float),
                ('z', ctypes.c_float),
                ('w', ctypes.c_float)
                ]
                
class rgba(ctypes.Structure):
    _fields_ = [
                ('r', ctypes.c_float),
                ('g', ctypes.c_float),
                ('b', ctypes.c_float),
                ('a', ctypes.c_float)
                ]
                
class stpq(ctypes.Structure):
    _fields_ = [
                ('s', ctypes.c_float),
                ('t', ctypes.c_float),
                ('p', ctypes.c_float),
                ('q', ctypes.c_float)
                ]
                
class float4(ctypes.Structure):
    _fields_ = [
                ('v', (ctypes.c_float * 4))
                ]
                
                
class GLKVector4(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ('s3'),
                    ('s4'),
                    ]
    _fields_ = [
                ('s1', xyzw),
                ('s2', rgba),
                ('s3', stpq),
                ('s4', float4),
                ]


if __name__ == "__main__":
    import OpenGLES.GLKit as gl
    v = GLKVector4()
    v.x = 1.0
    v.y = 0.0
    v.z = 0.0
    v.w = 1.0
    print v.x, v.y, v.z, v.w
    e = gl.effect.GLKBaseEffect()
    l0 = e.light0()
    l0.setPosition_(0, 0, 0, v, v, v)