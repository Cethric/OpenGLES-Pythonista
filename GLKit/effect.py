# coding: utf-8
import ctypes
from objc_util import *
from OpenGLES.GLES.headers.GLConstants import GLboolean
from OpenGLES.GLES.gles1 import GL_TRUE, GL_FALSE

import light
import material
import texture
import glkmath as GLKMath
from glkmath import *
import transform
from transform import *


class GLKBaseEffect(object):
    def __init__(self, c_effect=None):
        if c_effect is None:
            baseEffect = ObjCClass("GLKBaseEffect")
            self._effect = baseEffect.alloc().init()
        else:
            self._effect = c_effect
        
    def __str__(self):
        return str(self._effect.description())
        
    def setLabel(self, text):
        self._effect.setLabel_(text)
    
    def getLabel(self):
        inst = self._effect.label()
        return inst
        
    label = property(getLabel, setLabel)
    
    def setTransform(self, transform):
        self._effect.tansform = transform._trans
        
    def getTransform(self):
        return GLKEffectPropertyTransform(self._effect.transform())
        
    transform = property(getTransform, setTransform)
    
    def setLightingType(self, ltype):
        self._effect.setLightingType_(ltype)
        
    def getLightingType(self):
        return self._effect.lightingType()
        
    lightingType = property(getLightingType, setLightingType)
    
    def setLightModelTwoSided(self, sided):
        e = GL_TRUE if sided else GL_FALSE
        self._effect.setLightModelTwoSided_(GLboolean(e))
        
    def getLightModelTwoSided(self):
        i = self._effect.lightModelTwoSided()
        e = True if i==GL_TRUE else False
        return e
        
    lightModelTwoSided = property(getLightModelTwoSided, setLightModelTwoSided)
    
    def setMaterial(self, mat):
        self._effect.setMaterial_(mat._mat)
        
    def getMaterial(self):
        return self._effect.material()
        
    material = property(getMaterial, setMaterial)
    
    def setLightModelAmbientColor(self, color):
        return setGLKVector4(self._effect.setLightModelAmbientColor_, color)
        
    def getLightModelAmbientColor(self):
        return getGLKVector4(self._effect.lightModelAmbientColor)
        
    lightModelAmbientColor = property(getLightModelAmbientColor, setLightModelAmbientColor)
    
    @property
    def light0(self):
        return light.GLKEffectPropertyLight(self._effect.light0())
        
    @property
    def light1(self):
        return light.GLKEffectPropertyLight(self._effect.light1())
        
    @property
    def light2(self):
        return light.GLKEffectPropertyLight(self._effect.light2())
        
    def setTexture2d0(self, tex):
        self._effect.setTexture2d0_(tex._tex)
        
    def getTexture2d0(self):
        return texture.GLKEffectPropertyTexture(self._effect.texture2d0())
        
    texture2d0 = property(getTexture2d0, setTexture2d0)
    
    def setTexture2d1(self, tex):
        self._effect.setTexture2d0_(tex._tex)
        
    def getTexture2d1(self):
        return texture.GLKEffectPropertyTexture(self._effect.texture2d0())
        
    texture2d1 = property(getTexture2d1, setTexture2d1)
    
    def setTextureOrder(self, order):
        self._effect.setTextureOrder_(order)
        
    def getTextureOrder(self):
        return self._effect.textureOrder()
        
    textureOrder = property(getTextureOrder, setTextureOrder)
    
    def setColorMaterialEnabled(self, enabled):
        e = GL_TRUE if enabled else GL_FALSE
        self._effect.setColorMaterialEnabled_(GLboolean(e))
        
    def getColorMaterialEnabled(self):
        i = self._effect.colorMaterialEnabled()
        e = True if i==GL_TRUE else False
        return e
        
    colorMaterialEnabled = property(getColorMaterialEnabled, setColorMaterialEnabled)
    
    def setUseConstantColor(self, enabled):
        e = GL_TRUE if enabled else GL_FALSE
        self._effect.setUseConstantColor_(GLboolean(e))
        
    def getUseConstantColor(self):
        i = self._effect.useConstantColor()
        e = True if i==GL_TRUE else False
        return e
        
    useConstantColor = property(getUseConstantColor, setUseConstantColor)
    
    def setConstantColor(self, color):
        return setGLKVector4(self._effect.setConstantColor_, color)
        
    def getConstantColor(self):
        return getGLKVector4(self._effect.constantColor)
        
    constantColor = property(getConstantColor, setConstantColor)
    
    
    def prepareToDraw(self):
        self._effect.prepareToDraw()
        
        

