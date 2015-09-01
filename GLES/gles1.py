# coding: utf-8
import ctypes
from objc_util import *

import headers.gl_c
import headers.glext_c
from headers.gl_c import *
from headers.glext_c import *

#reload(headers.gl_c)
#reload(headers.glext_c)

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()