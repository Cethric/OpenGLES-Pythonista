# coding: utf-8
import ctypes
import cffi
from cffi import backend_ctypes
from objc_util import *

from headers.gl_c import *
from headers.glext_c import *

ffi = cffi.FFI(backend_ctypes.CTypesBackend())
CFFI = ffi.dlopen(None)

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()