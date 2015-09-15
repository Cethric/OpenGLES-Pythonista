# Generated Files. DO NOT EDIT
# Generated on: 09/15/15 17:53:14
import ctypes
from objc_util import *
from GLConstants import *

DEBUG = 1
loaded = [0, 0]

# GLES Constants
GL_INFO_LOG_LENGTH = 0x00008b84
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x00008cd6
GL_DEPTH_BITS = 0x00000d56
GL_LINE_STRIP = 0x00000003
GL_TEXTURE24 = 0x000084d8
GL_FRAMEBUFFER_COMPLETE = 0x00008cd5
GL_UNSIGNED_SHORT_5_6_5 = 0x00008363
GL_RGB5_A1 = 0x00008057
GL_TEXTURE30 = 0x000084de
GL_TEXTURE31 = 0x000084df
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x00008623
GL_TEXTURE_CUBE_MAP = 0x00008513
GL_SRC_ALPHA_SATURATE = 0x00000308
GL_VERTEX_SHADER = 0x00008b31
GL_TEXTURE5 = 0x000084c5
GL_CONSTANT_ALPHA = 0x00008003
GL_DEPTH_CLEAR_VALUE = 0x00000b73
GL_DITHER = 0x00000bd0
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x00008622
GL_TEXTURE20 = 0x000084d4
GL_FLOAT_VEC2 = 0x00008b50
GL_FLOAT_VEC3 = 0x00008b51
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x00008d44
GL_TEXTURE18 = 0x000084d2
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x00008cd0
GL_STENCIL_REF = 0x00000b97
GL_VALIDATE_STATUS = 0x00008b83
GL_FLOAT = 0x00001406
GL_ACTIVE_ATTRIBUTES = 0x00008b89
GL_COMPILE_STATUS = 0x00008b81
GL_POINTS = 0x00000000
GL_TEXTURE17 = 0x000084d1
GL_BLEND = 0x00000be2
GL_MIRRORED_REPEAT = 0x00008370
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_RENDERBUFFER_BLUE_SIZE = 0x00008d52
GL_UNSIGNED_SHORT = 0x00001403
GL_FASTEST = 0x00001101
GL_REPEAT = 0x00002901
GL_MAX_RENDERBUFFER_SIZE = 0x000084e8
GL_DEPTH_COMPONENT16 = 0x000081a5
GL_POLYGON_OFFSET_UNITS = 0x00002a00
GL_SHADER_SOURCE_LENGTH = 0x00008b88
GL_ONE_MINUS_DST_COLOR = 0x00000307
GL_ONE_MINUS_SRC_COLOR = 0x00000301
GL_TEXTURE22 = 0x000084d6
GL_TEXTURE21 = 0x000084d5
GL_TEXTURE7 = 0x000084c7
GL_TEXTURE27 = 0x000084db
GL_TEXTURE26 = 0x000084da
GL_TEXTURE25 = 0x000084d9
GL_TEXTURE = 0x00001702
GL_BLEND_EQUATION_ALPHA = 0x0000883d
GL_TEXTURE8 = 0x000084c8
GL_TEXTURE29 = 0x000084dd
GL_TEXTURE28 = 0x000084dc
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x00008895
GL_TEXTURE9 = 0x000084c9
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x00008518
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x00008516
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x0000851a
GL_STENCIL_PASS_DEPTH_PASS = 0x00000b96
GL_INCR_WRAP = 0x00008507
GL_LINE_LOOP = 0x00000002
GL_TEXTURE4 = 0x000084c4
GL_COLOR_BUFFER_BIT = 0x00004000
GL_TEXTURE6 = 0x000084c6
GL_DONT_CARE = 0x00001100
GL_ACTIVE_UNIFORMS = 0x00008b86
GL_LINEAR_MIPMAP_LINEAR = 0x00002703
GL_TEXTURE2 = 0x000084c2
GL_TEXTURE3 = 0x000084c3
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x00008517
GL_DECR_WRAP = 0x00008508
GL_UNSIGNED_INT = 0x00001405
GL_BLEND_EQUATION = 0x00008009
GL_BYTE = 0x00001400
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x00008dfb
GL_RGBA = 0x00001908
GL_ATTACHED_SHADERS = 0x00008b85
GL_INVALID_VALUE = 0x00000501
GL_RENDERBUFFER_STENCIL_SIZE = 0x00008d55
GL_GEQUAL = 0x00000206
GL_SAMPLE_COVERAGE_INVERT = 0x000080ab
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x000086a2
GL_LINES = 0x00000001
GL_ONE = 0x00000001
GL_TEXTURE19 = 0x000084d3
GL_TEXTURE16 = 0x000084d0
GL_TEXTURE0 = 0x000084c0
GL_LINE_WIDTH = 0x00000b21
GL_GENERATE_MIPMAP_HINT = 0x00008192
GL_TEXTURE12 = 0x000084cc
GL_COLOR_CLEAR_VALUE = 0x00000c22
GL_TEXTURE10 = 0x000084ca
GL_TEXTURE1 = 0x000084c1
GL_BUFFER_USAGE = 0x00008765
GL_BLEND_EQUATION_RGB = 0x00008009
GL_TEXTURE13 = 0x000084cd
GL_LINK_STATUS = 0x00008b82
GL_TRIANGLE_STRIP = 0x00000005
GL_VERSION = 0x00001f02
GL_BLEND_DST_ALPHA = 0x000080ca
GL_BLEND_COLOR = 0x00008005
GL_FUNC_ADD = 0x00008006
GL_ALPHA_BITS = 0x00000d55
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x00008515
GL_FLOAT_VEC4 = 0x00008b52
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x0000886a
GL_RENDERER = 0x00001f01
GL_ONE_MINUS_CONSTANT_ALPHA = 0x00008004
GL_NEAREST_MIPMAP_LINEAR = 0x00002702
GL_DEPTH_ATTACHMENT = 0x00008d00
GL_CURRENT_VERTEX_ATTRIB = 0x00008626
GL_ARRAY_BUFFER_BINDING = 0x00008894
GL_TEXTURE_2D = 0x00000de1
GL_SHADER_BINARY_FORMATS = 0x00008df8
GL_CONSTANT_COLOR = 0x00008001
GL_DYNAMIC_DRAW = 0x000088e8
GL_OUT_OF_MEMORY = 0x00000505
GL_TEXTURE15 = 0x000084cf
GL_BOOL_VEC3 = 0x00008b58
GL_STENCIL_FUNC = 0x00000b92
GL_VENDOR = 0x00001f00
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x00008cd9
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x00008625
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x00008b9a
GL_SAMPLER_2D = 0x00008b5e
GL_TEXTURE14 = 0x000084ce
GL_ALIASED_LINE_WIDTH_RANGE = 0x0000846e
GL_MAX_TEXTURE_SIZE = 0x00000d33
GL_STENCIL_INDEX8 = 0x00008d48
GL_STENCIL_WRITEMASK = 0x00000b98
GL_DECR = 0x00001e03
GL_BACK = 0x00000405
GL_STENCIL_ATTACHMENT = 0x00008d20
GL_INT = 0x00001404
GL_ES_VERSION_2_0 = 0x00000001
GL_ARRAY_BUFFER = 0x00008892
GL_NUM_SHADER_BINARY_FORMATS = 0x00008df9
GL_UNSIGNED_SHORT_5_5_5_1 = 0x00008034
GL_BOOL_VEC4 = 0x00008b59
GL_FLOAT_MAT4 = 0x00008b5c
GL_POLYGON_OFFSET_FILL = 0x00008037
GL_STREAM_DRAW = 0x000088e0
GL_ZERO = 0x00000000
GL_FRAMEBUFFER_BINDING = 0x00008ca6
GL_ELEMENT_ARRAY_BUFFER = 0x00008893
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x0000851c
GL_FRONT_AND_BACK = 0x00000408
GL_CURRENT_PROGRAM = 0x00008b8d
GL_FRAMEBUFFER = 0x00008d40
GL_FALSE = 0x00000000
GL_LINEAR_MIPMAP_NEAREST = 0x00002701
GL_STENCIL_TEST = 0x00000b90
GL_ONE_MINUS_SRC_ALPHA = 0x00000303
GL_UNSIGNED_SHORT_4_4_4_4 = 0x00008033
GL_SRC_ALPHA = 0x00000302
GL_STENCIL_CLEAR_VALUE = 0x00000b91
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x00008cd2
GL_GREEN_BITS = 0x00000d53
GL_ONE_MINUS_CONSTANT_COLOR = 0x00008002
GL_LUMINANCE_ALPHA = 0x0000190a
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x00008cd7
GL_NEAREST_MIPMAP_NEAREST = 0x00002700
GL_SHADING_LANGUAGE_VERSION = 0x00008b8c
GL_NOTEQUAL = 0x00000205
GL_INVERT = 0x0000150a
GL_MAX_VARYING_VECTORS = 0x00008dfc
GL_STENCIL_BACK_FAIL = 0x00008801
GL_POLYGON_OFFSET_FACTOR = 0x00008038
GL_INCR = 0x00001e02
GL_CULL_FACE = 0x00000b44
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x0000809e
GL_STENCIL_BITS = 0x00000d57
GL_SAMPLE_COVERAGE_VALUE = 0x000080aa
GL_FRAGMENT_SHADER = 0x00008b30
GL_LEQUAL = 0x00000203
GL_TRIANGLE_FAN = 0x00000006
GL_RENDERBUFFER_RED_SIZE = 0x00008d50
GL_STENCIL_PASS_DEPTH_FAIL = 0x00000b95
GL_MAX_VIEWPORT_DIMS = 0x00000d3a
GL_RENDERBUFFER_HEIGHT = 0x00008d43
GL_BLEND_SRC_RGB = 0x000080c9
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x00008b87
GL_NO_ERROR = 0x00000000
GL_STENCIL_BACK_WRITEMASK = 0x00008ca5
GL_FUNC_REVERSE_SUBTRACT = 0x0000800b
GL_VIEWPORT = 0x00000ba2
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x00008cd1
GL_BLEND_SRC_ALPHA = 0x000080cb
GL_INVALID_FRAMEBUFFER_OPERATION = 0x00000506
GL_RENDERBUFFER_ALPHA_SIZE = 0x00008d53
GL_TRIANGLES = 0x00000004
GL_TEXTURE_MAG_FILTER = 0x00002800
GL_STENCIL_VALUE_MASK = 0x00000b93
GL_INVALID_OPERATION = 0x00000502
GL_RENDERBUFFER = 0x00008d41
GL_LOW_INT = 0x00008df3
GL_NONE = 0x00000000
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x00008803
GL_KEEP = 0x00001e00
GL_RGB565 = 0x00008d62
GL_DELETE_STATUS = 0x00008b80
GL_RENDERBUFFER_DEPTH_SIZE = 0x00008d54
GL_TEXTURE11 = 0x000084cb
GL_COLOR_ATTACHMENT0 = 0x00008ce0
GL_SHADER_COMPILER = 0x00008dfa
GL_CLAMP_TO_EDGE = 0x0000812f
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x00008b4c
GL_FRONT = 0x00000404
GL_SCISSOR_BOX = 0x00000c10
GL_FIXED = 0x0000140c
GL_RGBA4 = 0x00008056
GL_SRC_COLOR = 0x00000300
GL_DEPTH_WRITEMASK = 0x00000b72
GL_PACK_ALIGNMENT = 0x00000d05
GL_SUBPIXEL_BITS = 0x00000d50
GL_SHORT = 0x00001402
GL_CULL_FACE_MODE = 0x00000b45
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x00008dfd
GL_CW = 0x00000900
GL_UNSIGNED_BYTE = 0x00001401
GL_SAMPLE_BUFFERS = 0x000080a8
GL_SAMPLER_CUBE = 0x00008b60
GL_NICEST = 0x00001102
GL_BOOL = 0x00008b56
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x00008b8a
GL_EXTENSIONS = 0x00001f03
GL_BUFFER_SIZE = 0x00008764
GL_STENCIL_BACK_FUNC = 0x00008800
GL_ACTIVE_TEXTURE = 0x000084e0
GL_ALPHA = 0x00001906
GL_STATIC_DRAW = 0x000088e4
GL_RENDERBUFFER_BINDING = 0x00008ca7
GL_NEVER = 0x00000200
GL_ONE_MINUS_DST_ALPHA = 0x00000305
GL_COLOR_WRITEMASK = 0x00000c23
GL_DST_COLOR = 0x00000306
GL_MEDIUM_INT = 0x00008df4
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x00008802
GL_DEPTH_FUNC = 0x00000b74
GL_ALWAYS = 0x00000207
GL_TEXTURE_WRAP_S = 0x00002802
GL_TEXTURE_WRAP_T = 0x00002803
__gl2_h_ = 0x00000001
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x00008645
GL_INVALID_ENUM = 0x00000500
GL_FLOAT_MAT2 = 0x00008b5a
GL_INT_VEC4 = 0x00008b55
GL_INT_VEC3 = 0x00008b54
GL_ALIASED_POINT_SIZE_RANGE = 0x0000846d
GL_INT_VEC2 = 0x00008b53
GL_STENCIL_FAIL = 0x00000b94
GL_LUMINANCE = 0x00001909
GL_CCW = 0x00000901
GL_MAX_VERTEX_ATTRIBS = 0x00008869
GL_DEPTH_COMPONENT = 0x00001902
GL_SCISSOR_TEST = 0x00000c11
GL_DEPTH_TEST = 0x00000b71
GL_BOOL_VEC2 = 0x00008b57
GL_SHADER_TYPE = 0x00008b4f
GL_FRAMEBUFFER_UNSUPPORTED = 0x00008cdd
GL_DST_ALPHA = 0x00000304
GL_TRUE = 0x00000001
GL_TEXTURE_MIN_FILTER = 0x00002801
GL_BLEND_DST_RGB = 0x000080c8
GL_LINEAR = 0x00002601
GL_BLUE_BITS = 0x00000d54
GL_FUNC_SUBTRACT = 0x0000800a
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x00008cd3
GL_LESS = 0x00000201
GL_RENDERBUFFER_GREEN_SIZE = 0x00008d51
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x0000889f
GL_RGB = 0x00001907
GL_EQUAL = 0x00000202
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x00008b9b
GL_TEXTURE_BINDING_CUBE_MAP = 0x00008514
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x00008519
GL_RENDERBUFFER_WIDTH = 0x00008d42
GL_RED_BITS = 0x00000d52
GL_STENCIL_BACK_VALUE_MASK = 0x00008ca4
GL_TEXTURE23 = 0x000084d7
GL_HIGH_FLOAT = 0x00008df2
GL_DEPTH_RANGE = 0x00000b70
GL_GREATER = 0x00000204
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x00008b4d
GL_NEAREST = 0x00002600
GL_COMPRESSED_TEXTURE_FORMATS = 0x000086a3
GL_SAMPLE_COVERAGE = 0x000080a0
GL_MAX_TEXTURE_IMAGE_UNITS = 0x00008872
GL_MEDIUM_FLOAT = 0x00008df1
GL_TEXTURE_BINDING_2D = 0x00008069
GL_FLOAT_MAT3 = 0x00008b5b
GL_FRONT_FACE = 0x00000b46
GL_STENCIL_BACK_REF = 0x00008ca3
GL_REPLACE = 0x00001e01
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x00008624
GL_LOW_FLOAT = 0x00008df0
GL_UNPACK_ALIGNMENT = 0x00000cf5
GL_HIGH_INT = 0x00008df5
GL_SAMPLES = 0x000080a9

