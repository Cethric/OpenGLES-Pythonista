# Generated Files. DO NOT EDIT
# Generated on: 09/16/15 08:53:58
import ctypes
from objc_util import *
from GLConstants import *

DEBUG = 1
loaded = [0, 0]

# GLES Constants
GL_UNSIGNED_SHORT_5_6_5 = 0x00008363
GL_DITHER = 0x00000bd0
GL_ALPHA_TEST_FUNC = 0x00000bc1
GL_BUFFER_SIZE = 0x00008764
GL_MAX_TEXTURE_STACK_DEPTH = 0x00000d39
GL_PALETTE8_R5_G6_B5_OES = 0x00008b97
GL_TEXTURE8 = 0x000084c8
GL_TEXTURE9 = 0x000084c9
GL_TEXTURE_COORD_ARRAY_STRIDE = 0x0000808a
GL_TEXTURE4 = 0x000084c4
GL_TEXTURE5 = 0x000084c5
GL_TEXTURE6 = 0x000084c6
GL_TEXTURE7 = 0x000084c7
GL_TEXTURE0 = 0x000084c0
GL_LINEAR_MIPMAP_LINEAR = 0x00002703
GL_TEXTURE2 = 0x000084c2
GL_TEXTURE3 = 0x000084c3
GL_BYTE = 0x00001400
GL_COLOR_ARRAY = 0x00008076
GL_POINT_SPRITE_OES = 0x00008861
GL_ONE = 0x00000001
GL_COLOR_CLEAR_VALUE = 0x00000c22
GL_DEPTH_WRITEMASK = 0x00000b72
GL_COLOR_ARRAY_POINTER = 0x00008090
GL_TRIANGLE_STRIP = 0x00000005
GL_NOOP = 0x00001505
GL_CLIP_PLANE4 = 0x00003004
GL_POINT_SIZE_MAX = 0x00008127
GL_MODELVIEW_MATRIX = 0x00000ba6
GL_UNSIGNED_SHORT_5_5_5_1 = 0x00008034
GL_COORD_REPLACE_OES = 0x00008862
GL_STENCIL_FUNC = 0x00000b92
GL_EXP = 0x00000800
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x0000889a
GL_TEXTURE_ENV = 0x00002300
GL_ALIASED_LINE_WIDTH_RANGE = 0x0000846e
GL_POINT_SIZE = 0x00000b11
GL_DECR = 0x00001e03
GL_BACK = 0x00000405
GL_POLYGON_OFFSET_FILL = 0x00008037
GL_MAX_CLIP_PLANES = 0x00000d32
GL_FRONT_AND_BACK = 0x00000408
GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES = 0x00008b9f
GL_STENCIL_CLEAR_VALUE = 0x00000b91
GL_GREEN_BITS = 0x00000d53
GL_STENCIL_WRITEMASK = 0x00000b98
GL_PALETTE4_R5_G6_B5_OES = 0x00008b92
GL_SRC2_RGB = 0x00008582
GL_UNSIGNED_SHORT_4_4_4_4 = 0x00008033
GL_FLOAT = 0x00001406
GL_NO_ERROR = 0x00000000
GL_PALETTE8_RGB8_OES = 0x00008b95
GL_VIEWPORT = 0x00000ba2
GL_PALETTE4_RGBA4_OES = 0x00008b93
GL_AND_REVERSE = 0x00001502
GL_LIGHT1 = 0x00004001
GL_LIGHT0 = 0x00004000
GL_LIGHT3 = 0x00004003
GL_LIGHT2 = 0x00004002
GL_LIGHT5 = 0x00004005
GL_LIGHT4 = 0x00004004
GL_BLEND_SRC = 0x00000be1
GL_LIGHT6 = 0x00004006
GL_KEEP = 0x00001e00
GL_ARRAY_BUFFER = 0x00008892
GL_FOG_MODE = 0x00000b65
GL_POINT_SIZE_ARRAY_OES = 0x00008b9c
GL_SRC_COLOR = 0x00000300
GL_PALETTE8_RGBA4_OES = 0x00008b98
GL_AND = 0x00001501
GL_POINT_SIZE_MIN = 0x00008126
GL_SAMPLE_BUFFERS = 0x000080a8
GL_EXTENSIONS = 0x00001f03
GL_NORMAL_ARRAY_POINTER = 0x0000808f
GL_ONE_MINUS_DST_ALPHA = 0x00000305
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_SMOOTH_POINT_SIZE_RANGE = 0x00000b12
GL_ELEMENT_ARRAY_BUFFER = 0x00008893
GL_ALIASED_POINT_SIZE_RANGE = 0x0000846d
GL_CCW = 0x00000901
GL_DEPTH_TEST = 0x00000b71
GL_SHADE_MODEL = 0x00000b54
GL_MULTISAMPLE = 0x0000809d
GL_LINEAR = 0x00002601
GL_VERTEX_ARRAY = 0x00008074
GL_OR_REVERSE = 0x0000150b
GL_VERTEX_ARRAY_BUFFER_BINDING = 0x00008896
GL_VERTEX_ARRAY_TYPE = 0x0000807b
GL_DEPTH_RANGE = 0x00000b70
GL_GREATER = 0x00000204
GL_CLAMP_TO_EDGE = 0x0000812f
GL_NEAREST = 0x00002600
GL_COMPRESSED_TEXTURE_FORMATS = 0x000086a3
GL_FRONT_FACE = 0x00000b46
GL_REPLACE = 0x00001e01
GL_OPERAND1_RGB = 0x00008591
GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES = 0x00008b9b
GL_TEXTURE30 = 0x000084de
GL_TEXTURE31 = 0x000084df
GL_POINT_SMOOTH = 0x00000b10
GL_SRC1_ALPHA = 0x00008589
GL_TEXTURE_ENV_COLOR = 0x00002201
GL_LINE_SMOOTH = 0x00000b20
GL_TEXTURE_STACK_DEPTH = 0x00000ba5
GL_BLEND = 0x00000be2
GL_OPERAND0_RGB = 0x00008590
GL_UNSIGNED_SHORT = 0x00001403
GL_ONE_MINUS_DST_COLOR = 0x00000307
GL_ONE_MINUS_SRC_COLOR = 0x00000301
GL_TEXTURE = 0x00001702
GL_MAX_PROJECTION_STACK_DEPTH = 0x00000d38
GL_OES_compressed_paletted_texture = 0x00000001
GL_COLOR_BUFFER_BIT = 0x00004000
GL_DONT_CARE = 0x00001100
GL_SPOT_CUTOFF = 0x00001206
GL_LINEAR_ATTENUATION = 0x00001208
GL_OPERAND2_RGB = 0x00008592
GL_INVALID_VALUE = 0x00000501
GL_NEAREST_MIPMAP_NEAREST = 0x00002700
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x000086a2
GL_OES_point_size_array = 0x00000001
GL_TEXTURE_MAG_FILTER = 0x00002800
GL_MAX_TEXTURE_UNITS = 0x000084e2
GL_TEXTURE1 = 0x000084c1
GL_ALPHA_BITS = 0x00000d55
GL_NEAREST_MIPMAP_LINEAR = 0x00002702
GL_SRC2_ALPHA = 0x0000858a
GL_AND_INVERTED = 0x00001504
GL_SRC0_RGB = 0x00008580
GL_FOG_END = 0x00000b64
GL_VERSION_ES_CM_1_0 = 0x00000001
GL_MAX_TEXTURE_SIZE = 0x00000d33
GL_COMBINE_ALPHA = 0x00008572
GL_QUADRATIC_ATTENUATION = 0x00001209
GL_FALSE = 0x00000000
GL_ONE_MINUS_SRC_ALPHA = 0x00000303
GL_SAMPLE_ALPHA_TO_ONE = 0x0000809f
GL_CLIENT_ACTIVE_TEXTURE = 0x000084e1
GL_OPERAND2_ALPHA = 0x0000859a
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x0000809e
GL_VERSION_ES_CM_1_1 = 0x00000001
GL_FOG_DENSITY = 0x00000b62
GL_STENCIL_BITS = 0x00000d57
GL_CONSTANT_ATTENUATION = 0x00001207
GL_STENCIL_PASS_DEPTH_FAIL = 0x00000b95
GL_TEXTURE_COORD_ARRAY_POINTER = 0x00008092
GL_SRC0_ALPHA = 0x00008588
GL_IMPLEMENTATION_COLOR_READ_TYPE_OES = 0x00008b9a
GL_DOT3_RGB = 0x000086ae
GL_MAX_MODELVIEW_STACK_DEPTH = 0x00000d36
GL_LINE_SMOOTH_HINT = 0x00000c52
GL_FRONT = 0x00000404
GL_SCISSOR_BOX = 0x00000c10
GL_AMBIENT = 0x00001200
GL_BUFFER_USAGE = 0x00008765
GL_CULL_FACE_MODE = 0x00000b45
GL_NORMAL_ARRAY_BUFFER_BINDING = 0x00008897
GL_ALPHA = 0x00001906
GL_SET = 0x0000150f
GL_COLOR_WRITEMASK = 0x00000c23
GL_DST_COLOR = 0x00000306
GL_OPERAND0_ALPHA = 0x00008598
GL_ALWAYS = 0x00000207
GL_TEXTURE_WRAP_S = 0x00002802
GL_TEXTURE_WRAP_T = 0x00002803
GL_DST_ALPHA = 0x00000304
GL_INVALID_OPERATION = 0x00000502
GL_PERSPECTIVE_CORRECTION_HINT = 0x00000c50
GL_SCISSOR_TEST = 0x00000c11
GL_FOG_START = 0x00000b63
GL_PROJECTION_STACK_DEPTH = 0x00000ba4
GL_TRUE = 0x00000001
GL_TEXTURE_MIN_FILTER = 0x00002801
GL_COLOR_ARRAY_TYPE = 0x00008082
GL_BLUE_BITS = 0x00000d54
GL_STACK_UNDERFLOW = 0x00000504
GL_MODULATE = 0x00002100
GL_EQUAL = 0x00000202
GL_ADD = 0x00000104
GL_INTERPOLATE = 0x00008575
GL_MODELVIEW_STACK_DEPTH = 0x00000ba3
GL_POINT_FADE_THRESHOLD_SIZE = 0x00008128
GL_UNPACK_ALIGNMENT = 0x00000cf5
GL_COMBINE_RGB = 0x00008571
GL_LINE_STRIP = 0x00000003
GL_COLOR_MATERIAL = 0x00000b57
GL_CLIP_PLANE1 = 0x00003001
GL_CLIP_PLANE0 = 0x00003000
GL_CLIP_PLANE3 = 0x00003003
GL_CLIP_PLANE2 = 0x00003002
GL_CLIP_PLANE5 = 0x00003005
GL_POINT_SMOOTH_HINT = 0x00000c51
GL_NORMAL_ARRAY_TYPE = 0x0000807e
GL_POINTS = 0x00000000
GL_FASTEST = 0x00001101
GL_TEXTURE_2D = 0x00000de1
GL_NAND = 0x0000150e
GL_OR = 0x00001507
GL_TEXTURE_COORD_ARRAY_TYPE = 0x00008089
GL_TEXTURE23 = 0x000084d7
GL_TEXTURE22 = 0x000084d6
GL_TEXTURE21 = 0x000084d5
GL_TEXTURE20 = 0x000084d4
GL_TEXTURE27 = 0x000084db
GL_TEXTURE26 = 0x000084da
GL_TEXTURE25 = 0x000084d9
GL_TEXTURE24 = 0x000084d8
GL_TEXTURE29 = 0x000084dd
GL_TEXTURE28 = 0x000084dc
GL_ADD_SIGNED = 0x00008574
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x00008895
GL_LINE_LOOP = 0x00000002
GL_ALPHA_SCALE = 0x00000d1c
GL_TEXTURE_COORD_ARRAY_SIZE = 0x00008088
GL_SUBPIXEL_BITS = 0x00000d50
GL_CURRENT_NORMAL = 0x00000b02
GL_GEQUAL = 0x00000206
GL_ALPHA_TEST = 0x00000bc0
GL_LINE_WIDTH = 0x00000b21
GL_LEQUAL = 0x00000203
GL_SUBTRACT = 0x000084e7
GL_LIGHT_MODEL_AMBIENT = 0x00000b53
GL_DEPTH_CLEAR_VALUE = 0x00000b73
GL_DOT3_RGBA = 0x000086af
GL_ARRAY_BUFFER_BINDING = 0x00008894
GL_POLYGON_OFFSET_UNITS = 0x00002a00
GL_VERTEX_ARRAY_STRIDE = 0x0000807c
GL_PRIMARY_COLOR = 0x00008577
GL_DYNAMIC_DRAW = 0x000088e8
GL_OUT_OF_MEMORY = 0x00000505
GL_NICEST = 0x00001102
GL_NORMAL_ARRAY_STRIDE = 0x0000807f
GL_POINT_SIZE_ARRAY_TYPE_OES = 0x0000898a
GL_SMOOTH = 0x00001d01
GL_CURRENT_TEXTURE_COORDS = 0x00000b03
GL_PALETTE8_RGB5_A1_OES = 0x00008b99
GL_PALETTE8_RGBA8_OES = 0x00008b96
GL_SPECULAR = 0x00001202
GL_STENCIL_TEST = 0x00000b90
GL_GENERATE_MIPMAP = 0x00008191
GL_LUMINANCE_ALPHA = 0x0000190a
GL_INVERT = 0x0000150a
GL_COLOR_ARRAY_SIZE = 0x00008081
GL_POLYGON_OFFSET_FACTOR = 0x00008038
GL_STENCIL_REF = 0x00000b97
GL_TRIANGLE_FAN = 0x00000006
GL_CURRENT_COLOR = 0x00000b00
GL_MODELVIEW = 0x00001700
GL_TRIANGLES = 0x00000004
GL_RED_BITS = 0x00000d52
GL_NOR = 0x00001508
GL_FOG = 0x00000b60
GL_FLAT = 0x00001d00
GL_PACK_ALIGNMENT = 0x00000d05
GL_POSITION = 0x00001203
GL_RENDERER = 0x00001f01
GL_ACTIVE_TEXTURE = 0x000084e0
GL_PALETTE4_RGB8_OES = 0x00008b90
GL_SMOOTH_LINE_WIDTH_RANGE = 0x00000b22
GL_COLOR_LOGIC_OP = 0x00000bf2
GL_PROJECTION = 0x00001701
GL_DEPTH_FUNC = 0x00000b74
GL_STENCIL_FAIL = 0x00000b94
GL_CONSTANT = 0x00008576
GL_RGB_SCALE = 0x00008573
GL_XOR = 0x00001506
GL_INVALID_ENUM = 0x00000500
GL_LESS = 0x00000201
GL_EMISSION = 0x00001600
GL_TEXTURE_ENV_MODE = 0x00002200
GL_EQUIV = 0x00001509
GL_FOG_COLOR = 0x00000b66
GL_VERSION_ES_CL_1_0 = 0x00000001
GL_VERSION_ES_CL_1_1 = 0x00000001
GL_SRC_ALPHA_SATURATE = 0x00000308
GL_REPEAT = 0x00002901
GL_RESCALE_NORMAL = 0x0000803a
GL_VERTEX_ARRAY_SIZE = 0x0000807a
GL_PREVIOUS = 0x00008578
GL_SPOT_DIRECTION = 0x00001204
GL_PALETTE4_RGBA8_OES = 0x00008b91
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_DIFFUSE = 0x00001201
GL_SRC1_RGB = 0x00008581
GL_LIGHTING = 0x00000b50
GL_STENCIL_PASS_DEPTH_PASS = 0x00000b96
GL_LIGHT_MODEL_TWO_SIDE = 0x00000b52
GL_VERTEX_ARRAY_POINTER = 0x0000808e
GL_SAMPLE_COVERAGE_INVERT = 0x000080ab
GL_LINES = 0x00000001
GL_TEXTURE18 = 0x000084d2
GL_TEXTURE19 = 0x000084d3
GL_TEXTURE16 = 0x000084d0
GL_TEXTURE17 = 0x000084d1
GL_TEXTURE14 = 0x000084ce
GL_GENERATE_MIPMAP_HINT = 0x00008192
GL_ALPHA_TEST_REF = 0x00000bc2
GL_TEXTURE13 = 0x000084cd
GL_TEXTURE10 = 0x000084ca
GL_TEXTURE11 = 0x000084cb
GL_POINT_SIZE_ARRAY_STRIDE_OES = 0x0000898b
GL_RGB = 0x00001907
GL_EXP2 = 0x00000801
GL_COPY_INVERTED = 0x0000150c
GL_STACK_OVERFLOW = 0x00000503
GL_FOG_HINT = 0x00000c54
GL_PALETTE4_RGB5_A1_OES = 0x00008b94
GL_PROJECTION_MATRIX = 0x00000ba7
GL_COLOR_ARRAY_BUFFER_BINDING = 0x00008898
GL_LINEAR_MIPMAP_NEAREST = 0x00002701
GL_POINT_DISTANCE_ATTENUATION = 0x00008129
GL_AMBIENT_AND_DIFFUSE = 0x00001602
GL_VERSION = 0x00001f02
GL_ZERO = 0x00000000
GL_COLOR_ARRAY_STRIDE = 0x00008083
GL_SRC_ALPHA = 0x00000302
GL_FIXED = 0x0000140c
GL_POINT_SIZE_ARRAY_POINTER_OES = 0x0000898c
GL_NOTEQUAL = 0x00000205
GL_TEXTURE_COORD_ARRAY = 0x00008078
GL_INCR = 0x00001e02
GL_CULL_FACE = 0x00000b44
GL_SAMPLE_COVERAGE_VALUE = 0x000080aa
GL_MAX_LIGHTS = 0x00000d31
GL_OES_read_format = 0x00000001
GL_MAX_VIEWPORT_DIMS = 0x00000d3a
GL_OES_point_sprite = 0x00000001
GL_OPERAND1_ALPHA = 0x00008599
GL_NORMALIZE = 0x00000ba1
GL_NEVER = 0x00000200
GL_TEXTURE15 = 0x000084cf
GL_STENCIL_VALUE_MASK = 0x00000b93
GL_BLEND_DST = 0x00000be0
GL_TEXTURE12 = 0x000084cc
GL_LOGIC_OP_MODE = 0x00000bf0
GL_SPOT_EXPONENT = 0x00001205
GL_RGBA = 0x00001908
GL_SHORT = 0x00001402
GL_CW = 0x00000900
GL_NORMAL_ARRAY = 0x00008075
GL_UNSIGNED_BYTE = 0x00001401
GL_VENDOR = 0x00001f00
GL_TEXTURE_BINDING_2D = 0x00008069
GL_STATIC_DRAW = 0x000088e4
GL_COMBINE = 0x00008570
GL_LUMINANCE = 0x00001909
GL_DEPTH_BITS = 0x00000d56
GL_OR_INVERTED = 0x0000150d
GL_COPY = 0x00001503
GL_TEXTURE_MATRIX = 0x00000ba8
GL_CLEAR = 0x00001500
GL_LIGHT7 = 0x00004007
GL_MATRIX_MODE = 0x00000ba0
GL_DECAL = 0x00002101
GL_SAMPLE_COVERAGE = 0x000080a0
GL_SHININESS = 0x00001601
GL_SAMPLES = 0x000080a9

