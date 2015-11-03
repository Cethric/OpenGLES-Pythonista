# coding: utf-8
import ctypes
from objc_util import *
import matrix4
import matrix3
import matrix2
import vector3
import vector4

def CFAllocatorGetDefault():
    func = c.CFAllocatorGetDefault
    func.argtypes = None
    func.restype = ctypes.c_void_p
    return ObjCInstance(func())

def GLKMatrixStackCreate(alloc):
    func = c.GLKMatrixStackCreate
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_void_p
    return ObjCInstance(func(ObjCInstance(alloc).ptr))
    
def GLKMatrixStackGetTypeID(stack_ptr):
    func = c.GLKMatrixStackGetTypeID
    func.argtypes = None
    func.restype = ctypes.c_void_p
    return ObjCInstance(func())
    
def GLKMatrixStackPush(stack):
    func = c.GLKMatrixStackPush
    func.argtypes = [ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackPop(stack):
    func = c.GLKMatrixStackPop
    func.argtypes = [ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackSize(stack):
    func = c.GLKMatrixStackSize
    func.argtypes = [ctypes.c_void_p]
    func.restype = ctypes.c_int
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackLoadMatrix4(stack, matrix):
    func = c.GLKMatrixStackLoadMatrix4
    func.argtypes = [ctypes.c_void_p, matrix4.GLKMatrix4]
    func.restype = None
    return func(ObjCInstance(stack).ptr, matrix)
    
def GLKMatrixStackGetMatrix4(stack):
    func = c.GLKMatrixStackGetMatrix4
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix4.GLKMatrix4
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackGetMatrix3(stack):
    func = c.GLKMatrixStackGetMatrix3
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix3.GLKMatrix3
    return func(ObjCInstance(stack).ptr)

def GLKMatrixStackGetMatrix2(stack):
    func = c.GLKMatrixStackGetMatrix2
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix2.GLKMatrix2
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackGetMatrix4Inverse(stack):
    func = c.GLKMatrixStackGetMatrix4Inverse
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix4.GLKMatrix4
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackGetMatrix4InverseTranspose(stack):
    func = c.GLKMatrixStackGetMatrix4InverseTranspose
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix4.GLKMatrix4
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackGetMatrix3Inverse(stack):
    func = c.GLKMatrixStackGetMatrix3Inverse
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix3.GLKMatrix3
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackGetMatrix3InverseTranspose(stack):
    func = c.GLKMatrixStackGetMatrix3InverseTranspose
    func.argtypes = [ctypes.c_void_p]
    func.restype = matrix3.GLKMatrix3
    return func(ObjCInstance(stack).ptr)
    
def GLKMatrixStackMultiplyMatrix4(stack, matrix):
    func = c.GLKMatrixStackMultiplyMatrix4
    func.argtypes = [ctypes.c_void_p, matrix4.GLKMatrix4]
    func.restype = None
    return func(ObjCInstance(stack).ptr, matrix)
    
def GLKMatrixStackMultiplyMatrixStack(stackLeft, stackRight):
    func = c.GLKMatrixStackMultiplyMatrixStack
    func.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    func.restype = None
    return func(ObjCInstance(stackLeft).ptr, ObjCInstance(stackRight).ptr)
    
def GLKMatrixStackTranslate(stack, tx, ty, tz):
    func = c.GLKMatrixStackTranslate
    func.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float]
    func.restype = None
    return func(ObjCInstance(stack), tx, ty, tz)
    
def GLKMatrixStackTranslateWithVector3(stack, translationVector):
    func = c.GLKMatrixStackTranslateWithVector3
    func.argtypes = [ctypes.c_void_p, vector3.GLKVector3]
    func.restype = None
    return func(ObjCInstance(stack).ptr, translationVector)
    
def GLKMatrixStackTranslateWithVector4(stack, translationVector):
    func = c.GLKMatrixStackTranslateWithVector4
    func.argtypes = [ctypes.c_void_p, vector4.GLKVector4]
    func.restype = None
    return func(ObjCInstance(stack).ptr, translationVector)
    
def GLKMatrixStackScale(stack, sx, sy, sz):
    func = c.GLKMatrixStackScale
    func.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float]
    func.restype = None
    return func(ObjCInstance(stack), sx, sy, sz)
    
