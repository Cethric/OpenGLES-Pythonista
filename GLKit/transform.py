# coding: utf-8
import ctypes
from objc_util import *

from glkmath.vector4 import *
from glkmath.matrix4 import *
from glkmath.matrix3 import *

PropTans = ObjCClass('GLKEffectPropertyTransform')

class GLKEffectPropertyTransform:
    def __init__(self, c_trans=None):
        if c_trans is None:
            self._trans = PropTans.alloc().init()
        else:
            self._trans = c_trans
            
    def setDirtyUniforms(self, uniforms):
        self._trans.setDirtyUniforms_(uniforms)
        
    def getDirtyUniforms(self):
        return self._trans.dirtyUniforms()
        
    dirtyUniforms = property(getDirtyUniforms, setDirtyUniforms)
    
    def setEffect(self, effect):
        self._trans.setEffect_(effect)
        
    def getEffect(self):
        return self._trans.effect()
        
    effect = property(getEffect, setEffect)
    
    def setFshSource(self, source):
        self._trans.setFshSource_(source)
        
    def getFshSource(self):
        return self._trans.fshSource()
        
    fshSource = property(getFshSource, setFshSource)
    
    def setInvModelviewMatrixLoc(self, mvl):
        self._trans.setInvModelviewMatrixLoc_(mvl)
        
    def getInvModelviewMatrixLoc(self):
        return self._trans.invModelviewMatrixLoc()
        
    invModelviewMatrixLoc = property(getInvModelviewMatrixLoc, setInvModelviewMatrixLoc)
    
    def setInvModelviewMatrix(self, imvm):
        self._trans.setInvModelviewMatrix_(imvm, argtypes=[GLKMatrix4], restype=None)
        
    def getInvModelviewMatrix(self):
        return self._trans.invModelviewMatrix(argtypes=[], restype=GLKMatrix4)
        
    invModelviewMatrix = property(getInvModelviewMatrix, setInvModelviewMatrix)
    
    def setLocation(self, sl):
        self._trans.setLocation_(sl)
        
    def getLocation(self):
        return self._trans.location()
        
    location = property(getLocation, setLocation)
    
    def setMasksInitialized(self, smi):
        self._trans.setMasksInitialized_(smi)
        
    def getMasksInitialized(self):
        return self._trans.masksInitialized()
        
    masksInitialized = property(getMasksInitialized, setMasksInitialized)
    
    def setModelviewMatrixLoc(self, mvl):
        self._trans.setModelviewMatrixLoc_(mvl)
        
    def getModelviewMatrixLoc(self):
        return self._trans.modelviewMatrixLoc()
        
    modelviewMatrixLoc = property(getModelviewMatrixLoc, setModelviewMatrixLoc)
    
    def setModelviewMatrix(self, mvm):
        self._trans.setModelviewMatrix_(mvm, argtypes=[GLKMatrix4], restype=None)
        
    def getModelviewMatrix(self):
        return self._trans.modelviewMatrix(argtypes=[], restype=GLKMatrix4)
        
    modelviewMatrix = property(getModelviewMatrix, setModelviewMatrix)
    
    def setMvpMatrixLoc(self, mvpl):
        self._trans.setMvpMatrixLoc_(mvpl)
        
    def getMvpMatrixLoc(self):
        return self._trans.mvpMatrixLoc()
        
    mvpMatrixLoc = property(getMvpMatrixLoc, setMvpMatrixLoc)
    
    def setMvpMatrix(self, mvp):
        self._trans.setMvpMatrix_(mvp, argtypes=[GLKMatrix4], restype=None)
        
    def getMvpMatrix(self):
        return self._trans.mvpMatrix(argtypes=[], restype=GLKMatrix4)
        
    mvpMatrix = property(getMvpMatrix, setMvpMatrix)
    
    def setNameString(self, nameString):
        self._trans.setNameString_(nameString)
        
    def getNameString(self):
        return self._trans.nameString()
        
    nameString = property(getNameString, setNameString)
    
    def setNormalMatrixLoc(self, nml):
        self._trans.setNormalMatrixLoc_(nml)
        
    def getNormalMatrixLoc(self):
        return self._trans.normalMatrixLoc()
        
    normalMatrixLoc = property(getNormalMatrixLoc, setNormalMatrixLoc)
    
    def setNormalMatrix(self, nm):
        self._trans.setNormalMatrix_(nm, argtypes=[GLKMatrix3], restype=None)
        
    def getNormalMatrix(self):
        return self._trans.normalMatrix(argtypes=[], restype=GLKMatrix3)
        
    normalMatrix = property(getNormalMatrix, setNormalMatrix)
    
    def setProjectionMatrixLoc(self, pml):
        self._trans.setProjectionMatrixLoc_(pml)
        
    def getProjectionMatrixLoc(self):
        return self._trans.projectionMatrixLoc()
        
    projectionMatrixLoc = property(getProjectionMatrixLoc, setProjectionMatrixLoc)
    
    def setProjectionMatrix(self, pm):
        self._trans.setProjectionMatrix_(pm, argtypes=[GLKMatrix4], restype=None)
        
    def getProjectionMatrix(self):
        return self._trans.projectionMatrix(argtypes=[], restype=GLKMatrix4)
        
    projectionMatrix = property(getProjectionMatrix, setProjectionMatrix)
    
    def setVshSource(self, source):
        self._trans.setVshSource_(source)
        
    def getVshSource(self):
        return self._trans.vshSource()
        
    vshSource = property(getVshSource, setVshSource)
    
    @property
    def description(self):
        return self._trans.description()
        
    def __str__(self):
        return str(self.description)
        
__all__ = ['GLKEffectPropertyTransform']

if __name__ == '__main__':
    t = GLKEffectPropertyTransform()
    print t
    # print t.dirtyUniforms
    # print t.effect
    # print t.fshSource
    # print t.invModelviewMatrixLoc
    # print t.invModelviewMatrix
    # print t.location
    # print t.masksInitialized
    # print t.modelviewMatrixLoc
    # print t.modelviewMatrix
    # print t.mvpMatrixLoc
    # print t.mvpMatrix
    # print t.nameString
    # print t.normalMatrixLoc
    print t.normalMatrix
    # print t.projectionMatrixLoc
    # print t.projectionMatrix
    # print t.vshSource