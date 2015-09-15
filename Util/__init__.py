# coding: utf-8
import ctypes
from objc_util import *
import math
try:
    import cmath
    HAS_CMATH = True
except ImportError as e:
    print e
    HAS_CMATH = False

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
        self._eye = euclid.Vector3(0,1,0)
        self._look_at = euclid.Vector3(0,5,10)
        self._up = euclid.Vector3(0,1,0)
        
    @property
    def view(self):
        print self._eye
        print self._look_at
        return euclid.Matrix4.new_look_at(
                                          self._eye,
                                          self._look_at,
                                          self._up)
    def look(self, x, y):
        pass
    
    def move(self, x, y):
        pass
        
    def update(self, dt):
        pass