# GL Functions
try:
    def glActiveTexture(texture, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glActiveTexture
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture)
    # Check if the function actually exists
    f = c.glActiveTexture
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glAttachShader(program, shader, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint]
        cfunc = c.glAttachShader
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, shader)
    # Check if the function actually exists
    f = c.glAttachShader
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindAttribLocation(program, index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLchar]
        cfunc = c.glBindAttribLocation
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, index, param0)
    # Check if the function actually exists
    f = c.glBindAttribLocation
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindBuffer(target, buffer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glBindBuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, buffer)
    # Check if the function actually exists
    f = c.glBindBuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindFramebuffer(target, framebuffer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glBindFramebuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, framebuffer)
    # Check if the function actually exists
    f = c.glBindFramebuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindRenderbuffer(target, renderbuffer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glBindRenderbuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, renderbuffer)
    # Check if the function actually exists
    f = c.glBindRenderbuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindTexture(target, texture, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glBindTexture
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, texture)
    # Check if the function actually exists
    f = c.glBindTexture
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBlendColor(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glBlendColor
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glBlendColor
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBlendEquation(mode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glBlendEquation
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode)
    # Check if the function actually exists
    f = c.glBlendEquation
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBlendEquationSeparate(modeRGB, modeAlpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum]
        cfunc = c.glBlendEquationSeparate
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(modeRGB, modeAlpha)
    # Check if the function actually exists
    f = c.glBlendEquationSeparate
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBlendFunc(sfactor, dfactor, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum]
        cfunc = c.glBlendFunc
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sfactor, dfactor)
    # Check if the function actually exists
    f = c.glBlendFunc
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum, GLenum]
        cfunc = c.glBlendFuncSeparate
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)
    # Check if the function actually exists
    f = c.glBlendFuncSeparate
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBufferData(target, size, voiddata, usage, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizeiptr, ctypes.c_void_p, GLenum]
        cfunc = c.glBufferData
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, size, voiddata, usage)
    # Check if the function actually exists
    f = c.glBufferData
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBufferSubData(target, offset, size, voiddata, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLintptr, GLsizeiptr, ctypes.c_void_p]
        cfunc = c.glBufferSubData
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, offset, size, voiddata)
    # Check if the function actually exists
    f = c.glBufferSubData
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCheckFramebufferStatus(target, argtypes_p=None):
        restype = GLenum
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glCheckFramebufferStatus
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glCheckFramebufferStatus
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClear(mask, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLbitfield]
        cfunc = c.glClear
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mask)
    # Check if the function actually exists
    f = c.glClear
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearColor(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glClearColor
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glClearColor
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearDepthf(d, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat]
        cfunc = c.glClearDepthf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(d)
    # Check if the function actually exists
    f = c.glClearDepthf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearStencil(s, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint]
        cfunc = c.glClearStencil
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(s)
    # Check if the function actually exists
    f = c.glClearStencil
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glColorMask(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLboolean, GLboolean, GLboolean, GLboolean]
        cfunc = c.glColorMask
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glColorMask
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCompileShader(shader, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glCompileShader
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader)
    # Check if the function actually exists
    f = c.glCompileShader
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, voiddata, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p]
        cfunc = c.glCompressedTexImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, width, height, border, imageSize, voiddata)
    # Check if the function actually exists
    f = c.glCompressedTexImage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, voiddata, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p]
        cfunc = c.glCompressedTexSubImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, width, height, format, imageSize, voiddata)
    # Check if the function actually exists
    f = c.glCompressedTexSubImage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint]
        cfunc = c.glCopyTexImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, x, y, width, height, border)
    # Check if the function actually exists
    f = c.glCopyTexImage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei]
        cfunc = c.glCopyTexSubImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, x, y, width, height)
    # Check if the function actually exists
    f = c.glCopyTexSubImage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCreateProgram(void, argtypes_p=None):
        restype = GLuint
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glCreateProgram
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glCreateProgram
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCreateShader(type, argtypes_p=None):
        restype = GLuint
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glCreateShader
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(type)
    # Check if the function actually exists
    f = c.glCreateShader
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCullFace(mode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glCullFace
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode)
    # Check if the function actually exists
    f = c.glCullFace
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteBuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteBuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteBuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteFramebuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteFramebuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteFramebuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteProgram(program, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glDeleteProgram
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program)
    # Check if the function actually exists
    f = c.glDeleteProgram
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteRenderbuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteRenderbuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteRenderbuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteShader(shader, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glDeleteShader
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader)
    # Check if the function actually exists
    f = c.glDeleteShader
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteTextures(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteTextures
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteTextures
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDepthFunc(func, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glDepthFunc
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(func)
    # Check if the function actually exists
    f = c.glDepthFunc
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDepthMask(flag, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLboolean]
        cfunc = c.glDepthMask
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(flag)
    # Check if the function actually exists
    f = c.glDepthMask
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDepthRangef(n, f, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat]
        cfunc = c.glDepthRangef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, f)
    # Check if the function actually exists
    f = c.glDepthRangef
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDetachShader(program, shader, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint]
        cfunc = c.glDetachShader
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, shader)
    # Check if the function actually exists
    f = c.glDetachShader
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDisable(cap, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glDisable
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(cap)
    # Check if the function actually exists
    f = c.glDisable
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDisableVertexAttribArray(index, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glDisableVertexAttribArray
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index)
    # Check if the function actually exists
    f = c.glDisableVertexAttribArray
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDrawArrays(mode, first, count, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLsizei]
        cfunc = c.glDrawArrays
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode, first, count)
    # Check if the function actually exists
    f = c.glDrawArrays
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDrawElements(mode, count, type, voidindices, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, ctypes.c_void_p]
        cfunc = c.glDrawElements
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode, count, type, voidindices)
    # Check if the function actually exists
    f = c.glDrawElements
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glEnable(cap, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glEnable
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(cap)
    # Check if the function actually exists
    f = c.glEnable
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glEnableVertexAttribArray(index, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glEnableVertexAttribArray
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index)
    # Check if the function actually exists
    f = c.glEnableVertexAttribArray
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFinish(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glFinish
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glFinish
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFlush(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glFlush
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glFlush
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum, GLuint]
        cfunc = c.glFramebufferRenderbuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, renderbuffertarget, renderbuffer)
    # Check if the function actually exists
    f = c.glFramebufferRenderbuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFramebufferTexture2D(target, attachment, textarget, texture, level, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum, GLuint, GLint]
        cfunc = c.glFramebufferTexture2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, textarget, texture, level)
    # Check if the function actually exists
    f = c.glFramebufferTexture2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFrontFace(mode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glFrontFace
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode)
    # Check if the function actually exists
    f = c.glFrontFace
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenBuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenBuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenBuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenerateMipmap(target, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glGenerateMipmap
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glGenerateMipmap
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenFramebuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenFramebuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenFramebuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenRenderbuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenRenderbuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenRenderbuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenTextures(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenTextures
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenTextures
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetActiveAttrib(program, index, bufSize, param0, param1, param2, param3, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLsizei, GLsizei, GLint, GLenum, GLchar]
        cfunc = c.glGetActiveAttrib
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, index, bufSize, param0, param1, param2, param3)
    # Check if the function actually exists
    f = c.glGetActiveAttrib
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetActiveUniform(program, index, bufSize, param0, param1, param2, param3, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLsizei, GLsizei, GLint, GLenum, GLchar]
        cfunc = c.glGetActiveUniform
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, index, bufSize, param0, param1, param2, param3)
    # Check if the function actually exists
    f = c.glGetActiveUniform
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetAttachedShaders(program, maxCount, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLsizei, GLuint]
        cfunc = c.glGetAttachedShaders
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, maxCount, param0, param1)
    # Check if the function actually exists
    f = c.glGetAttachedShaders
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetAttribLocation(program, param0, argtypes_p=None):
        restype = GLint
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLchar]
        cfunc = c.glGetAttribLocation
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, param0)
    # Check if the function actually exists
    f = c.glGetAttribLocation
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetBooleanv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLboolean]
        cfunc = c.glGetBooleanv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetBooleanv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetBufferParameteriv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glGetBufferParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetBufferParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetError(void, argtypes_p=None):
        restype = GLenum
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glGetError
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glGetError
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetFloatv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glGetFloatv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetFloatv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetFramebufferAttachmentParameteriv(target, attachment, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum, GLint]
        cfunc = c.glGetFramebufferAttachmentParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, pname, param0)
    # Check if the function actually exists
    f = c.glGetFramebufferAttachmentParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetIntegerv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint]
        cfunc = c.glGetIntegerv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetIntegerv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetProgramiv(program, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glGetProgramiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, pname, param0)
    # Check if the function actually exists
    f = c.glGetProgramiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetProgramInfoLog(program, bufSize, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLsizei, GLchar]
        cfunc = c.glGetProgramInfoLog
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, bufSize, param0, param1)
    # Check if the function actually exists
    f = c.glGetProgramInfoLog
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetRenderbufferParameteriv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glGetRenderbufferParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetRenderbufferParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetShaderiv(shader, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glGetShaderiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader, pname, param0)
    # Check if the function actually exists
    f = c.glGetShaderiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetShaderInfoLog(shader, bufSize, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLsizei, GLchar]
        cfunc = c.glGetShaderInfoLog
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader, bufSize, param0, param1)
    # Check if the function actually exists
    f = c.glGetShaderInfoLog
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetShaderPrecisionFormat(shadertype, precisiontype, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint, GLint]
        cfunc = c.glGetShaderPrecisionFormat
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shadertype, precisiontype, param0, param1)
    # Check if the function actually exists
    f = c.glGetShaderPrecisionFormat
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetShaderSource(shader, bufSize, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLsizei, GLchar]
        cfunc = c.glGetShaderSource
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader, bufSize, param0, param1)
    # Check if the function actually exists
    f = c.glGetShaderSource
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetTexParameterfv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glGetTexParameterfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexParameterfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetTexParameteriv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glGetTexParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetUniformfv(program, location, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint, GLfloat]
        cfunc = c.glGetUniformfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, location, param0)
    # Check if the function actually exists
    f = c.glGetUniformfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetUniformiv(program, location, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint, GLint]
        cfunc = c.glGetUniformiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, location, param0)
    # Check if the function actually exists
    f = c.glGetUniformiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetUniformLocation(program, param0, argtypes_p=None):
        restype = GLint
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLchar]
        cfunc = c.glGetUniformLocation
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, param0)
    # Check if the function actually exists
    f = c.glGetUniformLocation
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribfv(index, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLfloat]
        cfunc = c.glGetVertexAttribfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, pname, param0)
    # Check if the function actually exists
    f = c.glGetVertexAttribfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribiv(index, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glGetVertexAttribiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, pname, param0)
    # Check if the function actually exists
    f = c.glGetVertexAttribiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribPointerv(index, pname, voidpointer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, ctypes.c_void_p]
        cfunc = c.glGetVertexAttribPointerv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, pname, voidpointer)
    # Check if the function actually exists
    f = c.glGetVertexAttribPointerv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glHint(target, mode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum]
        cfunc = c.glHint
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, mode)
    # Check if the function actually exists
    f = c.glHint
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsBuffer(buffer, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsBuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(buffer)
    # Check if the function actually exists
    f = c.glIsBuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsEnabled(cap, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glIsEnabled
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(cap)
    # Check if the function actually exists
    f = c.glIsEnabled
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsFramebuffer(framebuffer, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsFramebuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(framebuffer)
    # Check if the function actually exists
    f = c.glIsFramebuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsProgram(program, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsProgram
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program)
    # Check if the function actually exists
    f = c.glIsProgram
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsRenderbuffer(renderbuffer, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsRenderbuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(renderbuffer)
    # Check if the function actually exists
    f = c.glIsRenderbuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsShader(shader, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsShader
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader)
    # Check if the function actually exists
    f = c.glIsShader
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsTexture(texture, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsTexture
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture)
    # Check if the function actually exists
    f = c.glIsTexture
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLineWidth(width, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat]
        cfunc = c.glLineWidth
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(width)
    # Check if the function actually exists
    f = c.glLineWidth
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLinkProgram(program, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glLinkProgram
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program)
    # Check if the function actually exists
    f = c.glLinkProgram
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPixelStorei(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint]
        cfunc = c.glPixelStorei
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glPixelStorei
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPolygonOffset(factor, units, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat]
        cfunc = c.glPolygonOffset
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(factor, units)
    # Check if the function actually exists
    f = c.glPolygonOffset
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glReadPixels(x, y, width, height, format, type, voidpixels, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p]
        cfunc = c.glReadPixels
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, width, height, format, type, voidpixels)
    # Check if the function actually exists
    f = c.glReadPixels
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glReleaseShaderCompiler(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glReleaseShaderCompiler
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glReleaseShaderCompiler
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorage(target, internalformat, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLsizei, GLsizei]
        cfunc = c.glRenderbufferStorage
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, internalformat, width, height)
    # Check if the function actually exists
    f = c.glRenderbufferStorage
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glSampleCoverage(value, invert, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLboolean]
        cfunc = c.glSampleCoverage
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(value, invert)
    # Check if the function actually exists
    f = c.glSampleCoverage
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glScissor(x, y, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLsizei, GLsizei]
        cfunc = c.glScissor
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, width, height)
    # Check if the function actually exists
    f = c.glScissor
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glShaderBinary(count, param0, binaryformat, voidbinary, length, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint, GLenum, ctypes.c_void_p, GLsizei]
        cfunc = c.glShaderBinary
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(count, param0, binaryformat, voidbinary, length)
    # Check if the function actually exists
    f = c.glShaderBinary
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glShaderSource(shader, count, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLchar, GLint]
        cfunc = c.glShaderSource
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(shader, count, param0, param1)
    # Check if the function actually exists
    f = c.glShaderSource
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glStencilFunc(func, ref, mask, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLuint]
        cfunc = c.glStencilFunc
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(func, ref, mask)
    # Check if the function actually exists
    f = c.glStencilFunc
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glStencilFuncSeparate(face, func, ref, mask, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint, GLuint]
        cfunc = c.glStencilFuncSeparate
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, func, ref, mask)
    # Check if the function actually exists
    f = c.glStencilFuncSeparate
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glStencilMask(mask, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glStencilMask
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mask)
    # Check if the function actually exists
    f = c.glStencilMask
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glStencilMaskSeparate(face, mask, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glStencilMaskSeparate
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, mask)
    # Check if the function actually exists
    f = c.glStencilMaskSeparate
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glStencilOp(fail, zfail, zpass, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum]
        cfunc = c.glStencilOp
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(fail, zfail, zpass)
    # Check if the function actually exists
    f = c.glStencilOp
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glStencilOpSeparate(face, sfail, dpfail, dppass, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum, GLenum]
        cfunc = c.glStencilOpSeparate
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, sfail, dpfail, dppass)
    # Check if the function actually exists
    f = c.glStencilOpSeparate
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexImage2D(target, level, internalformat, width, height, border, format, type, voidpixels, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p]
        cfunc = c.glTexImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, width, height, border, format, type, voidpixels)
    # Check if the function actually exists
    f = c.glTexImage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexParameterf(target, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glTexParameterf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexParameterf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexParameterfv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glTexParameterfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexParameterfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexParameteri(target, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glTexParameteri
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexParameteri
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexParameteriv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glTexParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, voidpixels, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p]
        cfunc = c.glTexSubImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, width, height, format, type, voidpixels)
    # Check if the function actually exists
    f = c.glTexSubImage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform1f(location, v0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLfloat]
        cfunc = c.glUniform1f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0)
    # Check if the function actually exists
    f = c.glUniform1f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform1fv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLfloat]
        cfunc = c.glUniform1fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform1fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform1i(location, v0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint]
        cfunc = c.glUniform1i
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0)
    # Check if the function actually exists
    f = c.glUniform1i
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform1iv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLint]
        cfunc = c.glUniform1iv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform1iv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform2f(location, v0, v1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLfloat, GLfloat]
        cfunc = c.glUniform2f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1)
    # Check if the function actually exists
    f = c.glUniform2f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform2fv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLfloat]
        cfunc = c.glUniform2fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform2fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform2i(location, v0, v1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLint]
        cfunc = c.glUniform2i
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1)
    # Check if the function actually exists
    f = c.glUniform2i
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform2iv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLint]
        cfunc = c.glUniform2iv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform2iv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform3f(location, v0, v1, v2, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLfloat, GLfloat, GLfloat]
        cfunc = c.glUniform3f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1, v2)
    # Check if the function actually exists
    f = c.glUniform3f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform3fv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLfloat]
        cfunc = c.glUniform3fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform3fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform3i(location, v0, v1, v2, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLint, GLint]
        cfunc = c.glUniform3i
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1, v2)
    # Check if the function actually exists
    f = c.glUniform3i
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform3iv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLint]
        cfunc = c.glUniform3iv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform3iv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform4f(location, v0, v1, v2, v3, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glUniform4f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1, v2, v3)
    # Check if the function actually exists
    f = c.glUniform4f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform4fv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLfloat]
        cfunc = c.glUniform4fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform4fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform4i(location, v0, v1, v2, v3, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLint, GLint, GLint]
        cfunc = c.glUniform4i
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1, v2, v3)
    # Check if the function actually exists
    f = c.glUniform4i
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform4iv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLint]
        cfunc = c.glUniform4iv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform4iv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix2fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix2fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix2fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix3fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix3fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix3fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix4fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix4fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix4fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUseProgram(program, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glUseProgram
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program)
    # Check if the function actually exists
    f = c.glUseProgram
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glValidateProgram(program, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glValidateProgram
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program)
    # Check if the function actually exists
    f = c.glValidateProgram
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib1f(index, x, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat]
        cfunc = c.glVertexAttrib1f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, x)
    # Check if the function actually exists
    f = c.glVertexAttrib1f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib1fv(index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat]
        cfunc = c.glVertexAttrib1fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, param0)
    # Check if the function actually exists
    f = c.glVertexAttrib1fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib2f(index, x, y, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat, GLfloat]
        cfunc = c.glVertexAttrib2f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, x, y)
    # Check if the function actually exists
    f = c.glVertexAttrib2f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib2fv(index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat]
        cfunc = c.glVertexAttrib2fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, param0)
    # Check if the function actually exists
    f = c.glVertexAttrib2fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib3f(index, x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat, GLfloat, GLfloat]
        cfunc = c.glVertexAttrib3f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, x, y, z)
    # Check if the function actually exists
    f = c.glVertexAttrib3f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib3fv(index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat]
        cfunc = c.glVertexAttrib3fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, param0)
    # Check if the function actually exists
    f = c.glVertexAttrib3fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib4f(index, x, y, z, w, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glVertexAttrib4f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, x, y, z, w)
    # Check if the function actually exists
    f = c.glVertexAttrib4f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib4fv(index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLfloat]
        cfunc = c.glVertexAttrib4fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, param0)
    # Check if the function actually exists
    f = c.glVertexAttrib4fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribPointer(index, size, type, normalized, stride, voidpointer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint, GLenum, GLboolean, GLsizei, ctypes.c_void_p]
        cfunc = c.glVertexAttribPointer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, size, type, normalized, stride, voidpointer)
    # Check if the function actually exists
    f = c.glVertexAttribPointer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glViewport(x, y, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLsizei, GLsizei]
        cfunc = c.glViewport
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, width, height)
    # Check if the function actually exists
    f = c.glViewport
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