# GL Functions
try:
    def glAlphaFunc(func, ref, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLclampf]
        cfunc = c.glAlphaFunc
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(func, ref)
    # Check if the function actually exists
    f = c.glAlphaFunc
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
            argtypes = [GLclampf, GLclampf, GLclampf, GLclampf]
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
    def glClearDepthf(depth, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLclampf]
        cfunc = c.glClearDepthf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(depth)
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
    def glClipPlanef(plane, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glClipPlanef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(plane, param0)
    # Check if the function actually exists
    f = c.glClipPlanef
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glColor4f(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glColor4f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glColor4f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDepthRangef(zNear, zFar, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLclampf, GLclampf]
        cfunc = c.glDepthRangef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(zNear, zFar)
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
    def glFogf(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glFogf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glFogf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFogfv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glFogfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glFogfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFrustumf(left, right, bottom, top, zNear, zFar, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glFrustumf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glFrustumf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetClipPlanef(pname, eqn, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, (GLfloat * 4)]
        cfunc = c.glGetClipPlanef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, eqn)
    # Check if the function actually exists
    f = c.glGetClipPlanef
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
    def glGetLightfv(light, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glGetLightfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param0)
    # Check if the function actually exists
    f = c.glGetLightfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetMaterialfv(face, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glGetMaterialfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param0)
    # Check if the function actually exists
    f = c.glGetMaterialfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetTexEnvfv(env, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glGetTexEnvfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(env, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexEnvfv
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
    def glLightModelf(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glLightModelf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glLightModelf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLightModelfv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glLightModelfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glLightModelfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLightf(light, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glLightf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param)
    # Check if the function actually exists
    f = c.glLightf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLightfv(light, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glLightfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param0)
    # Check if the function actually exists
    f = c.glLightfv
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
    def glLoadMatrixf(param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat]
        cfunc = c.glLoadMatrixf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glLoadMatrixf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMaterialf(face, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glMaterialf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param)
    # Check if the function actually exists
    f = c.glMaterialf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMaterialfv(face, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glMaterialfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param0)
    # Check if the function actually exists
    f = c.glMaterialfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMultMatrixf(param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat]
        cfunc = c.glMultMatrixf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glMultMatrixf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMultiTexCoord4f(target, s, t, r, q, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glMultiTexCoord4f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, s, t, r, q)
    # Check if the function actually exists
    f = c.glMultiTexCoord4f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glNormal3f(nx, ny, nz, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat]
        cfunc = c.glNormal3f
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(nx, ny, nz)
    # Check if the function actually exists
    f = c.glNormal3f
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glOrthof(left, right, bottom, top, zNear, zFar, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glOrthof
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glOrthof
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPointParameterf(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glPointParameterf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glPointParameterf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPointParameterfv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfloat]
        cfunc = c.glPointParameterfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glPointParameterfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPointSize(size, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat]
        cfunc = c.glPointSize
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size)
    # Check if the function actually exists
    f = c.glPointSize
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
    def glRotatef(angle, x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat, GLfloat]
        cfunc = c.glRotatef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(angle, x, y, z)
    # Check if the function actually exists
    f = c.glRotatef
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glScalef(x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat]
        cfunc = c.glScalef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z)
    # Check if the function actually exists
    f = c.glScalef
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexEnvf(target, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glTexEnvf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexEnvf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexEnvfv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfloat]
        cfunc = c.glTexEnvfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexEnvfv
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
    def glTranslatef(x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfloat, GLfloat, GLfloat]
        cfunc = c.glTranslatef
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z)
    # Check if the function actually exists
    f = c.glTranslatef
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

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
    def glAlphaFuncx(func, ref, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLclampx]
        cfunc = c.glAlphaFuncx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(func, ref)
    # Check if the function actually exists
    f = c.glAlphaFuncx
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
    def glBufferData(target, size, param0, usage, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizeiptr, GLvoid, GLenum]
        cfunc = c.glBufferData
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, size, param0, usage)
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
    def glBufferSubData(target, offset, size, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLintptr, GLsizeiptr, GLvoid]
        cfunc = c.glBufferSubData
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, offset, size, param0)
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
    def glClearColorx(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLclampx, GLclampx, GLclampx, GLclampx]
        cfunc = c.glClearColorx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glClearColorx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearDepthx(depth, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLclampx]
        cfunc = c.glClearDepthx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(depth)
    # Check if the function actually exists
    f = c.glClearDepthx
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
    def glClientActiveTexture(texture, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glClientActiveTexture
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture)
    # Check if the function actually exists
    f = c.glClientActiveTexture
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClipPlanex(plane, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glClipPlanex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(plane, param0)
    # Check if the function actually exists
    f = c.glClipPlanex
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glColor4ub(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLubyte, GLubyte, GLubyte, GLubyte]
        cfunc = c.glColor4ub
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glColor4ub
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glColor4x(red, green, blue, alpha, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed, GLfixed]
        cfunc = c.glColor4x
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glColor4x
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
    def glColorPointer(size, type, stride, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLenum, GLsizei, GLvoid]
        cfunc = c.glColorPointer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size, type, stride, param0)
    # Check if the function actually exists
    f = c.glColorPointer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, GLvoid]
        cfunc = c.glCompressedTexImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, width, height, border, imageSize, param0)
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
    def glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, GLvoid]
        cfunc = c.glCompressedTexSubImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, width, height, format, imageSize, param0)
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
    def glDepthRangex(zNear, zFar, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLclampx, GLclampx]
        cfunc = c.glDepthRangex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(zNear, zFar)
    # Check if the function actually exists
    f = c.glDepthRangex
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
    def glDisableClientState(array, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glDisableClientState
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(array)
    # Check if the function actually exists
    f = c.glDisableClientState
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
    def glDrawElements(mode, count, type, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, GLvoid]
        cfunc = c.glDrawElements
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode, count, type, param0)
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
    def glEnableClientState(array, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glEnableClientState
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(array)
    # Check if the function actually exists
    f = c.glEnableClientState
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
    def glFogx(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glFogx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glFogx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFogxv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glFogxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glFogxv
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
    def glFrustumx(left, right, bottom, top, zNear, zFar, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed, GLfixed, GLfixed, GLfixed]
        cfunc = c.glFrustumx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glFrustumx
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
    def glGetClipPlanex(pname, eqn, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, (GLfixed * 4)]
        cfunc = c.glGetClipPlanex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, eqn)
    # Check if the function actually exists
    f = c.glGetClipPlanex
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
    def glGetFixedv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glGetFixedv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetFixedv
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
    def glGetLightxv(light, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glGetLightxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param0)
    # Check if the function actually exists
    f = c.glGetLightxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetMaterialxv(face, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glGetMaterialxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param0)
    # Check if the function actually exists
    f = c.glGetMaterialxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetPointerv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLvoid]
        cfunc = c.glGetPointerv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetPointerv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetTexEnviv(env, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glGetTexEnviv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(env, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexEnviv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetTexEnvxv(env, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glGetTexEnvxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(env, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexEnvxv
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
    def glGetTexParameterxv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glGetTexParameterxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexParameterxv
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
    def glLightModelx(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glLightModelx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glLightModelx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLightModelxv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glLightModelxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glLightModelxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLightx(light, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glLightx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param)
    # Check if the function actually exists
    f = c.glLightx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLightxv(light, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glLightxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param0)
    # Check if the function actually exists
    f = c.glLightxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLineWidthx(width, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed]
        cfunc = c.glLineWidthx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(width)
    # Check if the function actually exists
    f = c.glLineWidthx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLoadIdentity(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glLoadIdentity
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glLoadIdentity
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLoadMatrixx(param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed]
        cfunc = c.glLoadMatrixx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glLoadMatrixx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glLogicOp(opcode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glLogicOp
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(opcode)
    # Check if the function actually exists
    f = c.glLogicOp
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMaterialx(face, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glMaterialx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param)
    # Check if the function actually exists
    f = c.glMaterialx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMaterialxv(face, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glMaterialxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param0)
    # Check if the function actually exists
    f = c.glMaterialxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMatrixMode(mode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glMatrixMode
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode)
    # Check if the function actually exists
    f = c.glMatrixMode
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMultMatrixx(param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed]
        cfunc = c.glMultMatrixx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glMultMatrixx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glMultiTexCoord4x(target, s, t, r, q, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed, GLfixed, GLfixed, GLfixed]
        cfunc = c.glMultiTexCoord4x
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, s, t, r, q)
    # Check if the function actually exists
    f = c.glMultiTexCoord4x
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glNormal3x(nx, ny, nz, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed]
        cfunc = c.glNormal3x
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(nx, ny, nz)
    # Check if the function actually exists
    f = c.glNormal3x
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glNormalPointer(type, stride, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLvoid]
        cfunc = c.glNormalPointer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(type, stride, param0)
    # Check if the function actually exists
    f = c.glNormalPointer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glOrthox(left, right, bottom, top, zNear, zFar, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed, GLfixed, GLfixed, GLfixed]
        cfunc = c.glOrthox
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glOrthox
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
    def glPointParameterx(pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glPointParameterx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glPointParameterx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPointParameterxv(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLfixed]
        cfunc = c.glPointParameterxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glPointParameterxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPointSizex(size, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed]
        cfunc = c.glPointSizex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size)
    # Check if the function actually exists
    f = c.glPointSizex
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPolygonOffsetx(factor, units, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed]
        cfunc = c.glPolygonOffsetx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(factor, units)
    # Check if the function actually exists
    f = c.glPolygonOffsetx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPopMatrix(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glPopMatrix
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glPopMatrix
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPushMatrix(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glPushMatrix
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glPushMatrix
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glReadPixels(x, y, width, height, format, type, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, GLvoid]
        cfunc = c.glReadPixels
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, width, height, format, type, param0)
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
    def glRotatex(angle, x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed, GLfixed]
        cfunc = c.glRotatex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(angle, x, y, z)
    # Check if the function actually exists
    f = c.glRotatex
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
            argtypes = [GLclampf, GLboolean]
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
    def glSampleCoveragex(value, invert, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLclampx, GLboolean]
        cfunc = c.glSampleCoveragex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(value, invert)
    # Check if the function actually exists
    f = c.glSampleCoveragex
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glScalex(x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed]
        cfunc = c.glScalex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z)
    # Check if the function actually exists
    f = c.glScalex
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
    def glShadeModel(mode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glShadeModel
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode)
    # Check if the function actually exists
    f = c.glShadeModel
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
    def glTexCoordPointer(size, type, stride, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLenum, GLsizei, GLvoid]
        cfunc = c.glTexCoordPointer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size, type, stride, param0)
    # Check if the function actually exists
    f = c.glTexCoordPointer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexEnvi(target, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glTexEnvi
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexEnvi
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexEnvx(target, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glTexEnvx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexEnvx
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexEnviv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glTexEnviv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexEnviv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexEnvxv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glTexEnvxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexEnvxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexImage2D(target, level, internalformat, width, height, border, format, type, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, GLvoid]
        cfunc = c.glTexImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, width, height, border, format, type, param0)
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
    def glTexParameterx(target, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glTexParameterx
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexParameterx
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
    def glTexParameterxv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLfixed]
        cfunc = c.glTexParameterxv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexParameterxv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, GLvoid]
        cfunc = c.glTexSubImage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, width, height, format, type, param0)
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
    def glTranslatex(x, y, z, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLfixed, GLfixed, GLfixed]
        cfunc = c.glTranslatex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z)
    # Check if the function actually exists
    f = c.glTranslatex
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexPointer(size, type, stride, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLenum, GLsizei, GLvoid]
        cfunc = c.glVertexPointer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size, type, stride, param0)
    # Check if the function actually exists
    f = c.glVertexPointer
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

try:
    def glPointSizePointerOES(type, stride, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLvoid]
        cfunc = c.glPointSizePointerOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(type, stride, param0)
    # Check if the function actually exists
    f = c.glPointSizePointerOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

print 'Loaded %i functions and failed to load %i functions of %i functions in the header gl.h' % (loaded[0], loaded[1], sum(loaded))
__all__ = ['glAlphaFunc', 'glClearColor', 'glClearDepthf', 'glClipPlanef', 'glColor4f', 'glDepthRangef', 'glFogf', 'glFogfv', 'glFrustumf', 'glGetClipPlanef', 'glGetFloatv', 'glGetLightfv', 'glGetMaterialfv', 'glGetTexEnvfv', 'glGetTexParameterfv', 'glLightModelf', 'glLightModelfv', 'glLightf', 'glLightfv', 'glLineWidth', 'glLoadMatrixf', 'glMaterialf', 'glMaterialfv', 'glMultMatrixf', 'glMultiTexCoord4f', 'glNormal3f', 'glOrthof', 'glPointParameterf', 'glPointParameterfv', 'glPointSize', 'glPolygonOffset', 'glRotatef', 'glScalef', 'glTexEnvf', 'glTexEnvfv', 'glTexParameterf', 'glTexParameterfv', 'glTranslatef', 'glActiveTexture', 'glAlphaFuncx', 'glBindBuffer', 'glBindTexture', 'glBlendFunc', 'glBufferData', 'glBufferSubData', 'glClear', 'glClearColorx', 'glClearDepthx', 'glClearStencil', 'glClientActiveTexture', 'glClipPlanex', 'glColor4ub', 'glColor4x', 'glColorMask', 'glColorPointer', 'glCompressedTexImage2D', 'glCompressedTexSubImage2D', 'glCopyTexImage2D', 'glCopyTexSubImage2D', 'glCullFace', 'glDeleteBuffers', 'glDeleteTextures', 'glDepthFunc', 'glDepthMask', 'glDepthRangex', 'glDisable', 'glDisableClientState', 'glDrawArrays', 'glDrawElements', 'glEnable', 'glEnableClientState', 'glFinish', 'glFlush', 'glFogx', 'glFogxv', 'glFrontFace', 'glFrustumx', 'glGetBooleanv', 'glGetBufferParameteriv', 'glGetClipPlanex', 'glGenBuffers', 'glGenTextures', 'glGetError', 'glGetFixedv', 'glGetIntegerv', 'glGetLightxv', 'glGetMaterialxv', 'glGetPointerv', 'glGetTexEnviv', 'glGetTexEnvxv', 'glGetTexParameteriv', 'glGetTexParameterxv', 'glHint', 'glIsBuffer', 'glIsEnabled', 'glIsTexture', 'glLightModelx', 'glLightModelxv', 'glLightx', 'glLightxv', 'glLineWidthx', 'glLoadIdentity', 'glLoadMatrixx', 'glLogicOp', 'glMaterialx', 'glMaterialxv', 'glMatrixMode', 'glMultMatrixx', 'glMultiTexCoord4x', 'glNormal3x', 'glNormalPointer', 'glOrthox', 'glPixelStorei', 'glPointParameterx', 'glPointParameterxv', 'glPointSizex', 'glPolygonOffsetx', 'glPopMatrix', 'glPushMatrix', 'glReadPixels', 'glRotatex', 'glSampleCoverage', 'glSampleCoveragex', 'glScalex', 'glScissor', 'glShadeModel', 'glStencilFunc', 'glStencilMask', 'glStencilOp', 'glTexCoordPointer', 'glTexEnvi', 'glTexEnvx', 'glTexEnviv', 'glTexEnvxv', 'glTexImage2D', 'glTexParameteri', 'glTexParameterx', 'glTexParameteriv', 'glTexParameterxv', 'glTexSubImage2D', 'glTranslatex', 'glVertexPointer', 'glViewport', 'glPointSizePointerOES', 'GL_UNSIGNED_SHORT_5_6_5', 'GL_DITHER', 'GL_ALPHA_TEST_FUNC', 'GL_BUFFER_SIZE', 'GL_MAX_TEXTURE_STACK_DEPTH', 'GL_PALETTE8_R5_G6_B5_OES', 'GL_TEXTURE8', 'GL_TEXTURE9', 'GL_TEXTURE_COORD_ARRAY_STRIDE', 'GL_TEXTURE4', 'GL_TEXTURE5', 'GL_TEXTURE6', 'GL_TEXTURE7', 'GL_TEXTURE0', 'GL_LINEAR_MIPMAP_LINEAR', 'GL_TEXTURE2', 'GL_TEXTURE3', 'GL_BYTE', 'GL_COLOR_ARRAY', 'GL_POINT_SPRITE_OES', 'GL_ONE', 'GL_COLOR_CLEAR_VALUE', 'GL_DEPTH_WRITEMASK', 'GL_COLOR_ARRAY_POINTER', 'GL_TRIANGLE_STRIP', 'GL_NOOP', 'GL_CLIP_PLANE4', 'GL_POINT_SIZE_MAX', 'GL_MODELVIEW_MATRIX', 'GL_UNSIGNED_SHORT_5_5_5_1', 'GL_COORD_REPLACE_OES', 'GL_STENCIL_FUNC', 'GL_EXP', 'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING', 'GL_TEXTURE_ENV', 'GL_ALIASED_LINE_WIDTH_RANGE', 'GL_POINT_SIZE', 'GL_DECR', 'GL_BACK', 'GL_POLYGON_OFFSET_FILL', 'GL_MAX_CLIP_PLANES', 'GL_FRONT_AND_BACK', 'GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES', 'GL_STENCIL_CLEAR_VALUE', 'GL_GREEN_BITS', 'GL_STENCIL_WRITEMASK', 'GL_PALETTE4_R5_G6_B5_OES', 'GL_SRC2_RGB', 'GL_UNSIGNED_SHORT_4_4_4_4', 'GL_FLOAT', 'GL_NO_ERROR', 'GL_PALETTE8_RGB8_OES', 'GL_VIEWPORT', 'GL_PALETTE4_RGBA4_OES', 'GL_AND_REVERSE', 'GL_LIGHT1', 'GL_LIGHT0', 'GL_LIGHT3', 'GL_LIGHT2', 'GL_LIGHT5', 'GL_LIGHT4', 'GL_BLEND_SRC', 'GL_LIGHT6', 'GL_KEEP', 'GL_ARRAY_BUFFER', 'GL_FOG_MODE', 'GL_POINT_SIZE_ARRAY_OES', 'GL_SRC_COLOR', 'GL_PALETTE8_RGBA4_OES', 'GL_AND', 'GL_POINT_SIZE_MIN', 'GL_SAMPLE_BUFFERS', 'GL_EXTENSIONS', 'GL_NORMAL_ARRAY_POINTER', 'GL_ONE_MINUS_DST_ALPHA', 'GL_DEPTH_BUFFER_BIT', 'GL_SMOOTH_POINT_SIZE_RANGE', 'GL_ELEMENT_ARRAY_BUFFER', 'GL_ALIASED_POINT_SIZE_RANGE', 'GL_CCW', 'GL_DEPTH_TEST', 'GL_SHADE_MODEL', 'GL_MULTISAMPLE', 'GL_LINEAR', 'GL_VERTEX_ARRAY', 'GL_OR_REVERSE', 'GL_VERTEX_ARRAY_BUFFER_BINDING', 'GL_VERTEX_ARRAY_TYPE', 'GL_DEPTH_RANGE', 'GL_GREATER', 'GL_CLAMP_TO_EDGE', 'GL_NEAREST', 'GL_COMPRESSED_TEXTURE_FORMATS', 'GL_FRONT_FACE', 'GL_REPLACE', 'GL_OPERAND1_RGB', 'GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES', 'GL_TEXTURE30', 'GL_TEXTURE31', 'GL_POINT_SMOOTH', 'GL_SRC1_ALPHA', 'GL_TEXTURE_ENV_COLOR', 'GL_LINE_SMOOTH', 'GL_TEXTURE_STACK_DEPTH', 'GL_BLEND', 'GL_OPERAND0_RGB', 'GL_UNSIGNED_SHORT', 'GL_ONE_MINUS_DST_COLOR', 'GL_ONE_MINUS_SRC_COLOR', 'GL_TEXTURE', 'GL_MAX_PROJECTION_STACK_DEPTH', 'GL_OES_compressed_paletted_texture', 'GL_COLOR_BUFFER_BIT', 'GL_DONT_CARE', 'GL_SPOT_CUTOFF', 'GL_LINEAR_ATTENUATION', 'GL_OPERAND2_RGB', 'GL_INVALID_VALUE', 'GL_NEAREST_MIPMAP_NEAREST', 'GL_NUM_COMPRESSED_TEXTURE_FORMATS', 'GL_OES_point_size_array', 'GL_TEXTURE_MAG_FILTER', 'GL_MAX_TEXTURE_UNITS', 'GL_TEXTURE1', 'GL_ALPHA_BITS', 'GL_NEAREST_MIPMAP_LINEAR', 'GL_SRC2_ALPHA', 'GL_AND_INVERTED', 'GL_SRC0_RGB', 'GL_FOG_END', 'GL_VERSION_ES_CM_1_0', 'GL_MAX_TEXTURE_SIZE', 'GL_COMBINE_ALPHA', 'GL_QUADRATIC_ATTENUATION', 'GL_FALSE', 'GL_ONE_MINUS_SRC_ALPHA', 'GL_SAMPLE_ALPHA_TO_ONE', 'GL_CLIENT_ACTIVE_TEXTURE', 'GL_OPERAND2_ALPHA', 'GL_SAMPLE_ALPHA_TO_COVERAGE', 'GL_VERSION_ES_CM_1_1', 'GL_FOG_DENSITY', 'GL_STENCIL_BITS', 'GL_CONSTANT_ATTENUATION', 'GL_STENCIL_PASS_DEPTH_FAIL', 'GL_TEXTURE_COORD_ARRAY_POINTER', 'GL_SRC0_ALPHA', 'GL_IMPLEMENTATION_COLOR_READ_TYPE_OES', 'GL_DOT3_RGB', 'GL_MAX_MODELVIEW_STACK_DEPTH', 'GL_LINE_SMOOTH_HINT', 'GL_FRONT', 'GL_SCISSOR_BOX', 'GL_AMBIENT', 'GL_BUFFER_USAGE', 'GL_CULL_FACE_MODE', 'GL_NORMAL_ARRAY_BUFFER_BINDING', 'GL_ALPHA', 'GL_SET', 'GL_COLOR_WRITEMASK', 'GL_DST_COLOR', 'GL_OPERAND0_ALPHA', 'GL_ALWAYS', 'GL_TEXTURE_WRAP_S', 'GL_TEXTURE_WRAP_T', 'GL_DST_ALPHA', 'GL_INVALID_OPERATION', 'GL_PERSPECTIVE_CORRECTION_HINT', 'GL_SCISSOR_TEST', 'GL_FOG_START', 'GL_PROJECTION_STACK_DEPTH', 'GL_TRUE', 'GL_TEXTURE_MIN_FILTER', 'GL_COLOR_ARRAY_TYPE', 'GL_BLUE_BITS', 'GL_STACK_UNDERFLOW', 'GL_MODULATE', 'GL_EQUAL', 'GL_ADD', 'GL_INTERPOLATE', 'GL_MODELVIEW_STACK_DEPTH', 'GL_POINT_FADE_THRESHOLD_SIZE', 'GL_UNPACK_ALIGNMENT', 'GL_COMBINE_RGB', 'GL_LINE_STRIP', 'GL_COLOR_MATERIAL', 'GL_CLIP_PLANE1', 'GL_CLIP_PLANE0', 'GL_CLIP_PLANE3', 'GL_CLIP_PLANE2', 'GL_CLIP_PLANE5', 'GL_POINT_SMOOTH_HINT', 'GL_NORMAL_ARRAY_TYPE', 'GL_POINTS', 'GL_FASTEST', 'GL_TEXTURE_2D', 'GL_NAND', 'GL_OR', 'GL_TEXTURE_COORD_ARRAY_TYPE', 'GL_TEXTURE23', 'GL_TEXTURE22', 'GL_TEXTURE21', 'GL_TEXTURE20', 'GL_TEXTURE27', 'GL_TEXTURE26', 'GL_TEXTURE25', 'GL_TEXTURE24', 'GL_TEXTURE29', 'GL_TEXTURE28', 'GL_ADD_SIGNED', 'GL_ELEMENT_ARRAY_BUFFER_BINDING', 'GL_LINE_LOOP', 'GL_ALPHA_SCALE', 'GL_TEXTURE_COORD_ARRAY_SIZE', 'GL_SUBPIXEL_BITS', 'GL_CURRENT_NORMAL', 'GL_GEQUAL', 'GL_ALPHA_TEST', 'GL_LINE_WIDTH', 'GL_LEQUAL', 'GL_SUBTRACT', 'GL_LIGHT_MODEL_AMBIENT', 'GL_DEPTH_CLEAR_VALUE', 'GL_DOT3_RGBA', 'GL_ARRAY_BUFFER_BINDING', 'GL_POLYGON_OFFSET_UNITS', 'GL_VERTEX_ARRAY_STRIDE', 'GL_PRIMARY_COLOR', 'GL_DYNAMIC_DRAW', 'GL_OUT_OF_MEMORY', 'GL_NICEST', 'GL_NORMAL_ARRAY_STRIDE', 'GL_POINT_SIZE_ARRAY_TYPE_OES', 'GL_SMOOTH', 'GL_CURRENT_TEXTURE_COORDS', 'GL_PALETTE8_RGB5_A1_OES', 'GL_PALETTE8_RGBA8_OES', 'GL_SPECULAR', 'GL_STENCIL_TEST', 'GL_GENERATE_MIPMAP', 'GL_LUMINANCE_ALPHA', 'GL_INVERT', 'GL_COLOR_ARRAY_SIZE', 'GL_POLYGON_OFFSET_FACTOR', 'GL_STENCIL_REF', 'GL_TRIANGLE_FAN', 'GL_CURRENT_COLOR', 'GL_MODELVIEW', 'GL_TRIANGLES', 'GL_RED_BITS', 'GL_NOR', 'GL_FOG', 'GL_FLAT', 'GL_PACK_ALIGNMENT', 'GL_POSITION', 'GL_RENDERER', 'GL_ACTIVE_TEXTURE', 'GL_PALETTE4_RGB8_OES', 'GL_SMOOTH_LINE_WIDTH_RANGE', 'GL_COLOR_LOGIC_OP', 'GL_PROJECTION', 'GL_DEPTH_FUNC', 'GL_STENCIL_FAIL', 'GL_CONSTANT', 'GL_RGB_SCALE', 'GL_XOR', 'GL_INVALID_ENUM', 'GL_LESS', 'GL_EMISSION', 'GL_TEXTURE_ENV_MODE', 'GL_EQUIV', 'GL_FOG_COLOR', 'GL_VERSION_ES_CL_1_0', 'GL_VERSION_ES_CL_1_1', 'GL_SRC_ALPHA_SATURATE', 'GL_REPEAT', 'GL_RESCALE_NORMAL', 'GL_VERTEX_ARRAY_SIZE', 'GL_PREVIOUS', 'GL_SPOT_DIRECTION', 'GL_PALETTE4_RGBA8_OES', 'GL_STENCIL_BUFFER_BIT', 'GL_DIFFUSE', 'GL_SRC1_RGB', 'GL_LIGHTING', 'GL_STENCIL_PASS_DEPTH_PASS', 'GL_LIGHT_MODEL_TWO_SIDE', 'GL_VERTEX_ARRAY_POINTER', 'GL_SAMPLE_COVERAGE_INVERT', 'GL_LINES', 'GL_TEXTURE18', 'GL_TEXTURE19', 'GL_TEXTURE16', 'GL_TEXTURE17', 'GL_TEXTURE14', 'GL_GENERATE_MIPMAP_HINT', 'GL_ALPHA_TEST_REF', 'GL_TEXTURE13', 'GL_TEXTURE10', 'GL_TEXTURE11', 'GL_POINT_SIZE_ARRAY_STRIDE_OES', 'GL_RGB', 'GL_EXP2', 'GL_COPY_INVERTED', 'GL_STACK_OVERFLOW', 'GL_FOG_HINT', 'GL_PALETTE4_RGB5_A1_OES', 'GL_PROJECTION_MATRIX', 'GL_COLOR_ARRAY_BUFFER_BINDING', 'GL_LINEAR_MIPMAP_NEAREST', 'GL_POINT_DISTANCE_ATTENUATION', 'GL_AMBIENT_AND_DIFFUSE', 'GL_VERSION', 'GL_ZERO', 'GL_COLOR_ARRAY_STRIDE', 'GL_SRC_ALPHA', 'GL_FIXED', 'GL_POINT_SIZE_ARRAY_POINTER_OES', 'GL_NOTEQUAL', 'GL_TEXTURE_COORD_ARRAY', 'GL_INCR', 'GL_CULL_FACE', 'GL_SAMPLE_COVERAGE_VALUE', 'GL_MAX_LIGHTS', 'GL_OES_read_format', 'GL_MAX_VIEWPORT_DIMS', 'GL_OES_point_sprite', 'GL_OPERAND1_ALPHA', 'GL_NORMALIZE', 'GL_NEVER', 'GL_TEXTURE15', 'GL_STENCIL_VALUE_MASK', 'GL_BLEND_DST', 'GL_TEXTURE12', 'GL_LOGIC_OP_MODE', 'GL_SPOT_EXPONENT', 'GL_RGBA', 'GL_SHORT', 'GL_CW', 'GL_NORMAL_ARRAY', 'GL_UNSIGNED_BYTE', 'GL_VENDOR', 'GL_TEXTURE_BINDING_2D', 'GL_STATIC_DRAW', 'GL_COMBINE', 'GL_LUMINANCE', 'GL_DEPTH_BITS', 'GL_OR_INVERTED', 'GL_COPY', 'GL_TEXTURE_MATRIX', 'GL_CLEAR', 'GL_LIGHT7', 'GL_MATRIX_MODE', 'GL_DECAL', 'GL_SAMPLE_COVERAGE', 'GL_SHININESS', 'GL_SAMPLES', 'GLchar', 'GLenum', 'GLboolean', 'GLbitfield', 'GLbyte', 'GLshort', 'GLint', 'GLint64', 'GLsizei', 'GLubyte', 'GLushort', 'GLuint', 'GLfloat', 'GLclampf', 'GLfixed', 'GLintptr', 'GLsizeiptr', 'GLclampx', 'void', 'GLvoid', 'GLsync']