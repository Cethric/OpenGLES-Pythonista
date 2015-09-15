# coding: utf-8
# NOTE:
# This example requires the euclid.py math library
#
import sys
import ui
from objc_util import *
import time
import colorsys
import math
import random
import copy
import time

import OpenGLES.GLES as GLES
import OpenGLES.EAGL as EAGL
import OpenGLES.GLKit as GLKit
import OpenGLES.Util as Util
import OpenGLES.Util.Shader
import OpenGLES.Util.Model    
from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *
from OpenGLES.Util import Physics

import euclid

reload(GLES)
reload(EAGL)
reload(GLKit)
reload(Util)
reload(OpenGLES.Util.Shader)
reload(OpenGLES.Util.Model)
reload(Physics)

VERTEX_SHADER_SOURCE = '''
attribute vec3 vPosition;
uniform mat4 M;
uniform mat4 V;
uniform mat4 P;

varying vec4 t;
void main() {
    mat4 mvp = P * V * M;
    t = vec4(vPosition.xyz, 1);
    gl_Position = mvp * t;
}
'''

FRAGMENT_SHADER_SOURCE = '''
precision mediump float;
varying vec4 t;
void main() {
    gl_FragColor = vec4(t.x, t.y, t.z, 1.0);
}
'''

glviewv = GLKit.GLKView(frame=(0, 0, 800, 600))

class PhysicsObject(Util.Model.XMLModel):
    def __init__(self, *args, **kwargs):
        Util.Model.XMLModel.__init__(self, *args, **kwargs)
        pos = [self.model.h, self.model.l, self.model.p]
        self.i = Physics.add_object(self.frames[self.frame], 10, pos, True)
        print "Object ID:", self.i
        
    @on_main_thread
    def get_mat(self):
        pos = on_main_thread(Physics.get_object_pos)(self.i)
        rot = on_main_thread(Physics.get_object_rot)(self.i)
        mat = euclid.Matrix4()
        mat.translate(pos.x, pos.y, pos.z)
        mat = mat * rot.get_matrix()
        return mat
    
    def update(self, dt):
        start = time.clock()
        self.model = self.get_mat()
        end = time.clock()
        #print end - start

class Renderer(Util.RenderCycle):
    def __init__(self):
        Util.RenderCycle.__init__(self)
        
        self.objects = []
        for x in range(1, random.randint(2, 8)):
            for y in range(1, random.randint(2, 8)):
                o1 = PhysicsObject("test_model.xml", euclid.Vector3(x*4, y*4, 0))
                self.objects.append(o1)
        self.v = Util.Shader.ShaderSource(VERTEX_SHADER_SOURCE, GL_VERTEX_SHADER)
        self.f = Util.Shader.ShaderSource(FRAGMENT_SHADER_SOURCE, GL_FRAGMENT_SHADER)
        self.sp = Util.Shader.ShaderProgram(self.v, self.f)
        
        self.eye = Util.LookObject(euclid.Vector3(0, 1.5, -10))
        
        self.projection = euclid.Matrix4.new_perspective(45.0, 800.0/600.0, 0.1, 1000.0)
        self.view = self.eye.view
        self.model = euclid.Matrix4.new_identity()
    
    def setup(self, context):
        if EAGL.setCurrentContext(context):
            print "Setup"
            self.sp.build()
            self.sp.bind()
            
            for rObj in self.objects:
                rObj.setup_object()
            
            glEnable(GL_CULL_FACE);
            glCullFace(GL_BACK)
            glEnable(GL_DEPTH_TEST);
            glDepthFunc(GL_LESS);
            glViewport(0, 0, int(glviewv.width*2), int(glviewv.height*2))
            
            glClearColor(0.1, 0.12, 0.39, 1.0)
            
            self.look_f([0,0])
        else:
            print "Could not Setup OpenGLES"
        self.last = time.clock()
            
    @on_main_thread
    def update(self, dt):
        start = time.clock()
        #Physics.step_simulation(dt*10.0, 10)
        glviewv.name = "FPS: %i. Frames: %s" % (self.fps, self.framesDisplayed)
        for rObj in self.objects:
            rObj.update(dt)
            
        self.eye.update(dt)
        self.view = self.eye.view
        
        end = time.clock()
        #print end - start
            
    def move_f(self, mdir):
        self.eye.move(*mdir)
    
    def look_f(self, ldir):
        self.eye.look(*ldir)
        
    def render(self, context):
        if EAGL.setCurrentContext(context):
            # Clear the color buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            glViewport(0, 0, 800*2, 600*2);
            
            self.sp.bind()
            self.sp.uniform4x4("V", list(self.view))
            self.sp.uniform4x4("P", list(self.projection))
            
            for rObj in self.objects:
                rObj.render(self.sp)
            
            self.sp.unbind()
        end = time.clock()
        #print (end - self.last) * 100
        self.last = end

@on_main_thread
def main():
    contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES2)
    GLKit.setRenderEngine(Renderer())
    glviewv.setDelegate(GLKit.GLKViewDelegate())
    glviewv.setContext(contextc)
    glviewv.present("sheet")

main()