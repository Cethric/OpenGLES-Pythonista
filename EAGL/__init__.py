# coding: utf-8
import ctypes
import cffi
from cffi import backend_ctypes
from objc_util import *
import ui
from objc_add import *
import RenderingAPI

ffi = cffi.FFI(backend_ctypes.CTypesBackend())
CFFI = ffi.dlopen(None)

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()

EAGLContext_OBJC = ObjCClass("EAGLContext")

#print get_methods(EAGLContext_OBJC)

def setCurrentContext(context):
    return EAGLContext_OBJC.setCurrentContext_(context)

class EAGLContext(object):
    def __init__(self, gles_api=RenderingAPI.OpenGLES2, c_context = None): 
        self._context = c_context if c_context != None else EAGLContext_OBJC.alloc().initWithAPI_(gles_api)
        
    def renderbufferStorage(self, gl_target, drawable):
        self._context.renderbufferStorage_(gl_target, drawable)