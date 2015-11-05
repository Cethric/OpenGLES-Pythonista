# coding: utf-8
import ctypes
from objc_util import *
from glkmath import *
import OpenGLES.GLES.gles1 as ES
import OpenGLES.GLES.gles1 as ES2
import OpenGLES.GLES.gles3 as ES3

from OpenGLES.EAGL import currentContext

import Image


class GLKTextureEnvMode:
    GLKTextureEnvModeReplace = 0
    GLKTextureEnvModeModulate = 1
    GLKTextureEnvModeDecal = 2


class GLKTextureTarget:
    GLKTextureTarget2D = ES.GL_TEXTURE_2D
    GLKTextureTargetCubeMap = ES3.GL_TEXTURE_CUBE_MAP
    GLKTextureTargetCt = 2
    
    
class GLKTextureInfoOrigin:
    GLKTextureInfoOriginUnknown = 0
    GLKTextureInfoOriginTopLeft = 1
    GLKTextureInfoOriginBottomLeft = 2
    

class GLKTextureInfoAlphaState:
    GLKTextureInfoAlphaStateNone = 0
    GLKTextureInfoAlphaStateNonPremultiplied = 1
    GLKTextureInfoAlphaStatePremultiplied = 2


class GLKEffectPropertyTexture(object):
    def __init__(self, c_tex=None):
        if c_tex is None:
            self._tex = ObjCClass('GLKEffectPropertyTexture').alloc().init()
        else:
            self._tex = c_tex
            
    def __str__(self):
        return str(self._tex.description())
        
    def setEnabled(self, enabled):
        e = ES.GL_TRUE if enabled else ES.GL_FALSE
        self._tex.enabled = ES.GLboolean(e)
        
    def getEnabled(self):
        i = self._tex.enabled()
        e = True if i==ES.GL_TRUE else False
        return e
        
    enabled = property(getEnabled, setEnabled)
    
    def setEnvMode(self, mode):
        self._tex.setEnvMode_(mode)
        
    def getEnvMode(self):
        return self._tex.envMode()
        
    envMode = property(getEnvMode, setEnvMode)
    
    def setName(self, name):
        self._tex.setName_(name)
        
    def getName(self):
        return self._tex.name()
        
    name = property(getName, setName)
    
    def setTarget(self, target):
        self._tex.setTarget_(target)
        
    def getTarget(self):
        return self._tex.target()
        
    target = property(getTarget, setTarget)
    
    

class GLKTextureInfo(object):
    def __init__(self, c_tex=None):
        if c_tex is None:
            tex = ObjCClass('GLKTextureInfo')
            self._tex = tex.alloc().init()
        else:
            self._tex = c_tex
            
    def __str__(self):
        return str(self._tex.description())
        
    def setName(self, name):
        self._tex.setName_(name)
        
    def getName(self):
        return self._tex.name()
        
    name = property(getName, setName)
    
    def setTarget(self, target):
        self._tex.setTarget_(target)
        
    def getTarget(self):
        return self._tex.target()
        
    target = property(getTarget, setTarget)
    
    def setHeight(self, height):
        self._tex.setHeight_(height)
        
    def getHeight(self):
        return self._tex.height()
        
    height = property(getHeight, setHeight)
    
    def setWidth(self, width):
        self._tex.setWidth_(width)
        
    def getWidth(self):
        return self._tex.width()
        
    width = property(getWidth, setWidth)
    
    def setTextureOrigin(self, origin):
        self._tex.setTextureOrigin_(origin)
    
    def getTextureOrigin(self):
        return self._tex.textureOrigin()
        
    textureOrigin = property(getTextureOrigin, setTextureOrigin)
    
    def setAlphaState(self, state):
        self._tex.setAlphaState_(state)
        
    def getAlphaState(self):
        return self._tex.alphaState()
        
    alphaState = property(getAlphaState, setAlphaState)
    
    @property
    def containsMipmaps(self):
        i = self._tex.containsMipmaps()
        return i
        
        
