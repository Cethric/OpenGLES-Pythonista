# coding: utf-8
import ctypes
import euclid


class float16(ctypes.Structure):
    _fields_ = [
                ('m', (ctypes.c_float * 16)),
                ]

class m16(ctypes.Structure):
    _fields_ = [
                ('m00', ctypes.c_float),
                ('m01', ctypes.c_float),
                ('m02', ctypes.c_float),
                ('m03', ctypes.c_float),
                ('m10', ctypes.c_float),
                ('m11', ctypes.c_float),
                ('m12', ctypes.c_float),
                ('m13', ctypes.c_float),
                ('m20', ctypes.c_float),
                ('m21', ctypes.c_float),
                ('m22', ctypes.c_float),
                ('m23', ctypes.c_float),
                ('m30', ctypes.c_float),
                ('m31', ctypes.c_float),
                ('m32', ctypes.c_float),
                ('m33', ctypes.c_float),
                ]
                
class GLKMatrix4(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ]
    _fields_ = [
                ('s1', float16),
                ('s2', m16),
                ]
    
    def __str__(self):
        mstr = '''GLKMatrix4 { {%.3f, %.3f, %.3f, %.3f} {%.3f, %.3f, %.3f, %.3f} {%.3f, %.3f, %.3f, %.3f {%.3f, %.3f, %.3f, %.3f} }''' % tuple([float(x) for x in self.s1.m])
        return mstr
        

__all__ = ['GLKMatrix4']