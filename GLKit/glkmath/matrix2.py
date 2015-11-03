# coding: utf-8
import ctypes


class m21(ctypes.Structure):
    _fields_ = [
                ('m00', ctypes.c_float),
                ('m01', ctypes.c_float),
                ('m20', ctypes.c_float),
                ('m21', ctypes.c_float),
                ]


class float4(ctypes.Structure):
    _fields_ = [
                ('m', (ctypes.c_float * 4)),
                ]


class GLKMatrix2(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ]
    _fields_ = [
                ('s1', float4),
                ('s2', m21),
                ]
    
    def __str__(self):
        mstr = '''GLKMatrix2 { {%.3f\t%.3f}\t{%.3f\t%.3f} }'''
        mstr %= tuple([float(x) for x in self.s1.m])
        return mstr
        
def GLKMatrix2Make(m00, m01, m20, m21):
    m = GLKMatrix2()
    m.m00 = m00
    m.m01 = m01
    m.m20 = m20
    m.m21 = m21
    return m
    
def GLKMatrix2MakeWithArray(values):
    return GLKMatrix2Make(*values)
        
__all__ = ['GLKMatrix2', 'GLKMatrix2Make', 'GLKMatrix2MakeWithArray']

if __name__ == '__main__':
    print GLKMatrix2()