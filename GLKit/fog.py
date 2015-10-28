# coding: utf-8
from objc_util import *
from glkmath import *
import OpenGLES.GLES.gles1 as ES


class GLKFogMode:
    GLKFogModeExp = 0
    GLKFogModeExp2 = 1
    GLKFogModeLinear = 2


class GLKEffectPropertyFog(object):
    def __init__(self, c_fog=None):
        if c_fog is None:
            self._fog = ObjCClass('GLKEffectPropertyFog').alloc().init()
        else:
            self._fog = c_fog
            
    def __str__(self):
        return str(self._fog.description())
        
    def setEnabled(self, enabled):
        e = ES.GL_TRUE if enabled else ES.GL_FALSE
        self._fog.enabled = ES.GLboolean(e)
        
    def getEnabled(self):
        i = self._fog.enabled()
        e = True if i==ES.GL_TRUE else False
        return e
        
    enabled = property(getEnabled, setEnabled)
    
    def setMode(self, mode):
        self._fog.setMode_(mode)
        
    def getMode(self):
        return self._fog.mode()
        
    mode = property(getMode, setMode)
    
    def setColor(self, color):
        return setGLKVector4(self._fog.setColor_, color)
        
    def getColor(self):
        return getGLKVector4(self._fog.color)
        
    color = property(getColor, setColor)
    
    def setDensity(self, density):
        self._fog.setDensity_(density)
        
    def getDensity(self):
        return self._fog.density()
        
    density = property(getDensity, setDensity)
    
    def setStart(self, start):
        self._fog.setStart_(start)
        
    def getStart(self):
        return self._fog.start()
        
    start = property(getStart, setStart)
    
    def setEnd(self, end):
        self._fog.setEnd_(end)
        
    def getEnd(self):
        return self._fog.end()
        
    end = property(getEnd, setEnd)
    
if __name__ == '__main__':
    f = GLKEffectPropertyFog()
    print f
    print f.enabled
    print f.mode
    print f.color
    print f.density
    print f.start
    print f.end