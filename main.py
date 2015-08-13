# coding: utf-8
import ui
from objc_util import *
import time
import colorsys

import GLES
import EAGL
import GLKit
import Util
from GLES.gles1 import *
from GLES.gles2 import *

reload(GLES)
reload(EAGL)
reload(GLKit)
reload(Util)

class Renderer(Util.RenderCycle):
    def __init__(self):
        Util.RenderCycle.__init__(self)
        self.r, self.g, self.b = colorsys.hsv_to_rgb((time.time() * 0.1) % 1.0, 0.1, 1)
    
    def setup(self, context):
        if (EAGL.setCurrentContext(context)):
            glClearColor(1, 1, 1, 1.0)
            vert = Util.loadShader("attribute vec4 vPosition;\n"
                                   "void main() {\n"
                                   "    gl_Position = vPosition;\n"
                                   "}",
                                   GLenum(GL_VERTEX_SHADER))
            frag = Util.loadShader("precision mediump float;\n"
                                   "void main() {\n"
                                   "    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);\n"
                                   "}",
                                   GLenum(GL_FRAGMENT_SHADER))
            programObject = glCreateProgram(None)
            print programObject
            if(programObject > 0):
                glAttachShader(programObject, vert);
                glAttachShader(programObject, frag);
                # Bind vPosition to attribute 0
                glBindAttribLocation(programObject, 0, "vPosition");
                # Link the program
                glLinkProgram(programObject);
                # Check the link status
                linked = GLint()
                glGetProgramiv(programObject, GL_LINK_STATUS, ctypes.byref(linked))
                print linked
                if(not linked):
                    infoLen = GLint()
                    glGetProgramiv(programObject, GL_INFO_LOG_LENGTH, ctypes.byref(infoLen))
                    if(infoLen > 1):
                        infoLog = (ctypes.c_char * infoLen)();
                        glGetProgramInfoLog(programObject, infoLen, 0, infoLog);
                        esLogMessage("Error linking program:\n%s\n" % infoLog);
                glDeleteProgram(programObject);
                
            # Store the program object
            self.programObject = programObject;
        else:
            print "Could not Setup OpenGLES"
            
    def update(self, dt):
        self.r, self.g, self.b = colorsys.hsv_to_rgb((time.time() * 0.1) % 1.0, 1.0, 1)
    
    def render(self, context):
        print context.API()
        if (EAGL.setCurrentContext(context)):
            glClearColor(self.r, self.g, self.b, 1.0)
            verts = (0.0, 0.5, 0.0, -0.5, -0.5, 0.0, 0.5, -0.5, 0.0)
            vVertices = (GLfloat * 9)(*verts)
            # Set the viewport
            glViewport(0, 0, 800, 600);
            # Clear the color buffer
            glClear(GL_COLOR_BUFFER_BIT);
            # Use the program object
            glUseProgram(self.programObject)
            # Load the vertex data
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, vVertices);
            glEnableVertexAttribArray(0);
            glDrawArrays(GL_TRIANGLES, 0, 3);

@on_main_thread
def main():
    glviewv = GLKit.GLKView(frame=(0, 0, 200, 200))
    glview = glviewv.glview
    contextc = EAGL.EAGLContext(EAGL.RenderingAPI.OpenGLES3)
    context = contextc._context
    r = Renderer()
    
    GLKit.renderEngine = r
    
    delegate = GLKit.GLKViewDelegate()
    glviewv.setDelegate(delegate)
    glviewv.setContext(contextc)

    
    glviewv.width = 800
    glviewv.height = 600
    glviewv.present("sheet")

main()