# coding: utf-8
import ctypes
from objc_util import *
from OpenGLES.GLES.headers.GLConstants import *
from OpenGLES.GLES.gles1 import GL_TRUE, GL_FALSE

BASE_EFFECT = ObjCClass("GLKBaseEffect")

def GLKBaseEffect():
    return BASE_EFFECT.alloc().init()


if __name__ == "__main__":
    e = GLKBaseEffect()
    e.light0().enabled = GLboolean(GL_TRUE)
    
    print dir(e)
    