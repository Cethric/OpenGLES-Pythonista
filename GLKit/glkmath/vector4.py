# coding: utf-8
import math
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
                
    def __str__(self):
        r = []
        s1 = self.s1
        s2 = self.s2
        s3 = self.s3
        s4 = self.s4
        r.extend([float(x) for x in s4.v])
        vstr = '''GLKVector4 { %.4f\t%.4f\t%.4f\t%.4f }''' % tuple(r)
        return vstr
        

glk4 = parse_struct('{glkvec4=ffff}')

def to_glk4(old):
    return ctypes.cast(ctypes.pointer(old),ctypes.POINTER(glk4)).contents
    
def from_glk4(old):
    return ctypes.cast(ctypes.pointer(old),ctypes.POINTER(GLKVector4)).contents
    
def getGLKVector4(func):
    return from_glk4(func(restype=glk4, argtypes=[]))
    
def setGLKVector4(func, newvalue):
    newvalue = to_glk4(newvalue)
    return func(newvalue, restype=ctypes.c_void_p, argtypes=[glk4])
    
    
def GLKVector4Make(x, y, z, w):
    return GLKVector4(x=x, y=y, z=z, w=w)
    
def GLKVector4MakeWithArray(array):
    return GLKVector4(v=(ctypes.c_float * 4)(*array))
    
def GLKVector4MakeWithVector3(vec3, w):
    return GLKVector4(x=vec3.x, y=vec3.y, z=vec3.z, w=w)
    
def GLKVector4Length(vector):
    v = [float(x) for x in vector.v]
    r = 0
    for x in v:
        r += math.pow(x, 2)
    return math.sqrt(r)
    
def GLKVector4Distance(vectorStart, vectorEnd):
    assert isinstance(vectorEnd, GLKVector4)
    return math.sqrt(math.pow(vectorStart.x - vectorEnd.x, 2) +
                     math.pow(vectorStart.y - vectorEnd.y, 2) +
                     math.pow(vectorStart.z - vectorEnd.z, 2) +
                     math.pow(vectorStart.w - vectorEnd.z, 2))
                     
def GLKVector4Negate(vector):
    v = GLKVector4()
    v.x = -vector.x
    v.y = -vector.y
    v.z = -vector.z
    v.w = -vector.w
    return v
    
def GLKVector4Normalize(vector):
    l = GLKVector4Length(vector)
    nv = GLKVector4()
    if l != 0:
        nv.x = vector.x / l
        nv.y = vector.y / l
        nv.z = vector.z / l
        nv.w = vector.w / l
        return nv
    else:
        raise ValueError('Cannot Normalise Vector of length 0')

def GLKVector4AddScalar(vector, value):
    v = GLKVector4()
    v.x = vector.x + value
    v.y = vector.y + value
    v.z = vector.z + value
    v.w = vector.w + value
    return v
    
def GLKVector4SubtractScalar(vector, value):
    v = GLKVector4()
    v.x = vector.x - value
    v.y = vector.y - value
    v.z = vector.z - value
    v.w = vector.w - value
    return v
    
def GLKVector4MultiplyScalar(vector, value):
    v = GLKVector4()
    v.x = vector.x * value
    v.y = vector.y * value
    v.z = vector.z * value
    v.w = vector.w * value
    return v
    
def GLKVector4DivideScalar(vector, value):
    v = GLKVector4()
    v.x = vector.x / value
    v.y = vector.y / value
    v.z = vector.z / value
    v.w = vector.w / value
    return v
    
