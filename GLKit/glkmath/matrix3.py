# coding: utf-8
import math
import ctypes
import vector3
import matrix2
import quaternion
from objc_util import *


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
        mstr = '''GLKMatrix3 { {%.3f\t%.3f\t%.3f}\t{%.3f\t%.3f\t%.3f}\t{%.3f\t%.3f\t%.3f} }'''
        mstr %= tuple([float(x) for x in self.s1.m])
        return mstr


def GLKMatrix3Make(m00, m01, m02, m10, m11, m12, m20, m21, m22):
    m = GLKMatrix3()
    m.m00 = m00
    m.m01 = m01
    m.m02 = m02
    m.m10 = m10
    m.m11 = m11
    m.m12 = m12
    m.m20 = m20
    m.m21 = m21
    m.m22 = m22
    return m
    
def GLKMatrix3MakeIdentity():
    return GLKMatrix3Make(1,0,0, 0,1,0, 0,0,1)
    
def GLKMatrix3MakeAndTranspose(m00, m01, m02, m10, m11, m12, m20, m21, m22):
    return GLKMatrix3Transpose(GLKMatrix3Make(m00, m01, m02, m10, m11, m12, m20, m21, m22))
    
def GLKMatrix3MakeWithArray(values):
    m = GLKMatrix3()
    m.m = (ctypes.c_float * 9)(*values)
    return m
    
def GLKMatrix3MakeWithArrayAndTranspose(values):
    return GLKMatrix3Transpose(GLKMatrix3MakeWithArray(values))
    
def GLKMatrix3MakeWithColumns(column0, column1, column2):
    m = GLKMatrix3()
    m.m00 = column0.x
    m.m01 = column0.y
    m.m02 = column0.z
    m.m10 = column1.x
    m.m11 = column1.y
    m.m12 = column1.z
    m.m20 = column2.x
    m.m21 = column2.y
    m.m22 = column2.z
    return m
    
def GLKMatrix3MakeWithRows(row0, row1, row2):
    m = GLKMatrix3()
    m.m00 = row0.x
    m.m01 = row1.x
    m.m02 = row2.x
    m.m10 = row0.y
    m.m11 = row1.y
    m.m12 = row2.y
    m.m20 = row0.z
    m.m21 = row1.z
    m.m22 = row2.z
    return m
    
def GLKMatrix3MakeRotation(radians, x, y, z):
    v = vector3.GLKVector3Normalize(vector3.GLKVector3Make(x, y, z))
    cos = math.cos(radians)
    cosp = 1.0 - cos
    sin = math.sin(radians)
    
    m = GLKMatrix3()
    m.m00 = cos + cosp * v.x * v.x
    m.m01 = cosp * v.x * v.y + v.z * sin
    m.m02 = cosp * v.x * v.z - v.y * sin
    
    m.m10 = cosp * v.x * v.y - v.z * sin
    m.m11 = cos + cosp * v.y * v.y
    m.m12 = cosp * v.y * v.z + v.x * sin
    
    m.m20 = cosp * v.x * v.z + v.y * sin
    m.m21 = cosp * v.y * v.z - v.x * sin
    m.m22 = cos + cosp * v.z * v.z
    
    return m
    
def GLKMatrix3MakeXRotation(radians):
    cos = math.cos(radians)
    sin = math.sin(radians)
    
    m = GLKMatrix3()
    m.m00 = 1.0
    m.m01 = 0.0
    m.m02 = 0.0
    
    m.m10 = 0.0
    m.m11 = cos
    m.m12 = sin
    
    m.m20 = 0.0
    m.m21 = -sin
    m.m22 = cos
    
    return m
    
def GLKMatrix3MakeYRotation(radians):
    cos = math.cos(radians)
    sin = math.sin(radians)
    
    m = GLKMatrix3()
    m.m00 = cos
    m.m01 = 0.0
    m.m02 = -sin
    
    m.m10 = 0.0
    m.m11 = 1.0
    m.m12 = 0.0
    
    m.m20 = sin
    m.m21 = 0.0
    m.m22 = cos
    
    return m
    
def GLKMatrix3MakeZRotation(radians):
    cos = math.cos(radians)
    sin = math.sin(radians)
    
    m = GLKMatrix3()
    m.m00 = cos
    m.m01 = sin
    m.m02 = 0.0
    
    m.m10 = -sin
    m.m11 = cos
    m.m12 = 0.0
    
    m.m20 = 0.0
    m.m21 = 0.0
    m.m22 = 1.0
    
    return m
    
def GLKMatrix3MakeWithQuaternion(quat):
    quat = quaternion.GLKQuaternionNormalize(quat)
    x = quat.x
    y = quat.y
    z = quat.z
    w = quat.w
    
    _2x = x + x
    _2y = y + y
    _2z = z + z
    _2w = w + w
    
    m = GLKMatrix3()
    m.m00 = 1.0 - _2y * y - _2z * z
    m.m01 = _2x * y + _2w * z
    m.m02 = _2x * z - _2w * y
    
    m.m10 = _2x * y - _2w * z
    m.m11 = 1.0 - _2x * x - _2z * z
    m.m12 = _2y * z + _2w * x
    
    m.m20 = _2x * z + _2w * y
    m.m21 = _2y * z - _2w * x
    m.m22 = 1.0 - _2x * x - _2y * y
    
