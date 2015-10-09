# coding: utf-8
from objc_util import *
from glkmath import *
import OpenGLES.GLES.gles1 as ES


PropLight = ObjCClass('GLKEffectPropertyLight')


class GLKLightingType:
    PerVertex = 0
    PerPixel = 1
    

class GLKEffectPropertyLight(object):
    def __init__(self, c_light=None):
        if c_light is None:
            self._light = PropLight.alloc().init()
        else:
            self._light = c_light
            
    def __str__(self):
        return str(self._light.description())
        
    def setPosition(self, new_pos):
        self._light.setPosition_(new_pos, argtypes=[GLKVector4], restype=None)
        
    def getPosition(self):
        return self._light.position(argtypes=[], restype=GLKVector4)
        
    position = property(getPosition, setPosition)
        
    def setEnabled(self, enabled):
        e = ES.GL_TRUE if enabled else ES.GL_FALSE
        self._light.enabled = ES.GLboolean(e)
        
    def getEnabled(self):
        i = self._light.enabled()
        e = True if i==ES.GL_TRUE else False
        return e
        
    enabled = property(getEnabled, setEnabled)
    
    def setTransform(self, transform):
        self._light.tansform = transform._trans
        
    def getTransform(self):
        return GLKEffectPropertyTransform(self._light.transform())
        
    transform = property(getTransform, setTransform)
    
__all__ = ['GLKEffectPropertyLight', 'GLKLightingType']