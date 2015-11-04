# coding: utf-8
import math
import ctypes
from objc_util import *
import vector3
import vector4
import matrix3


class vectScale(ctypes.Structure):
    _fields_ = [
                ('v', vector3.GLKVector3),
                ('s', ctypes.c_float),
                ]


class xyzw(ctypes.Structure):
    _fields_ = [
                ('x', ctypes.c_float),
                ('y', ctypes.c_float),
                ('z', ctypes.c_float),
                ('w', ctypes.c_float),
                ]


class float4(ctypes.Structure):
    _fields_ = [
                ('q', (ctypes.c_float * 4))
                ]


class GLKQuaternion(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ('s3'),
                    ]
    _fields_ = [
                ('s1', vectScale),
                ('s2', xyzw),
                ('s3', float4),
                ]
                
    def __str__(self):
        vstr = '''GLKQuaternion { %.4f\t%s }''' % (self.s1.s, self.s1.v)
        return vstr
        
def GLKQuaternionMake(x, y, z, w):
    return GLKQuaternion(x=x, y=y, z=z, w=w)
    
def GLKQuaternionMakeWithVector3(vector, scalar):
    q =  GLKQuaternion()
    q.s1.v = vector
    q.s1.s = scalar
    return q;
    
def GLKQuaternionMakeWithArray(values):
    return GLKQuaternionMake(*values)
    
def GLKQuaternionMakeWithAngleAndAxis(radians, x, y, z):
    halfAngle = radians * 0.5;
    scale = math.sin(halfAngle);
    return GLKQuaternionMake(scale * x, scale * y, scale * z, math.cos(halfAngle))
    
def GLKQuaternionMakeWithAngleAndVector3Axis(radians, axisVector):
    return GLKQuaternionMakeWithAngleAndAxis(radians, axisVector.v[0], axisVector.v[1], axisVector.v[2]);
    
def GLKQuaternionMakeWithMatrix3(matrix):
    func = c.GLKQuaternionMakeWithMatrix3
    func.argtypes = [matrix3.GLKMatrix3]
    func.restype = GLKQuaternion
    return func(matrix)
    
def GLKQuaternionAdd(quaternionLeft, quaternionRight):
    array = [
                quaternionLeft.q[0] + quaternionRight.q[0],
                quaternionLeft.q[1] + quaternionRight.q[1],
                quaternionLeft.q[2] + quaternionRight.q[2],
                quaternionLeft.q[3] + quaternionRight.q[3]]
    return GLKQuaternionMakeWithArray(array)
    
def GLKQuaternionSubtract(quaternionLeft, quaternionRight):
    array = [
                quaternionLeft.q[0] - quaternionRight.q[0],
                quaternionLeft.q[1] - quaternionRight.q[1],
                quaternionLeft.q[2] - quaternionRight.q[2],
                quaternionLeft.q[3] - quaternionRight.q[3]]
    return GLKQuaternionMakeWithArray(array)
    
def GLKQuaternionMultiply(quaternionLeft, quaternionRight):
    array = [
                quaternionLeft.q[3] * quaternionRight.q[0] +
                quaternionLeft.q[0] * quaternionRight.q[3] +
                quaternionLeft.q[1] * quaternionRight.q[2] -
                quaternionLeft.q[2] * quaternionRight.q[1],
                
                quaternionLeft.q[3] * quaternionRight.q[1] +
                quaternionLeft.q[1] * quaternionRight.q[3] +
                quaternionLeft.q[2] * quaternionRight.q[0] -
                quaternionLeft.q[0] * quaternionRight.q[2],
                
                quaternionLeft.q[3] * quaternionRight.q[2] +
                quaternionLeft.q[2] * quaternionRight.q[3] +
                quaternionLeft.q[0] * quaternionRight.q[1] -
                quaternionLeft.q[1] * quaternionRight.q[0],
                
                quaternionLeft.q[3] * quaternionRight.q[3] -
                quaternionLeft.q[0] * quaternionRight.q[0] -
                quaternionLeft.q[1] * quaternionRight.q[1] -
                quaternionLeft.q[2] * quaternionRight.q[2]]
    return GLKQuaternionMakeWithArray(array)
    
