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
        self.vSize = len(vertices)
        self.model = euclid.Matrix4.new_identity()
        self.model.translate(*list(pos))
        
    def setup_object(self):
        pass
        
    def teardown(self):
        pass
        
    def render(self, sp):
        sp.uniform4x4("M", list(self.model))
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, self.vVertices, voidpointer_t=(GLfloat * self.vSize));
        glEnableVertexAttribArray(0);
        glDrawArrays(GL_TRIANGLES, 0, self.vSize / 3);
        
    def update(self, dt):
        pass
        
class LookObject(object):
    def __init__(self, position=euclid.Vector3(0,0,0), up=euclid.Vector3(0,1,0), yaw=0.0, pitch=0.0):
        self.position = position
        self.worldup = up
        self.up = euclid.Vector3(0, 0, 0)
        self.front = euclid.Vector3(0, 0, -1)
        self.right = euclid.Vector3(0, 0, 0)
        self.yaw = yaw
        self.pitch = pitch
        self.strafe = [0,0]
        self.speed = 10
        
        self.update(0)
        
    @property
    def view(self):
        return euclid.Matrix4.new_look_at(
                                          self.position,
                                          self.position + self.front,
                                          self.up)
    def look(self, dx, dy):
        self.yaw -= dx
        self.pitch += dy
        
        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0
        self.yaw = self.yaw % 360
    
    def move(self, dx, dy):
        self.strafe = [dx,-dy]
        
    def update(self, dt):
        self.front = euclid.Vector3(
                                    math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
                                    math.sin(math.radians(self.pitch)),
                                    math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
                                    ) * 1
        self.right = self.front.cross(self.worldup)
        self.up = self.right.cross(self.front)
        
        speed = dt * self.speed
        
        start = self.position
        if self.strafe[0] != 0:
            start += (self.front * (speed * self.strafe[0]))
        if self.strafe[1] != 0:
            start += (self.right * (speed * self.strafe[1]))
        
        self.position = start
        
if __name__ == "__main__":
    c = LookObject()
    print c.front
    print c.right
    c.look(10, 20)
    c.move(10, 20)
    c.update(10)
    print c.front
    print c.right
    print c.view