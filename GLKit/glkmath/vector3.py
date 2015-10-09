# coding: utf-8
import ctypes

class xyz(ctypes.Structure):
    _fields_ = [
                ('x', ctypes.c_float),
                ('y', ctypes.c_float),
                ('z', ctypes.c_float),
                ]
                
class rgb(ctypes.Structure):
    _fields_ = [
                ('r', ctypes.c_float),
                ('g', ctypes.c_float),
                ('b', ctypes.c_float),
                ]
                
class stp(ctypes.Structure):
    _fields_ = [
                ('s', ctypes.c_float),
                ('t', ctypes.c_float),
                ('p', ctypes.c_float),
                ]
                
class float3(ctypes.Structure):
    _fields_ = [
                ('v', (ctypes.c_float * 3))
                ]
                
                
class GLKVector3(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ('s3'),
                    ('s4'),
                    ]
    _fields_ = [
                ('s1', xyz),
                ('s2', rgb),
                ('s3', stp),
                ('s4', float3),
                ]
                
    def __str__(self):
        r = []
        s1 = self.s1
        s2 = self.s2
        s3 = self.s3
        s4 = self.s4
        r.extend([float(s1.x), float(s1.y), float(s1.z)])
        r.extend([float(s2.r), float(s2.g), float(s2.b)])
        r.extend([float(s3.s), float(s3.t), float(s3.p)])
        r.extend([float(x) for x in s4.v])
        vstr = '''GLKVector {
xyz = {%f, %f, %f}
rgb = {%f, %f, %f}
stp = {%f, %f, %f}
float3 = {%f, %f, %f}
}''' % tuple(r)
        return vstr
        


__all__ = ['GLKVector3']