def GLKQuaternionLength(quaternion):
    return math.sqrt(
                    quaternion.q[0] * quaternion.q[0] + 
                    quaternion.q[1] * quaternion.q[1] +
                    quaternion.q[2] * quaternion.q[2] +
                    quaternion.q[3] * quaternion.q[3]);
                    
def GLKQuaternionConjugate(quaternion):
    return GLKQuaternionMakeWithArray([
                                        -quaternion.q[0], -quaternion.q[1],
                                        -quaternion.q[2], quaternion.q[3]])

def GLKQuaternionInvert(quaternion):
    scale = 1.0 / (
                        quaternion.q[0] * quaternion.q[0] + 
                        quaternion.q[1] * quaternion.q[1] +
                        quaternion.q[2] * quaternion.q[2] +
                        quaternion.q[3] * quaternion.q[3]);
    return GLKQuaternionMakeWithArray([
                                        -quaternion.q[0] * scale, -quaternion.q[1] * scale,
                                        -quaternion.q[2] * scale, quaternion.q[3] * scale])
                                        
def GLKQuaternionNormalize(quaternion):
    scale = 1.0 / GLKQuaternionLength(quaternion);
    return GLKQuaternionMakeWithArray([
                                        quaternion.q[0] * scale, quaternion.q[1] * scale,
                                        quaternion.q[2] * scale, quaternion.q[3] * scale])
                                        
def GLKQuaternionRotateVector3(quaternion, vector):
    rotatedQuaternion = GLKQuaternionMake(vector.v[0], vector.v[1], vector.v[2], 0.0);
    rotatedQuaternion = GLKQuaternionMultiply(GLKQuaternionMultiply(quaternion, rotatedQuaternion), GLKQuaternionInvert(quaternion));
    
    return vector3.GLKVector3Make(rotatedQuaternion.q[0], rotatedQuaternion.q[1], rotatedQuaternion.q[2]);

def GLKQuaternionRotateVector4(quaternion, vector):
    rotatedQuaternion = GLKQuaternionMake(vector.v[0], vector.v[1], vector.v[2], 0.0);
    rotatedQuaternion = GLKQuaternionMultiply(GLKQuaternionMultiply(quaternion, rotatedQuaternion), GLKQuaternionInvert(quaternion));
    
    return vector4.GLKVector4Make(rotatedQuaternion.q[0], rotatedQuaternion.q[1], rotatedQuaternion.q[2], vector.v[3]);
    
__all__ = ['GLKQuaternion', 'GLKQuaternionMake', 'GLKQuaternionMakeWithVector3', 'GLKQuaternionMakeWithArray', 'GLKQuaternionMakeWithAngleAndAxis', 'GLKQuaternionMakeWithAngleAndVector3Axis', 'GLKQuaternionAdd', 'GLKQuaternionSubtract', 'GLKQuaternionMultiply', 'GLKQuaternionLength', 'GLKQuaternionConjugate', 'GLKQuaternionInvert', 'GLKQuaternionNormalize', 'GLKQuaternionRotateVector3', 'GLKQuaternionRotateVector4']
    
if __name__ == '__main__':
    q1 = GLKQuaternionMakeWithAngleAndAxis(10, 0, 1, 0)
    q2 = GLKQuaternionMakeWithAngleAndAxis(10, 0, 1, 5)
    q3 = GLKQuaternionMakeWithAngleAndAxis(10, 7, 1, 0)
    print GLKQuaternionSubtract(GLKQuaternionAdd(q1, q2), q3)
    print GLKQuaternionMultiply(q1, q3)
    print GLKQuaternionLength(q2)