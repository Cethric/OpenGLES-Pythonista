# coding: utf-8
import ctypes
import cffi
from cffi import backend_ctypes
from objc_util import *

from headers.gl2_c import *
from headers.gl2ext_c import *

ffi = cffi.FFI(backend_ctypes.CTypesBackend())
CFFI = ffi.dlopen(None)

def glGenRenderbuffers(amount):
    target = GLuint(0)
    func = c.glGenRenderbuffers
    func.argtypes = [GLsizei, ctypes.POINTER(GLuint)]
    func.restype = None
    func(amount, ctypes.byref(target))
    print target
    return target.value
    
def glBindRenderbuffer(mode, target):
    c.glBindRenderbuffer(mode, target)

def glCheckFramebufferStatus(target):
    func = c.glCheckFramebufferStatus
    func.argtypes = [GLenum]
    return func(target)