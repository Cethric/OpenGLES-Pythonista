# coding: utf-8
import ctypes
from objc_util import *
import ui
import RenderingAPI

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()

EAGLContext_OBJC = ObjCClass("EAGLContext")

#print get_methods(EAGLContext_OBJC)

def setCurrentContext(context):
    return EAGLContext_OBJC.setCurrentContext_(context)

class EAGLContext(object):
    def __init__(self, gles_api=RenderingAPI.OpenGLES2, c_context = None): 
        self._context = c_context if c_context != None else EAGLContext_OBJC.alloc().initWithAPI_(gles_api)
        #self._context.setMultiThreaded_(True)
        
    def renderbufferStorage(self, gl_target, drawable):
        self._context.renderbufferStorage_(gl_target, drawable)