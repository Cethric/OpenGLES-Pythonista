# coding: utf-8
import ctypes
from objc_util import *
import glkmath as GLKMath

class GLKEffectPropertyMaterial:
    def __init__(self, c_mat = None):
        if c_mat is None:
            self._mat = ObjCClass('GLKEffectPropertyMaterial').alloc().init()
            print dir(self._mat)
        else:
            self._mat = c_mat
            
    def __str__(self):
        return str(self._mat.description())
            
    def setAmbientColor(self, color):
        self._mat.setAmbientColor_(color, argtypes=[GLKMath.GLKVector4], restype=None)
        
    def getAmbientColor(self):
        return self._mat.ambientColor(argtypes=[], restype=GLKMath.GLKVector4)
        
    ambientColor = property(getAmbientColor, setAmbientColor)
    
    def setDiffuseColor(self, color):
        self._mat.setDiffuseColor_(color, argtypes=[GLKMath.GLKVector4], restype=None)
        
    def getDiffuseColor(self):
        return self._mat.diffuseColor(argtypes=[], restype=GLKMath.GLKVector4)
        
    diffuseColor = property(getDiffuseColor, setDiffuseColor)
    
    def setEmissiveColor(self, color):
        self._mat.setEmissiveColor_(color, argtypes=[GLKMath.GLKVector4], restype=None)
        
    def getEmissiveColor(self):
        return self._mat.emissiveColor(argtypes=[], restype=GLKMath.GLKVector4)
        
    emissiveColor = property(getEmissiveColor, setEmissiveColor)
    
    def setSpecularColor(self, color):
        self._mat.setSpecularColor_(color, argtypes=[GLKMath.GLKVector4], restype=None)
        
    def getSpecularColor(self):
        return self._mat.specularColor(argtypes=[], restype=GLKMath.GLKVector4)
        
    specularColor = property(getSpecularColor, setSpecularColor)
            

__all__ = ['GLKEffectPropertyMaterial']

if __name__ == '__main__':
    m = GLKEffectPropertyMaterial()
    m.ambientColor = GLKMath.GLKVector4(r=0.0, g=1.0, b=0.5, a=0.2)
    print 'ambientColor', m.ambientColor
    print 'diffuseColor', m.diffuseColor
    print 'emissiveColor', m.emissiveColor
    print 'specularColor', m.specularColor