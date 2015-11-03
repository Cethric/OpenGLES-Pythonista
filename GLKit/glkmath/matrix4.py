# coding: utf-8
import math
import ctypes
import vector3
import vector4
import matrix2
import quaternion
from objc_util import *

class float16(ctypes.Structure):
    _fields_ = [
                ('m', (ctypes.c_float * 16)),
                ]

class m16(ctypes.Structure):
    _fields_ = [
                ('m00', ctypes.c_float),
                ('m01', ctypes.c_float),
                ('m02', ctypes.c_float),
                ('m03', ctypes.c_float),
                ('m10', ctypes.c_float),
                ('m11', ctypes.c_float),
                ('m12', ctypes.c_float),
                ('m13', ctypes.c_float),
                ('m20', ctypes.c_float),
                ('m21', ctypes.c_float),
                ('m22', ctypes.c_float),
                ('m23', ctypes.c_float),
                ('m30', ctypes.c_float),
                ('m31', ctypes.c_float),
                ('m32', ctypes.c_float),
                ('m33', ctypes.c_float),
                ]
                
class GLKMatrix4(ctypes.Union):
    _anonymous_ = [
                    ('s1'),
                    ('s2'),
                    ]
    _fields_ = [
                ('s1', float16),
                ('s2', m16),
                ]
    
    def __str__(self):
        mstr = '''GLKMatrix4 {\n{%.3f, %.3f, %.3f, %.3f}\n{%.3f, %.3f, %.3f, %.3f}\n{%.3f, %.3f, %.3f, %.3f}\n{%.3f, %.3f, %.3f, %.3f}\n}''' % tuple([float(x) for x in self.s1.m])
        return mstr
        
        
def GLKMatrix4Make(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33):
    matrix = GLKMatrix4()
    matrix.m00 = m00
    matrix.m01 = m01
    matrix.m02 = m02
    matrix.m03 = m03
    matrix.m10 = m10
    matrix.m11 = m11
    matrix.m12 = m12
    matrix.m13 = m13
    matrix.m20 = m20
    matrix.m21 = m21
    matrix.m22 = m22
    matrix.m23 = m23
    matrix.m30 = m30
    matrix.m31 = m31
    matrix.m32 = m32
    matrix.m33 = m33
    return matrix
    
    
def GLKMatrix4Identity():
    return GLKMatrix4Make(1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1)
    
def GLKMatrix4MakeAndTranspose(m00, m01, m02, m03,
                                m10, m11, m12, m13,
                                m20, m21, m22, m23,
                                m30, m31, m32, m33):
    return GLKMatrix4Traspose(GLKMatrix4Make(m00, m01, m02, m03,
                                                m10, m11, m12, m13,
                                                m20, m21, m22, m23,
                                                m30, m31, m32, m33))
                                                
def GLKMatrix4MakeWithArray(values):
    return GLKMatrix4Make(*values)
    
def GLKMatrix4MakeWithArrayAndTranspose(values):
    return GLKMatrix4MakeAndTranspose(*values)
    
def GLKMatrix4MakeWithRows(row0, row1, row2, row3):
    array = [
        row0.x, row1.x, row2.x, row3.x,
        row0.y, row1.y, row2.y, row3.y,
        row0.z, row1.z, row2.z, row3.z,
        row0.w, row1.w, row2.w, row3.w,
    ]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeWithColumns(col0, col1, col2, col3):
    array = [
        col0.x, col0.y, col0.z, col0.w,
        col1.x, col1.y, col1.z, col1.w,
        col2.x, col2.y, col2.z, col2.w,
        col3.x, col3.y, col3.z, col3.w,
    ]
    return GLKMatrix4MakeWithArray(array)
    
    