def GLKVector4Add(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = vectorLeft.x + vectorRight.x
    v.y = vectorLeft.y + vectorRight.y
    v.z = vectorLeft.z + vectorRight.z
    v.w = vectorLeft.w + vectorRight.w
    return v
    
def GLKVector4Subtract(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = vectorLeft.x - vectorRight.x
    v.y = vectorLeft.y - vectorRight.y
    v.z = vectorLeft.z - vectorRight.z
    v.w = vectorLeft.w - vectorRight.w
    return v
    
def GLKVector4Multiply(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = vectorLeft.x * vectorRight.x
    v.y = vectorLeft.y * vectorRight.y
    v.z = vectorLeft.z * vectorRight.z
    v.w = vectorLeft.w * vectorRight.w
    return v
    
def GLKVector4Divide(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = vectorLeft.x / vectorRight.x
    v.y = vectorLeft.y / vectorRight.y
    v.z = vectorLeft.z / vectorRight.z
    v.w = vectorLeft.w / vectorRight.w
    return v
    
def GLKVector4DotProduct(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    return vectorLeft.x * vectorRight.x + vectorLeft.y * vectorRight.y + vectorLeft.z * vectorRight.z + vectorLeft.w * vectorRight.w
    
def GLKVector4CrossProduct(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = vectorLeft.y * vectorRight.z - vectorLeft.z * vectorRight.y
    v.y = vectorLeft.z * vectorRight.x - vectorLeft.x * vectorRight.z
    v.z = vectorLeft.x * vectorRight.y - vectorLeft.y * vectorRight.x
    v.w = 0
    return v
    
def GLKVector4Lerp(vectorStart, vectorEnd, t):
    assert isinstance(vectorEnd, GLKVector4)
    v = GLKVector4()
    v.x = vectorStart.x + ((vectorEnd.x - vectorStart.x) * t)
    v.y = vectorStart.y + ((vectorEnd.y - vectorStart.y) * t)
    v.z = vectorStart.z + ((vectorEnd.z - vectorStart.z) * t)
    v.w = vectorStart.w + ((vectorEnd.w - vectorStart.w) * t)
    
def GLKVector4Project(vectorToProject, projectionVector):
    assert isinstance(projectionVector, GLKVector4)
    scale = GLKVector4DotProduct(projectionVector, vectorToProject)
    scale /= GLKVector4DotProduct(projectionVector, projectionVector)
    v = GLKVector4MultiplyScalar(projectionVector, scale)
    return v
    
def GLKVector4Maximum(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = max(vectorLeft.x, vectorRight.x)
    v.y = max(vectorLeft.y, vectorRight.y)
    v.z = max(vectorLeft.z, vectorRight.z)
    v.w = max(vectorLeft.w, vectorRight.w)
    return v
    
def GLKVector4Minimum(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    v = GLKVector4()
    v.x = min(vectorLeft.x, vectorRight.x)
    v.y = min(vectorLeft.y, vectorRight.y)
    v.z = min(vectorLeft.z, vectorRight.z)
    v.w = min(vectorLeft.w, vectorRight.w)
    return v
    
def GLKVector4EqualToScalar(vector, value):
    x = vector.x == value
    y = vector.y == value
    z = vector.z == value
    w = vector.w == value
    return x and y and z and w
    
def GLKVector4AllEqualToVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    x = vectorLeft.x == vectorRight.x
    y = vectorLeft.y == vectorRight.y
    z = vectorLeft.z == vectorRight.z
    w = vectorLeft.w == vectorRight.w
    return x and y and z and w
    
def GLKVector4AllGreaterThanOrEqualToScalar(vector, value):
    x = vector.x >= value
    y = vector.y >= value
    z = vector.z >= value
    w = vector.w >= value
    return x and y and z and w
    
def GLKVector4AllGreaterThanOrEqualToVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    x = vectorLeft.x >= vectorRight.x
    y = vectorLeft.y >= vectorRight.y
    z = vectorLeft.z >= vectorRight.z
    w = vectorLeft.w >= vectorRight.w
    return x and y and z and w
    
def GLKVector4AllGreaterThanScalar(vector, value):
    x = vector.x > value
    y = vector.y > value
    z = vector.z > value
    w = vector.w > value
    return x and y and z and w
    
def GLKVector4AllGreaterThanVector4(vectorLeft, vectorRight):
    assert isinstance(vectorRight, GLKVector4)
    x = vectorLeft.x > vectorRight.x
    y = vectorLeft.y > vectorRight.y
    z = vectorLeft.z > vectorRight.z
    w = vectorLeft.w > vectorRight.w
    return x and y and z and w
    
__all__ = ['GLKVector4', 'getGLKVector4', 'setGLKVector4', 'GLKVector4Make', 'GLKVector4MakeWithArray', 'GLKVector4MakeWithVector3', 'GLKVector4Length', 'GLKVector4Distance', 'GLKVector4Negate', 'GLKVector4Normalize', 'GLKVector4AddScalar', 'GLKVector4SubtractScalar', 'GLKVector4MultiplyScalar', 'GLKVector4DivideScalar', 'GLKVector4Add', 'GLKVector4Subtract', 'GLKVector4Multiply', 'GLKVector4Divide', 'GLKVector4DotProduct', 'GLKVector4CrossProduct', 'GLKVector4Lerp', 'GLKVector4Project', 'GLKVector4Maximum', 'GLKVector4Minimum', 'GLKVector4EqualToScalar', 'GLKVector4AllEqualToVector4', 'GLKVector4AllGreaterThanOrEqualToScalar', 'GLKVector4AllGreaterThanOrEqualToVector4', 'GLKVector4AllGreaterThanScalar', 'GLKVector4AllGreaterThanVector4']

if __name__ == '__main__':
    v = GLKVector4Make(1, 1, 1, 1)
    print v
    print GLKVector4AddScalar(v, 10)
    print GLKVector4Length(GLKVector4Normalize(GLKVector4AddScalar(v, 10)))
    print GLKVector4Minimum(v, GLKVector4MultiplyScalar(v, 35))
    print GLKVector4Normalize(GLKVector4AddScalar(v, 10))
    print GLKVector4AllGreaterThanScalar(v, 1.1)
    