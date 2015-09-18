# coding: utf-8
from OpenGLES.GLES import gles1 as GLES1
from OpenGLES.GLES import gles2 as GLES2
from OpenGLES.GLES import gles3 as GLES3
import OpenGLES
import euclid
import math
import ctypes
import xmltodict


__all__ = ["XMLModel"]

_loaded_files = {}

class XMLModel(OpenGLES.Util.RenderObject):
    def __init__(self, obj_xml, pos=euclid.Vector3(0,0,0)):
        OpenGLES.Util.RenderObject.__init__(self, pos)
        self.frames = {}
        self.frame = 0
        
        if obj_xml in _loaded_files:
            self.frames = _loaded_files[obj_xml]
            return None
        
        print "Loading Object File"
        
        with open(obj_xml, "rb") as f:
            self.data = xmltodict.parse(f.read())["model"]
        
        for anim in self.data:
            for frame in self.data[anim]:
                self._parse_frame(self.data[anim][frame])
                
        _loaded_files[obj_xml] = self.frames
            
    def _parse_frame(self, frame):
        verts = []
        for vert in frame["vert"]:
            x,y,z = vert["#text"].split(" ")
            verts.append(float(x))
            verts.append(float(y))
            verts.append(float(z))
            
        print "Frame '%i' registered" % int(frame["@num"])
        self.bind_frame_to_buffer(int(frame["@num"]), verts)
        
    def bind_frame_to_buffer(self, frame_id, verts):
        vertextArray = GLES1.GLuint()
        vertexBuffer = GLES1.GLuint()
        print vertexBuffer, vertextArray
        GLES2.glGenVertexArraysOES(1, ctypes.byref(vertextArray), GLES1.GLsizei, ctypes.POINTER(GLES1.GLuint))
        GLES2.glBindVertexArrayOES(vertextArray)
        
        GLES2.glGenBuffers(1, ctypes.byref(vertexBuffer), GLES1.GLsizei, ctypes.POINTER(GLES1.GLuint))
        GLES2.glBindBuffer(GLES2.GL_ARRAY_BUFFER, vertexBuffer)
        GLES2.glBufferData(
                           GLES2.GL_ARRAY_BUFFER,
                           len(verts) * ctypes.sizeof(GLES2.GLfloat),
                           (GLES2.GLfloat * len(verts))(*verts),
                           GLES2.GL_STATIC_DRAW,
                           voiddata_t=(GLES2.GLfloat * len(verts)))
                           
        self.frames[frame_id] = (ctypes.c_float * len(verts))(*verts)
        
    def render(self, sp):
        sp.uniform4x4("M", list(self.model))
        frame = self.frames[self.frame]
        GLES2.glVertexAttribPointer(0,
                                    3, 
                                    GLES2.GL_FLOAT,
                                    GLES2.GL_FALSE,
                                    0,
                                    ctypes.pointer(frame),
                                    GLES1.GLuint,
                                    GLES1.GLint,
                                    GLES1.GLenum,
                                    GLES1.GLboolean,
                                    GLES1.GLsizei,
                                    ctypes.POINTER((ctypes.c_float * len(frame)))
                                    )
        GLES2.glEnableVertexAttribArray(0)
        GLES2.glDrawArrays(GLES2.GL_TRIANGLES, 0, len(frame) / 3)
            

if __name__ == "__main__":
    m = XMLModel("../test_model.xml")
    print m
    print _loaded_files