def GLKMatrixStackScaleWithVector3(stack, scaleVector):
    func = c.GLKMatrixStackScaleWithVector3
    func.argtypes = [ctypes.c_void_p, vector3.GLKVector3]
    func.restype = None
    return func(ObjCInstance(stack).ptr, scaleVector)
    
def GLKMatrixStackScaleWithVector4(stack, scaleVector):
    func = c.GLKMatrixStackScaleWithVector4
    func.argtypes = [ctypes.c_void_p, vector4.GLKVector4]
    func.restype = None
    return func(ObjCInstance(stack).ptr, scaleVector)
    
def GLKMatrixStackRotate(stack, radians, x, y, z):
    func = c.GLKMatrixStackRotate
    func.argtypes = [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
    func.restype = None
    return func(ObjCInstance(stack), radians, x, y, z)
    
def GLKMatrixStackRotateWithVector3(stack, radians, axisVector):
    func = c.GLKMatrixStackRotateWithVector3
    func.argtypes = [ctypes.c_void_p, ctypes.c_float,vector3.GLKVector3]
    func.restype = None
    return func(ObjCInstance(stack).ptr, radians, axisVector)
    
def GLKMatrixStackRotateWithVector4(stack, radians, axisVector):
    func = c.GLKMatrixStackRotateWithVector4
    func.argtypes = [ctypes.c_void_p, ctypes.c_float, vector4.GLKVector4]
    func.restype = None
    return func(ObjCInstance(stack).ptr, radians, axisVector)
    
def GLKMatrixStackRotateX(stack, radians):
    func = c.GLKMatrixStackRotateX
    func.argtypes = [ctypes.c_void_p, ctypes.c_float]
    func.restype = None
    return func(ObjCInstance(stack).ptr, radians)

def GLKMatrixStackRotateY(stack, radians):
    func = c.GLKMatrixStackRotateY
    func.argtypes = [ctypes.c_void_p, ctypes.c_float]
    func.restype = None
    return func(ObjCInstance(stack).ptr, radians)

def GLKMatrixStackRotateZ(stack, radians):
    func = c.GLKMatrixStackRotateZ
    func.argtypes = [ctypes.c_void_p, ctypes.c_float]
    func.restype = None
    return func(ObjCInstance(stack).ptr, radians)
    
__all__ = ['CFAllocatorGetDefault', 'GLKMatrixStackCreate', 'GLKMatrixStackGetTypeID', 'GLKMatrixStackPush', 'GLKMatrixStackPop', 'GLKMatrixStackSize', 'GLKMatrixStackLoadMatrix4', 'GLKMatrixStackGetMatrix4', 'GLKMatrixStackGetMatrix3', 'GLKMatrixStackGetMatrix2', 'GLKMatrixStackGetMatrix4Inverse', 'GLKMatrixStackGetMatrix4InverseTranspose', 'GLKMatrixStackGetMatrix3Inverse', 'GLKMatrixStackGetMatrix3InverseTranspose', 'GLKMatrixStackMultiplyMatrix4', 'GLKMatrixStackMultiplyMatrixStack', 'GLKMatrixStackTranslate', 'GLKMatrixStackTranslateWithVector3', 'GLKMatrixStackTranslateWithVector4', 'GLKMatrixStackScale', 'GLKMatrixStackScaleWithVector3', 'GLKMatrixStackScaleWithVector4', 'GLKMatrixStackRotate', 'GLKMatrixStackRotateWithVector3', 'GLKMatrixStackRotateWithVector4', 'GLKMatrixStackRotateX', 'GLKMatrixStackRotateY', 'GLKMatrixStackRotateZ']
    
if __name__ == '__main__':
    stack = GLKMatrixStackCreate(CFAllocatorGetDefault())
    GLKMatrixStackPush(stack)
    GLKMatrixStackPush(stack)
    GLKMatrixStackPop(stack)
    GLKMatrixStackPop(stack)
    GLKMatrixStackPop(stack)
    GLKMatrixStackPop(stack)
    print stack
    print GLKMatrixStackSize(stack)
    
    GLKMatrixStackLoadMatrix4(stack, matrix4.GLKMatrix4MakeTranslation(10, 0, 0))
    
    print GLKMatrixStackGetMatrix4(stack)
    
    GLKMatrixStackTranslate(stack, 10, 4, 8)