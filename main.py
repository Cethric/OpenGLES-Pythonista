# coding: utf-8
import ui
from objc_util import *
import time
import colorsys

import GLES
import EAGL
import GLKit
from GLES.gles1 import *
from GLES.gles2 import *

reload(GLES)
reload(EAGL)
reload(GLKit)

class Renderer(object):
    def __init__(self):
        self.r, self.g, self.b = colorsys.hsv_to_rgb((time.time() * 0.1) % 1.0, 0.1, 1)
    
    def setup(self, context):
        if (EAGL.setCurrentContext(context)):
            glClearColor(1, 1, 1, 1.0)
        else:
            print "Could not Setup OpenGLES"
            
    def update(self, dt):
        self.r, self.g, self.b = colorsys.hsv_to_rgb((time.time() * 0.1) % 1.0, 1.0, 1)
    
    def render(self, context):
        glClearColor(self.r, self.g, self.b, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

@on_main_thread
def main():
    glviewv = GLKit.GLKView(frame=(0, 0, 200, 200))
    glview = glviewv.glview
    contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES3)
    context = contextc._context
    r = Renderer()
    
    GLKit.glDraw = r.render
    GLKit.glUpdate = r.update
    GLKit.glSetup = r.setup
    
    delegate = GLKit.GLKViewDelegate()
    glviewv.setDelegate(delegate)
    glviewv.setContext(contextc)
    
    glviewv.width = 800
    glviewv.height = 600
    glviewv.present("sheet")

main()