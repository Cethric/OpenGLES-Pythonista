# coding: utf-8
import ctypes
from objc_util import *
import math

from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *
from OpenGLES.GLES.gles3 import *
from OpenGLES.GLES.headers.GLConstants import *
import euclid


class RenderCycle(object):
    def __init__(self):
        self.fps = 0
        self.framesDisplayed = 0
    
    def teardown(self):
        pass
        
    def render(self, context):
        print "Draw"
        
    def update(self, dt):
        print "Updating with a time step of %f s" % dt
        
    def setup(self, context):
        pass
        
    def move_f(self, mdir):
        pass
    
    def look_f(self, ldir):
        pass
        
class RenderObject(object):
    def __init__(self, pos, vertices=[], colour=[], uv=[], indices=[]):
        self.vVertices = (GLfloat * len(vertices))(*vertices)
        self.model = euclid.Matrix4.new_identity()
        self.model.translate(*list(pos))
        
    def setup_object(self):
        pass
        
    def teardown(self):
        pass
        
    def render(self, sp):
        sp.uniform4x4("M", list(self.model))
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, self.vVertices, voidpointer_t=(GLfloat * 9));
        glEnableVertexAttribArray(0);
        glDrawArrays(GL_TRIANGLES, 0, 3*3);
        
    def update(self, dt):
        pass
        
class LookObject(object):
    def __init__(self, initial_eye=euclid.Vector3(0,0,0)):
        self._eye = initial_eye
        self._look_at = euclid.Vector3(0,0,0)
        self._up = euclid.Vector3(0,1,0)
        self._heading = 0
        self._attitude = 0
        self._bank = 0
        self.strafe_dir = euclid.Vector3(1,0,0)
        self.strafe = []
        self.speed = 10
        self.look(0.001, 0.001)
        
    @property
    def view(self):
        return euclid.Matrix4.new_look_at(
                                          self._eye,
                                          self._look_at,
                                          self._up).inverse()
    def look(self, dx, dy):
        if dx == 0 and dy == 0:
            return
        self._heading -= math.radians(dx)
        self._heading %= math.radians(360)
        self._bank += dy
        self._bank = max(-88, min(88, self._bank))
        bank = math.degrees(self._bank)
        heading = math.degrees(self._heading)
        
        cosX = math.cos(math.radians(bank))
        sinX = math.sin(math.radians(bank))
        cosY = math.cos(math.radians(heading))
        sinY = math.sin(math.radians(heading))
        
        self._look_at.x = float(-(-cosX * sinY) + self._eye.x)
        self._look_at.y = float(sinX + self._eye.y)
        self._look_at.z = float(-(-cosX * sinY) + self._eye.z)
        
        self.strafe_dir.x = float(cosY)
        self.strafe_dir.y = 0.0
        self.strafe_dir.z = float(-sinY)
    
    def move(self, x, y):
        self.strafe = [x,y]
        
    def update(self, dt):
        if any(self.strafe):
            if self.strafe[0] != 0:
                stepX = (self._look_at.x - self._eye.x) * (self.strafe[0] * self.speed * (dt))
                stepZ = (self._look_at.z - self._eye.z) * (self.strafe[0] * self.speed * (dt))
                
                self._eye.x += stepX
                self._look_at.x += stepX
                
                self._eye.z += stepZ
                self._look_at.z += stepZ
                
            if self.strafe[1] != 0:
                self._eye.x += self.strafe_dir.x * (self.strafe[1] * self.speed * (dt))
                self._eye.y += self.strafe_dir.y * (self.strafe[1] * self.speed * (dt))
                self._eye.z += self.strafe_dir.z * (self.strafe[1] * self.speed * (dt))
                
                self._look_at.x += self.strafe_dir.x * (self.strafe[1] * self.speed * (dt))
                self._look_at.y += self.strafe_dir.y * (self.strafe[1] * self.speed * (dt))
                self._look_at.z += self.strafe_dir.z * (self.strafe[1] * self.speed * (dt))