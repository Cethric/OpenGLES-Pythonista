# coding: utf-8
import ui
import ctypes
import weakref
from objc_util import *

from OpenGLES.EAGL import *

from effect import *
from view import *
from glkmath import *
from fog import *
from light import *
from texture import *
from material import *

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/GLKit.framework").load()


__all__ = ["GLKView", "GLKViewDelegate", "setRenderEngine", "getRenderEngine"]

if __name__ == "__main__":
    v = GLKView(frame=(0,0,800,600))
    d = GLKViewDelegate()
    vc = GKLViewController("GLKit Demo", v)
    vcd = GLKViewControllerDelegate()
    vc.delegate = vcd
    t = TouchController()
    t.present(debug=True)
    # print v
    # print d
    # print vc
    # print vcd