# coding: utf-8
import math
import euclid
from OpenGLES.Util import LookObject
from OpenGLES.Util.Model import XMLModel

__all__ = ['set_PhysicsWorld', 'Light', 'PhysicsCamera']

_PhysicsWorld = None

def set_PhysicsWorld(pw):
    global _PhysicsWorld
    _PhysicsWorld = pw
    

class PhysicsCamera(LookObject):
    def __init__(self, position=euclid.Vector3(0,0,0), up=euclid.Vector3(0,1,0), yaw=0.0, pitch=0.0):
        self.position = position
        self.worldup = up
        self.up = euclid.Vector3(0, 0, 0)
        self.front = euclid.Vector3(0, 0, -1)
        self.right = euclid.Vector3(0, 0, 0)
        self.yaw = yaw
        self.pitch = pitch
        self.strafe = [0,0]
        self.speed = 10.0
        self.camera_id = _PhysicsWorld.add_camera(self)
        print "Camera ID:", self.camera_id
        
        self.debug_model = XMLModel(__file__.replace('LightsCameras.py', '../test_model.xml'))
        self.update(0)
        
    @property
    def view(self):
        """
        Returns:
            (euclid.Matrix4): The view matrix to be applied to a MVP
        """
        return euclid.Matrix4.new_look_at(
                                          self.position,
                                          self.position + self.front,
                                          self.up)
    def look(self, dx, dy):
        """
        Set the yaw and pitch of a camera
        Args:
            dx (float): The new yaw to be subtracted from the old yaw
            dy (float): The new pitch to be added to the old pitch
        """
        self.yaw -= dx
        self.yaw %= 360
        self.pitch += dy
        if self.pitch > 89.0:
            self.pitch = 89.0
        elif self.pitch < -89.0:
            self.pitch = -89.0

    
    def move(self, dx, dy):
        """
        Set strafe values
        Args:
            dx (int): The new strafe x value
            dy (int): The new negative strafe y value
        """
        self.strafe = [dx,-dy]
        
    def debug_draw(self, sp):
        self.debug_model.render(sp)
        
    def update(self, dt):
        self.front = euclid.Vector3(
                                    math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch)),
                                    math.sin(math.radians(self.pitch)),
                                    math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
                                    ) * 1
        self.right = self.front.cross(self.worldup)
        self.up = self.right.cross(self.front)
        if self.camera_id:
            (npos,nrot) = _PhysicsWorld.get_object_pos_rot(self.camera_id)
            ny = npos.y
            position = npos
            (heading, attitude, bank) = nrot.get_euler()
            yawd = abs(attitude - self.yaw)
            speed = dt * self.speed
            if self.strafe[0] != 0:
                position += self.front * speed * self.strafe[0]
            if self.strafe[1] != 0:
                position += self.right * speed * self.strafe[1]
            p = position
            _PhysicsWorld.js.eval_js('set_object_pos(%i, %f, %f, %f);' % (self.camera_id, p.x, ny, p.z))
            q = euclid.Quaternion.new_rotate_euler(0, self.yaw + yawd, 0)
            _PhysicsWorld.js.eval_js('set_object_rot(%i, %f, %f, %f, %f);' % (self.camera_id, q.w, q.x, q.y, q.z))
            (npos,nrot) = _PhysicsWorld.get_object_pos_rot(self.camera_id)
            position = euclid.Vector3(*npos)
            self.position = position
            nmodel = euclid.Matrix4.new_translate(*position)
            nmodel *= q.get_matrix()
            self.debug_model.model = nmodel
        else:
            speed = dt * self.speed
            if self.strafe[0] != 0:
                self.position += self.front * speed * self.strafe[0]
            if self.strafe[1] != 0:
                self.position += self.right * speed * self.strafe[1]
                
        self.debug_model.update(dt)
        
if __name__ == '__main__':
    import OpenGLES.Util.Physics
    OpenGLES.Util.Physics.reset()
    _PhysicsWorld = OpenGLES.Util.Physics.PhysicsWorld
    c = PhysicsCamera(euclid.Vector3(10, 10, 10))
    c.update(123)