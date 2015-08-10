# coding: utf-8
import ctypes
import cffi
from cffi import backend_ctypes
from objc_util import *

from headers.gl_c import *
from headers.glext_c import *

ffi = cffi.FFI(backend_ctypes.CTypesBackend())
CFFI = ffi.dlopen(None)

def glClear(mode):
    c.glClear(mode)
    
def glClearColor(r, g, b, a):
    c.glClearColor(ctypes.c_float(r), ctypes.c_float(g), ctypes.c_float(b), ctypes.c_float(a))