def GLKTextureLoaderCallback(_texinfo, _error):
    print _texinfo, _error
    
    
class CBlock(ObjCBlock):
    def __init__(self, func, restype=None, argtypes=None):
        super(CBlock, self).__init__(func, restype=None, argtypes=None)
        self.func = func

type_encodings['@?'] = CBlock



default_opt = {
    'GLKTextureLoaderApplyPremultiplication': 0,
    'GLKTextureLoaderGenerateMipmaps': 0,
    'GLKTextureLoaderOriginBottomLeft': 0,
    'GLKTextureLoaderGrayscaleAsAlpha': 0,
    'GLKTextureLoaderSRGB': 0
}

DEFAULTS = ns(default_opt)
        
class GLKTextureLoader:
    def __init__(self, sharegroup=None):
        if sharegroup is None:
            sharegroup = currentContext().sharegroup
            print sharegroup
        tl = ObjCClass('GLKTextureLoader')
        if '_sharegroup' in sharegroup.__dict__:
            sharegroup = sharegroup._sharegroup
        self._loader = tl.alloc().initWithSharegroup_(sharegroup)
        
    def textureFromFile(self, path):
        def test(*args, **kwargs):
            print args, kwargs
        callback = CBlock(
                            test,
                            restype=None,
                            argtypes=None
                          )
        
        self._loader.textureWithContentsOfFile_options_queue_completionHandler_(path, DEFAULTS, None, test)
        
    def textureFromURL(self, path):
        url = nsurl(path)
        for x in dir(self._loader):
            if 'texture' in x:
                print x
                
        def test(*args, **kwargs):
            print args, kwargs
        
        self._loader.textureWithContentsOfURL_options_queue_completionHandler_(url, DEFAULTS, None, test)


positions = [ES.GL_TEXTURE0, ES.GL_TEXTURE1, ES.GL_TEXTURE2, ES.GL_TEXTURE3, ES.GL_TEXTURE4, ES.GL_TEXTURE5, ES.GL_TEXTURE6, ES.GL_TEXTURE7, ES.GL_TEXTURE8, ES.GL_TEXTURE9, ES.GL_TEXTURE10, ES.GL_TEXTURE11, ES.GL_TEXTURE12, ES.GL_TEXTURE13, ES.GL_TEXTURE14, ES.GL_TEXTURE15, ES.GL_TEXTURE16, ES.GL_TEXTURE17, ES.GL_TEXTURE18, ES.GL_TEXTURE19, ES.GL_TEXTURE20, ES.GL_TEXTURE21, ES.GL_TEXTURE22, ES.GL_TEXTURE23, ES.GL_TEXTURE24, ES.GL_TEXTURE25, ES.GL_TEXTURE26, ES.GL_TEXTURE27, ES.GL_TEXTURE28, ES.GL_TEXTURE29, ES.GL_TEXTURE30, ES.GL_TEXTURE31]

