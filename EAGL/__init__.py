# coding: utf-8
import ctypes
from objc_util import *
import ui
import RenderingAPI

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()

EAGLContext_OBJC = ObjCClass("EAGLContext")


class EAGLSharegroup(object):
    def __init__(self, c_sharegroup=None, gles_api=RenderingAPI.OpenGLES2):
        if c_sharegroup is None:
            sg = ObjCClass('EAGLSharegroup')
            self._sharegroup = sg.alloc().initWithAPI_(gles_api)
        else:
            self._sharegroup = c_sharegroup
            
    def __str__(self):
        return str(self._sharegroup.description())
        
    def setDebugLabel(self, label):
        self._sharegroup.setDebugLabel_(label)
        
    def getDebugLabel(self):
        return self._sharegroup.debugLabel()
        
    debugLabel = property(getDebugLabel, setDebugLabel)


class EAGLContext(object):
    def __init__(self, gles_api=RenderingAPI.OpenGLES2, c_context=None, sharegroup=None):
        if c_context is None:
            if sharegroup is None:
                self._context = EAGLContext_OBJC.alloc().initWithAPI_(gles_api)
            else:
                self._context = EAGLContext_OBJC.alloc()
                self._context.initWithAPI_sharegroup_(gles_api, sharegroup._sharegroup)
            self._context.setMultiThreaded_(True)
        else:
            self._context = c_context
    
    def __str__(self):
        return str(self._context.description())
        
    def setMultiThreaded(self, threaded):
        self._context.setMultiThreaded_(threaded)
        
    def getMultiThreaded(self):
        return self._context.isMultiThreaded()
        
    multiThreaded = property(getMultiThreaded, setMultiThreaded)
    
    @property
    def sharegroup(self):
        return EAGLSharegroup(self._context.sharegroup())


def setCurrentContext(context=None):
    context = getattr(context, '_context', context)
    return EAGLContext_OBJC.setCurrentContext_(context)
    
def currentContext():
    c = EAGLContext_OBJC.currentContext()
    return EAGLContext(None, c) if c is not None else None
    
    
__all__ = ["setCurrentContext", 'currentContext', "EAGLContext", 'EAGLSharegroup']

if __name__ == '__main__':
    c = EAGLContext()
    print c
    c.sharegroup.debugLabel = 'ABC'
    print c.sharegroup.debugLabel
    print c.sharegroup
    c2 = EAGLContext(sharegroup=c.sharegroup)
    print c2
    
    print dir(c._context)
    setCurrentContext(c2)
    setCurrentContext(c._context)
    setCurrentContext(None)
    print currentContext()
    