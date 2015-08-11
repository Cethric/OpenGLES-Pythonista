# coding: utf-8
import ui
from objc_util import *
import time
import colorsys

import GLES
import EAGL
import GLKit
from OpenGLES.GLES.gles1 import *

reload(GLES)
reload(EAGL)
reload(GLKit)

GLKView = ObjCClass('GLKView')
GLKViewController = ObjCClass('GLKViewController')
UINavigationController = ObjCClass('UINavigationController')

def test_draw():
    r, g, b = colorsys.hsv_to_rgb((time.time() * 0.1) % 1.0, 1, 1)
    glClearColor(1, g, b, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

def dismiss(_self, _cmd):
    self = ObjCInstance(_self)
    self.view().delegate().release()
    self.view().setDelegate_(None)
    self.dismissViewControllerAnimated_completion_(True, None)

@on_main_thread
def main():
    glview = GLKit.GLKView(None, None).glview
    context = EAGL.EAGLContext()._context
    GLKit.draw = test_draw
    delegate = GLKit.GLKViewDelegate()
    glview.setDelegate_(delegate)
    glview.setContext_(context)
    glview.setEnableSetNeedsDisplay_(False)
    
    glvc = GLKit.GKLViewController("Test GLES", glview)
    nav = UINavigationController.alloc().initWithRootViewController_(glvc)
    print "HELLO WORLD"
    
    v = ui.View()
    vo = ObjCInstance(v)
    vo.addChildViewController_(nav)
    
    v.present()
    
    #rootvc = UIApplication.sharedApplication().keyWindow().rootViewController()
    #rootvc.presentModalViewController_animated_(nav, True)
    nav.release()

main()