# coding: utf-8
import ctypes

                
class m9(ctypes.Structure):
    _fields_ = [
                ('m00', ctypes.c_float),
                ('m01', ctypes.c_float),
                ('m02', ctypes.c_float),
                ('m10', ctypes.c_float),
                ('m11', ctypes.c_float),
                ('m12', ctypes.c_float),
                ('m20', ctypes.c_float),
                ('m21', ctypes.c_float),
                ('m22', ctypes.c_float),
                ]
                
                
class float9(ctypes.Structure):
    _fields_ = [
                ('m', ctypes.c_float * 9)
                ]

class GLKMatrix3(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ]
    _fields_ = [
                ('s1', float9),
                ('s2', m9),
                ]
    
    def __str__(self):
        mstr = '''GLKMatrix3
{
{%.3f, %.3f, %.3f}
{%.3f, %.3f, %.3f}
{%.3f, %.3f, %.3f}
}''' % tuple([float(x) for x in self.s1.m])
        return mstr
        
__all__ = ['GLKMatrix3']