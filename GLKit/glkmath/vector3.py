# coding: utf-8
import ctypes
import math
from objc_util import *


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
        r.extend([float(x) for x in s4.v])
        vstr = '''GLKVector3 { %.4f\t%.4f\t%.4f }''' % tuple(r)
        return vstr
        

glk3 = parse_struct('{glkvec3=fff}')

def to_glk3(old):
    return ctypes.cast(ctypes.pointer(old),ctypes.POINTER(glk3)).contents
    
def from_glk3(old):
    return ctypes.cast(ctypes.pointer(old),ctypes.POINTER(GLKVector3)).contents
    
def getGLKVector3(func):
    return from_glk3(func(restype=glk3, argtypes=[]))
    
def setGLKVector3(func, newvalue):
    newvalue = to_glk3(newvalue)
    return func(newvalue, restype=ctypes.c_void_p, argtypes=[glk3])
    
def GLKVector3Make(x, y, z):
    return GLKVector3(x=x, y=y, z=z)
    
def GLKVector3MakeWithArray(values):
    return GLKVector3(v=(ctypes.c_float * 3)(*values))
    
def GLKVector3Length(vector):
    v = [float(x) for x in vector.v]
    r = 0
    for x in v:
        r += math.pow(x, 2)
    return math.sqrt(r)
    
def GLKVector3Distance(vectorStart, vectorEnd):
    assert isinstance(vectorEnd, GLKVector3)
    return math.sqrt(math.pow(vectorStart.x - vectorEnd.x, 2) +
                     math.pow(vectorStart.y - vectorEnd.y, 2) +
                     math.pow(vectorStart.z - vectorEnd.z, 2))
                     
def GLKVector3Negate(vector):
    v = GLKVector3()
    v.x = -vector.x
    v.y = -vector.y
    v.z = -vector.z
    return v
    
def GLKVector3Normalize(vector):
    l = GLKVector3Length(vector)
    nv = GLKVector3()
    if l != 0:
        nv.x = vector.x / l
        nv.y = vector.y / l
        nv.z = vector.z / l
        return nv
    else:
        raise ValueError('Cannot Normalise Vector of length 0')

def GLKVector3AddScalar(vector, value):
    v = GLKVector3()
    v.x = vector.x + value
    v.y = vector.y + value
    v.z = vector.z + value
    return v
    
def GLKVector3SubtractScalar(vector, value):
    v = GLKVector3()
    v.x = vector.x - value
    v.y = vector.y - value
    v.z = vector.z - value
    return v
    
def GLKVector3MultiplyScalar(vector, value):
    v = GLKVector3()
    v.x = vector.x * value
    v.y = vector.y * value
    v.z = vector.z * value
    return v
    
def GLKVector3DivideScalar(vector, value):
    v = GLKVector3()
    v.x = vector.x / value
    v.y = vector.y / value
    v.z = vector.z / value
    return v
    
