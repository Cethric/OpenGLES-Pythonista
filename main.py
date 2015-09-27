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

def physics_info(sender):
    Physics.PhysicsWorld.js.present("sheet")
btn = ui.ButtonItem()
btn.title = "Physics Info"
btn.action = physics_info
glviewv.left_button_items = [btn]

TRIANGLE = [
    0.0, 0.5, 0.0,
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0
]


class Renderer(Util.RenderCycle):
    def __init__(self):
        Util.RenderCycle.__init__(self)
        
        self.objects = []
        for x in range(-10, 10, 4):
            for y in range(-10, 10, 4):
                for z in range(10, 14, 4):
                    o1 = Util.Model.PhysicsObject("test_model.xml", euclid.Vector3(x, y, z))
                    # o1 = Util.Model.XMLModel("test_model.xml", euclid.Vector3(y, x, z))
                    self.objects.append(o1)
        
        self.v = Util.Shader.ShaderSource(VERTEX_SHADER_SOURCE, GL_VERTEX_SHADER)
        self.f = Util.Shader.ShaderSource(FRAGMENT_SHADER_SOURCE, GL_FRAGMENT_SHADER)
        self.sp = Util.Shader.ShaderProgram(self.v, self.f)
        
        self.eye = Util.LookObject(euclid.Vector3(-10, 2, 0))
        
        self.projection = euclid.Matrix4.new_perspective(45.0, 800.0/600.0, 0.1, 1000.0)
        self.view = self.eye.view
        self.model = euclid.Matrix4.new_identity()
        
        self.rt = 0
        self.ut = 0
        
    def setup(self, context):
        if EAGL.setCurrentContext(context):
            self.sp.build()
            self.sp.bind()
            
            print len(self.objects), " object/s in the world"
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
        # Physics.PhysicsWorld.js.eval_js('done();')
    
    def update(self, dt):
        start = time.clock()
        # Physics.PhysicsWorld.step_simulation(dt, 10)  # Should add some form of simulation step
        Physics.PhysicsWorld.js.eval_js('startUpdates();')
        end = time.clock()
        # print "simulation update", end - start
        # glviewv.name = "FPS: %i. Frames: %s" % (self.fps, self.framesDisplayed)
        glviewv.name = "Render Time: %.3f\tUpdate Time: %.3f\tFrames: %i" % (self.rt, self.ut, self.framesDisplayed)
        su = time.clock()
        for rObj in self.objects:
            so = time.clock()
            rObj.update(dt)
            eo = time.clock()
            # print 'time to update object', rObj, eo - so
        eu = time.clock()
        # print 'time to update all objects', eu - su
        self.eye.update(dt)
        self.view = self.eye.view
        
        end = time.clock()
        self.ut = end - start
        # print "update", end - start
            
    def move_f(self, mdir):
        mdir.reverse()
        self.eye.move(*mdir)
    
    def look_f(self, ldir):
        self.eye.look(*ldir)
        
    def render(self, context):
        start = time.clock()
        if EAGL.setCurrentContext(context):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            glViewport(0, 0, int(glviewv.width*2), int(glviewv.height*2))
            self.sp.bind()
            self.sp.uniform4x4("V", list(self.view))
            self.sp.uniform4x4("P", list(self.projection))
            for rObj in self.objects:
                rObj.render(self.sp)
        end = time.clock()
        # print 'render', (end - self.last)
        self.rt = end - start
        self.last = end

@on_main_thread
def main():
    contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES2)
    GLKit.setRenderEngine(Renderer())
    glviewv.setDelegate(GLKit.GLKViewDelegate())
    glviewv.setContext(contextc)
    glviewv.present("sheet")

main()