class GLKReflectionMapEffect(GLKBaseEffect):
    def __init__(self, c_effect=None):
        if c_effect is None:
            baseEffect = ObjCClass("GLKReflectionMapEffect")
            c_effect = baseEffect.alloc().init()
        super(GLKReflectionMapEffect, self).__init__(c_effect)
        
    def setTextureCubeMap(self, tex_map):
        self._effect.setTextureCubeMap_(tex_map._tex)
        
    def getTextureCubeMap(self):
        return texture.GLKEffectPropertyTexture(self._effect.textureCubeMap())
        
    textureCubeMap = property(getTextureCubeMap, setTextureCubeMap)
    
    def setMatrix(self, mat):
        self._effect.setMatrix_(mat, argtypes=[GLKMath.GLKMatrix3], restype=None)
        
    def getMatrix(self):
        return self._effect.matrix(argtypes=[], restype=GLKMath.GLKMatrix3)
        
    matrix = property(getMatrix, setMatrix)
    

class GLKSkyboxEffect(object):
    def __init__(self, c_effect=None):
        if c_effect is None:
            effect = ObjCClass('GLKSkyboxEffect')
            self._effect = effect.alloc().init()
        else:
            self._effect = c_effect
            
    def __str__(self):
        return str(self._effect.description())
        
    def setLabel(self, text):
        self._effect.setLabel_(text)
    
    def getLabel(self):
        inst = self._effect.label()
        return inst
        
    label = property(getLabel, setLabel)
    
    def prepareToDraw(self):
        self._effect.prepareToDraw()
        
    def draw(self):
        self._effect.draw()
        
    def setTransform(self, transform):
        self._effect.tansform = transform._trans
        
    def getTransform(self):
        return GLKEffectPropertyTransform(self._effect.transform())
        
    transform = property(getTransform, setTransform)
    
    def setTextureCubeMap(self, cubeMap):
        self._effect.setTextureCubeMap_(cubeMap._tex)
        
    def getTextureCubeMap(self):
        return texture.GLKEffectPropertyTexture(self._effect.textureCubeMap())
        
    textureCubeMap = property(getTextureCubeMap, setTextureCubeMap)
    
    def setCenter(self, center):
        return setGLKVector3(self._effect.setCenter_, center)
        
    def getCenter(self):
        return getGLKVector3(self._effect.center)
        
    center = property(getCenter, setCenter)
    
    def setXSize(self, x):
        self._effect.setXSize_(x)
        
    def getXSize(self):
        return self._effect.xSize()
        
    xSize = property(getXSize, setXSize)
    
    def setYSize(self, y):
        self._effect.setYSize_(y)
        
    def getYSize(self):
        return self._effect.ySize()
        
    ySize = property(getYSize, setYSize)
    
    def setZSize(self, z):
        self._effect.setXSize_(z)
        
    def getZSize(self):
        return self._effect.zSize()
        
    zSize = property(getXSize, setXSize)

if __name__ == "__main__":
    e = GLKBaseEffect()
    e.constantColor = GLKVector4(r=0.0, g=0.1, b=0.2, a=1)
    print e
    print e.constantColor
    print "REFLECTION MAP EFFECT"
    r = GLKReflectionMapEffect()
    print r
    print "SKYBOX EFFECT"
    s = GLKSkyboxEffect()
    s.center = GLKVector3(x=0.0, y=10.0, z=0.0)
    print s
    print s.center
    print s.xSize