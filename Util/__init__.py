# coding: utf-8
import ctypes
from objc_util import *

from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *
from OpenGLES.GLES.gles3 import *

import euclid


class RenderCycle(object):
    def __init__(self):
        self.fps = 0
        self.framesDisplayed = 0
        
    def render(self, context):
        print "Draw"
        
    def update(self, dt):
        print "Updating with a time step of %f s" % dt
        
    def setup(self, context):
        pass
        
        
class RenderObject(object):
    def __init__(self, vertices=[], colour=[], uv=[], indices=[]):
        self.vVertices = (GLfloat * len(vertices))(*vertices)
        self.model = euclid.Matrix4.new_identity()
        
    def setup_object(self):
        pass
        
    def render(self):
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, self.vVertices);
        glEnableVertexAttribArray(0);
        glDrawArrays(GL_TRIANGLES, 0, 12*3);
        
    def update(self):
        pass
        
class LookObject(object):
    def __init__(self, *args, **kwargs):
        self.view = euclid.Matrix4.new_look_at(
                                                euclid.Vector3(10,0,10),
                                                euclid.Vector3(0,0,0),
                                                euclid.Vector3(0,1,0))
                                                
    def look(self, *args):
        pass
    
    def move(self, *args):
        pass
        
    def update(self, *args):
        pass