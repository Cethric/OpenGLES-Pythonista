# coding: utf-8
import ctypes
from objc_util import *

import headers.gl2_c
import headers.gl2ext_c
from headers.gl2_c import *
from headers.gl2ext_c import *

reload(headers.gl2_c)
reload(headers.gl2ext_c)

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/OpenGLES.framework").load()