# coding: utf-8
import ctypes
import cffi
from cffi import backend_ctypes
from objc_util import *
import ui
ffi = cffi.FFI(backend_ctypes.CTypesBackend())
CFFI = ffi.dlopen(None)

import OpenGLES.EAGL as EAGL
import OpenGLES.GLES.gles1 as ES1
import OpenGLES.GLES.gles2 as ES2
reload(EAGL)
reload(ES1)
reload(ES2)

GLKView_OBJC = ObjCClass("GLKView")

class GLKView(ui.View):
    @on_main_thread
    def __init__(self, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)
        frame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
        self.gl_kit_view = GLKView_OBJC.alloc().initWithFrame_(frame)
        flex_width, flex_height = (1<<1), (1<<4)
        self.gl_kit_view.setAutoresizingMask_(flex_width|flex_height)
        self_objc = ObjCInstance(self)
        self_objc.addSubview_(self.gl_kit_view)
        self.background_color = "#ff0000"
        
    def setup_gl(self):
        glView = self.gl_kit_view
        context = self.context
        if EAGL.setCurrentContext(self.context._context):
            renderBuffer = ES2.glGenRenderbuffers(1)
            ES2.glCheckFramebufferStatus(ES2.GL_RENDERBUFFER)
            ES2.glBindRenderbuffer(ES2.GL_RENDERBUFFER, renderBuffer)
        else:
            print "Cannot setup gl"
        
    def getContext(self):
        return EAGL.EAGLContext(c_context = self.gl_kit_view.context)
        
    def setContext(self, context):
        self.gl_kit_view.setContext_(context._context)
        self.setup_gl()
        
    context = property(getContext, setContext, None, None)
        
    @on_main_thread
    def draw(self):
        if EAGL.setCurrentContext(self.context._context):
            ES1.glClearColor(0.1, 0.0, 1.0, 0.0)
            ES1.glClear(ES1.GL_COLOR_BUFFER_BIT | ES1.GL_DEPTH_BUFFER_BIT)
        else:
            print "Failed to render. Could not get context"
    
    @on_main_thread
    def on_close(self):
        self.gl_kit_view.release()