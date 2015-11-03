# coding: utf-8
import math
import ctypes
from objc_util import *

import matrix4
import matrix3
import matrix2
import vector3
import vector4
import quaternion


def GLKMathDegreesToRadians(degrees):
    return degrees * (math.pi / 180)
    
def GLKMathRadiansToDegrees(radians):
    return radians * (180 / math.pi)

def GLKMathProject(object, model, projection, viewport):
    func = c.GLKMathProject
    func.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
    func.restyps = ctypes.c_void_p
    return func(object, model, projection, viewport)
    
def GLKMathUnproject(window, model, projection, viewport, success):
    func = c.GLKMathUnproject
    func.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool)]
    func.restype = ctypes.c_void_p
    return func(window, model, projection, viewport, success)
    
def NSStringFromGLKMatrix2(matrix):
    func = c.NSStringFromGLKMatrix2
    func.argtypes = [matrix2.GLKMatrix2]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(matrix))
    
def NSStringFromGLKMatrix3(matrix):
    func = c.NSStringFromGLKMatrix3
    func.argtypes = [matrix3.GLKMatrix3]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(matrix))
    
def NSStringFromGLKMatrix4(matrix):
    func = c.NSStringFromGLKMatrix4
    func.argtypes = [matrix4.GLKMatrix4]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(matrix))
    
def NSStringFromGLKVector2(vector):
    func = c.NSStringFromGLKVector2
    func.argtypes = [vector2.GLKVector2]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(vector))
    
def NSStringFromGLKVector3(vector):
    func = c.NSStringFromGLKVector3
    func.argtypes = [vector3.GLKVector3]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(vector))
    
def NSStringFromGLKVector4(vector):
    func = c.NSStringFromGLKVector4
    func.argtypes = [vector4.GLKVector4]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(vector))
    
def NSStringFromGLKQuaternion(quat):
    func = c.NSStringFromGLKQuaternion
    func.argtypes = [quaternion.GLKQuaternion]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(quat))
    
    
__all__ = ['GLKMathDegreesToRadians', 'GLKMathRadiansToDegrees', 'GLKMathProject', 'GLKMathUnproject', 'NSStringFromGLKMatrix2', 'NSStringFromGLKMatrix3', 'NSStringFromGLKMatrix4', 'NSStringFromGLKVector2', 'NSStringFromGLKVector3', 'NSStringFromGLKVector4', 'NSStringFromGLKQuaternion']
    
if __name__ == '__main__':
    m = matrix4.GLKMatrix4Identity()
    print NSStringFromGLKMatrix4(m)
    q = quaternion.GLKQuaternionNormalize(quaternion.GLKQuaternionMakeWithAngleAndAxis(40, 5, 8, 9))
    print q
    print NSStringFromGLKQuaternion(q)