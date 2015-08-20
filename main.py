# coding: utf-8
# NOTE:
# This example requires the euclid.py math library
#1
import sys
if not "." in sys.path:
    sys.path.insert(0, ".")
import ui
from objc_util import *
import time
import colorsys
import math

import OpenGLES.GLES as GLES
import OpenGLES.EAGL as EAGL
import OpenGLES.GLKit as GLKit
import OpenGLES.Util as Util
import OpenGLES.Util.Shader
from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *

import euclid

reload(GLES)
reload(EAGL)
reload(GLKit)
reload(Util)
reload(OpenGLES.Util.Shader)

VERTEX_SHADER_SOURCE = '''
attribute vec3 vPosition;
uniform mat4 MVP;

void main() {
    gl_Position = MVP * vec4(vPosition.xyz, 1);
}
'''

FRAGMENT_SHADER_SOURCE = '''
precision mediump float;
void main() {
    gl_FragColor = vec4(1.0, 0.1, 0.0, 1.0);
}
'''

glviewv = GLKit.GLKView(frame=(0, 0, 800, 600))

class Renderer(Util.RenderCycle):
    def __init__(self):
        Util.RenderCycle.__init__(self)
        self.r, self.g, self.b = (0,0,0)
        
        self.objects = []
        o2 = Util.RenderObject((
                                -1.0,-1.0,-1.0,
                                -1.0,-1.0, 1.0,
                                -1.0, 1.0, 1.0,
                                1.0, 1.0,-1.0,
                                -1.0,-1.0,-1.0,
                                -1.0, 1.0,-1.0,
                                1.0,-1.0, 1.0,
                                -1.0,-1.0,-1.0,
                                1.0,-1.0,-1.0,
                                1.0, 1.0,-1.0,
                                1.0,-1.0,-1.0,
                                -1.0,-1.0,-1.0,
                                -1.0,-1.0,-1.0,
                                -1.0, 1.0, 1.0,
                                -1.0, 1.0,-1.0,
                                1.0,-1.0, 1.0,
                                -1.0,-1.0, 1.0,
                                -1.0,-1.0,-1.0,
                                -1.0, 1.0, 1.0,
                                -1.0,-1.0, 1.0,
                                1.0,-1.0, 1.0,
                                1.0, 1.0, 1.0,
                                1.0,-1.0,-1.0,
                                1.0, 1.0,-1.0,
                                1.0,-1.0,-1.0,
                                1.0, 1.0, 1.0,
                                1.0,-1.0, 1.0,
                                1.0, 1.0, 1.0,
                                1.0, 1.0,-1.0,
                                -1.0, 1.0,-1.0,
                                1.0, 1.0, 1.0,
                                -1.0, 1.0,-1.0,
                                -1.0, 1.0, 1.0,
                                1.0, 1.0, 1.0,
                                -1.0, 1.0, 1.0,
                                1.0,-1.0, 1.0))
        self.objects.append(o2)
        self.v = Util.Shader.ShaderSource(VERTEX_SHADER_SOURCE, GL_VERTEX_SHADER)
        self.f = Util.Shader.ShaderSource(FRAGMENT_SHADER_SOURCE, GL_FRAGMENT_SHADER)
        self.sp = Util.Shader.ShaderProgram(self.v, self.f)
        
        self.projection = euclid.Matrix4.new_perspective(45.0, 600.0/800.0, 0.1, 1000.0)
        self.view = euclid.Matrix4.new_look_at(
                                                euclid.Vector3(4, 3, 3),
                                                euclid.Vector3(0, 0, 0),
                                                euclid.Vector3(0, 1, 0))
        self.model = euclid.Matrix4.new_identity()
        self.MVP = self.projection * self.view * self.model
    
    def setup(self, context):
        if EAGL.setCurrentContext(context):
            self.sp.build()
            self.sp.bind()
            attr = (ctypes.c_char * 3)()
            attr[:] = "MVP"
            glGetUniformLocation.argtypes = [GLuint, (ctypes.c_char * 3)]
            self.MatrixID = glGetUniformLocation(self.sp.programObject, attr);
            if self.MatrixID < 0:
                print "Could not bind 'MVP' "
            glClearColor(1, 1, 1, 1.0)
            
            for rObj in self.objects:
                rObj.setup_object()
                
            glEnable(GL_DEPTH_TEST);
            glDepthFunc(GL_LESS);
            
            glViewport(0, 0, 800, 600);
        else:
            print "Could not Setup OpenGLES"
            
    def update(self, dt):
        #self.r, self.g, self.b = colorsys.hsv_to_rgb((time.time() * 0.1) % 1.0, 1.0, 1)
        glviewv.name = "FPS: %s. Frames: %s" % (self.fps, self.framesDisplayed)
        for rObj in self.objects:
            rObj.update()
    
    def render(self, context):
        if EAGL.setCurrentContext(context):
            # Clear the color buffer
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
            
            glClearColor(self.r, self.g, self.b, 1.0)
            # Set the viewport
            glViewport(0, 0, 800, 600);
            # Use the program object
            self.sp.bind()
                
            #glLoadIdentity(0)
            glUniformMatrix4fv(self.MatrixID, 1, GL_FALSE, (GLfloat * 16)(*list(self.MVP)));
            
            for rObj in self.objects:
                rObj.render()
            #glLoadIdentity(0);

@on_main_thread
def main():
    contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES2)
    GLKit.setRenderEngine(Renderer())
    glviewv.setDelegate(GLKit.GLKViewDelegate())
    glviewv.setContext(contextc)
    glviewv.width = 800
    glviewv.height = 600
    glviewv.present("sheet")

main()