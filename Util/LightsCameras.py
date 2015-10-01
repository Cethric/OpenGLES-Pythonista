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
        self.camera_id = None
        self.debug_model = None
        LookObject.__init__(self, position, up, yaw, pitch)
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
        p = self.position
        p.y += 1.0
        res = euclid.Matrix4.new_look_at(p, p + self.front, self.up)
        return res
                                          
    def debug_draw(self, sp):
        if self.debug_model:
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
            speed = dt * self.speed
            if self.strafe[0] != 0:
                position += self.front * speed * self.strafe[0]
            if self.strafe[1] != 0:
                position += self.right * speed * self.strafe[1]
            p = position
            _PhysicsWorld.js.eval_js('set_object_pos(%i, %f, %f, %f);' % (self.camera_id, p.x, ny, p.z))
            # I don't like how rotations are handled.
            # They should pay more attention to what is happening in the physics environment as well.
            r = math.radians(-self.yaw)
            q = euclid.Quaternion.new_rotate_euler(r, 0, 0)
            _PhysicsWorld.js.eval_js('set_object_rot(%i, %f, %f, %f, %f);' % (self.camera_id, q.w, q.x, q.y, q.z))
            (npos,nrot) = _PhysicsWorld.get_object_pos_rot(self.camera_id)
            position = euclid.Vector3(*npos)
            self.position = position
            if self.debug_model:
                nmodel = euclid.Matrix4.new_translate(*position)
                nmodel *= q.get_matrix()
                self.debug_model.model = nmodel
        else:
            speed = dt * self.speed
            if self.strafe[0] != 0:
                self.position += self.front * speed * self.strafe[0]
            if self.strafe[1] != 0:
                self.position += self.right * speed * self.strafe[1]
        if self.debug_model:        
            self.debug_model.update(dt)
        
if __name__ == '__main__':
    import OpenGLES.Util.Physics
    OpenGLES.Util.Physics.reset()
    _PhysicsWorld = OpenGLES.Util.Physics.PhysicsWorld
    c = PhysicsCamera(euclid.Vector3(10, 10, 10))
    c.update(123)