def loadTexture(pathOrURL, tex_pos=None):
    if tex_pos is None:
        tex_pos = 0
    ES.glActiveTexture(positions[tex_pos])
    
    r = pathOrURL
    d = Image.open(r)
    d.load()
    # d.show()
    width, height = d.width, d.height
    b = list(d.getdata())
    t = (ctypes.c_ubyte * len(b * len(b[0])))
    pt = t()
    print len(b)
    for (i,p) in enumerate(b):
        if not len(p) == len(pt[i*len(b[0]):i*len(b[0])+len(b[0])]):
            print len(p), len(pt[i*len(b[0]):i*len(b[0])+len(b[0])])
            print p
        pt[i*len(b[0]):i*len(b[0])+len(b[0])] = p[:]
    tex_id = ES.GLuint()
    ES.glGenTextures(1, ctypes.byref(tex_id), param0_t=ctypes.POINTER(ES.GLuint))
    ES.glBindTexture(ES.GL_TEXTURE_2D, tex_id)
    ES.glTexParameteri(ES.GL_TEXTURE_2D, ES.GL_TEXTURE_WRAP_S, ES.GL_REPEAT)
    ES.glTexParameteri(ES.GL_TEXTURE_2D, ES.GL_TEXTURE_WRAP_T, ES.GL_REPEAT)
    
    ES.glTexParameteri(ES.GL_TEXTURE_2D, ES.GL_TEXTURE_MAG_FILTER, ES.GL_LINEAR)
    ES.glTexParameteri(ES.GL_TEXTURE_2D, ES.GL_TEXTURE_MIN_FILTER, ES.GL_LINEAR)
    
    ES.glGenerateMipmapOES(ES.GL_TEXTURE_2D)
    
    ES.glTexImage2D(ES.GL_TEXTURE_2D, 0, ES.GL_RGBA, width, height, 0, ES.GL_RGBA, ES.GL_UNSIGNED_BYTE, byref(pt))
    del pt
    return tex_id

def useTexture(tex_id, shader_program, name='texture', tex_pos=None):
    if tex_pos is None:
        tex_pos = 0
    if tex_id is not None:
        ES.glActiveTexture(positions[tex_pos])
        ES.glBindTexture(ES.GL_TEXTURE_2D, tex_id)
        shader_program.uniform1i(name, tex_pos)
    
    

__all__ = [
            'GLKEffectPropertyTexture', 'GLKTextureTarget', 'GLKTextureEnvMode',
            'GLKTextureInfo', 'GLKTextureInfoOrigin', 'GLKTextureInfoAlphaState',
            'loadTexture', 'useTexture'
          ]

if __name__ == '__main__':
    def dispatch_queue_create(name, parent):
        func = c.dispatch_queue_create
        func.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
        func.restype = ctypes.c_void_p
        return ObjCInstance(func(name, parent))
    
    textureloader = ObjCClass('GLKTextureLoader')
    print dir(textureloader.alloc())
    queue = dispatch_queue_create('test_queue', None)
    
    def callback_func(_self, _info, _error):
        if _error is not None:
            print 'Error Loading texture'
            print ObjCInstance(_error)
        else:
            print ObjCInstance(_info)
    
    callback = ObjCBlock(callback_func, None, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p])
    textureloader.alloc().textureWithContentsOfURL_options_queue_completionHandler_(nsurl(os.path.abspath('test.png')), DEFAULTS, queue, callback)
    
    
    import sys
    sys.exit(0)
    from OpenGLES.EAGL import setCurrentContext, EAGLContext
    c = EAGLContext()
    c.label = 'Test Context'
    setCurrentContext(c)
    
    t = GLKEffectPropertyTexture()
    print t
    print t.enabled
    print t.envMode
    print t.name
    print t.target
    
    ti = GLKTextureInfo()
    print ti
    print ti.name
    print ti.target
    print ti.height
    print ti.containsMipmaps
    
    from ui import Image as image
    i = image.named('test:Lenna')
    d = i.to_png()
    with open('test.png', 'wb') as f:
        f.write(d)
    t = (ctypes.c_char_p * len(d))
    pt = t()
    pt[:] = d[:]
    tid = loadTexture('test:Lenna')
    print tid
    from OpenGLES.Util.Shader import ShaderProgram
    from OpenGLES.Util.Shader import ShaderSource
    
    with open("../shader.vs", "rb") as f:
        v = ShaderSource(f.read(), ES3.GL_VERTEX_SHADER)
    with open("../shader.fs", "rb") as f:
        f = ShaderSource(f.read(), ES3.GL_FRAGMENT_SHADER)
    s = ShaderProgram(v, f)
    s.build()
    useTexture(tid, s)
    # useTexture(loadTexture('http://i.imgur.com/hCrSRTN.png'), s)
    # tl.textureFromFile('test.png')
    # tl.textureFromURL('http://i.imgur.com/hCrSRTN.png')