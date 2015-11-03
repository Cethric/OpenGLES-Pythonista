# coding: utf-8
import math
import ctypes
from objc_util import *


class xy(ctypes.Structure):
    _fields_ = [
                ('x', ctypes.c_float),
                ('y', ctypes.c_float),
                ]
                
                
class st(ctypes.Structure):
    _fields_ = [
                ('s', ctypes.c_float),
                ('t', ctypes.c_float),
                ]
                
class float2(ctypes.Structure):
    _fields_ = [
                ('v', (ctypes.c_float * 2))
                ]
                
                
class GLKVector2(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ('s3'),
                    ]
    _fields_ = [
                ('s1', xy),
                ('s2', st),
                ('s3', float2),
                ]
                
    def __str__(self):
        r = []
        s3 = self.s3
        r.extend([float(x) for x in s3.v])
        vstr = '''GLKVector2 { %.4f\t%.4f }''' % tuple(r)
        return vstr
        

glk2 = parse_struct('{glkvec2=fff}')

def to_glk2(old):
    return ctypes.cast(ctypes.pointer(old),ctypes.POINTER(glk2)).contents
    
def from_glk2(old):
    return ctypes.cast(ctypes.pointer(old),ctypes.POINTER(GLKVector2)).contents
    
def getGLKVector2(func):
    return from_glk2(func(restype=glk2, argtypes=[]))
    
def setGLKVector2(func, newvalue):
    newvalue = to_glk2(newvalue)
    return func(newvalue, restype=ctypes.c_void_p, argtypes=[glk2])
    
def GLKVector2Make(x, y):
    return GLKVector2(x=x, y=y)
    
def GLKVector2MakeWithArray(values):
    return GLKVector2(v=(ctypes.c_float * 2)(*values))
    
def GLKVector2Length(vector):
    v = [float(x) for x in vector.v]
    r = 0
    for x in v:
        r += math.pow(x, 2)
    return math.sqrt(r)
    
def GLKVector2Distance(vectorStart, vectorEnd):
    assert isinstance(vectorEnd, GLKVector2)
    return math.sqrt(math.pow(vectorStart.x - vectorEnd.x, 2) +
                     math.pow(vectorStart.y - vectorEnd.y, 2))
                     
def GLKVector2Negate(vector):
    v = GLKVector2()
    v.x = -vector.x
    v.y = -vector.y
    return v
    
def GLKVector2Normalize(vector):
    l = GLKVector2Length(vector)
    nv = GLKVector2()
    if l != 0:
        nv.x = vector.x / l
        nv.y = vector.y / l
        return nv
    else:
        raise ValueError('Cannot Normalise Vector of length 0')

def GLKVector2AddScalar(vector, value):
    v = GLKVector2()
    v.x = vector.x + value
    v.y = vector.y + value
    return v
    
def GLKVector2SubtractScalar(vector, value):
    v = GLKVector2()
    v.x = vector.x - value
    v.y = vector.y - value
    return v
    
def GLKVector2MultiplyScalar(vector, value):
    v = GLKVector2()
    v.x = vector.x * value
    v.y = vector.y * value
    return v
    
def GLKVector2DivideScalar(vector, value):
    v = GLKVector2()
    v.x = vector.x / value
    v.y = vector.y / value
    return v
    
def GLKVector2Add(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    v = GLKVector2()
    v.x = vectorLeft.x + vectorRight.x
    v.y = vectorLeft.y + vectorRight.y
    return v
    
def GLKVector2Subtract(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    v = GLKVector2()
    v.x = vectorLeft.x - vectorRight.x
    v.y = vectorLeft.y - vectorRight.y
    return v
    
def GLKVector2Multiply(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    v = GLKVector2()
    v.x = vectorLeft.x * vectorRight.x
    v.y = vectorLeft.y * vectorRight.y
    return v
    
def GLKVector2Divide(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    v = GLKVector2()
    v.x = vectorLeft.x / vectorRight.x
    v.y = vectorLeft.y / vectorRight.y
    return v
    
def GLKVector2DotProduct(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    return vectorLeft.x * vectorRight.x + vectorLeft.y * vectorRight.y
    
def GLKVector2Lerp(vectorStart, vectorEnd, t):
    assert isinstance(vectorEnd, GLKVector2)
    v = GLKVector2()
    v.x = vectorStart.x + ((vectorEnd.x - vectorStart.x) * t)
    v.y = vectorStart.y + ((vectorEnd.y - vectorStart.y) * t)
    
def GLKVector2Project(vectorToProject, projectionVector):
    assert isinstance(projectionVector, GLKVector2)
    scale = GLKVector2DotProduct(projectionVector, vectorToProject)
    scale /= GLKVector2DotProduct(projectionVector, projectionVector)
    v = GLKVector2MultiplyScalar(projectionVector, scale)
    return v
    
def GLKVector2Maximum(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    v = GLKVector2()
    v.x = max(vectorLeft.x, vectorRight.x)
    v.y = max(vectorLeft.y, vectorRight.y)
    return v
    
def GLKVector2Minimum(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    v = GLKVector2()
    v.x = min(vectorLeft.x, vectorRight.x)
    v.y = min(vectorLeft.y, vectorRight.y)
    return v
    
def GLKVector2EqualToScalar(vector, value):
    x = vector.x == value
    y = vector.y == value
    return x and y
    
'GLKVector2Make', 'GLKVector2MakeWithArray', 'GLKVector2Length', 'GLKVector2Distance', 'GLKVector2Negate', 'GLKVector2Normalize', 'GLKVector2AddScalar', 'GLKVector2SubtractScalar', 'GLKVector2MultiplyScalar', 'GLKVector2DivideScalar', 'GLKVector2Add', 'GLKVector2Subtract', 'GLKVector2Multiply', 'GLKVector2Divide', 'GLKVector2DotProduct', 'GLKVector2Lerp', 'GLKVector2Project', 'GLKVector2Maximum', 'GLKVector2Minimum', 'GLKVector2EqualToScalar', 'GLKVector2AllEqualToVector4', 'GLKVector2AllGreaterThanOrEqualToScalar', 
    
def GLKVector2AllEqualToVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    x = vectorLeft.x == vectorRight.x
    y = vectorLeft.y == vectorRight.y
    return x and y
    
def GLKVector2AllGreaterThanOrEqualToScalar(vector, value):
    x = vector.x >= value
    y = vector.y >= value
    return x and y
    
def GLKVector2AllGreaterThanOrEqualToVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    x = vectorLeft.x >= vectorRight.x
    y = vectorLeft.y >= vectorRight.y
    return x and y
    
def GLKVector2AllGreaterThanScalar(vector, value):
    x = vector.x > value
    y = vector.y > value
    return x and y
    
def GLKVector2AllGreaterThanVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector2)
    x = vectorLeft.x > vectorRight.x
    y = vectorLeft.y > vectorRight.y
    return x and y

__all__ = ['GLKVector2', 'setGLKVector2', 'getGLKVector2']

if __name__ == '__main__':
    v = GLKVector2Make(1, 1)
    print v
    print GLKVector2AddScalar(v, 10)
    print GLKVector2Length(GLKVector2Normalize(GLKVector2AddScalar(v, 10)))
    print GLKVector2Minimum(v, GLKVector2MultiplyScalar(v, 35))
    print GLKVector2Normalize(GLKVector2AddScalar(v, 10))
    print GLKVector2AllGreaterThanScalar(v, 1.1)
    