def GLKVector3Add(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = vectorLeft.x + vectorRight.x
    v.y = vectorLeft.y + vectorRight.y
    v.z = vectorLeft.z + vectorRight.z
    return v
    
def GLKVector3Subtract(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = vectorLeft.x - vectorRight.x
    v.y = vectorLeft.y - vectorRight.y
    v.z = vectorLeft.z - vectorRight.z
    return v
    
def GLKVector3Multiply(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = vectorLeft.x * vectorRight.x
    v.y = vectorLeft.y * vectorRight.y
    v.z = vectorLeft.z * vectorRight.z
    return v
    
def GLKVector3Divide(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = vectorLeft.x / vectorRight.x
    v.y = vectorLeft.y / vectorRight.y
    v.z = vectorLeft.z / vectorRight.z
    return v
    
def GLKVector3DotProduct(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    return vectorLeft.x * vectorRight.x + vectorLeft.y * vectorRight.y + vectorLeft.z * vectorRight.z
    
def GLKVector3CrossProduct(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = vectorLeft.y * vectorRight.z - vectorLeft.z * vectorRight.y
    v.y = vectorLeft.z * vectorRight.x - vectorLeft.x * vectorRight.z
    v.z = vectorLeft.x * vectorRight.y - vectorLeft.y * vectorRight.x
    return v
    
def GLKVector3Lerp(vectorStart, vectorEnd, t):
    assert isinstance(vectorEnd, GLKVector3)
    v = GLKVector3()
    v.x = vectorStart.x + ((vectorEnd.x - vectorStart.x) * t)
    v.y = vectorStart.y + ((vectorEnd.y - vectorStart.y) * t)
    v.z = vectorStart.z + ((vectorEnd.z - vectorStart.z) * t)
    
def GLKVector3Project(vectorToProject, projectionVector):
    assert isinstance(projectionVector, GLKVector3)
    scale = GLKVector3DotProduct(projectionVector, vectorToProject)
    scale /= GLKVector3DotProduct(projectionVector, projectionVector)
    v = GLKVector3MultiplyScalar(projectionVector, scale)
    return v
    
def GLKVector3Maximum(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = max(vectorLeft.x, vectorRight.x)
    v.y = max(vectorLeft.y, vectorRight.y)
    v.z = max(vectorLeft.z, vectorRight.z)
    return v
    
def GLKVector3Minimum(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    v = GLKVector3()
    v.x = min(vectorLeft.x, vectorRight.x)
    v.y = min(vectorLeft.y, vectorRight.y)
    v.z = min(vectorLeft.z, vectorRight.z)
    return v
    
def GLKVector3EqualToScalar(vector, value):
    x = vector.x == value
    y = vector.y == value
    z = vector.z == value
    return x and y and z
    
def GLKVector3AllEqualToVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    x = vectorLeft.x == vectorRight.x
    y = vectorLeft.y == vectorRight.y
    z = vectorLeft.z == vectorRight.z
    return x and y and z
    
def GLKVector3AllGreaterThanOrEqualToScalar(vector, value):
    x = vector.x >= value
    y = vector.y >= value
    z = vector.z >= value
    return x and y and z
    
def GLKVector3AllGreaterThanOrEqualToVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    x = vectorLeft.x >= vectorRight.x
    y = vectorLeft.y >= vectorRight.y
    z = vectorLeft.z >= vectorRight.z
    return x and y and z
    
def GLKVector3AllGreaterThanScalar(vector, value):
    x = vector.x > value
    y = vector.y > value
    z = vector.z > value
    return x and y and z
    
def GLKVector3AllGreaterThanVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector3)
    x = vectorLeft.x > vectorRight.x
    y = vectorLeft.y > vectorRight.y
    z = vectorLeft.z > vectorRight.z
    return x and y and z

__all__ = ['GLKVector3', 'setGLKVector3', 'getGLKVector3', 'GLKVector3Make', 'GLKVector3MakeWithArray', 'GLKVector3Length', 'GLKVector3Distance', 'GLKVector3Negate', 'GLKVector3Normalize', 'GLKVector3AddScalar', 'GLKVector3SubtractScalar', 'GLKVector3MultiplyScalar', 'GLKVector3DivideScalar', 'GLKVector3Add', 'GLKVector3Subtract', 'GLKVector3Multiply', 'GLKVector3Divide', 'GLKVector3DotProduct', 'GLKVector3CrossProduct', 'GLKVector3Lerp', 'GLKVector3Project', 'GLKVector3Maximum', 'GLKVector3Minimum', 'GLKVector3EqualToScalar', 'GLKVector3AllEqualToVector4', 'GLKVector3AllGreaterThanOrEqualToScalar', 'GLKVector3AllGreaterThanOrEqualToVector4', 'GLKVector3AllGreaterThanScalar', 'GLKVector3AllGreaterThanVector4']

if __name__ == '__main__':
    v = GLKVector3Make(1, 1, 1)
    print v
    print GLKVector3AddScalar(v, 10)
    print GLKVector3Length(GLKVector3Normalize(GLKVector3AddScalar(v, 10)))
    print GLKVector3Minimum(v, GLKVector3MultiplyScalar(v, 35))
    print GLKVector3Normalize(GLKVector3AddScalar(v, 10))
    print GLKVector3AllGreaterThanScalar(v, 1.1)
    v1 = GLKVector3Make(5, 0, 0)
    print GLKVector3Length(v1)