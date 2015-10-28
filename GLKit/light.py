# coding: utf-8
import ctypes
from objc_util import *
from glkmath import *
import OpenGLES.GLES.gles1 as ES
import transform


PropLight = ObjCClass('GLKEffectPropertyLight')


glk4 = parse_struct('{glkvec4=ffff}')
glk4_union = parse_struct('{glkvec4union=fffff}')

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
        return setGLKVector4(self._light.setPosition_, new_pos)
        
    def getPosition(self):
        return getGLKVector4(self._light.position)
        
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
        return transform.GLKEffectPropertyTransform(self._light.transform())
        
    transform = property(getTransform, setTransform)
    
__all__ = ['GLKEffectPropertyLight', 'GLKLightingType']

if __name__ == '__main__':
    l = GLKEffectPropertyLight()
    print dir(l._light)
    print l.position
    l.position = GLKVector4(x=10, y=10, z=10, w=1)
    print l.position
    t = l.transform
    print t
    tmv = GLKMatrix4()
    tmv.m[:] = [1,1,1,1, 0,0,0,0, 1,1,1,1, 0,0,0,0]
    t.modelviewMatrix = tmv
    print t.modelviewMatrix
    print t