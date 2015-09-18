# Generated Files. DO NOT EDIT
# Generated on: 09/19/15 09:14:33
import ctypes
from objc_util import *
from GLConstants import *

DEBUG = 0
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
    def glActiveTexture(texture, texture_t=GLenum):
        restype = None
        argtypes = [texture_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glAttachShader(program, shader, program_t=GLuint, shader_t=GLuint):
        restype = None
        argtypes = [program_t, shader_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindAttribLocation(program, index, param0, program_t=GLuint, index_t=GLuint, param0_t=GLchar):
        restype = None
        argtypes = [program_t, index_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindBuffer(target, buffer, target_t=GLenum, buffer_t=GLuint):
        restype = None
        argtypes = [target_t, buffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindFramebuffer(target, framebuffer, target_t=GLenum, framebuffer_t=GLuint):
        restype = None
        argtypes = [target_t, framebuffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindRenderbuffer(target, renderbuffer, target_t=GLenum, renderbuffer_t=GLuint):
        restype = None
        argtypes = [target_t, renderbuffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindTexture(target, texture, target_t=GLenum, texture_t=GLuint):
        restype = None
        argtypes = [target_t, texture_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendColor(red, green, blue, alpha, red_t=GLfloat, green_t=GLfloat, blue_t=GLfloat, alpha_t=GLfloat):
        restype = None
        argtypes = [red_t, green_t, blue_t, alpha_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendEquation(mode, mode_t=GLenum):
        restype = None
        argtypes = [mode_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendEquationSeparate(modeRGB, modeAlpha, modeRGB_t=GLenum, modeAlpha_t=GLenum):
        restype = None
        argtypes = [modeRGB_t, modeAlpha_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendFunc(sfactor, dfactor, sfactor_t=GLenum, dfactor_t=GLenum):
        restype = None
        argtypes = [sfactor_t, dfactor_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha, sfactorRGB_t=GLenum, dfactorRGB_t=GLenum, sfactorAlpha_t=GLenum, dfactorAlpha_t=GLenum):
        restype = None
        argtypes = [sfactorRGB_t, dfactorRGB_t, sfactorAlpha_t, dfactorAlpha_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBufferData(target, size, voiddata, usage, target_t=GLenum, size_t=GLsizeiptr, voiddata_t=ctypes.c_void_p, usage_t=GLenum):
        restype = None
        argtypes = [target_t, size_t, voiddata_t, usage_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBufferSubData(target, offset, size, voiddata, target_t=GLenum, offset_t=GLintptr, size_t=GLsizeiptr, voiddata_t=ctypes.c_void_p):
        restype = None
        argtypes = [target_t, offset_t, size_t, voiddata_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCheckFramebufferStatus(target, target_t=GLenum):
        restype = GLenum
        argtypes = [target_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClear(mask, mask_t=GLbitfield):
        restype = None
        argtypes = [mask_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClearColor(red, green, blue, alpha, red_t=GLfloat, green_t=GLfloat, blue_t=GLfloat, alpha_t=GLfloat):
        restype = None
        argtypes = [red_t, green_t, blue_t, alpha_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClearDepthf(d, d_t=GLfloat):
        restype = None
        argtypes = [d_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClearStencil(s, s_t=GLint):
        restype = None
        argtypes = [s_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glColorMask(red, green, blue, alpha, red_t=GLboolean, green_t=GLboolean, blue_t=GLboolean, alpha_t=GLboolean):
        restype = None
        argtypes = [red_t, green_t, blue_t, alpha_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCompileShader(shader, shader_t=GLuint):
        restype = None
        argtypes = [shader_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, voiddata, target_t=GLenum, level_t=GLint, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei, border_t=GLint, imageSize_t=GLsizei, voiddata_t=ctypes.c_void_p):
        restype = None
        argtypes = [target_t, level_t, internalformat_t, width_t, height_t, border_t, imageSize_t, voiddata_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, voiddata, target_t=GLenum, level_t=GLint, xoffset_t=GLint, yoffset_t=GLint, width_t=GLsizei, height_t=GLsizei, format_t=GLenum, imageSize_t=GLsizei, voiddata_t=ctypes.c_void_p):
        restype = None
        argtypes = [target_t, level_t, xoffset_t, yoffset_t, width_t, height_t, format_t, imageSize_t, voiddata_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border, target_t=GLenum, level_t=GLint, internalformat_t=GLenum, x_t=GLint, y_t=GLint, width_t=GLsizei, height_t=GLsizei, border_t=GLint):
        restype = None
        argtypes = [target_t, level_t, internalformat_t, x_t, y_t, width_t, height_t, border_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height, target_t=GLenum, level_t=GLint, xoffset_t=GLint, yoffset_t=GLint, x_t=GLint, y_t=GLint, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [target_t, level_t, xoffset_t, yoffset_t, x_t, y_t, width_t, height_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCreateProgram(void, void_t=ctypes.c_void_p):
        restype = GLuint
        argtypes = [void_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCreateShader(type, type_t=GLenum):
        restype = GLuint
        argtypes = [type_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCullFace(mode, mode_t=GLenum):
        restype = None
        argtypes = [mode_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteBuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteFramebuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteProgram(program, program_t=GLuint):
        restype = None
        argtypes = [program_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteRenderbuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteShader(shader, shader_t=GLuint):
        restype = None
        argtypes = [shader_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteTextures(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDepthFunc(func, func_t=GLenum):
        restype = None
        argtypes = [func_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDepthMask(flag, flag_t=GLboolean):
        restype = None
        argtypes = [flag_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDepthRangef(n, f, n_t=GLfloat, f_t=GLfloat):
        restype = None
        argtypes = [n_t, f_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDetachShader(program, shader, program_t=GLuint, shader_t=GLuint):
        restype = None
        argtypes = [program_t, shader_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDisable(cap, cap_t=GLenum):
        restype = None
        argtypes = [cap_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDisableVertexAttribArray(index, index_t=GLuint):
        restype = None
        argtypes = [index_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawArrays(mode, first, count, mode_t=GLenum, first_t=GLint, count_t=GLsizei):
        restype = None
        argtypes = [mode_t, first_t, count_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawElements(mode, count, type, voidindices, mode_t=GLenum, count_t=GLsizei, type_t=GLenum, voidindices_t=ctypes.c_void_p):
        restype = None
        argtypes = [mode_t, count_t, type_t, voidindices_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glEnable(cap, cap_t=GLenum):
        restype = None
        argtypes = [cap_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glEnableVertexAttribArray(index, index_t=GLuint):
        restype = None
        argtypes = [index_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFinish(void, void_t=ctypes.c_void_p):
        restype = None
        argtypes = [void_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFlush(void, void_t=ctypes.c_void_p):
        restype = None
        argtypes = [void_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer, target_t=GLenum, attachment_t=GLenum, renderbuffertarget_t=GLenum, renderbuffer_t=GLuint):
        restype = None
        argtypes = [target_t, attachment_t, renderbuffertarget_t, renderbuffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFramebufferTexture2D(target, attachment, textarget, texture, level, target_t=GLenum, attachment_t=GLenum, textarget_t=GLenum, texture_t=GLuint, level_t=GLint):
        restype = None
        argtypes = [target_t, attachment_t, textarget_t, texture_t, level_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFrontFace(mode, mode_t=GLenum):
        restype = None
        argtypes = [mode_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenBuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenerateMipmap(target, target_t=GLenum):
        restype = None
        argtypes = [target_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenFramebuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenRenderbuffers(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenTextures(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetActiveAttrib(program, index, bufSize, param0, param1, param2, param3, program_t=GLuint, index_t=GLuint, bufSize_t=GLsizei, param0_t=GLsizei, param1_t=GLint, param2_t=GLenum, param3_t=GLchar):
        restype = None
        argtypes = [program_t, index_t, bufSize_t, param0_t, param1_t, param2_t, param3_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetActiveUniform(program, index, bufSize, param0, param1, param2, param3, program_t=GLuint, index_t=GLuint, bufSize_t=GLsizei, param0_t=GLsizei, param1_t=GLint, param2_t=GLenum, param3_t=GLchar):
        restype = None
        argtypes = [program_t, index_t, bufSize_t, param0_t, param1_t, param2_t, param3_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetAttachedShaders(program, maxCount, param0, param1, program_t=GLuint, maxCount_t=GLsizei, param0_t=GLsizei, param1_t=GLuint):
        restype = None
        argtypes = [program_t, maxCount_t, param0_t, param1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetAttribLocation(program, param0, program_t=GLuint, param0_t=GLchar):
        restype = GLint
        argtypes = [program_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetBooleanv(pname, param0, pname_t=GLenum, param0_t=GLboolean):
        restype = None
        argtypes = [pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetBufferParameteriv(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetError(void, void_t=ctypes.c_void_p):
        restype = GLenum
        argtypes = [void_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetFloatv(pname, param0, pname_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetFramebufferAttachmentParameteriv(target, attachment, pname, param0, target_t=GLenum, attachment_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [target_t, attachment_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetIntegerv(pname, param0, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetProgramiv(program, pname, param0, program_t=GLuint, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [program_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetProgramInfoLog(program, bufSize, param0, param1, program_t=GLuint, bufSize_t=GLsizei, param0_t=GLsizei, param1_t=GLchar):
        restype = None
        argtypes = [program_t, bufSize_t, param0_t, param1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetRenderbufferParameteriv(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetShaderiv(shader, pname, param0, shader_t=GLuint, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [shader_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetShaderInfoLog(shader, bufSize, param0, param1, shader_t=GLuint, bufSize_t=GLsizei, param0_t=GLsizei, param1_t=GLchar):
        restype = None
        argtypes = [shader_t, bufSize_t, param0_t, param1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetShaderPrecisionFormat(shadertype, precisiontype, param0, param1, shadertype_t=GLenum, precisiontype_t=GLenum, param0_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [shadertype_t, precisiontype_t, param0_t, param1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetShaderSource(shader, bufSize, param0, param1, shader_t=GLuint, bufSize_t=GLsizei, param0_t=GLsizei, param1_t=GLchar):
        restype = None
        argtypes = [shader_t, bufSize_t, param0_t, param1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexParameterfv(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexParameteriv(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetUniformfv(program, location, param0, program_t=GLuint, location_t=GLint, param0_t=GLfloat):
        restype = None
        argtypes = [program_t, location_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetUniformiv(program, location, param0, program_t=GLuint, location_t=GLint, param0_t=GLint):
        restype = None
        argtypes = [program_t, location_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetUniformLocation(program, param0, program_t=GLuint, param0_t=GLchar):
        restype = GLint
        argtypes = [program_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribfv(index, pname, param0, index_t=GLuint, pname_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [index_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribiv(index, pname, param0, index_t=GLuint, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [index_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribPointerv(index, pname, voidpointer, index_t=GLuint, pname_t=GLenum, voidpointer_t=ctypes.c_void_p):
        restype = None
        argtypes = [index_t, pname_t, voidpointer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glHint(target, mode, target_t=GLenum, mode_t=GLenum):
        restype = None
        argtypes = [target_t, mode_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsBuffer(buffer, buffer_t=GLuint):
        restype = GLboolean
        argtypes = [buffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsEnabled(cap, cap_t=GLenum):
        restype = GLboolean
        argtypes = [cap_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsFramebuffer(framebuffer, framebuffer_t=GLuint):
        restype = GLboolean
        argtypes = [framebuffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsProgram(program, program_t=GLuint):
        restype = GLboolean
        argtypes = [program_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsRenderbuffer(renderbuffer, renderbuffer_t=GLuint):
        restype = GLboolean
        argtypes = [renderbuffer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsShader(shader, shader_t=GLuint):
        restype = GLboolean
        argtypes = [shader_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsTexture(texture, texture_t=GLuint):
        restype = GLboolean
        argtypes = [texture_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLineWidth(width, width_t=GLfloat):
        restype = None
        argtypes = [width_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLinkProgram(program, program_t=GLuint):
        restype = None
        argtypes = [program_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glPixelStorei(pname, param, pname_t=GLenum, param_t=GLint):
        restype = None
        argtypes = [pname_t, param_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glPolygonOffset(factor, units, factor_t=GLfloat, units_t=GLfloat):
        restype = None
        argtypes = [factor_t, units_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glReadPixels(x, y, width, height, format, type, voidpixels, x_t=GLint, y_t=GLint, width_t=GLsizei, height_t=GLsizei, format_t=GLenum, type_t=GLenum, voidpixels_t=ctypes.c_void_p):
        restype = None
        argtypes = [x_t, y_t, width_t, height_t, format_t, type_t, voidpixels_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glReleaseShaderCompiler(void, void_t=ctypes.c_void_p):
        restype = None
        argtypes = [void_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorage(target, internalformat, width, height, target_t=GLenum, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [target_t, internalformat_t, width_t, height_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glSampleCoverage(value, invert, value_t=GLfloat, invert_t=GLboolean):
        restype = None
        argtypes = [value_t, invert_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glScissor(x, y, width, height, x_t=GLint, y_t=GLint, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [x_t, y_t, width_t, height_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glShaderBinary(count, param0, binaryformat, voidbinary, length, count_t=GLsizei, param0_t=GLuint, binaryformat_t=GLenum, voidbinary_t=ctypes.c_void_p, length_t=GLsizei):
        restype = None
        argtypes = [count_t, param0_t, binaryformat_t, voidbinary_t, length_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glShaderSource(shader, count, param0, param1, shader_t=GLuint, count_t=GLsizei, param0_t=GLchar, param1_t=GLint):
        restype = None
        argtypes = [shader_t, count_t, param0_t, param1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStencilFunc(func, ref, mask, func_t=GLenum, ref_t=GLint, mask_t=GLuint):
        restype = None
        argtypes = [func_t, ref_t, mask_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStencilFuncSeparate(face, func, ref, mask, face_t=GLenum, func_t=GLenum, ref_t=GLint, mask_t=GLuint):
        restype = None
        argtypes = [face_t, func_t, ref_t, mask_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStencilMask(mask, mask_t=GLuint):
        restype = None
        argtypes = [mask_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStencilMaskSeparate(face, mask, face_t=GLenum, mask_t=GLuint):
        restype = None
        argtypes = [face_t, mask_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStencilOp(fail, zfail, zpass, fail_t=GLenum, zfail_t=GLenum, zpass_t=GLenum):
        restype = None
        argtypes = [fail_t, zfail_t, zpass_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStencilOpSeparate(face, sfail, dpfail, dppass, face_t=GLenum, sfail_t=GLenum, dpfail_t=GLenum, dppass_t=GLenum):
        restype = None
        argtypes = [face_t, sfail_t, dpfail_t, dppass_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexImage2D(target, level, internalformat, width, height, border, format, type, voidpixels, target_t=GLenum, level_t=GLint, internalformat_t=GLint, width_t=GLsizei, height_t=GLsizei, border_t=GLint, format_t=GLenum, type_t=GLenum, voidpixels_t=ctypes.c_void_p):
        restype = None
        argtypes = [target_t, level_t, internalformat_t, width_t, height_t, border_t, format_t, type_t, voidpixels_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexParameterf(target, pname, param, target_t=GLenum, pname_t=GLenum, param_t=GLfloat):
        restype = None
        argtypes = [target_t, pname_t, param_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexParameterfv(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexParameteri(target, pname, param, target_t=GLenum, pname_t=GLenum, param_t=GLint):
        restype = None
        argtypes = [target_t, pname_t, param_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexParameteriv(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, voidpixels, target_t=GLenum, level_t=GLint, xoffset_t=GLint, yoffset_t=GLint, width_t=GLsizei, height_t=GLsizei, format_t=GLenum, type_t=GLenum, voidpixels_t=ctypes.c_void_p):
        restype = None
        argtypes = [target_t, level_t, xoffset_t, yoffset_t, width_t, height_t, format_t, type_t, voidpixels_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform1f(location, v0, location_t=GLint, v0_t=GLfloat):
        restype = None
        argtypes = [location_t, v0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform1fv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform1i(location, v0, location_t=GLint, v0_t=GLint):
        restype = None
        argtypes = [location_t, v0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform1iv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLint):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform2f(location, v0, v1, location_t=GLint, v0_t=GLfloat, v1_t=GLfloat):
        restype = None
        argtypes = [location_t, v0_t, v1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform2fv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform2i(location, v0, v1, location_t=GLint, v0_t=GLint, v1_t=GLint):
        restype = None
        argtypes = [location_t, v0_t, v1_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform2iv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLint):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform3f(location, v0, v1, v2, location_t=GLint, v0_t=GLfloat, v1_t=GLfloat, v2_t=GLfloat):
        restype = None
        argtypes = [location_t, v0_t, v1_t, v2_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform3fv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform3i(location, v0, v1, v2, location_t=GLint, v0_t=GLint, v1_t=GLint, v2_t=GLint):
        restype = None
        argtypes = [location_t, v0_t, v1_t, v2_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform3iv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLint):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform4f(location, v0, v1, v2, v3, location_t=GLint, v0_t=GLfloat, v1_t=GLfloat, v2_t=GLfloat, v3_t=GLfloat):
        restype = None
        argtypes = [location_t, v0_t, v1_t, v2_t, v3_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform4fv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform4i(location, v0, v1, v2, v3, location_t=GLint, v0_t=GLint, v1_t=GLint, v2_t=GLint, v3_t=GLint):
        restype = None
        argtypes = [location_t, v0_t, v1_t, v2_t, v3_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniform4iv(location, count, param0, location_t=GLint, count_t=GLsizei, param0_t=GLint):
        restype = None
        argtypes = [location_t, count_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix2fv(location, count, transpose, param0, location_t=GLint, count_t=GLsizei, transpose_t=GLboolean, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, transpose_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix3fv(location, count, transpose, param0, location_t=GLint, count_t=GLsizei, transpose_t=GLboolean, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, transpose_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix4fv(location, count, transpose, param0, location_t=GLint, count_t=GLsizei, transpose_t=GLboolean, param0_t=GLfloat):
        restype = None
        argtypes = [location_t, count_t, transpose_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUseProgram(program, program_t=GLuint):
        restype = None
        argtypes = [program_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glValidateProgram(program, program_t=GLuint):
        restype = None
        argtypes = [program_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib1f(index, x, index_t=GLuint, x_t=GLfloat):
        restype = None
        argtypes = [index_t, x_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib1fv(index, param0, index_t=GLuint, param0_t=GLfloat):
        restype = None
        argtypes = [index_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib2f(index, x, y, index_t=GLuint, x_t=GLfloat, y_t=GLfloat):
        restype = None
        argtypes = [index_t, x_t, y_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib2fv(index, param0, index_t=GLuint, param0_t=GLfloat):
        restype = None
        argtypes = [index_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib3f(index, x, y, z, index_t=GLuint, x_t=GLfloat, y_t=GLfloat, z_t=GLfloat):
        restype = None
        argtypes = [index_t, x_t, y_t, z_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib3fv(index, param0, index_t=GLuint, param0_t=GLfloat):
        restype = None
        argtypes = [index_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib4f(index, x, y, z, w, index_t=GLuint, x_t=GLfloat, y_t=GLfloat, z_t=GLfloat, w_t=GLfloat):
        restype = None
        argtypes = [index_t, x_t, y_t, z_t, w_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttrib4fv(index, param0, index_t=GLuint, param0_t=GLfloat):
        restype = None
        argtypes = [index_t, param0_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glVertexAttribPointer(index, size, type, normalized, stride, voidpointer, index_t=GLuint, size_t=GLint, type_t=GLenum, normalized_t=GLboolean, stride_t=GLsizei, voidpointer_t=ctypes.c_void_p):
        restype = None
        argtypes = [index_t, size_t, type_t, normalized_t, stride_t, voidpointer_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glViewport(x, y, width, height, x_t=GLint, y_t=GLint, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [x_t, y_t, width_t, height_t]
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
    if DEBUG > 0:
        print 'could not load the function'
        print e

print 'Loaded %i functions and failed to load %i functions of %i functions in the header gl2.h' % (loaded[0], loaded[1], sum(loaded))
__all__ = ['glActiveTexture', 'glAttachShader', 'glBindAttribLocation', 'glBindBuffer', 'glBindFramebuffer', 'glBindRenderbuffer', 'glBindTexture', 'glBlendColor', 'glBlendEquation', 'glBlendEquationSeparate', 'glBlendFunc', 'glBlendFuncSeparate', 'glBufferData', 'glBufferSubData', 'glCheckFramebufferStatus', 'glClear', 'glClearColor', 'glClearDepthf', 'glClearStencil', 'glColorMask', 'glCompileShader', 'glCompressedTexImage2D', 'glCompressedTexSubImage2D', 'glCopyTexImage2D', 'glCopyTexSubImage2D', 'glCreateProgram', 'glCreateShader', 'glCullFace', 'glDeleteBuffers', 'glDeleteFramebuffers', 'glDeleteProgram', 'glDeleteRenderbuffers', 'glDeleteShader', 'glDeleteTextures', 'glDepthFunc', 'glDepthMask', 'glDepthRangef', 'glDetachShader', 'glDisable', 'glDisableVertexAttribArray', 'glDrawArrays', 'glDrawElements', 'glEnable', 'glEnableVertexAttribArray', 'glFinish', 'glFlush', 'glFramebufferRenderbuffer', 'glFramebufferTexture2D', 'glFrontFace', 'glGenBuffers', 'glGenerateMipmap', 'glGenFramebuffers', 'glGenRenderbuffers', 'glGenTextures', 'glGetActiveAttrib', 'glGetActiveUniform', 'glGetAttachedShaders', 'glGetAttribLocation', 'glGetBooleanv', 'glGetBufferParameteriv', 'glGetError', 'glGetFloatv', 'glGetFramebufferAttachmentParameteriv', 'glGetIntegerv', 'glGetProgramiv', 'glGetProgramInfoLog', 'glGetRenderbufferParameteriv', 'glGetShaderiv', 'glGetShaderInfoLog', 'glGetShaderPrecisionFormat', 'glGetShaderSource', 'glGetTexParameterfv', 'glGetTexParameteriv', 'glGetUniformfv', 'glGetUniformiv', 'glGetUniformLocation', 'glGetVertexAttribfv', 'glGetVertexAttribiv', 'glGetVertexAttribPointerv', 'glHint', 'glIsBuffer', 'glIsEnabled', 'glIsFramebuffer', 'glIsProgram', 'glIsRenderbuffer', 'glIsShader', 'glIsTexture', 'glLineWidth', 'glLinkProgram', 'glPixelStorei', 'glPolygonOffset', 'glReadPixels', 'glReleaseShaderCompiler', 'glRenderbufferStorage', 'glSampleCoverage', 'glScissor', 'glShaderBinary', 'glShaderSource', 'glStencilFunc', 'glStencilFuncSeparate', 'glStencilMask', 'glStencilMaskSeparate', 'glStencilOp', 'glStencilOpSeparate', 'glTexImage2D', 'glTexParameterf', 'glTexParameterfv', 'glTexParameteri', 'glTexParameteriv', 'glTexSubImage2D', 'glUniform1f', 'glUniform1fv', 'glUniform1i', 'glUniform1iv', 'glUniform2f', 'glUniform2fv', 'glUniform2i', 'glUniform2iv', 'glUniform3f', 'glUniform3fv', 'glUniform3i', 'glUniform3iv', 'glUniform4f', 'glUniform4fv', 'glUniform4i', 'glUniform4iv', 'glUniformMatrix2fv', 'glUniformMatrix3fv', 'glUniformMatrix4fv', 'glUseProgram', 'glValidateProgram', 'glVertexAttrib1f', 'glVertexAttrib1fv', 'glVertexAttrib2f', 'glVertexAttrib2fv', 'glVertexAttrib3f', 'glVertexAttrib3fv', 'glVertexAttrib4f', 'glVertexAttrib4fv', 'glVertexAttribPointer', 'glViewport', 'GL_INFO_LOG_LENGTH', 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT', 'GL_DEPTH_BITS', 'GL_LINE_STRIP', 'GL_TEXTURE24', 'GL_FRAMEBUFFER_COMPLETE', 'GL_UNSIGNED_SHORT_5_6_5', 'GL_RGB5_A1', 'GL_TEXTURE30', 'GL_TEXTURE31', 'GL_VERTEX_ATTRIB_ARRAY_SIZE', 'GL_TEXTURE_CUBE_MAP', 'GL_SRC_ALPHA_SATURATE', 'GL_VERTEX_SHADER', 'GL_TEXTURE5', 'GL_CONSTANT_ALPHA', 'GL_DEPTH_CLEAR_VALUE', 'GL_DITHER', 'GL_VERTEX_ATTRIB_ARRAY_ENABLED', 'GL_TEXTURE20', 'GL_FLOAT_VEC2', 'GL_FLOAT_VEC3', 'GL_RENDERBUFFER_INTERNAL_FORMAT', 'GL_TEXTURE18', 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE', 'GL_STENCIL_REF', 'GL_VALIDATE_STATUS', 'GL_FLOAT', 'GL_ACTIVE_ATTRIBUTES', 'GL_COMPILE_STATUS', 'GL_POINTS', 'GL_TEXTURE17', 'GL_BLEND', 'GL_MIRRORED_REPEAT', 'GL_STENCIL_BUFFER_BIT', 'GL_RENDERBUFFER_BLUE_SIZE', 'GL_UNSIGNED_SHORT', 'GL_FASTEST', 'GL_REPEAT', 'GL_MAX_RENDERBUFFER_SIZE', 'GL_DEPTH_COMPONENT16', 'GL_POLYGON_OFFSET_UNITS', 'GL_SHADER_SOURCE_LENGTH', 'GL_ONE_MINUS_DST_COLOR', 'GL_ONE_MINUS_SRC_COLOR', 'GL_TEXTURE22', 'GL_TEXTURE21', 'GL_TEXTURE7', 'GL_TEXTURE27', 'GL_TEXTURE26', 'GL_TEXTURE25', 'GL_TEXTURE', 'GL_BLEND_EQUATION_ALPHA', 'GL_TEXTURE8', 'GL_TEXTURE29', 'GL_TEXTURE28', 'GL_ELEMENT_ARRAY_BUFFER_BINDING', 'GL_TEXTURE9', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z', 'GL_STENCIL_PASS_DEPTH_PASS', 'GL_INCR_WRAP', 'GL_LINE_LOOP', 'GL_TEXTURE4', 'GL_COLOR_BUFFER_BIT', 'GL_TEXTURE6', 'GL_DONT_CARE', 'GL_ACTIVE_UNIFORMS', 'GL_LINEAR_MIPMAP_LINEAR', 'GL_TEXTURE2', 'GL_TEXTURE3', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y', 'GL_DECR_WRAP', 'GL_UNSIGNED_INT', 'GL_BLEND_EQUATION', 'GL_BYTE', 'GL_MAX_VERTEX_UNIFORM_VECTORS', 'GL_RGBA', 'GL_ATTACHED_SHADERS', 'GL_INVALID_VALUE', 'GL_RENDERBUFFER_STENCIL_SIZE', 'GL_GEQUAL', 'GL_SAMPLE_COVERAGE_INVERT', 'GL_NUM_COMPRESSED_TEXTURE_FORMATS', 'GL_LINES', 'GL_ONE', 'GL_TEXTURE19', 'GL_TEXTURE16', 'GL_TEXTURE0', 'GL_LINE_WIDTH', 'GL_GENERATE_MIPMAP_HINT', 'GL_TEXTURE12', 'GL_COLOR_CLEAR_VALUE', 'GL_TEXTURE10', 'GL_TEXTURE1', 'GL_BUFFER_USAGE', 'GL_BLEND_EQUATION_RGB', 'GL_TEXTURE13', 'GL_LINK_STATUS', 'GL_TRIANGLE_STRIP', 'GL_VERSION', 'GL_BLEND_DST_ALPHA', 'GL_BLEND_COLOR', 'GL_FUNC_ADD', 'GL_ALPHA_BITS', 'GL_TEXTURE_CUBE_MAP_POSITIVE_X', 'GL_FLOAT_VEC4', 'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED', 'GL_RENDERER', 'GL_ONE_MINUS_CONSTANT_ALPHA', 'GL_NEAREST_MIPMAP_LINEAR', 'GL_DEPTH_ATTACHMENT', 'GL_CURRENT_VERTEX_ATTRIB', 'GL_ARRAY_BUFFER_BINDING', 'GL_TEXTURE_2D', 'GL_SHADER_BINARY_FORMATS', 'GL_CONSTANT_COLOR', 'GL_DYNAMIC_DRAW', 'GL_OUT_OF_MEMORY', 'GL_TEXTURE15', 'GL_BOOL_VEC3', 'GL_STENCIL_FUNC', 'GL_VENDOR', 'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS', 'GL_VERTEX_ATTRIB_ARRAY_TYPE', 'GL_IMPLEMENTATION_COLOR_READ_TYPE', 'GL_SAMPLER_2D', 'GL_TEXTURE14', 'GL_ALIASED_LINE_WIDTH_RANGE', 'GL_MAX_TEXTURE_SIZE', 'GL_STENCIL_INDEX8', 'GL_STENCIL_WRITEMASK', 'GL_DECR', 'GL_BACK', 'GL_STENCIL_ATTACHMENT', 'GL_INT', 'GL_ES_VERSION_2_0', 'GL_ARRAY_BUFFER', 'GL_NUM_SHADER_BINARY_FORMATS', 'GL_UNSIGNED_SHORT_5_5_5_1', 'GL_BOOL_VEC4', 'GL_FLOAT_MAT4', 'GL_POLYGON_OFFSET_FILL', 'GL_STREAM_DRAW', 'GL_ZERO', 'GL_FRAMEBUFFER_BINDING', 'GL_ELEMENT_ARRAY_BUFFER', 'GL_MAX_CUBE_MAP_TEXTURE_SIZE', 'GL_FRONT_AND_BACK', 'GL_CURRENT_PROGRAM', 'GL_FRAMEBUFFER', 'GL_FALSE', 'GL_LINEAR_MIPMAP_NEAREST', 'GL_STENCIL_TEST', 'GL_ONE_MINUS_SRC_ALPHA', 'GL_UNSIGNED_SHORT_4_4_4_4', 'GL_SRC_ALPHA', 'GL_STENCIL_CLEAR_VALUE', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL', 'GL_GREEN_BITS', 'GL_ONE_MINUS_CONSTANT_COLOR', 'GL_LUMINANCE_ALPHA', 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT', 'GL_NEAREST_MIPMAP_NEAREST', 'GL_SHADING_LANGUAGE_VERSION', 'GL_NOTEQUAL', 'GL_INVERT', 'GL_MAX_VARYING_VECTORS', 'GL_STENCIL_BACK_FAIL', 'GL_POLYGON_OFFSET_FACTOR', 'GL_INCR', 'GL_CULL_FACE', 'GL_SAMPLE_ALPHA_TO_COVERAGE', 'GL_STENCIL_BITS', 'GL_SAMPLE_COVERAGE_VALUE', 'GL_FRAGMENT_SHADER', 'GL_LEQUAL', 'GL_TRIANGLE_FAN', 'GL_RENDERBUFFER_RED_SIZE', 'GL_STENCIL_PASS_DEPTH_FAIL', 'GL_MAX_VIEWPORT_DIMS', 'GL_RENDERBUFFER_HEIGHT', 'GL_BLEND_SRC_RGB', 'GL_ACTIVE_UNIFORM_MAX_LENGTH', 'GL_NO_ERROR', 'GL_STENCIL_BACK_WRITEMASK', 'GL_FUNC_REVERSE_SUBTRACT', 'GL_VIEWPORT', 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME', 'GL_BLEND_SRC_ALPHA', 'GL_INVALID_FRAMEBUFFER_OPERATION', 'GL_RENDERBUFFER_ALPHA_SIZE', 'GL_TRIANGLES', 'GL_TEXTURE_MAG_FILTER', 'GL_STENCIL_VALUE_MASK', 'GL_INVALID_OPERATION', 'GL_RENDERBUFFER', 'GL_LOW_INT', 'GL_NONE', 'GL_STENCIL_BACK_PASS_DEPTH_PASS', 'GL_KEEP', 'GL_RGB565', 'GL_DELETE_STATUS', 'GL_RENDERBUFFER_DEPTH_SIZE', 'GL_TEXTURE11', 'GL_COLOR_ATTACHMENT0', 'GL_SHADER_COMPILER', 'GL_CLAMP_TO_EDGE', 'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS', 'GL_FRONT', 'GL_SCISSOR_BOX', 'GL_FIXED', 'GL_RGBA4', 'GL_SRC_COLOR', 'GL_DEPTH_WRITEMASK', 'GL_PACK_ALIGNMENT', 'GL_SUBPIXEL_BITS', 'GL_SHORT', 'GL_CULL_FACE_MODE', 'GL_MAX_FRAGMENT_UNIFORM_VECTORS', 'GL_CW', 'GL_UNSIGNED_BYTE', 'GL_SAMPLE_BUFFERS', 'GL_SAMPLER_CUBE', 'GL_NICEST', 'GL_BOOL', 'GL_ACTIVE_ATTRIBUTE_MAX_LENGTH', 'GL_EXTENSIONS', 'GL_BUFFER_SIZE', 'GL_STENCIL_BACK_FUNC', 'GL_ACTIVE_TEXTURE', 'GL_ALPHA', 'GL_STATIC_DRAW', 'GL_RENDERBUFFER_BINDING', 'GL_NEVER', 'GL_ONE_MINUS_DST_ALPHA', 'GL_COLOR_WRITEMASK', 'GL_DST_COLOR', 'GL_MEDIUM_INT', 'GL_DEPTH_BUFFER_BIT', 'GL_STENCIL_BACK_PASS_DEPTH_FAIL', 'GL_DEPTH_FUNC', 'GL_ALWAYS', 'GL_TEXTURE_WRAP_S', 'GL_TEXTURE_WRAP_T', '__gl2_h_', 'GL_VERTEX_ATTRIB_ARRAY_POINTER', 'GL_INVALID_ENUM', 'GL_FLOAT_MAT2', 'GL_INT_VEC4', 'GL_INT_VEC3', 'GL_ALIASED_POINT_SIZE_RANGE', 'GL_INT_VEC2', 'GL_STENCIL_FAIL', 'GL_LUMINANCE', 'GL_CCW', 'GL_MAX_VERTEX_ATTRIBS', 'GL_DEPTH_COMPONENT', 'GL_SCISSOR_TEST', 'GL_DEPTH_TEST', 'GL_BOOL_VEC2', 'GL_SHADER_TYPE', 'GL_FRAMEBUFFER_UNSUPPORTED', 'GL_DST_ALPHA', 'GL_TRUE', 'GL_TEXTURE_MIN_FILTER', 'GL_BLEND_DST_RGB', 'GL_LINEAR', 'GL_BLUE_BITS', 'GL_FUNC_SUBTRACT', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE', 'GL_LESS', 'GL_RENDERBUFFER_GREEN_SIZE', 'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING', 'GL_RGB', 'GL_EQUAL', 'GL_IMPLEMENTATION_COLOR_READ_FORMAT', 'GL_TEXTURE_BINDING_CUBE_MAP', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z', 'GL_RENDERBUFFER_WIDTH', 'GL_RED_BITS', 'GL_STENCIL_BACK_VALUE_MASK', 'GL_TEXTURE23', 'GL_HIGH_FLOAT', 'GL_DEPTH_RANGE', 'GL_GREATER', 'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS', 'GL_NEAREST', 'GL_COMPRESSED_TEXTURE_FORMATS', 'GL_SAMPLE_COVERAGE', 'GL_MAX_TEXTURE_IMAGE_UNITS', 'GL_MEDIUM_FLOAT', 'GL_TEXTURE_BINDING_2D', 'GL_FLOAT_MAT3', 'GL_FRONT_FACE', 'GL_STENCIL_BACK_REF', 'GL_REPLACE', 'GL_VERTEX_ATTRIB_ARRAY_STRIDE', 'GL_LOW_FLOAT', 'GL_UNPACK_ALIGNMENT', 'GL_HIGH_INT', 'GL_SAMPLES', 'GLchar', 'GLenum', 'GLboolean', 'GLbitfield', 'GLbyte', 'GLshort', 'GLint', 'GLint64', 'GLsizei', 'GLubyte', 'GLushort', 'GLuint', 'GLfloat', 'GLclampf', 'GLfixed', 'GLintptr', 'GLsizeiptr', 'GLclampx', 'void', 'GLvoid', 'GLsync', 'GLeglImageOES', 'GLDEBUGPROCKHR', 'GLuint64']