def GLKMatrix4MakeWithQuaternion(quat):
    raise NotImplementedError('No GLKQuaternion Class yet.')
    quat = quaternion.GLKQuaternionNormalize(quat)
    x = quat.q[0];
    y = quat.q[1];
    z = quat.q[2];
    w = quat.q[3];
    
    _2x = x + x;
    _2y = y + y;
    _2z = z + z;
    _2w = w + w;
    
    array = [
                1.0 - _2y * y - _2z * z, _2x * y + _2w * z, _2x * z - _2w * y, 0.0,
                _2x * y - _2w * z, 1.0 - _2x * x - _2z * z, _2y * z + _2w * x, 0.0,
                _2x * z + _2w * y, _2y * z - _2w * x, 1.0 - _2x * x - _2y * y, 0.0,
                0.0, 0.0, 0.0, 1.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeTranslation(tx, ty, tz):
    m = GLKMatrix4Identity()
    m.m[12] = tx
    m.m[13] = ty
    m.m[14] = tz
    return m
    
def GLKMatrix4MakeScale(sx, sy, sz):
    m = GLKMatrix4Identity()
    m.m[0] = sx
    m.m[5] = sy
    m.m[10] = sz
    return m
    
def GLKMatrix4MakeRotation(radians, x, y, z):
    v = vector3.GLKVector3Normalize(vector3.GLKVector3Make(x, y, z));
    cos = math.cos(radians);
    cosp = 1.0 - cos;
    sin = math.sin(radians);
    
    array = [
                cos + cosp * v.v[0] * v.v[0], cosp * v.v[0] * v.v[1] + v.v[2] * sin, cosp * v.v[0] * v.v[2] - v.v[1] * sin, 0.0,
                cosp * v.v[0] * v.v[1] - v.v[2] * sin,    cos + cosp * v.v[1] * v.v[1],    cosp * v.v[1] * v.v[2] + v.v[0] * sin,    0.0,
                cosp * v.v[0] * v.v[2] + v.v[1] * sin, cosp * v.v[1] * v.v[2] - v.v[0] * sin, cos + cosp * v.v[2] * v.v[2], 0.0,
                0.0, 0.0, 0.0, 1.0]

    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeXRotation(radians):
    cos = math.cos(radians);
    sin = math.sin(radians);
    
    array = [
                1.0, 0.0, 0.0, 0.0,
                0.0, cos, sin, 0.0,
                0.0, -sin, cos, 0.0,
                0.0, 0.0, 0.0, 1.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeYRotation(radians):
    cos = math.cos(radians);
    sin = math.sin(radians);
    
    array = [
                cos, 0.0, -sin, 0.0,
                0.0, 1.0, 0.0, 0.0,
                sin, 0.0, cos, 0.0,
                0.0, 0.0, 0.0, 1.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeZRotation(radians):
    cos = math.cos(radians);
    sin = math.sin(radians);
    
    array = [
                cos, sin, 0.0, 0.0,
                -sin, cos, 0.0, 0.0,
                0.0, 0.0, 1.0, 0.0,
                0.0, 0.0, 0.0, 1.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakePerspective(fovyRadians, aspect, nearZ, farZ):
    cotan = 1.0 / math.tan(fovyRadians / 2.0);
    array = [
                cotan / aspect, 0.0, 0.0, 0.0,
                0.0, cotan, 0.0, 0.0,
                0.0, 0.0, (farZ + nearZ) / (nearZ - farZ), -1.0,
                0.0, 0.0, (2.0 * farZ * nearZ) / (nearZ - farZ), 0.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeFrustum(
                            left, right,
                            bottom, top,
                            nearZ, farZ):
    ral = right + left;
    rsl = right - left;
    tsb = top - bottom;
    tab = top + bottom;
    fan = farZ + nearZ;
    fsn = farZ - nearZ;
    array = [
                2.0 * nearZ / rsl, 0.0, 0.0, 0.0,
                0.0, 2.0 * nearZ / tsb, 0.0, 0.0,
                ral / rsl, tab / tsb, -fan / fsn, -1.0,
                0.0, 0.0, (-2.0 * farZ * nearZ) / fsn, 0.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeOrtho(
                        left, right,
                        bottom, top,
                        nearZ, farZ):
    ral = right + left;
    rsl = right - left;
    tab = top + bottom;
    tsb = top - bottom;
    fan = farZ + nearZ;
    fsn = farZ - nearZ;
    
    array = [
                2.0 / rsl, 0.0, 0.0, 0.0,
                0.0, 2.0 / tsb, 0.0, 0.0,
                0.0, 0.0, -2.0 / fsn, 0.0,
                -ral / rsl, -tab / tsb, -fan / fsn, 1.0]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4MakeLookAt(
                            eyeX, eyeY, eyeZ,
                            centerX, centerY, centerZ,
                            upX, upY, upZ):
    ev = vector3.GLKVector3MakeWithArray([eyeX, eyeY, eyeZ])
    cv = vector3.GLKVector3MakeWithArray([centerX, centerY, centerZ])
    uv = vector3.GLKVector3MakeWithArray([upX, upY, upZ])
    n = vector3.GLKVector3Normalize(vector3.GLKVector3Add(ev, vector3.GLKVector3Negate(cv)));
    u = vector3.GLKVector3Normalize(vector3.GLKVector3CrossProduct(uv, n));
    v = vector3.GLKVector3CrossProduct(n, u);
    
    array = [
                u.v[0], v.v[0], n.v[0], 0.0,
                u.v[1], v.v[1], n.v[1], 0.0,
                u.v[2], v.v[2], n.v[2], 0.0,
                vector3.GLKVector3DotProduct(vector3.GLKVector3Negate(u), ev),
                vector3.GLKVector3DotProduct(vector3.GLKVector3Negate(v), ev),
                vector3.GLKVector3DotProduct(vector3.GLKVector3Negate(n), ev),
                1.0]
    
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4GetMatrix3(matrix):
    array = [
                matrix.m[0], matrix.m[1], matrix.m[2],
                matrix.m[4], matrix.m[5], matrix.m[6],
                matrix.m[8], matrix.m[9], matrix.m[10]]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4GetMatrix2(matrix):
    raise NotImplementedError('No Matrix2 class yet')
    array = [
                matrix.m[0], matrix.m[1],
                matrix.m[4], matrix.m[5]]
    return matrix2.GLKMatrix2MakeWithArray(array)
    
def GLKMatrix4GetRow(matrix, row):
    return vector4.GLKVector4MakeWithArray([
                                                matrix.m[row],
                                                matrix.m[4 + row],
                                                matrix.m[8 + row],
                                                matrix.m[12 + row]
                                            ])
                                            
def GLKMatrix4GetColumn(matrix, column):
    return vector4.GLKVector4MakeWithArray([
                                                matrix.m[column * 4 + 0],
                                                matrix.m[column * 4 + 1],
                                                matrix.m[column * 4 + 2],
                                                matrix.m[column * 4 + 3]
                                            ])
                                            
def GLKMatrix4SetRow(matrix, row, vector):
    matrix.m[row] = vector.v[0];
    matrix.m[row + 4] = vector.v[1];
    matrix.m[row + 8] = vector.v[2];
    matrix.m[row + 12] = vector.v[3];
    return matrix;
    
def GLKMatrix4SetColumn(matrix, column, vector):
    matrix.m[column * 4 + 0] = vector.v[0];
    matrix.m[column * 4 + 1] = vector.v[1];
    matrix.m[column * 4 + 2] = vector.v[2];
    matrix.m[column * 4 + 3] = vector.v[3];
    return matrix;
    
def GLKMatrix4Transpose(matrix):
    array = [
                matrix.m[0], matrix.m[4], matrix.m[8], matrix.m[12],
                matrix.m[1], matrix.m[5], matrix.m[9], matrix.m[13],
                matrix.m[2], matrix.m[6], matrix.m[10], matrix.m[14],
                matrix.m[3], matrix.m[7], matrix.m[11], matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4Multiply(matrixLeft, matrixRight):
    m = GLKMatrix4()
    m.m[0] = matrixLeft.m[0] * matrixRight.m[0] + matrixLeft.m[4] * matrixRight.m[1] + matrixLeft.m[8] * matrixRight.m[2] + matrixLeft.m[12] * matrixRight.m[3]
    m.m[4]  = matrixLeft.m[0] * matrixRight.m[4]  + matrixLeft.m[4] * matrixRight.m[5]  + matrixLeft.m[8] * matrixRight.m[6]   + matrixLeft.m[12] * matrixRight.m[7];
    m.m[8]  = matrixLeft.m[0] * matrixRight.m[8]  + matrixLeft.m[4] * matrixRight.m[9]  + matrixLeft.m[8] * matrixRight.m[10]  + matrixLeft.m[12] * matrixRight.m[11];
    m.m[12] = matrixLeft.m[0] * matrixRight.m[12] + matrixLeft.m[4] * matrixRight.m[13] + matrixLeft.m[8] * matrixRight.m[14]  + matrixLeft.m[12] * matrixRight.m[15];
    
    m.m[1]  = matrixLeft.m[1] * matrixRight.m[0]  + matrixLeft.m[5] * matrixRight.m[1]  + matrixLeft.m[9] * matrixRight.m[2]   + matrixLeft.m[13] * matrixRight.m[3];
    m.m[5]  = matrixLeft.m[1] * matrixRight.m[4]  + matrixLeft.m[5] * matrixRight.m[5]  + matrixLeft.m[9] * matrixRight.m[6]   + matrixLeft.m[13] * matrixRight.m[7];
    m.m[9]  = matrixLeft.m[1] * matrixRight.m[8]  + matrixLeft.m[5] * matrixRight.m[9]  + matrixLeft.m[9] * matrixRight.m[10]  + matrixLeft.m[13] * matrixRight.m[11];
    m.m[13] = matrixLeft.m[1] * matrixRight.m[12] + matrixLeft.m[5] * matrixRight.m[13] + matrixLeft.m[9] * matrixRight.m[14]  + matrixLeft.m[13] * matrixRight.m[15];
    
    m.m[2]  = matrixLeft.m[2] * matrixRight.m[0]  + matrixLeft.m[6] * matrixRight.m[1]  + matrixLeft.m[10] * matrixRight.m[2]  + matrixLeft.m[14] * matrixRight.m[3];
    m.m[6]  = matrixLeft.m[2] * matrixRight.m[4]  + matrixLeft.m[6] * matrixRight.m[5]  + matrixLeft.m[10] * matrixRight.m[6]  + matrixLeft.m[14] * matrixRight.m[7];
    m.m[10] = matrixLeft.m[2] * matrixRight.m[8]  + matrixLeft.m[6] * matrixRight.m[9]  + matrixLeft.m[10] * matrixRight.m[10] + matrixLeft.m[14] * matrixRight.m[11];
    m.m[14] = matrixLeft.m[2] * matrixRight.m[12] + matrixLeft.m[6] * matrixRight.m[13] + matrixLeft.m[10] * matrixRight.m[14] + matrixLeft.m[14] * matrixRight.m[15];
    
    m.m[3]  = matrixLeft.m[3] * matrixRight.m[0]  + matrixLeft.m[7] * matrixRight.m[1]  + matrixLeft.m[11] * matrixRight.m[2]  + matrixLeft.m[15] * matrixRight.m[3];
    m.m[7]  = matrixLeft.m[3] * matrixRight.m[4]  + matrixLeft.m[7] * matrixRight.m[5]  + matrixLeft.m[11] * matrixRight.m[6]  + matrixLeft.m[15] * matrixRight.m[7];
    m.m[11] = matrixLeft.m[3] * matrixRight.m[8]  + matrixLeft.m[7] * matrixRight.m[9]  + matrixLeft.m[11] * matrixRight.m[10] + matrixLeft.m[15] * matrixRight.m[11];
    m.m[15] = matrixLeft.m[3] * matrixRight.m[12] + matrixLeft.m[7] * matrixRight.m[13] + matrixLeft.m[11] * matrixRight.m[14] + matrixLeft.m[15] * matrixRight.m[15];
    
    return m;
    
def GLKMatrix4Add(matrixLeft, matrixRight):
    m = GLKMatrix4()
    
    m.m[0] = matrixLeft.m[0] + matrixRight.m[0];
    m.m[1] = matrixLeft.m[1] + matrixRight.m[1];
    m.m[2] = matrixLeft.m[2] + matrixRight.m[2];
    m.m[3] = matrixLeft.m[3] + matrixRight.m[3];
    
    m.m[4] = matrixLeft.m[4] + matrixRight.m[4];
    m.m[5] = matrixLeft.m[5] + matrixRight.m[5];
    m.m[6] = matrixLeft.m[6] + matrixRight.m[6];
    m.m[7] = matrixLeft.m[7] + matrixRight.m[7];
    
    m.m[8] = matrixLeft.m[8] + matrixRight.m[8];
    m.m[9] = matrixLeft.m[9] + matrixRight.m[9];
    m.m[10] = matrixLeft.m[10] + matrixRight.m[10];
    m.m[11] = matrixLeft.m[11] + matrixRight.m[11];
    
    m.m[12] = matrixLeft.m[12] + matrixRight.m[12];
    m.m[13] = matrixLeft.m[13] + matrixRight.m[13];
    m.m[14] = matrixLeft.m[14] + matrixRight.m[14];
    m.m[15] = matrixLeft.m[15] + matrixRight.m[15];
    
    return m;

def GLKMatrix4Subtract(matrixLeft, matrixRight):
    m = GLKMatrix4()
    
    m.m[0] = matrixLeft.m[0] - matrixRight.m[0];
    m.m[1] = matrixLeft.m[1] - matrixRight.m[1];
    m.m[2] = matrixLeft.m[2] - matrixRight.m[2];
    m.m[3] = matrixLeft.m[3] - matrixRight.m[3];
    
    m.m[4] = matrixLeft.m[4] - matrixRight.m[4];
    m.m[5] = matrixLeft.m[5] - matrixRight.m[5];
    m.m[6] = matrixLeft.m[6] - matrixRight.m[6];
    m.m[7] = matrixLeft.m[7] - matrixRight.m[7];
    
    m.m[8] = matrixLeft.m[8] - matrixRight.m[8];
    m.m[9] = matrixLeft.m[9] - matrixRight.m[9];
    m.m[10] = matrixLeft.m[10] - matrixRight.m[10];
    m.m[11] = matrixLeft.m[11] - matrixRight.m[11];
    
    m.m[12] = matrixLeft.m[12] - matrixRight.m[12];
    m.m[13] = matrixLeft.m[13] - matrixRight.m[13];
    m.m[14] = matrixLeft.m[14] - matrixRight.m[14];
    m.m[15] = matrixLeft.m[15] - matrixRight.m[15];
    
    return m;
    
def GLKMatrix4Translate(matrix, tx, ty, tz):
    array = [
                matrix.m[0], matrix.m[1], matrix.m[2], matrix.m[3],
                matrix.m[4], matrix.m[5], matrix.m[6], matrix.m[7],
                matrix.m[8], matrix.m[9], matrix.m[10], matrix.m[11],
                matrix.m[0] * tx + matrix.m[4] * ty + matrix.m[8] * tz + matrix.m[12],
                matrix.m[1] * tx + matrix.m[5] * ty + matrix.m[9] * tz + matrix.m[13],
                matrix.m[2] * tx + matrix.m[6] * ty + matrix.m[10] * tz + matrix.m[14],
                matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4TranslateWithVector3(matrix, translationVector):
    array = [
                matrix.m[0], matrix.m[1], matrix.m[2], matrix.m[3],
                matrix.m[4], matrix.m[5], matrix.m[6], matrix.m[7],
                matrix.m[8], matrix.m[9], matrix.m[10], matrix.m[11],
                matrix.m[0] * translationVector.v[0] + matrix.m[4] * translationVector.v[1] + matrix.m[8] * translationVector.v[2] + matrix.m[12],
                matrix.m[1] * translationVector.v[0] + matrix.m[5] * translationVector.v[1] + matrix.m[9] * translationVector.v[2] + matrix.m[13],
                matrix.m[2] * translationVector.v[0] + matrix.m[6] * translationVector.v[1] + matrix.m[10] * translationVector.v[2] + matrix.m[14],
                matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4TranslateWithVector4(matrix, translationVector):
    array = [
                matrix.m[0], matrix.m[1], matrix.m[2], matrix.m[3],
                matrix.m[4], matrix.m[5], matrix.m[6], matrix.m[7],
                matrix.m[8], matrix.m[9], matrix.m[10], matrix.m[11],
                matrix.m[0] * translationVector.v[0] + matrix.m[4] * translationVector.v[1] + matrix.m[8] * translationVector.v[2] + matrix.m[12],
                matrix.m[1] * translationVector.v[0] + matrix.m[5] * translationVector.v[1] + matrix.m[9] * translationVector.v[2] + matrix.m[13],
                matrix.m[2] * translationVector.v[0] + matrix.m[6] * translationVector.v[1] + matrix.m[10] * translationVector.v[2] + matrix.m[14],
                matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4Scale(matrix, sx, sy, sz):
    array = [
                matrix.m[0] * sx, matrix.m[1] * sx, matrix.m[2] * sx, matrix.m[3] * sx,
                matrix.m[4] * sy, matrix.m[5] * sy, matrix.m[6] * sy, matrix.m[7] * sy,
                matrix.m[8] * sz, matrix.m[9] * sz, matrix.m[10] * sz, matrix.m[11] * sz,
                matrix.m[12], matrix.m[13], matrix.m[14], matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)
    
def GLKMatrix4ScaleWithVector3(matrix, scaleVector):
    array = [
                matrix.m[0] * scaleVector.v[0], matrix.m[1] * scaleVector.v[0], matrix.m[2] * scaleVector.v[0], matrix.m[3] * scaleVector.v[0],
                matrix.m[4] * scaleVector.v[1], matrix.m[5] * scaleVector.v[1], matrix.m[6] * scaleVector.v[1], matrix.m[7] * scaleVector.v[1],
                matrix.m[8] * scaleVector.v[2], matrix.m[9] * scaleVector.v[2], matrix.m[10] * scaleVector.v[2], matrix.m[11] * scaleVector.v[2],
                matrix.m[12], matrix.m[13], matrix.m[14], matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)

def GLKMatrix4ScaleWithVector4(matrix, scaleVector):
    array = [
                matrix.m[0] * scaleVector.v[0], matrix.m[1] * scaleVector.v[0], matrix.m[2] * scaleVector.v[0], matrix.m[3] * scaleVector.v[0],
                matrix.m[4] * scaleVector.v[1], matrix.m[5] * scaleVector.v[1], matrix.m[6] * scaleVector.v[1], matrix.m[7] * scaleVector.v[1],
                matrix.m[8] * scaleVector.v[2], matrix.m[9] * scaleVector.v[2], matrix.m[10] * scaleVector.v[2], matrix.m[11] * scaleVector.v[2],
                matrix.m[12], matrix.m[13], matrix.m[14], matrix.m[15]]
    return GLKMatrix4MakeWithArray(array)

def GLKMatrix4Rotate(matrix, radians, x, y, z):
    rm = GLKMatrix4MakeRotation(radians, x, y, z);
    return GLKMatrix4Multiply(matrix, rm);
    
def GLKMatrix4RotateWithVector3(matrix, radians, axisVector):
    rm = GLKMatrix4MakeRotation(radians, axisVector.v[0], axisVector.v[1], axisVector.v[2]);
    return GLKMatrix4Multiply(matrix, rm);
    
def GLKMatrix4RotateWithVector4(matrix, radians, axisVector):
    rm = GLKMatrix4MakeRotation(radians, axisVector.v[0], axisVector.v[1], axisVector.v[2]);
    return GLKMatrix4Multiply(matrix, rm);
    
def GLKMatrix4RotateX(matrix, radians):
    rm = GLKMatrix4MakeXRotation(radians);
    return GLKMatrix4Multiply(matrix, rm);
    
def GLKMatrix4RotateY(matrix, radians):
    rm = GLKMatrix4MakeYRotation(radians);
    return GLKMatrix4Multiply(matrix, rm);
    
def GLKMatrix4RotateZ(matrix, radians):
    rm = GLKMatrix4MakeZRotation(radians);
    return GLKMatrix4Multiply(matrix, rm);
    
def GLKMatrix4MultiplyVector3(matrixLeft, vectorRight):
    v4 = GLKMatrix4MultiplyVector4(matrixLeft, GLKVector4Make(vectorRight.v[0], vectorRight.v[1], vectorRight.v[2], 0.0));
    return vector3.GLKVector3Make(v4.v[0], v4.v[1], v4.v[2]);
    
def GLKMatrix4MultiplyVector3WithTranslation(matrixLeft, vectorRight):
    v4 = GLKMatrix4MultiplyVector4(matrixLeft, GLKVector4Make(vectorRight.v[0], vectorRight.v[1], vectorRight.v[2], 1.0));
    return vector3.GLKVector3Make(v4.v[0], v4.v[1], v4.v[2]);
    
def GLKMatrix4MultiplyAndProjectVector3(matrixLeft, vectorRight):
    v4 = GLKMatrix4MultiplyVector4(matrixLeft, vector4.GLKVector4Make(vectorRight.v[0], vectorRight.v[1], vectorRight.v[2], 1.0));
    return vector3.GLKVector3MultiplyScalar(vector3.GLKVector3Make(v4.v[0], v4.v[1], v4.v[2]), 1.0 / v4.v[3]);
    
def GLKMatrix4MultiplyVector3Array(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyVector3(matrix, vectors[i]);
        
def GLKMatrix4MultiplyVector3ArrayWithTranslation(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyVector3WithTranslation(matrix, vectors[i]);
        
def GLKMatrix4MultiplyAndProjectVector3Array(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyAndProjectVector3(matrix, vectors[i]);
        
def GLKMatrix4MultiplyVector3Array(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyVector3(matrix, vectors[i]);
        
def GLKMatrix4MultiplyVector3ArrayWithTranslation(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyVector3WithTranslation(matrix, vectors[i]);
        
def GLKMatrix4MultiplyAndProjectVector3Array(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyAndProjectVector3(matrix, vectors[i]);
        
def GLKMatrix4MultiplyVector4(matrixLeft, vectorRight):
    array = [
                matrixLeft.m[0] * vectorRight.v[0] + matrixLeft.m[4] * vectorRight.v[1] + matrixLeft.m[8] * vectorRight.v[2] + matrixLeft.m[12] * vectorRight.v[3],
                matrixLeft.m[1] * vectorRight.v[0] + matrixLeft.m[5] * vectorRight.v[1] + matrixLeft.m[9] * vectorRight.v[2] + matrixLeft.m[13] * vectorRight.v[3],
                matrixLeft.m[2] * vectorRight.v[0] + matrixLeft.m[6] * vectorRight.v[1] + matrixLeft.m[10] * vectorRight.v[2] + matrixLeft.m[14] * vectorRight.v[3],
                matrixLeft.m[3] * vectorRight.v[0] + matrixLeft.m[7] * vectorRight.v[1] + matrixLeft.m[11] * vectorRight.v[2] + matrixLeft.m[15] * vectorRight.v[3]]
    return vector4.GLKVector4MakeWithArray(array)
    
def GLKMatrix4MultiplyVector4Array(matrix, vectors, vectorCount):
    for i in range(vectorCount):
        vectors[i] = GLKMatrix4MultiplyVector4(matrix, vectors[i]);
        
def GLKMatrix4Invert(matrix):
    func = c.GLKMatrix4Invert
    func.argtypes = [GLKMatrix4]
    func.restype = GLKMatrix4
    return func(matrix)

__all__ = ['GLKMatrix4', 'GLKMatrix4Make', 'GLKMatrix4Identity', 'GLKMatrix4MakeAndTranspose', 'GLKMatrix4MakeWithArray', 'GLKMatrix4MakeWithRows', 'GLKMatrix4MakeWithColumns', 'GLKMatrix4MakeWithQuaternion', 'GLKMatrix4MakeTranslation', 'GLKMatrix4MakeScale', 'GLKMatrix4MakeRotation', 'GLKMatrix4MakeXRotation', 'GLKMatrix4MakeYRotation', 'GLKMatrix4MakeZRotation', 'GLKMatrix4MakePerspective', 'GLKMatrix4MakeFrustum', 'GLKMatrix4MakeOrtho', 'GLKMatrix4MakeLookAt', 'GLKMatrix4GetMatrix3', 'GLKMatrix4GetMatrix2', 'GLKMatrix4GetRow', 'GLKMatrix4GetColumn', 'GLKMatrix4SetRow', 'GLKMatrix4SetColumn', 'GLKMatrix4Transpose', 'GLKMatrix4Multiply', 'GLKMatrix4Add', 'GLKMatrix4Subtract', 'GLKMatrix4Translate', 'GLKMatrix4TranslateWithVector3', 'GLKMatrix4TranslateWithVector4', 'GLKMatrix4Scale', 'GLKMatrix4ScaleWithVector3', 'GLKMatrix4ScaleWithVector4', 'GLKMatrix4Rotate', 'GLKMatrix4RotateWithVector3', 'GLKMatrix4RotateWithVector4', 'GLKMatrix4RotateX', 'GLKMatrix4RotateY', 'GLKMatrix4RotateZ', 'GLKMatrix4MultiplyVector3', 'GLKMatrix4MultiplyVector3WithTranslation', 'GLKMatrix4MultiplyAndProjectVector3', 'GLKMatrix4MultiplyVector3Array', 'GLKMatrix4MultiplyVector3ArrayWithTranslation', 'GLKMatrix4MultiplyAndProjectVector3Array', 'GLKMatrix4MultiplyVector3Array', 'GLKMatrix4MultiplyVector3ArrayWithTranslation', 'GLKMatrix4MultiplyAndProjectVector3Array', 'GLKMatrix4MultiplyVector4', 'GLKMatrix4MultiplyVector4Array', 
'GLKMatrix4Invert']

if __name__ == '__main__':
    m = GLKMatrix4Make(1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1)
    print m
    print GLKMatrix4Identity()
    print GLKMatrix4MakeWithRows(vector4.GLKVector4Make(1,0,0,0), vector4.GLKVector4Make(0,1,0,0), vector4.GLKVector4Make(0,0,1,0), vector4.GLKVector4Make(0,0,0,1))
    print GLKMatrix4MakeWithColumns(vector4.GLKVector4Make(1,0,0,0), vector4.GLKVector4Make(0,1,0,0), vector4.GLKVector4Make(0,0,1,0), vector4.GLKVector4Make(0,0,0,1))
    print GLKMatrix4MakeTranslation(0, 10, 0)
    mr = GLKMatrix4MakeRotation(10, 0, 1, 0)
    print 'GLKMatrix4MakeRotation', mr
    mi = GLKMatrix4Invert(GLKMatrix4MakeRotation(10, 0, 1, 0))
    print 'GLKMatrix4Invert', mi
    print 'GLKMatrix4Multiply', GLKMatrix4Multiply(mi, mr)
    print GLKMatrix4MakeLookAt(10, 10, -10, 0, 0, 0, 0, 1, 0)