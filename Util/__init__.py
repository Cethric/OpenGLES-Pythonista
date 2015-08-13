# coding: utf-8
import ctypes
from objc_util import *

from OpenGLES.GLES.gles1 import *
from OpenGLES.GLES.gles2 import *
from OpenGLES.GLES.gles3 import *


class RenderCycle(object):
    def __init__(self):
        pass
        
    def render(self, context):
        print "Draw"
        
    def update(self, dt):
        print "Updating with a time step of %f s" % dt
        
    def setup(self, context):
        pass
        
        
class RenderObject(object):
    def __init__(self, verticies=[], colour=[], uv=[], indecies=[]):
        pass
        
    def _setup_object(self):
        pass
        
    def render(self):
        pass
        
    def update(self):
        pass
        
        
def create_GLchar(string):
    return (GLchar * len(string))(*list(string))
    
def loadShader(source, glsl_type):
    shader = GLuint()
    compiled = GLint()
    # Create the shader object
    shader = glCreateShader(glsl_type)
    if(shader == 0):
        print "Failed to create shader"
        return 0;
    # Load the shader source
    glShaderSource(shader, 1, shaderSrc, 0)
    # Compile the shader
    glCompileShader(shader)
    # Check the compile status
    
    glGetShaderiv(shader, GL_COMPILE_STATUS, ctypes.byref(compiled))
    if(not compiled):
        infoLen = GLint(0)
        glGetShaderiv(shader, GL_INFO_LOG_LENGTH, ctypes.byref(infoLen))
        if(infoLen > 1):
            infoLog = (ctypes.c_char * infoLen)()
            glGetShaderInfoLog(shader, infoLen, 0, infoLog);
            print("Error compiling shader:\n%s\n" % infoLog);
        glDeleteShader(shader);
        return 0;
    return shader;