print 'Loaded %i functions and failed\n'\
      'to load %i functions of %i functions in\n'\
      'the header gl2.h' % (loaded[0], loaded[1], sum(loaded))
__all__ = [glActiveTexture, glAttachShader, glBindAttribLocation, glBindBuffer, glBindFramebuffer, glBindRenderbuffer, glBindTexture, glBlendColor, glBlendEquation, glBlendEquationSeparate, glBlendFunc, glBlendFuncSeparate, glBufferData, glBufferSubData, glCheckFramebufferStatus, glClear, glClearColor, glClearDepthf, glClearStencil, glColorMask, glCompileShader, glCompressedTexImage2D, glCompressedTexSubImage2D, glCopyTexImage2D, glCopyTexSubImage2D, glCreateProgram, glCreateShader, glCullFace, glDeleteBuffers, glDeleteFramebuffers, glDeleteProgram, glDeleteRenderbuffers, glDeleteShader, glDeleteTextures, glDepthFunc, glDepthMask, glDepthRangef, glDetachShader, glDisable, glDisableVertexAttribArray, glDrawArrays, glDrawElements, glEnable, glEnableVertexAttribArray, glFinish, glFlush, glFramebufferRenderbuffer, glFramebufferTexture2D, glFrontFace, glGenBuffers, glGenerateMipmap, glGenFramebuffers, glGenRenderbuffers, glGenTextures, glGetActiveAttrib, glGetActiveUniform, glGetAttachedShaders, glGetAttribLocation, glGetBooleanv, glGetBufferParameteriv, glGetError, glGetFloatv, glGetFramebufferAttachmentParameteriv, glGetIntegerv, glGetProgramiv, glGetProgramInfoLog, glGetRenderbufferParameteriv, glGetShaderiv, glGetShaderInfoLog, glGetShaderPrecisionFormat, glGetShaderSource, glGetTexParameterfv, glGetTexParameteriv, glGetUniformfv, glGetUniformiv, glGetUniformLocation, glGetVertexAttribfv, glGetVertexAttribiv, glGetVertexAttribPointerv, glHint, glIsBuffer, glIsEnabled, glIsFramebuffer, glIsProgram, glIsRenderbuffer, glIsShader, glIsTexture, glLineWidth, glLinkProgram, glPixelStorei, glPolygonOffset, glReadPixels, glReleaseShaderCompiler, glRenderbufferStorage, glSampleCoverage, glScissor, glShaderBinary, glShaderSource, glStencilFunc, glStencilFuncSeparate, glStencilMask, glStencilMaskSeparate, glStencilOp, glStencilOpSeparate, glTexImage2D, glTexParameterf, glTexParameterfv, glTexParameteri, glTexParameteriv, glTexSubImage2D, glUniform1f, glUniform1fv, glUniform1i, glUniform1iv, glUniform2f, glUniform2fv, glUniform2i, glUniform2iv, glUniform3f, glUniform3fv, glUniform3i, glUniform3iv, glUniform4f, glUniform4fv, glUniform4i, glUniform4iv, glUniformMatrix2fv, glUniformMatrix3fv, glUniformMatrix4fv, glUseProgram, glValidateProgram, glVertexAttrib1f, glVertexAttrib1fv, glVertexAttrib2f, glVertexAttrib2fv, glVertexAttrib3f, glVertexAttrib3fv, glVertexAttrib4f, glVertexAttrib4fv, glVertexAttribPointer, glViewport]