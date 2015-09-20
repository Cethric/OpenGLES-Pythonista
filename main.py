# coding: utf-8
# NOTE:
# This example requires the euclid.py math library
#
import ui
import sys
import time
import math
import copy
import time
import random
import euclid
import colorsys
from objc_util import *

import OpenGLES.Util.Model
import OpenGLES.Util.Shader
import OpenGLES.GLES as GLES
import OpenGLES.EAGL as EAGL
import OpenGLES.Util as Util
import OpenGLES.GLKit as GLKit
from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *
from OpenGLES.Util import Physics

reload(Util)
reload(GLES)
reload(EAGL)
reload(GLKit)
reload(OpenGLES.Util.Shader)
reload(OpenGLES.Util.Model)
reload(OpenGLES.Util.Physics)

with open("shader.vs", "rb") as f:
    VERTEX_SHADER_SOURCE = f.read()
    
with open("shader.fs", "rb") as f:
    FRAGMENT_SHADER_SOURCE = f.read()
    
glviewv = GLKit.GLKView(frame=(0, 0, 800, 600))

TRIANGLE = [
    0.0, 0.5, 0.0,
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0
]


class Renderer(Util.RenderCycle):
    def __init__(self):
        Util.RenderCycle.__init__(self)
        
        self.objects = []
        o2 = Util.Model.XMLModel("test_model.xml", euclid.Vector3(10, 0, 4))
        #o1 = Util.Model.PhysicsObject("test_model.xml", euclid.Vector3(10, 0, 0))
        #self.objects.append(o1)
        self.objects.append(o2)
        
        self.v = Util.Shader.ShaderSource(VERTEX_SHADER_SOURCE, GL_VERTEX_SHADER)
        self.f = Util.Shader.ShaderSource(FRAGMENT_SHADER_SOURCE, GL_FRAGMENT_SHADER)
        self.sp = Util.Shader.ShaderProgram(self.v, self.f)
        
        self.eye = Util.LookObject(euclid.Vector3(0, 0, 0))
        
        self.projection = euclid.Matrix4.new_perspective(45.0, 800.0/600.0, 0.1, 1000.0)
        self.view = self.eye.view
        self.model = euclid.Matrix4.new_identity()
        
    def setup(self, context):
        if EAGL.setCurrentContext(context):
            self.sp.build()
            self.sp.bind()
            
            for rObj in self.objects:
                rObj.setup_object()
            
            glEnable(GL_CULL_FACE);
            glCullFace(GL_BACK)
            glEnable(GL_DEPTH_TEST);
            glDepthFunc(GL_LESS);
            glViewport(0, 0, int(glviewv.width*2), int(glviewv.height*2))
            
            glClearColor(0.1, 0.12, 0.45, 1.0)
        else:
            print "Could not Setup OpenGLES"
        self.last = time.clock()
        
    def teardown(self):
        self.sp.teardown()
        EAGL.setCurrentContext(None)
        
    def update(self, dt):
        start = time.clock()
        @on_main_thread
        def update(dt):
            Physics.step_simulation(dt*10.0, 10)
        # update(dt)
        glviewv.name = "FPS: %i. Frames: %s" % (self.fps, self.framesDisplayed)
        for rObj in self.objects:
            rObj.update(dt)
            rObj.model.rotatex(0.5 * dt)
            rObj.model.rotatey(0.5 * dt)
            rObj.model.rotatez(0.5 * dt)
        self.eye.update(dt)
        self.view = self.eye.view
        
        end = time.clock()
        # print end - start
            
    def move_f(self, mdir):
        mdir.reverse()
        self.eye.move(*mdir)
    
    def look_f(self, ldir):
        self.eye.look(*ldir)
        
    def render(self, context):
        if EAGL.setCurrentContext(context):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            glViewport(0, 0, int(glviewv.width*2), int(glviewv.height*2))
            self.sp.bind()
            self.sp.uniform4x4("V", list(self.view))
            self.sp.uniform4x4("P", list(self.projection))
            for rObj in self.objects:
                rObj.render(self.sp)
        end = time.clock()
        # print (end - self.last) * 100
        self.last = end

@on_main_thread
def main():
    contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES2)
    GLKit.setRenderEngine(Renderer())
    glviewv.setDelegate(GLKit.GLKViewDelegate())
    glviewv.setContext(contextc)
    glviewv.present("sheet")

main()