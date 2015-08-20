# coding: utf-8
from OpenGLES.GLES import gles2
from OpenGLES.GLES.gles2 import *
reload(gles2)

class ShaderSource(object):
    def __init__(self, source, shader_type):
        if isinstance(source, file):
            print "Source is of File type"
        self.source = source
        self.shader_type = shader_type
        self.compiled = False
        self.shader_id = None
        
    def compile(self):
        shader = glCreateShader(self.shader_type)
        if(shader == 0):
            print "Failed to create shader"
            return 0
        # Load the shader source
        char_arr = (ctypes.c_char_p * len(self.source))
        ca = char_arr()
        ca[0] = self.source
        args = (GLuint(shader),
                GLsizei(1),
                ca,
                GLint(0))
        glShaderSource.argtypes = (GLuint, GLsizei, char_arr, GLint)
        glShaderSource(*args)
        # Compile the shader
        glCompileShader(shader)
        # Check the compile status
        compiled = GLint(0)
        sargs = (shader, GL_COMPILE_STATUS, ctypes.byref(compiled))
        glGetShaderiv.argtypes = [GLuint, GLenum, ctypes.POINTER(GLint)]
        glGetShaderiv(*sargs)
        print "%s Shader Compile Status: %s" % ("Vertex" if self.shader_type == GL_VERTEX_SHADER else "Fragment", "success" if compiled.value == GL_TRUE else "fail")
        if(compiled.value == GL_FALSE):
            infoLen = GLint()
            glGetShaderiv(shader, GL_INFO_LOG_LENGTH, ctypes.byref(infoLen))
            if(infoLen > 1):
                print "Info len: ", infoLen.value
                infoLog = (ctypes.c_char_p * infoLen.value)()
                glGetShaderInfoLog.argtypes = [
                                                GLuint,
                                                GLsizei,
                                                GLsizei,
                                                ctypes.POINTER((ctypes.c_char_p * infoLen.value))]
                glGetShaderInfoLog(shader, infoLen.value, 0, ctypes.byref(infoLog))
                print ctypes.string_at(infoLog)
            glDeleteShader(shader);
            return 0;
        self.compiled = True
        self.shader_id = shader
        return shader;
    

class ShaderProgram(object):
    def __init__(self, vertex_shader=None, fragment_shader=None, geometry_shader=None):
        self.compiled = False
        self.vertex, self.fragment, self.geometry = vertex_shader, fragment_shader, geometry_shader
        
    def build(self):
        if self.compiled:
            return
            
        if self.vertex:
            self.vertex.compile()
            if not self.vertex.compiled:
                raise RuntimeError("Could not compile vertex shader")
        if self.fragment:
            self.fragment.compile()
            if not self.fragment.compiled:
                raise RuntimeError("Could not compile fragment shader")
        if self.geometry:
            self.geometry.compile()
            if not self.geometry.compiled:
                raise RuntimeError("Could not compile geometry shader")
                
        programObject = glCreateProgram(None)
        if programObject > 0:
            if self.vertex:
                glAttachShader(programObject, self.vertex.shader_id);
            if self.fragment:
                glAttachShader(programObject, self.fragment.shader_id);
            if self.geometry:
                glAttachShader(programObject, self.geometry.shader_id);
            # Bind vPosition to attribute 0
            attr = (ctypes.c_char_p * 1024)()
            attr[0] = "vPosition"
            glBindAttribLocation.argtypes = [GLuint, GLuint, ctypes.c_char_p * 1024]
            glBindAttribLocation(programObject, 0, attr);
            # Link the program
            glLinkProgram(programObject);
            # Check the link status
            linked = GLint()
            glGetProgramiv(programObject, GL_LINK_STATUS, ctypes.byref(linked))
            print "Linked Status in %i" % linked.value
            if linked.value == GL_FALSE:
                infoLen = GLint()
                glGetProgramiv(programObject, GL_INFO_LOG_LENGTH, ctypes.byref(infoLen))
                if(infoLen > 1):
                    print "Info len: ", infoLen.value
                    infoLog = (ctypes.c_char_p * infoLen.value)()
                    glGetProgramInfoLog.argtypes = [
                                                    GLuint,
                                                    GLsizei,
                                                    GLsizei,
                                                    ctypes.POINTER((ctypes.c_char_p * infoLen.value))]
                    glGetProgramInfoLog(programObject, infoLen, 0, ctypes.byref(infoLog))
                    print ctypes.string_at(infoLog)
                glDeleteProgram(programObject);
        self.programObject = programObject
        
    def bind(self):
        glUseProgram(self.programObject)