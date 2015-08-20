# Generated Files. DO NOT EDIT
# Generated on: 08/14/15 21:51:10
import ctypes
from objc_util import *

DEBUG = 1
loaded = [0, 0]

GLchar = ctypes.c_char
GLenum = ctypes.c_uint32
GLboolean = ctypes.c_uint8
GLbitfield = ctypes.c_uint32
GLbyte = ctypes.c_int8
GLshort = ctypes.c_int16
GLint = ctypes.c_int32
GLint64 = ctypes.c_int64
GLsizei = ctypes.c_int32
GLubyte = ctypes.c_uint8
GLushort = ctypes.c_uint16
GLuint = ctypes.c_uint32
GLfloat = ctypes.c_float
GLclampf = ctypes.c_float
GLfixed = ctypes.c_int32
GLintptr = ctypes.c_int32
GLsizeiptr = ctypes.c_int32
GLclampx = ctypes.c_int
void = ctypes.c_void_p
GLvoid = ctypes.c_void_p
GLsync = None

# GLES Constants

# GL Functions
print 'Loaded %i functions and failed to load %i functions of %i functions in the header gl2platform.h' % (loaded[0], loaded[1], sum(loaded))