def GLKMatrix3MakeScale(sx, sy, sz):
    m = GLKMatrix3()
    m.m[0] = sx
    m.m[4] = sy
    m.m[8] = sz
    return m
    
def GLKMatrix3GetMatrix2(matrix):
    m = matrix2.GLKMatrix2()
    m.m[0] = matrix.m[0]
    m.m[1] = matrix.m[1]
    m.m[2] = matrix.m[3]
    m.m[3] = matrix.m[4]
    
def GLKMatrix3GetColumn(matrix, column):
    assert isinstance(column, int)
    v = vector3.GLKVector3()
    v.x = matrix.m[column * 3 + 0]
    v.y = matrix.m[column * 3 + 1]
    v.z = matrix.m[column * 3 + 2]
    return v
    
def GLKMatrix3GetRow(matrix, row):
    assert isinstance(row, int)
    v = vector3.GLKVector3()
    v.x = matrix.m[row + 0]
    v.y = matrix.m[row + 3]
    v.z = matrix.m[row + 6]
    return v
    
def GLKMatrix3SetColumn(matrix, column, vector):
    m = GLKMatrix3()
    m.m[column * 3 + 0] = vector.x
    m.m[column * 3 + 1] = vector.y
    m.m[column * 3 + 2] = vector.z

def GLKMatrix3SetRow(matrix, row, vector):
    matrix.m[row + 0] = vector.x
    matrix.m[row + 3] = vector.y
    matrix.m[row + 6] = vector.z
    return matrix
    
def GLKMatrix3Invert(matrix):
    func = c.GLKMatrix3Invert
    func.argtypes = [GLKMatrix3]
    func.restype = GLKMatrix3
    return func(matrix)
    
def GLKMatrix3Transpose(matrix):
    matrix = GLKMatrix3MakeWithArray([matrix.m[0], matrix.m[3], matrix.m[6],
                                      matrix.m[1], matrix.m[4], matrix.m[7],
                                      matrix.m[2], matrix.m[5], matrix.m[8]])
    return matrix
    
def GLKMatrix3InvertAndTranspose(matrix):
    return GLKMatrix3Transpose(GLKMatrix3Invert(matrix))
    
def GLKMatrix3Multiply(matrixLeft, matrixRight):
    rl1 = GLKMatrix3GetRow(matrixLeft, 0)
    rl2 = GLKMatrix3GetRow(matrixLeft, 1)
    rl3 = GLKMatrix3GetRow(matrixLeft, 2)
    cl1 = GLKMatrix3GetColumn(matrixRight, 0)
    cl2 = GLKMatrix3GetColumn(matrixRight, 1)
    cl3 = GLKMatrix3GetColumn(matrixRight, 2)
    
    m = GLKMatrix3()
    d10 = vector3.GLKVector3DotProduct(rl1, cl1)
    d11 = vector3.GLKVector3DotProduct(rl1, cl2)
    d12 = vector3.GLKVector3DotProduct(rl1, cl3)
    GLKMatrix3SetRow(m, 0, vector3.GLKVector3Make(d10, d11, d12))
    
    d20 = vector3.GLKVector3DotProduct(rl2, cl1)
    d21 = vector3.GLKVector3DotProduct(rl2, cl2)
    d22 = vector3.GLKVector3DotProduct(rl2, cl3)
    GLKMatrix3SetRow(m, 1, vector3.GLKVector3Make(d20, d21, d22))
    
    d30 = vector3.GLKVector3DotProduct(rl3, cl1)
    d31 = vector3.GLKVector3DotProduct(rl3, cl2)
    d32 = vector3.GLKVector3DotProduct(rl3, cl3)
    GLKMatrix3SetRow(m, 2, vector3.GLKVector3Make(d30, d31, d32))
    
    return m

__all__ = ['GLKMatrix3', 'GLKMatrix3Make', 'GLKMatrix3MakeIdentity', 'GLKMatrix3MakeAndTranspose', 'GLKMatrix3MakeWithArray', 'GLKMatrix3MakeWithArrayAndTranspose', 'GLKMatrix3MakeWithColumns', 'GLKMatrix3MakeWithRows', 'GLKMatrix3MakeRotation', 'GLKMatrix3MakeXRotation', 'GLKMatrix3MakeYRotation', 'GLKMatrix3MakeZRotation', 'GLKMatrix3MakeWithQuaternion', 'GLKMatrix3MakeScale', 'GLKMatrix3GetMatrix2', 'GLKMatrix3GetColumn', 'GLKMatrix3GetRow', 'GLKMatrix3SetColumn', 'GLKMatrix3SetRow', 'GLKMatrix3Invert', 'GLKMatrix3Transpose', 'GLKMatrix3InvertAndTranspose', 'GLKMatrix3Multiply']


if __name__ == '__main__':
    m = GLKMatrix3MakeRotation(math.radians(65), 0, 0, 1)
    m2 = GLKMatrix3MakeScale(3, 1, 3)
    
    mi = GLKMatrix3Make(0, 1, 0, 0, 1, 0, 0, 0, 1)
    mv = GLKMatrix3Make(1, 3, 3, 1, 4, 3, 1, 3, 4)
    print m
    print GLKMatrix3GetColumn(m, 1)
    print m2