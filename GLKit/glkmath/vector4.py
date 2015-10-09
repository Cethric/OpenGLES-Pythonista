# coding: utf-8
import ctypes

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
                
    def __str__(self):
        r = []
        s1 = self.s1
        s2 = self.s2
        s3 = self.s3
        s4 = self.s4
        r.extend([float(s1.x), float(s1.y), float(s1.z), float(s1.w)])
        r.extend([float(s2.r), float(s2.g), float(s2.b), float(s2.a)])
        r.extend([float(s3.s), float(s3.t), float(s3.p), float(s3.q)])
        r.extend([float(x) for x in s4.v])
        vstr = '''GLKVector {
xyzw = {%f, %f, %f, %f}
rgba = {%f, %f, %f, %f}
stpq = {%f, %f, %f, %f}
float4 = {%f, %f, %f, %f}
}''' % tuple(r)
        return vstr
        


__all__ = ['GLKVector4']
