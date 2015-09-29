# coding: utf-8
"""
OpenGLES.Util.Model.py
Object rendering methods
Attributes:
    _loaded_files (dict): Stores all of the already loaded files to
                          save time loading data
    _loaded_vbos (dict): If the file has already been loaded once before
                         then don't load it again just refrence this value
"""
from OpenGLES.GLES import gles1 as GLES1
from OpenGLES.GLES import gles2 as GLES2
from OpenGLES.GLES import gles3 as GLES3
from OpenGLES.Util import Physics
import OpenGLES
import euclid
import math
import ctypes
import time
import os
import xmltodict
from objc_util import *


__all__ = ["XMLModel", "PhysicsObject"]

# {'filename': {'framenum': ctypes.c_float_array}}
_loaded_files = {}
# {'filename': {'framenum': ctypes.c_uint `bufferid`}}
_loaded_vbos = {}


class XMLModel(OpenGLES.Util.RenderObject):
    def __init__(self, obj_xml, pos=euclid.Vector3(0,0,0)):
        """
        Subclass of OpenGLES.Util.RenderObject
        Args:
            obj_xml (str): The path to the xml file storing the object data
            pos (Optional[euclid.Vector3]): The initial position of the object
        Attributes:
            file (str): The filename of the object
            frames (dict): To be implimented later to support animations
            bframes (dict): To be implimented later to support animations
            frame (int): The current frame to render
            data (dict): Dictionary representation of the XML file
        """
        OpenGLES.Util.RenderObject.__init__(self, pos)
        self.file = os.path.basename(obj_xml)
        self.frames = {}
        self.bframes = {}
        self.frame = 0
        if self.file in _loaded_files:
            self.frames = _loaded_files[self.file]
            return None
            
        self.data = {}
        with open(obj_xml, "rb") as f:
            self.data = xmltodict.parse(f.read())["model"]
        
        for frame in self.data['anim']:
            frame = self.data['anim'][frame]
            self._parse_frame(frame)
            
        _loaded_files[self.file] = self.frames
            
    def setup_object(self):
        """
        Called once to set the object up before rendering
        """
        for frame in self.frames:
            self.bind_frame_to_buffer(frame, self.frames[frame])
            
    def _parse_frame(self, frame):
        """
        Parse the frame to get vertex positions and eventually
        other data out of the XML dictionary
        Args:
            frame (dict): A single frame from the XML file
        """
        verts = []
        for vert in frame["vert"]:
            x,y,z = vert["#text"].split(" ")
            verts.append(float(x))
            verts.append(float(y))
            verts.append(float(z))
            
        print "Frame '%i' registered" % int(frame["@num"])
        frame_id = int(frame["@num"])
        self.frames[frame_id] = (ctypes.c_float * len(verts))(*verts)
        
    def bind_frame_to_buffer(self, frame_id, verts):
        """
        For every frame create a OpenGLES GL_ARRAY_BUFFER for rendering
        Args:
            frame_id (int): The id of the frame to be setup
            verts (array(OpenGLES.GLES.header.GLConstants.GLfloat): A ctypes array of the
                                                                    vertex data.
        """
        if self.file in _loaded_vbos:
            if frame_id in _loaded_vbos[self.file]:
                self.vertexBuffer = _loaded_vbos[self.file][frame_id]
                return
        vertexBuffer = GLES1.GLuint()
        GLES2.glGenBuffers(1, ctypes.byref(vertexBuffer), GLES1.GLsizei, ctypes.POINTER(GLES1.GLuint))
        GLES2.glBindBuffer(GLES2.GL_ARRAY_BUFFER, vertexBuffer)
        v = verts
        lv = len(v)
        va = (GLES2.GLfloat * len(v))
        GLES2.glBufferData(
                           GLES2.GL_ARRAY_BUFFER,
                           lv,
                           v,
                           GLES2.GL_STATIC_DRAW,
                           voiddata_t=va)
        self.vertexBuffer = vertexBuffer
        _loaded_vbos[self.file] = {frame_id: vertexBuffer}
        GLES2.glBindBuffer(GLES2.GL_ARRAY_BUFFER, 0)
        
    def render(self, sp):
        """
        Called every frame to render the object
        Args:
            sp (OpenGLES.Util.Shader.ShaderObject): The currently bound shader object to pass
                                                    the model matrix to.
        """
        if self.renderable:
            # GLES2.glBindBuffer(GLES2.GL_ARRAY_BUFFER, self.vertexBuffer)
            sp.uniform4x4("M", list(self.model))
            GLES2.glVertexAttribPointer(0, 3, GLES1.GL_FLOAT, GLES1.GL_FALSE, 0, self.vVertices, voidpointer_t=(GLES1.GLfloat * self.vSize));
            GLES2.glEnableVertexAttribArray(0);
            GLES2.glDrawArrays(GLES2.GL_TRIANGLES, 0, self.vSize / 3);
            # GLES2.glBindBuffer(GLES2.GL_ARRAY_BUFFER, 0)
        
    def update(self, dt):
        """
        Called every frame before rendering
        Args:
            dt (int): The time since last update
        """
        frame = self.frames[self.frame]
        self.vSize = len(frame)
        self.vVertices = frame
        
        
class PhysicsObject(XMLModel):
    def __init__(self, *args, **kwargs):
        """
        Subclass of OpenGLES.Util.Model.XMLModel with reference to a physics body
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Attributes:
            pos (list(float)): Initial position of the object
            i (int): The id of the physics object
        """
        XMLModel.__init__(self, *args, **kwargs)
        # self.model.d = x pos, self.model.h = y pos, self.model.l = z pos... I think
        self.pos = [self.model.d, self.model.h, self.model.l]
        # self.i = Physics.PhysicsWorld.add_object(self.frames[self.frame], 10, self.pos, True)
        self.i = Physics.PhysicsWorld.add_cube(*self.pos)
        # print "Object ID:", self.i
        
    def get_mat(self):
        """
        Get the model matrix for the object
        Attributes:
            start (float): the start time of this function
            end (float): the end time of this function
            mat (euclid.Matrix4): the model matrix of the object
        Returns:
            mat (euclid.Matrix4): the model matrix of the object
        """
        start = time.clock()
        mat = Physics.PhysicsWorld.get_object_mat(self.i)
        end = time.clock()
        # print self, '.get_mat', end - start
        return mat
    
    def update(self, dt):
        """
        Called every frame before rendering
        Args:
            dt (int): The time since last update
        """
        XMLModel.update(self, dt)
        start = time.clock()
        self.model = self.get_mat()
        end = time.clock()
        #print end - start

if __name__ == "__main__":
    m = XMLModel("../test_model.xml")
    m.setup_object()
    m2 = PhysicsObject("../test_model.xml")
    m2.setup_object()
    print '_loaded_files', _loaded_files
    print '_loaded_vbos', _loaded_vbos
    