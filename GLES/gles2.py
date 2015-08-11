# coding: utf-8
import ctypes
import cffi
from cffi import backend_ctypes
from objc_util import *

from headers.gl2_c import *
from headers.gl2ext_c import *

ffi = cffi.FFI(backend_ctypes.CTypesBackend())
CFFI = ffi.dlopen(None)

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()