# coding: utf-8
import ctypes
from objc_util import *
from glkmath import *
import OpenGLES.GLES.gles1 as ES
import OpenGLES.GLES.gles3 as ES3

from OpenGLES.EAGL import currentContext


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
        self._loader = tl.alloc().initWithSharegroup_(sharegroup._sharegroup)
        
    def textureFromFile(self, path):
        callback = CBlock(GLKTextureLoaderCallback, restype=None, argtypes=[ctypes.c_void_p, ctypes.c_void_p])
        print dir(self._loader)
        print DEFAULTS
        # self._loader.textureWithContentsOfFile_options_queue_completionHandler_(path, DEFAULTS, None, callback)
    
    
__all__ = [
            'GLKEffectPropertyTexture', 'GLKTextureTarget', 'GLKTextureEnvMode',
            'GLKTextureInfo', 'GLKTextureInfoOrigin', 'GLKTextureInfoAlphaState',
          ]
    
    
if __name__ == '__main__':
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
    
    tl = GLKTextureLoader()
    from ui import Image
    i = Image.named('test:Lenna')
    with open('test.png', 'wb') as f:
        f.write(i.to_png())
    tl.textureFromFile('test.png')