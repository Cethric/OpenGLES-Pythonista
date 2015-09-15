# Generated Files. DO NOT EDIT
# Generated on: 09/16/15 08:54:00
import ctypes
from objc_util import *
from GLConstants import *

DEBUG = 1
loaded = [0, 0]

# GLES Constants
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x00008214
GL_UNSIGNED_INT_VEC2 = 0x00008dc6
GL_UNSIGNED_INT_VEC3 = 0x00008dc7
GL_UNSIGNED_INT_VEC4 = 0x00008dc8
GL_UNSIGNED_SHORT_5_6_5 = 0x00008363
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x00008623
GL_DEPTH_ATTACHMENT = 0x00008d00
GL_DITHER = 0x00000bd0
GL_TRANSFORM_FEEDBACK_PAUSED = 0x00008e23
GL_RGB16UI = 0x00008d77
__gl3_h_ = 0x00000001
GL_QUERY_RESULT = 0x00008866
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x00008217
GL_FLOAT_VEC2 = 0x00008b50
GL_FLOAT_VEC3 = 0x00008b51
GL_FLOAT_VEC4 = 0x00008b52
GL_FLOAT = 0x00001406
GL_INT_2_10_10_10_REV = 0x00008d9f
GL_RGB32UI = 0x00008d71
GL_TEXTURE_MAX_LOD = 0x0000813b
GL_BUFFER_MAP_OFFSET = 0x00009121
GL_BUFFER_SIZE = 0x00008764
GL_RGB9_E5 = 0x00008c3d
GL_UNIFORM_BUFFER_START = 0x00008a29
GL_COMPRESSED_R11_EAC = 0x00009270
GL_RGBA32UI = 0x00008d70
GL_UNSIGNED_INT_SAMPLER_2D = 0x00008dd2
GL_TEXTURE_MIN_LOD = 0x0000813a
GL_TEXTURE8 = 0x000084c8
GL_TEXTURE9 = 0x000084c9
GL_TEXTURE4 = 0x000084c4
GL_TEXTURE5 = 0x000084c5
GL_TEXTURE6 = 0x000084c6
GL_TEXTURE7 = 0x000084c7
GL_TEXTURE0 = 0x000084c0
GL_LINEAR_MIPMAP_LINEAR = 0x00002703
GL_TEXTURE2 = 0x000084c2
GL_TEXTURE3 = 0x000084c3
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x00008517
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x00008515
GL_BLEND_EQUATION = 0x00008009
GL_BYTE = 0x00001400
GL_BOOL_VEC3 = 0x00008b58
GL_BOOL_VEC2 = 0x00008b57
GL_TIMEOUT_IGNORED = 0xffffffffffffffff
GL_MAX_VARYING_VECTORS = 0x00008dfc
GL_RENDERBUFFER_SAMPLES = 0x00008cab
GL_ONE = 0x00000001
GL_RG = 0x00008227
GL_COLOR_CLEAR_VALUE = 0x00000c22
GL_MAX_SAMPLES = 0x00008d57
GL_BUFFER_USAGE = 0x00008765
GL_UNPACK_IMAGE_HEIGHT = 0x0000806e
GL_FLOAT_MAT3x2 = 0x00008b67
GL_TRIANGLE_STRIP = 0x00000005
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x00008257
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x00008c8f
GL_FLOAT_MAT3x4 = 0x00008b68
GL_COLOR_ATTACHMENT28 = 0x00008cfc
GL_COLOR_ATTACHMENT29 = 0x00008cfd
GL_COLOR_ATTACHMENT24 = 0x00008cf8
GL_COLOR_ATTACHMENT25 = 0x00008cf9
GL_COLOR_ATTACHMENT26 = 0x00008cfa
GL_COLOR_ATTACHMENT27 = 0x00008cfb
GL_COLOR_ATTACHMENT20 = 0x00008cf4
GL_COLOR_ATTACHMENT21 = 0x00008cf5
GL_COLOR_ATTACHMENT22 = 0x00008cf6
GL_COLOR_ATTACHMENT23 = 0x00008cf7
GL_TRANSFORM_FEEDBACK_BUFFER = 0x00008c8e
GL_BLUE = 0x00001905
GL_VERTEX_ARRAY_BINDING = 0x000085b5
GL_UNSIGNED_SHORT_5_5_5_1 = 0x00008034
GL_TIMEOUT_EXPIRED = 0x0000911b
GL_COMPRESSED_RGB8_ETC2 = 0x00009274
GL_SIGNED_NORMALIZED = 0x00008f9c
GL_STENCIL_FUNC = 0x00000b92
GL_MAX_TEXTURE_LOD_BIAS = 0x000084fd
GL_ALIASED_LINE_WIDTH_RANGE = 0x0000846e
GL_DECR = 0x00001e03
GL_BACK = 0x00000405
GL_ES_VERSION_3_0 = 0x00000001
GL_TEXTURE_COMPARE_FUNC = 0x0000884d
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 0x00008c7f
GL_INT = 0x00001404
GL_COMPRESSED_SIGNED_RG11_EAC = 0x00009273
GL_POLYGON_OFFSET_FILL = 0x00008037
GL_MINOR_VERSION = 0x0000821c
GL_FRONT_AND_BACK = 0x00000408
GL_R8 = 0x00008229
GL_RGB_INTEGER = 0x00008d98
GL_STENCIL = 0x00001802
GL_SRGB = 0x00008c40
GL_GREEN_BITS = 0x00000d53
GL_SYNC_FENCE = 0x00009116
GL_ONE_MINUS_CONSTANT_COLOR = 0x00008002
GL_SHADING_LANGUAGE_VERSION = 0x00008b8c
GL_RGB8_SNORM = 0x00008f96
GL_UNPACK_SKIP_PIXELS = 0x00000cf4
GL_TEXTURE_IMMUTABLE_LEVELS = 0x000082df
GL_FRAGMENT_SHADER = 0x00008b30
GL_UNSIGNED_INT_2_10_10_10_REV = 0x00008368
GL_UNSIGNED_SHORT_4_4_4_4 = 0x00008033
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x00008c8b
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x00008b8b
GL_NO_ERROR = 0x00000000
GL_VIEWPORT = 0x00000ba2
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x00008cd1
GL_BLEND_SRC_ALPHA = 0x000080cb
GL_DRAW_BUFFER6 = 0x0000882b
GL_DRAW_BUFFER7 = 0x0000882c
GL_DRAW_BUFFER4 = 0x00008829
GL_DRAW_BUFFER5 = 0x0000882a
GL_DRAW_BUFFER2 = 0x00008827
GL_DRAW_BUFFER3 = 0x00008828
GL_DRAW_BUFFER0 = 0x00008825
GL_DRAW_BUFFER1 = 0x00008826
GL_UNIFORM_TYPE = 0x00008a37
GL_QUERY_RESULT_AVAILABLE = 0x00008867
GL_DRAW_BUFFER8 = 0x0000882d
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x00008cd7
GL_MAX_DRAW_BUFFERS = 0x00008824
GL_KEEP = 0x00001e00
GL_DELETE_STATUS = 0x00008b80
GL_R32UI = 0x00008236
GL_RGBA8_SNORM = 0x00008f97
GL_INT_SAMPLER_3D = 0x00008dcb
GL_SRC_COLOR = 0x00000300
GL_SAMPLER_BINDING = 0x00008919
GL_DEPTH24_STENCIL8 = 0x000088f0
GL_SAMPLE_BUFFERS = 0x000080a8
GL_MAJOR_VERSION = 0x0000821b
GL_STATIC_COPY = 0x000088e6
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x00008b8a
GL_EXTENSIONS = 0x00001f03
GL_UNIFORM_BUFFER_BINDING = 0x00008a28
GL_RGBA16UI = 0x00008d76
GL_COPY_READ_BUFFER_BINDING = 0x00008f36
GL_TEXTURE_COMPARE_MODE = 0x0000884c
GL_ANY_SAMPLES_PASSED = 0x00008c2f
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x00008215
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x00008802
GL_UNIFORM_BUFFER = 0x00008a11
GL_MAP_WRITE_BIT = 0x00000002
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x00008645
GL_ALIASED_POINT_SIZE_RANGE = 0x0000846d
GL_CCW = 0x00000901
GL_MAP_INVALIDATE_BUFFER_BIT = 0x00000008
GL_DEPTH_COMPONENT24 = 0x000081a6
GL_UNSIGNED_INT_5_9_9_9_REV = 0x00008c3e
GL_DEPTH_TEST = 0x00000b71
GL_SYNC_GPU_COMMANDS_COMPLETE = 0x00009117
GL_VERTEX_ATTRIB_ARRAY_INTEGER = 0x000088fd
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 0x00008a2d
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x00008216
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x00008b87
GL_STREAM_READ = 0x000088e1
GL_LINEAR = 0x00002601
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x00008c88
GL_FUNC_SUBTRACT = 0x0000800a
GL_R32F = 0x0000822e
GL_MAX_VARYING_COMPONENTS = 0x00008b4b
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x00008a35
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x00008b9b
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x00008210
GL_HALF_FLOAT = 0x0000140b
GL_COLOR_ATTACHMENT15 = 0x00008cef
GL_COLOR_ATTACHMENT14 = 0x00008cee
GL_HIGH_FLOAT = 0x00008df2
GL_DEPTH_RANGE = 0x00000b70
GL_GREATER = 0x00000204
GL_CLAMP_TO_EDGE = 0x0000812f
GL_COLOR_ATTACHMENT13 = 0x00008ced
GL_COLOR_ATTACHMENT12 = 0x00008cec
GL_NEAREST = 0x00002600
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x00008622
GL_COLOR_ATTACHMENT19 = 0x00008cf3
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x00008cd4
GL_MAX_TEXTURE_IMAGE_UNITS = 0x00008872
GL_RGB32F = 0x00008815
GL_FLOAT_MAT2 = 0x00008b5a
GL_FLOAT_MAT3 = 0x00008b5b
GL_FRONT_FACE = 0x00000b46
GL_DEPTH = 0x00001801
GL_FLOAT_MAT4 = 0x00008b5c
GL_RENDERBUFFER_GREEN_SIZE = 0x00008d51
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x00008212
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x00008cd6
GL_TEXTURE30 = 0x000084de
GL_TEXTURE31 = 0x000084df
GL_RG8I = 0x00008237
GL_RGBA8I = 0x00008d8e
GL_RG8UI = 0x00008238
GL_DEPTH_CLEAR_VALUE = 0x00000b73
GL_BUFFER_MAP_POINTER = 0x000088bd
GL_RENDERBUFFER_BINDING = 0x00008ca7
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x00008cd0
GL_STENCIL_REF = 0x00000b97
GL_MAX_3D_TEXTURE_SIZE = 0x00008073
GL_R16UI = 0x00008234
GL_COPY_WRITE_BUFFER_BINDING = 0x00008f37
GL_COPY_WRITE_BUFFER = 0x00008f37
GL_BLEND = 0x00000be2
GL_MIRRORED_REPEAT = 0x00008370
GL_SAMPLER_CUBE_SHADOW = 0x00008dc5
GL_TEXTURE_BINDING_3D = 0x0000806a
GL_UNSIGNED_SHORT = 0x00001403
GL_MIN = 0x00008007
GL_ONE_MINUS_DST_COLOR = 0x00000307
GL_ONE_MINUS_SRC_COLOR = 0x00000301
GL_TEXTURE = 0x00001702
GL_COLOR_BUFFER_BIT = 0x00004000
GL_DONT_CARE = 0x00001100
GL_ACTIVE_UNIFORMS = 0x00008b86
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x00009277
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x00008dfb
GL_TEXTURE_BINDING_CUBE_MAP = 0x00008514
GL_SAMPLER_2D = 0x00008b5e
GL_INVALID_VALUE = 0x00000501
GL_NEAREST_MIPMAP_NEAREST = 0x00002700
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x000086a2
GL_PACK_SKIP_ROWS = 0x00000d03
GL_TEXTURE_MAG_FILTER = 0x00002800
GL_R8I = 0x00008231
GL_TEXTURE1 = 0x000084c1
GL_BLEND_EQUATION_RGB = 0x00008009
GL_LINK_STATUS = 0x00008b82
GL_TEXTURE_MAX_LEVEL = 0x0000813d
GL_R32I = 0x00008235
GL_BLEND_COLOR = 0x00008005
GL_ALPHA_BITS = 0x00000d55
GL_BOOL_VEC4 = 0x00008b59
GL_ONE_MINUS_CONSTANT_ALPHA = 0x00008004
GL_NEAREST_MIPMAP_LINEAR = 0x00002702
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x00008519
GL_WAIT_FAILED = 0x0000911d
GL_UNIFORM_BLOCK_NAME_LENGTH = 0x00008a41
GL_MAX_TEXTURE_SIZE = 0x00000d33
GL_RG32F = 0x00008230
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x00008dd7
GL_ARRAY_BUFFER = 0x00008892
GL_DEPTH_COMPONENT16 = 0x000081a5
GL_UNSIGNALED = 0x00009118
GL_RGB32I = 0x00008d83
GL_BLEND_SRC_RGB = 0x000080c9
GL_FRAMEBUFFER_UNDEFINED = 0x00008219
GL_SYNC_FLAGS = 0x00009115
GL_FALSE = 0x00000000
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x00008a31
GL_ONE_MINUS_SRC_ALPHA = 0x00000303
GL_RG32I = 0x0000823b
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x00008d44
GL_NUM_SHADER_BINARY_FORMATS = 0x00008df9
GL_RGBA16I = 0x00008d88
GL_RGBA16F = 0x0000881a
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x0000809e
GL_INT_SAMPLER_2D = 0x00008dca
GL_STENCIL_BITS = 0x00000d57
GL_STENCIL_PASS_DEPTH_FAIL = 0x00000b95
GL_RED = 0x00001903
GL_MAX_ELEMENT_INDEX = 0x00008d6b
GL_MAX_VERTEX_UNIFORM_BLOCKS = 0x00008a2b
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x00008cd9
GL_RGBA8UI = 0x00008d7c
GL_GREEN = 0x00001904
GL_INVALID_OPERATION = 0x00000502
GL_RED_INTEGER = 0x00008d94
GL_NONE = 0x00000000
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x00008803
GL_COLOR_ATTACHMENT5 = 0x00008ce5
GL_FUNC_REVERSE_SUBTRACT = 0x0000800b
GL_COLOR_ATTACHMENT7 = 0x00008ce7
GL_COLOR_ATTACHMENT6 = 0x00008ce6
GL_COLOR_ATTACHMENT1 = 0x00008ce1
GL_COLOR_ATTACHMENT0 = 0x00008ce0
GL_COLOR_ATTACHMENT3 = 0x00008ce3
GL_COLOR_ATTACHMENT2 = 0x00008ce2
GL_UNIFORM_BLOCK_INDEX = 0x00008a3a
GL_FRAMEBUFFER_DEFAULT = 0x00008218
GL_COLOR_ATTACHMENT9 = 0x00008ce9
GL_COLOR_ATTACHMENT8 = 0x00008ce8
GL_COLOR_ATTACHMENT10 = 0x00008cea
GL_FRONT = 0x00000404
GL_SCISSOR_BOX = 0x00000c10
GL_UNIFORM_BLOCK_DATA_SIZE = 0x00008a40
GL_LEQUAL = 0x00000203
GL_CULL_FACE_MODE = 0x00000b45
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x00008dfd
GL_NUM_EXTENSIONS = 0x0000821d
GL_UNIFORM_IS_ROW_MAJOR = 0x00008a3e
GL_MAX_UNIFORM_BLOCK_SIZE = 0x00008a30
GL_BOOL = 0x00008b56
GL_MAX_COMBINED_UNIFORM_BLOCKS = 0x00008a2e
GL_FRAMEBUFFER_BINDING = 0x00008ca6
GL_UNSIGNED_INT_24_8 = 0x000084fa
GL_COMPRESSED_TEXTURE_FORMATS = 0x000086a3
GL_ALPHA = 0x00001906
GL_COLOR_WRITEMASK = 0x00000c23
GL_DST_COLOR = 0x00000306
GL_UNSIGNED_INT = 0x00001405
GL_DEPTH_FUNC = 0x00000b74
GL_ALWAYS = 0x00000207
GL_TEXTURE_WRAP_S = 0x00002802
GL_TEXTURE_WRAP_T = 0x00002803
GL_INVALID_ENUM = 0x00000500
GL_PROGRAM_BINARY_LENGTH = 0x00008741
GL_STENCIL_BACK_VALUE_MASK = 0x00008ca4
GL_INT_SAMPLER_2D_ARRAY = 0x00008dcf
GL_COLOR_ATTACHMENT11 = 0x00008ceb
GL_DEPTH_COMPONENT = 0x00001902
GL_SCISSOR_TEST = 0x00000c11
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x00008a43
GL_SHADER_TYPE = 0x00008b4f
GL_COMPARE_REF_TO_TEXTURE = 0x0000884e
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x00008d56
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x00008211
GL_TRUE = 0x00000001
GL_TEXTURE_MIN_FILTER = 0x00002801
GL_REPLACE = 0x00001e01
GL_BLUE_BITS = 0x00000d54
GL_RG_INTEGER = 0x00008228
GL_TEXTURE_SWIZZLE_R = 0x00008e42
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x00008624
GL_EQUAL = 0x00000202
GL_TEXTURE_SWIZZLE_G = 0x00008e43
GL_DEPTH_STENCIL_ATTACHMENT = 0x0000821a
GL_RENDERBUFFER_HEIGHT = 0x00008d43
GL_RG16UI = 0x0000823a
GL_DRAW_BUFFER12 = 0x00008831
GL_TEXTURE_SWIZZLE_A = 0x00008e45
GL_LOW_FLOAT = 0x00008df0
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x00008b49
GL_FLOAT_MAT4x3 = 0x00008b6a
GL_DRAW_BUFFER15 = 0x00008834
GL_DYNAMIC_COPY = 0x000088ea
GL_STENCIL_BACK_REF = 0x00008ca3
GL_UNPACK_ALIGNMENT = 0x00000cf5
GL_ALREADY_SIGNALED = 0x0000911a
GL_LINE_STRIP = 0x00000003
GL_STREAM_COPY = 0x000088e2
GL_PACK_ROW_LENGTH = 0x00000d02
GL_NUM_SAMPLE_COUNTS = 0x00009380
GL_MEDIUM_INT = 0x00008df4
GL_TEXTURE_CUBE_MAP = 0x00008513
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x00008a42
GL_COLOR = 0x00001800
GL_RENDERBUFFER_DEPTH_SIZE = 0x00008d54
GL_DYNAMIC_READ = 0x000088e9
GL_PROGRAM_BINARY_FORMATS = 0x000087ff
GL_LOW_INT = 0x00008df3
GL_DEPTH_STENCIL = 0x000084f9
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x000088fe
GL_MAX_VERTEX_OUTPUT_COMPONENTS = 0x00009122
GL_POINTS = 0x00000000
GL_COMPRESSED_RG11_EAC = 0x00009272
GL_RENDERBUFFER_BLUE_SIZE = 0x00008d52
GL_UNIFORM_NAME_LENGTH = 0x00008a39
GL_FASTEST = 0x00001101
GL_SYNC_CONDITION = 0x00009113
GL_TEXTURE_2D = 0x00000de1
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x00008c80
GL_MAP_INVALIDATE_RANGE_BIT = 0x00000004
GL_TEXTURE23 = 0x000084d7
GL_TEXTURE22 = 0x000084d6
GL_TEXTURE21 = 0x000084d5
GL_TEXTURE20 = 0x000084d4
GL_TEXTURE27 = 0x000084db
GL_TEXTURE26 = 0x000084da
GL_TEXTURE25 = 0x000084d9
GL_TEXTURE24 = 0x000084d8
GL_R8_SNORM = 0x00008f94
GL_TEXTURE29 = 0x000084dd
GL_TEXTURE28 = 0x000084dc
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x00008895
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x00008518
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x00008516
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x0000851a
GL_LINE_LOOP = 0x00000002
GL_READ_BUFFER = 0x00000c02
GL_MAP_FLUSH_EXPLICIT_BIT = 0x00000010
GL_PACK_SKIP_PIXELS = 0x00000d04
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x00008a33
GL_SUBPIXEL_BITS = 0x00000d50
GL_SRGB8 = 0x00008c41
GL_GEQUAL = 0x00000206
GL_UNIFORM_BLOCK_BINDING = 0x00008a3f
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x00008a34
GL_LINE_WIDTH = 0x00000b21
GL_UNIFORM_OFFSET = 0x00008a3b
GL_R16F = 0x0000822d
GL_REPEAT = 0x00002901
GL_TRANSFORM_FEEDBACK = 0x00008e22
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x00009279
GL_UNSIGNED_INT_SAMPLER_CUBE = 0x00008dd4
GL_COLOR_ATTACHMENT4 = 0x00008ce4
GL_UNIFORM_SIZE = 0x00008a38
GL_FUNC_ADD = 0x00008006
GL_FLOAT_MAT4x2 = 0x00008b69
GL_SHADER_SOURCE_LENGTH = 0x00008b88
GL_CURRENT_VERTEX_ATTRIB = 0x00008626
GL_ARRAY_BUFFER_BINDING = 0x00008894
GL_POLYGON_OFFSET_UNITS = 0x00002a00
GL_DYNAMIC_DRAW = 0x000088e8
GL_OUT_OF_MEMORY = 0x00000505
GL_NICEST = 0x00001102
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x00008b9a
GL_UNPACK_ROW_LENGTH = 0x00000cf2
GL_CURRENT_PROGRAM = 0x00008b8d
GL_BUFFER_MAPPED = 0x000088bc
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x00008c8a
GL_RASTERIZER_DISCARD = 0x00008c89
GL_NUM_PROGRAM_BINARY_FORMATS = 0x000087fe
GL_STREAM_DRAW = 0x000088e0
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x00008a44
GL_MAX_UNIFORM_BUFFER_BINDINGS = 0x00008a2f
GL_SIGNALED = 0x00009119
GL_FRAMEBUFFER = 0x00008d40
GL_MEDIUM_FLOAT = 0x00008df1
GL_STENCIL_TEST = 0x00000b90
GL_R11F_G11F_B10F = 0x00008c3a
GL_LUMINANCE_ALPHA = 0x0000190a
GL_PIXEL_UNPACK_BUFFER_BINDING = 0x000088ef
GL_INVERT = 0x0000150a
GL_STENCIL_BACK_FAIL = 0x00008801
GL_POLYGON_OFFSET_FACTOR = 0x00008038
GL_TRANSFORM_FEEDBACK_VARYINGS = 0x00008c83
GL_DEPTH_COMPONENT32F = 0x00008cac
GL_TRIANGLE_FAN = 0x00000006
GL_SYNC_FLUSH_COMMANDS_BIT = 0x00000001
GL_ONE_MINUS_DST_ALPHA = 0x00000305
GL_DRAW_FRAMEBUFFER_BINDING = 0x00008ca6
GL_MAX_ELEMENTS_VERTICES = 0x000080e8
GL_STENCIL_BACK_WRITEMASK = 0x00008ca5
GL_INVALID_FRAMEBUFFER_OPERATION = 0x00000506
GL_BUFFER_ACCESS_FLAGS = 0x0000911f
GL_COMPRESSED_RGBA8_ETC2_EAC = 0x00009278
GL_UNIFORM_BUFFER_SIZE = 0x00008a2a
GL_TRIANGLES = 0x00000004
GL_SAMPLER_2D_ARRAY_SHADOW = 0x00008dc4
GL_DEPTH32F_STENCIL8 = 0x00008cad
GL_MAX_ARRAY_TEXTURE_LAYERS = 0x000088ff
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x0000889f
GL_UNIFORM_MATRIX_STRIDE = 0x00008a3d
GL_MAX_SERVER_WAIT_TIMEOUT = 0x00009111
GL_SRGB8_ALPHA8 = 0x00008c43
GL_PACK_ALIGNMENT = 0x00000d05
GL_SAMPLER_2D_ARRAY = 0x00008dc1
GL_RENDERER = 0x00001f01
GL_MAX_COLOR_ATTACHMENTS = 0x00008cdf
GL_ACTIVE_UNIFORM_BLOCKS = 0x00008a36
GL_UNPACK_SKIP_IMAGES = 0x0000806d
GL_STENCIL_BACK_FUNC = 0x00008800
GL_RGB16I = 0x00008d89
GL_ACTIVE_TEXTURE = 0x000084e0
GL_TEXTURE_BASE_LEVEL = 0x0000813c
GL_INTERLEAVED_ATTRIBS = 0x00008c8c
GL_RGB16F = 0x0000881b
GL_COMPRESSED_SIGNED_R11_EAC = 0x00009271
GL_UNSIGNED_INT_SAMPLER_3D = 0x00008dd3
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x00008c76
GL_TEXTURE_WRAP_R = 0x00008072
GL_INT_VEC4 = 0x00008b55
GL_INT_VEC3 = 0x00008b54
GL_INT_VEC2 = 0x00008b53
GL_STENCIL_FAIL = 0x00000b94
GL_MAX_VERTEX_ATTRIBS = 0x00008869
GL_CONDITION_SATISFIED = 0x0000911c
GL_TEXTURE_IMMUTABLE_FORMAT = 0x0000912f
GL_FRAMEBUFFER_UNSUPPORTED = 0x00008cdd
GL_DST_ALPHA = 0x00000304
GL_LESS = 0x00000201
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x0000851c
GL_RGB565 = 0x00008d62
GL_TRANSFORM_FEEDBACK_BINDING = 0x00008e25
GL_RENDERBUFFER_WIDTH = 0x00008d42
GL_READ_FRAMEBUFFER_BINDING = 0x00008caa
GL_RGBA4 = 0x00008056
GL_DRAW_BUFFER10 = 0x0000882f
GL_DRAW_BUFFER11 = 0x00008830
GL_RGBA8 = 0x00008058
GL_DRAW_BUFFER13 = 0x00008832
GL_DRAW_BUFFER14 = 0x00008833
GL_LUMINANCE = 0x00001909
GL_INFO_LOG_LENGTH = 0x00008b84
GL_DEPTH_WRITEMASK = 0x00000b72
GL_PRIMITIVE_RESTART_FIXED_INDEX = 0x00008d69
GL_SRC_ALPHA_SATURATE = 0x00000308
GL_RENDERBUFFER_STENCIL_SIZE = 0x00008d55
GL_CONSTANT_ALPHA = 0x00008003
GL_R16I = 0x00008233
GL_RG8_SNORM = 0x00008f95
GL_PIXEL_PACK_BUFFER = 0x000088eb
GL_STATIC_READ = 0x000088e5
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x00009276
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x00008a46
GL_VALIDATE_STATUS = 0x00008b83
GL_MAP_READ_BIT = 0x00000001
GL_STENCIL_CLEAR_VALUE = 0x00000b91
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_TEXTURE_SWIZZLE_B = 0x00008e44
GL_COLOR_ATTACHMENT17 = 0x00008cf1
GL_BLEND_EQUATION_ALPHA = 0x0000883d
GL_RGBA_INTEGER = 0x00008d99
GL_ACTIVE_ATTRIBUTES = 0x00008b89
GL_MAX_RENDERBUFFER_SIZE = 0x000084e8
GL_COLOR_ATTACHMENT31 = 0x00008cff
GL_COLOR_ATTACHMENT30 = 0x00008cfe
GL_STENCIL_PASS_DEPTH_PASS = 0x00000b96
GL_INCR_WRAP = 0x00008507
GL_RENDERBUFFER_ALPHA_SIZE = 0x00008d53
GL_HIGH_INT = 0x00008df5
GL_COLOR_ATTACHMENT16 = 0x00008cf0
GL_DECR_WRAP = 0x00008508
GL_ATTACHED_SHADERS = 0x00008b85
GL_MAX_FRAGMENT_INPUT_COMPONENTS = 0x00009125
GL_SAMPLE_COVERAGE_INVERT = 0x000080ab
GL_LINES = 0x00000001
GL_TEXTURE18 = 0x000084d2
GL_TEXTURE19 = 0x000084d3
GL_TEXTURE16 = 0x000084d0
GL_TEXTURE17 = 0x000084d1
GL_TEXTURE14 = 0x000084ce
GL_GENERATE_MIPMAP_HINT = 0x00008192
GL_TEXTURE12 = 0x000084cc
GL_TEXTURE13 = 0x000084cd
GL_TEXTURE10 = 0x000084ca
GL_UNPACK_SKIP_ROWS = 0x00000cf3
GL_BLEND_DST_ALPHA = 0x000080ca
GL_RGB = 0x00001907
GL_INT_SAMPLER_CUBE = 0x00008dcc
GL_CURRENT_QUERY = 0x00008865
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x0000886a
GL_RGB5_A1 = 0x00008057
GL_VERTEX_SHADER = 0x00008b31
GL_TRANSFORM_FEEDBACK_BUFFER_START = 0x00008c84
GL_MAX_PROGRAM_TEXEL_OFFSET = 0x00008905
GL_SHADER_BINARY_FORMATS = 0x00008df8
GL_CONSTANT_COLOR = 0x00008001
GL_RGBA32F = 0x00008814
GL_RGBA32I = 0x00008d82
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x00008625
GL_PIXEL_UNPACK_BUFFER = 0x000088ec
GL_LINEAR_MIPMAP_NEAREST = 0x00002701
GL_STENCIL_WRITEMASK = 0x00000b98
GL_RG8 = 0x0000822b
GL_RGB10_A2 = 0x00008059
GL_ES_VERSION_2_0 = 0x00000001
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x00008cd3
GL_VERSION = 0x00001f02
GL_MAP_UNSYNCHRONIZED_BIT = 0x00000020
GL_ZERO = 0x00000000
GL_ELEMENT_ARRAY_BUFFER = 0x00008893
GL_SYNC_STATUS = 0x00009114
GL_BUFFER_MAP_LENGTH = 0x00009120
GL_MAX_ELEMENTS_INDICES = 0x000080e9
GL_UNSIGNED_NORMALIZED = 0x00008c17
GL_SRC_ALPHA = 0x00000302
GL_TEXTURE_3D = 0x0000806f
GL_FIXED = 0x0000140c
GL_RGB8 = 0x00008051
GL_NOTEQUAL = 0x00000205
GL_UNIFORM_ARRAY_STRIDE = 0x00008a3c
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 0x00008dad
GL_INCR = 0x00001e02
GL_CULL_FACE = 0x00000b44
GL_SAMPLE_COVERAGE_VALUE = 0x000080aa
GL_RENDERBUFFER_RED_SIZE = 0x00008d50
GL_MAX_VIEWPORT_DIMS = 0x00000d3a
GL_RG32UI = 0x0000823c
GL_NEVER = 0x00000200
GL_TEXTURE15 = 0x000084cf
GL_STENCIL_VALUE_MASK = 0x00000b93
GL_DRAW_BUFFER9 = 0x0000882e
GL_COMPILE_STATUS = 0x00008b81
GL_FRAMEBUFFER_COMPLETE = 0x00008cd5
GL_TEXTURE11 = 0x000084cb
GL_COPY_READ_BUFFER = 0x00008f36
GL_SHADER_COMPILER = 0x00008dfa
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x00008b4d
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x00008b4c
GL_RGBA = 0x00001908
GL_SHORT = 0x00001402
GL_READ_FRAMEBUFFER = 0x00008ca8
GL_CW = 0x00000900
GL_MIN_PROGRAM_TEXEL_OFFSET = 0x00008904
GL_UNSIGNED_BYTE = 0x00001401
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x00008b4a
GL_VENDOR = 0x00001f00
GL_TEXTURE_2D_ARRAY = 0x00008c1a
GL_UNSIGNED_INT_10F_11F_11F_REV = 0x00008c3b
GL_TEXTURE_BINDING_2D = 0x00008069
GL_OBJECT_TYPE = 0x00009112
GL_R8UI = 0x00008232
GL_STATIC_DRAW = 0x000088e4
GL_RENDERBUFFER = 0x00008d41
GL_FLOAT_MAT2x3 = 0x00008b65
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x00008213
GL_FLOAT_MAT2x4 = 0x00008b66
GL_RGB8I = 0x00008d8f
GL_COLOR_ATTACHMENT18 = 0x00008cf2
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x00008c85
GL_TRANSFORM_FEEDBACK_ACTIVE = 0x00008e24
GL_SEPARATE_ATTRIBS = 0x00008c8d
GL_SAMPLER_3D = 0x00008b5f
GL_MAX = 0x00008008
GL_STENCIL_INDEX8 = 0x00008d48
GL_DEPTH_BITS = 0x00000d56
GL_RGB8UI = 0x00008d7d
GL_INVALID_INDEX = 0xffffffff
GL_COMPRESSED_SRGB8_ETC2 = 0x00009275
GL_BLEND_DST_RGB = 0x000080c8
GL_SAMPLER_2D_SHADOW = 0x00008b62
GL_TEXTURE_BINDING_2D_ARRAY = 0x00008c1d
GL_RG16F = 0x0000822f
GL_SAMPLER_CUBE = 0x00008b60
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x00008cd2
GL_RED_BITS = 0x00000d52
GL_RG16I = 0x00008239
GL_PIXEL_PACK_BUFFER_BINDING = 0x000088ed
GL_STENCIL_ATTACHMENT = 0x00008d20
GL_SAMPLE_COVERAGE = 0x000080a0
GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 0x00008d6a
GL_DRAW_FRAMEBUFFER = 0x00008ca9
GL_RGB10_A2UI = 0x0000906f
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

try:
    def glReadBuffer(src, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glReadBuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(src)
    # Check if the function actually exists
    f = c.glReadBuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDrawRangeElements(mode, start, end, count, type, voidindices, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint, GLuint, GLsizei, GLenum, ctypes.c_void_p]
        cfunc = c.glDrawRangeElements
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode, start, end, count, type, voidindices)
    # Check if the function actually exists
    f = c.glDrawRangeElements
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, voidpixels, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p]
        cfunc = c.glTexImage3D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, width, height, depth, border, format, type, voidpixels)
    # Check if the function actually exists
    f = c.glTexImage3D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, voidpixels, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p]
        cfunc = c.glTexSubImage3D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, voidpixels)
    # Check if the function actually exists
    f = c.glTexSubImage3D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei]
        cfunc = c.glCopyTexSubImage3D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, zoffset, x, y, width, height)
    # Check if the function actually exists
    f = c.glCopyTexSubImage3D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, voiddata, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p]
        cfunc = c.glCompressedTexImage3D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, internalformat, width, height, depth, border, imageSize, voiddata)
    # Check if the function actually exists
    f = c.glCompressedTexImage3D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, voiddata, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p]
        cfunc = c.glCompressedTexSubImage3D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, voiddata)
    # Check if the function actually exists
    f = c.glCompressedTexSubImage3D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenQueries(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenQueries
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenQueries
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteQueries(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteQueries
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteQueries
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsQuery(id, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsQuery
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(id)
    # Check if the function actually exists
    f = c.glIsQuery
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBeginQuery(target, id, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glBeginQuery
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, id)
    # Check if the function actually exists
    f = c.glBeginQuery
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glEndQuery(target, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glEndQuery
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glEndQuery
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetQueryiv(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint]
        cfunc = c.glGetQueryiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetQueryiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetQueryObjectuiv(id, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLuint]
        cfunc = c.glGetQueryObjectuiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(id, pname, param0)
    # Check if the function actually exists
    f = c.glGetQueryObjectuiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUnmapBuffer(target, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glUnmapBuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glUnmapBuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetBufferPointerv(target, pname, voidparams, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, ctypes.c_void_p]
        cfunc = c.glGetBufferPointerv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, voidparams)
    # Check if the function actually exists
    f = c.glGetBufferPointerv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDrawBuffers(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLenum]
        cfunc = c.glDrawBuffers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDrawBuffers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix2x3fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix2x3fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix2x3fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix3x2fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix3x2fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix3x2fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix2x4fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix2x4fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix2x4fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix4x2fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix4x2fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix4x2fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix3x4fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix3x4fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix3x4fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformMatrix4x3fv(location, count, transpose, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLboolean, GLfloat]
        cfunc = c.glUniformMatrix4x3fv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, transpose, param0)
    # Check if the function actually exists
    f = c.glUniformMatrix4x3fv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum]
        cfunc = c.glBlitFramebuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)
    # Check if the function actually exists
    f = c.glBlitFramebuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorageMultisample(target, samples, internalformat, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, GLsizei, GLsizei]
        cfunc = c.glRenderbufferStorageMultisample
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, samples, internalformat, width, height)
    # Check if the function actually exists
    f = c.glRenderbufferStorageMultisample
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFramebufferTextureLayer(target, attachment, texture, level, layer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLuint, GLint, GLint]
        cfunc = c.glFramebufferTextureLayer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, texture, level, layer)
    # Check if the function actually exists
    f = c.glFramebufferTextureLayer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glFlushMappedBufferRange(target, offset, length, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLintptr, GLsizeiptr]
        cfunc = c.glFlushMappedBufferRange
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, offset, length)
    # Check if the function actually exists
    f = c.glFlushMappedBufferRange
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindVertexArray(array, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glBindVertexArray
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(array)
    # Check if the function actually exists
    f = c.glBindVertexArray
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteVertexArrays(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteVertexArrays
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteVertexArrays
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenVertexArrays(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenVertexArrays
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenVertexArrays
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsVertexArray(array, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsVertexArray
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(array)
    # Check if the function actually exists
    f = c.glIsVertexArray
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetIntegeri_v(target, index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint, GLint]
        cfunc = c.glGetIntegeri_v
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, index, param0)
    # Check if the function actually exists
    f = c.glGetIntegeri_v
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBeginTransformFeedback(primitiveMode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum]
        cfunc = c.glBeginTransformFeedback
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(primitiveMode)
    # Check if the function actually exists
    f = c.glBeginTransformFeedback
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glEndTransformFeedback(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glEndTransformFeedback
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glEndTransformFeedback
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindBufferRange(target, index, buffer, offset, size, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint, GLuint, GLintptr, GLsizeiptr]
        cfunc = c.glBindBufferRange
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, index, buffer, offset, size)
    # Check if the function actually exists
    f = c.glBindBufferRange
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindBufferBase(target, index, buffer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint, GLuint]
        cfunc = c.glBindBufferBase
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, index, buffer)
    # Check if the function actually exists
    f = c.glBindBufferBase
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTransformFeedbackVaryings(program, count, param0, bufferMode, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLchar, GLenum]
        cfunc = c.glTransformFeedbackVaryings
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, count, param0, bufferMode)
    # Check if the function actually exists
    f = c.glTransformFeedbackVaryings
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetTransformFeedbackVarying(program, index, bufSize, param0, param1, param2, param3, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLsizei, GLsizei, GLsizei, GLenum, GLchar]
        cfunc = c.glGetTransformFeedbackVarying
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, index, bufSize, param0, param1, param2, param3)
    # Check if the function actually exists
    f = c.glGetTransformFeedbackVarying
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribIPointer(index, size, type, stride, voidpointer, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint, GLenum, GLsizei, ctypes.c_void_p]
        cfunc = c.glVertexAttribIPointer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, size, type, stride, voidpointer)
    # Check if the function actually exists
    f = c.glVertexAttribIPointer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribIiv(index, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glGetVertexAttribIiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, pname, param0)
    # Check if the function actually exists
    f = c.glGetVertexAttribIiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetVertexAttribIuiv(index, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLuint]
        cfunc = c.glGetVertexAttribIuiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, pname, param0)
    # Check if the function actually exists
    f = c.glGetVertexAttribIuiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribI4i(index, x, y, z, w, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint, GLint, GLint, GLint]
        cfunc = c.glVertexAttribI4i
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, x, y, z, w)
    # Check if the function actually exists
    f = c.glVertexAttribI4i
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribI4ui(index, x, y, z, w, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLuint, GLuint, GLuint]
        cfunc = c.glVertexAttribI4ui
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, x, y, z, w)
    # Check if the function actually exists
    f = c.glVertexAttribI4ui
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribI4iv(index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint]
        cfunc = c.glVertexAttribI4iv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, param0)
    # Check if the function actually exists
    f = c.glVertexAttribI4iv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribI4uiv(index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint]
        cfunc = c.glVertexAttribI4uiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, param0)
    # Check if the function actually exists
    f = c.glVertexAttribI4uiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetUniformuiv(program, location, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLint, GLuint]
        cfunc = c.glGetUniformuiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, location, param0)
    # Check if the function actually exists
    f = c.glGetUniformuiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetFragDataLocation(program, param0, argtypes_p=None):
        restype = GLint
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLchar]
        cfunc = c.glGetFragDataLocation
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, param0)
    # Check if the function actually exists
    f = c.glGetFragDataLocation
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform1ui(location, v0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLuint]
        cfunc = c.glUniform1ui
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0)
    # Check if the function actually exists
    f = c.glUniform1ui
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform2ui(location, v0, v1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLuint, GLuint]
        cfunc = c.glUniform2ui
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1)
    # Check if the function actually exists
    f = c.glUniform2ui
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform3ui(location, v0, v1, v2, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLuint, GLuint, GLuint]
        cfunc = c.glUniform3ui
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1, v2)
    # Check if the function actually exists
    f = c.glUniform3ui
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform4ui(location, v0, v1, v2, v3, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLuint, GLuint, GLuint, GLuint]
        cfunc = c.glUniform4ui
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, v0, v1, v2, v3)
    # Check if the function actually exists
    f = c.glUniform4ui
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform1uiv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLuint]
        cfunc = c.glUniform1uiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform1uiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform2uiv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLuint]
        cfunc = c.glUniform2uiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform2uiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform3uiv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLuint]
        cfunc = c.glUniform3uiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform3uiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniform4uiv(location, count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLint, GLsizei, GLuint]
        cfunc = c.glUniform4uiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(location, count, param0)
    # Check if the function actually exists
    f = c.glUniform4uiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearBufferiv(buffer, drawbuffer, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLint]
        cfunc = c.glClearBufferiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(buffer, drawbuffer, param0)
    # Check if the function actually exists
    f = c.glClearBufferiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearBufferuiv(buffer, drawbuffer, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLuint]
        cfunc = c.glClearBufferuiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(buffer, drawbuffer, param0)
    # Check if the function actually exists
    f = c.glClearBufferuiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearBufferfv(buffer, drawbuffer, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLfloat]
        cfunc = c.glClearBufferfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(buffer, drawbuffer, param0)
    # Check if the function actually exists
    f = c.glClearBufferfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glClearBufferfi(buffer, drawbuffer, depth, stencil, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLfloat, GLint]
        cfunc = c.glClearBufferfi
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(buffer, drawbuffer, depth, stencil)
    # Check if the function actually exists
    f = c.glClearBufferfi
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLintptr, GLintptr, GLsizeiptr]
        cfunc = c.glCopyBufferSubData
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(readTarget, writeTarget, readOffset, writeOffset, size)
    # Check if the function actually exists
    f = c.glCopyBufferSubData
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetUniformIndices(program, uniformCount, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLchar, GLuint]
        cfunc = c.glGetUniformIndices
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, uniformCount, param0, param1)
    # Check if the function actually exists
    f = c.glGetUniformIndices
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetActiveUniformsiv(program, uniformCount, param0, pname, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLuint, GLenum, GLint]
        cfunc = c.glGetActiveUniformsiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, uniformCount, param0, pname, param1)
    # Check if the function actually exists
    f = c.glGetActiveUniformsiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetUniformBlockIndex(program, param0, argtypes_p=None):
        restype = GLuint
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLchar]
        cfunc = c.glGetUniformBlockIndex
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, param0)
    # Check if the function actually exists
    f = c.glGetUniformBlockIndex
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLenum, GLint]
        cfunc = c.glGetActiveUniformBlockiv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, uniformBlockIndex, pname, param0)
    # Check if the function actually exists
    f = c.glGetActiveUniformBlockiv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, param0, param1, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLsizei, GLsizei, GLchar]
        cfunc = c.glGetActiveUniformBlockName
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, uniformBlockIndex, bufSize, param0, param1)
    # Check if the function actually exists
    f = c.glGetActiveUniformBlockName
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint, GLuint]
        cfunc = c.glUniformBlockBinding
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, uniformBlockIndex, uniformBlockBinding)
    # Check if the function actually exists
    f = c.glUniformBlockBinding
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDrawArraysInstanced(mode, first, count, instancecount, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint, GLsizei, GLsizei]
        cfunc = c.glDrawArraysInstanced
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode, first, count, instancecount)
    # Check if the function actually exists
    f = c.glDrawArraysInstanced
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDrawElementsInstanced(mode, count, type, voidindices, instancecount, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei]
        cfunc = c.glDrawElementsInstanced
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode, count, type, voidindices, instancecount)
    # Check if the function actually exists
    f = c.glDrawElementsInstanced
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetInteger64v(pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLint64]
        cfunc = c.glGetInteger64v
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetInteger64v
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetInteger64i_v(target, index, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint, GLint64]
        cfunc = c.glGetInteger64i_v
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, index, param0)
    # Check if the function actually exists
    f = c.glGetInteger64i_v
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetBufferParameteri64v(target, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLint64]
        cfunc = c.glGetBufferParameteri64v
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetBufferParameteri64v
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenSamplers(count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenSamplers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(count, param0)
    # Check if the function actually exists
    f = c.glGenSamplers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteSamplers(count, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteSamplers
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(count, param0)
    # Check if the function actually exists
    f = c.glDeleteSamplers
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsSampler(sampler, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsSampler
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler)
    # Check if the function actually exists
    f = c.glIsSampler
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindSampler(unit, sampler, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint]
        cfunc = c.glBindSampler
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(unit, sampler)
    # Check if the function actually exists
    f = c.glBindSampler
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glSamplerParameteri(sampler, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glSamplerParameteri
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler, pname, param)
    # Check if the function actually exists
    f = c.glSamplerParameteri
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glSamplerParameteriv(sampler, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glSamplerParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler, pname, param0)
    # Check if the function actually exists
    f = c.glSamplerParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glSamplerParameterf(sampler, pname, param, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLfloat]
        cfunc = c.glSamplerParameterf
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler, pname, param)
    # Check if the function actually exists
    f = c.glSamplerParameterf
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glSamplerParameterfv(sampler, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLfloat]
        cfunc = c.glSamplerParameterfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler, pname, param0)
    # Check if the function actually exists
    f = c.glSamplerParameterfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetSamplerParameteriv(sampler, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glGetSamplerParameteriv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler, pname, param0)
    # Check if the function actually exists
    f = c.glGetSamplerParameteriv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetSamplerParameterfv(sampler, pname, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLfloat]
        cfunc = c.glGetSamplerParameterfv
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(sampler, pname, param0)
    # Check if the function actually exists
    f = c.glGetSamplerParameterfv
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glVertexAttribDivisor(index, divisor, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLuint]
        cfunc = c.glVertexAttribDivisor
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(index, divisor)
    # Check if the function actually exists
    f = c.glVertexAttribDivisor
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glBindTransformFeedback(target, id, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLuint]
        cfunc = c.glBindTransformFeedback
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, id)
    # Check if the function actually exists
    f = c.glBindTransformFeedback
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glDeleteTransformFeedbacks(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glDeleteTransformFeedbacks
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteTransformFeedbacks
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGenTransformFeedbacks(n, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLsizei, GLuint]
        cfunc = c.glGenTransformFeedbacks
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenTransformFeedbacks
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glIsTransformFeedback(id, argtypes_p=None):
        restype = GLboolean
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint]
        cfunc = c.glIsTransformFeedback
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(id)
    # Check if the function actually exists
    f = c.glIsTransformFeedback
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glPauseTransformFeedback(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glPauseTransformFeedback
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glPauseTransformFeedback
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glResumeTransformFeedback(void, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [ctypes.c_void_p]
        cfunc = c.glResumeTransformFeedback
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glResumeTransformFeedback
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetProgramBinary(program, bufSize, param0, param1, voidbinary, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLsizei, GLsizei, GLenum, ctypes.c_void_p]
        cfunc = c.glGetProgramBinary
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, bufSize, param0, param1, voidbinary)
    # Check if the function actually exists
    f = c.glGetProgramBinary
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glProgramBinary(program, binaryFormat, voidbinary, length, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, ctypes.c_void_p, GLsizei]
        cfunc = c.glProgramBinary
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, binaryFormat, voidbinary, length)
    # Check if the function actually exists
    f = c.glProgramBinary
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glProgramParameteri(program, pname, value, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLuint, GLenum, GLint]
        cfunc = c.glProgramParameteri
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, pname, value)
    # Check if the function actually exists
    f = c.glProgramParameteri
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glInvalidateFramebuffer(target, numAttachments, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum]
        cfunc = c.glInvalidateFramebuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, numAttachments, param0)
    # Check if the function actually exists
    f = c.glInvalidateFramebuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glInvalidateSubFramebuffer(target, numAttachments, param0, x, y, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, GLint, GLint, GLsizei, GLsizei]
        cfunc = c.glInvalidateSubFramebuffer
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, numAttachments, param0, x, y, width, height)
    # Check if the function actually exists
    f = c.glInvalidateSubFramebuffer
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexStorage2D(target, levels, internalformat, width, height, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, GLsizei, GLsizei]
        cfunc = c.glTexStorage2D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, levels, internalformat, width, height)
    # Check if the function actually exists
    f = c.glTexStorage2D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glTexStorage3D(target, levels, internalformat, width, height, depth, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei]
        cfunc = c.glTexStorage3D
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, levels, internalformat, width, height, depth)
    # Check if the function actually exists
    f = c.glTexStorage3D
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

try:
    def glGetInternalformativ(target, internalformat, pname, bufSize, param0, argtypes_p=None):
        restype = None
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [GLenum, GLenum, GLenum, GLsizei, GLint]
        cfunc = c.glGetInternalformativ
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, internalformat, pname, bufSize, param0)
    # Check if the function actually exists
    f = c.glGetInternalformativ
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 1:
        print 'could not load the function'
        print e

print 'Loaded %i functions and failed to load %i functions of %i functions in the header gl3.h' % (loaded[0], loaded[1], sum(loaded))
__all__ = ['glActiveTexture', 'glAttachShader', 'glBindAttribLocation', 'glBindBuffer', 'glBindFramebuffer', 'glBindRenderbuffer', 'glBindTexture', 'glBlendColor', 'glBlendEquation', 'glBlendEquationSeparate', 'glBlendFunc', 'glBlendFuncSeparate', 'glBufferData', 'glBufferSubData', 'glCheckFramebufferStatus', 'glClear', 'glClearColor', 'glClearDepthf', 'glClearStencil', 'glColorMask', 'glCompileShader', 'glCompressedTexImage2D', 'glCompressedTexSubImage2D', 'glCopyTexImage2D', 'glCopyTexSubImage2D', 'glCreateProgram', 'glCreateShader', 'glCullFace', 'glDeleteBuffers', 'glDeleteFramebuffers', 'glDeleteProgram', 'glDeleteRenderbuffers', 'glDeleteShader', 'glDeleteTextures', 'glDepthFunc', 'glDepthMask', 'glDepthRangef', 'glDetachShader', 'glDisable', 'glDisableVertexAttribArray', 'glDrawArrays', 'glDrawElements', 'glEnable', 'glEnableVertexAttribArray', 'glFinish', 'glFlush', 'glFramebufferRenderbuffer', 'glFramebufferTexture2D', 'glFrontFace', 'glGenBuffers', 'glGenerateMipmap', 'glGenFramebuffers', 'glGenRenderbuffers', 'glGenTextures', 'glGetActiveAttrib', 'glGetActiveUniform', 'glGetAttachedShaders', 'glGetAttribLocation', 'glGetBooleanv', 'glGetBufferParameteriv', 'glGetError', 'glGetFloatv', 'glGetFramebufferAttachmentParameteriv', 'glGetIntegerv', 'glGetProgramiv', 'glGetProgramInfoLog', 'glGetRenderbufferParameteriv', 'glGetShaderiv', 'glGetShaderInfoLog', 'glGetShaderPrecisionFormat', 'glGetShaderSource', 'glGetTexParameterfv', 'glGetTexParameteriv', 'glGetUniformfv', 'glGetUniformiv', 'glGetUniformLocation', 'glGetVertexAttribfv', 'glGetVertexAttribiv', 'glGetVertexAttribPointerv', 'glHint', 'glIsBuffer', 'glIsEnabled', 'glIsFramebuffer', 'glIsProgram', 'glIsRenderbuffer', 'glIsShader', 'glIsTexture', 'glLineWidth', 'glLinkProgram', 'glPixelStorei', 'glPolygonOffset', 'glReadPixels', 'glReleaseShaderCompiler', 'glRenderbufferStorage', 'glSampleCoverage', 'glScissor', 'glShaderBinary', 'glShaderSource', 'glStencilFunc', 'glStencilFuncSeparate', 'glStencilMask', 'glStencilMaskSeparate', 'glStencilOp', 'glStencilOpSeparate', 'glTexImage2D', 'glTexParameterf', 'glTexParameterfv', 'glTexParameteri', 'glTexParameteriv', 'glTexSubImage2D', 'glUniform1f', 'glUniform1fv', 'glUniform1i', 'glUniform1iv', 'glUniform2f', 'glUniform2fv', 'glUniform2i', 'glUniform2iv', 'glUniform3f', 'glUniform3fv', 'glUniform3i', 'glUniform3iv', 'glUniform4f', 'glUniform4fv', 'glUniform4i', 'glUniform4iv', 'glUniformMatrix2fv', 'glUniformMatrix3fv', 'glUniformMatrix4fv', 'glUseProgram', 'glValidateProgram', 'glVertexAttrib1f', 'glVertexAttrib1fv', 'glVertexAttrib2f', 'glVertexAttrib2fv', 'glVertexAttrib3f', 'glVertexAttrib3fv', 'glVertexAttrib4f', 'glVertexAttrib4fv', 'glVertexAttribPointer', 'glViewport', 'glReadBuffer', 'glDrawRangeElements', 'glTexImage3D', 'glTexSubImage3D', 'glCopyTexSubImage3D', 'glCompressedTexImage3D', 'glCompressedTexSubImage3D', 'glGenQueries', 'glDeleteQueries', 'glIsQuery', 'glBeginQuery', 'glEndQuery', 'glGetQueryiv', 'glGetQueryObjectuiv', 'glUnmapBuffer', 'glGetBufferPointerv', 'glDrawBuffers', 'glUniformMatrix2x3fv', 'glUniformMatrix3x2fv', 'glUniformMatrix2x4fv', 'glUniformMatrix4x2fv', 'glUniformMatrix3x4fv', 'glUniformMatrix4x3fv', 'glBlitFramebuffer', 'glRenderbufferStorageMultisample', 'glFramebufferTextureLayer', 'glFlushMappedBufferRange', 'glBindVertexArray', 'glDeleteVertexArrays', 'glGenVertexArrays', 'glIsVertexArray', 'glGetIntegeri_v', 'glBeginTransformFeedback', 'glEndTransformFeedback', 'glBindBufferRange', 'glBindBufferBase', 'glTransformFeedbackVaryings', 'glGetTransformFeedbackVarying', 'glVertexAttribIPointer', 'glGetVertexAttribIiv', 'glGetVertexAttribIuiv', 'glVertexAttribI4i', 'glVertexAttribI4ui', 'glVertexAttribI4iv', 'glVertexAttribI4uiv', 'glGetUniformuiv', 'glGetFragDataLocation', 'glUniform1ui', 'glUniform2ui', 'glUniform3ui', 'glUniform4ui', 'glUniform1uiv', 'glUniform2uiv', 'glUniform3uiv', 'glUniform4uiv', 'glClearBufferiv', 'glClearBufferuiv', 'glClearBufferfv', 'glClearBufferfi', 'glCopyBufferSubData', 'glGetUniformIndices', 'glGetActiveUniformsiv', 'glGetUniformBlockIndex', 'glGetActiveUniformBlockiv', 'glGetActiveUniformBlockName', 'glUniformBlockBinding', 'glDrawArraysInstanced', 'glDrawElementsInstanced', 'glGetInteger64v', 'glGetInteger64i_v', 'glGetBufferParameteri64v', 'glGenSamplers', 'glDeleteSamplers', 'glIsSampler', 'glBindSampler', 'glSamplerParameteri', 'glSamplerParameteriv', 'glSamplerParameterf', 'glSamplerParameterfv', 'glGetSamplerParameteriv', 'glGetSamplerParameterfv', 'glVertexAttribDivisor', 'glBindTransformFeedback', 'glDeleteTransformFeedbacks', 'glGenTransformFeedbacks', 'glIsTransformFeedback', 'glPauseTransformFeedback', 'glResumeTransformFeedback', 'glGetProgramBinary', 'glProgramBinary', 'glProgramParameteri', 'glInvalidateFramebuffer', 'glInvalidateSubFramebuffer', 'glTexStorage2D', 'glTexStorage3D', 'glGetInternalformativ', 'GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE', 'GL_UNSIGNED_INT_VEC2', 'GL_UNSIGNED_INT_VEC3', 'GL_UNSIGNED_INT_VEC4', 'GL_UNSIGNED_SHORT_5_6_5', 'GL_VERTEX_ATTRIB_ARRAY_SIZE', 'GL_DEPTH_ATTACHMENT', 'GL_DITHER', 'GL_TRANSFORM_FEEDBACK_PAUSED', 'GL_RGB16UI', '__gl3_h_', 'GL_QUERY_RESULT', 'GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE', 'GL_FLOAT_VEC2', 'GL_FLOAT_VEC3', 'GL_FLOAT_VEC4', 'GL_FLOAT', 'GL_INT_2_10_10_10_REV', 'GL_RGB32UI', 'GL_TEXTURE_MAX_LOD', 'GL_BUFFER_MAP_OFFSET', 'GL_BUFFER_SIZE', 'GL_RGB9_E5', 'GL_UNIFORM_BUFFER_START', 'GL_COMPRESSED_R11_EAC', 'GL_RGBA32UI', 'GL_UNSIGNED_INT_SAMPLER_2D', 'GL_TEXTURE_MIN_LOD', 'GL_TEXTURE8', 'GL_TEXTURE9', 'GL_TEXTURE4', 'GL_TEXTURE5', 'GL_TEXTURE6', 'GL_TEXTURE7', 'GL_TEXTURE0', 'GL_LINEAR_MIPMAP_LINEAR', 'GL_TEXTURE2', 'GL_TEXTURE3', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y', 'GL_TEXTURE_CUBE_MAP_POSITIVE_X', 'GL_BLEND_EQUATION', 'GL_BYTE', 'GL_BOOL_VEC3', 'GL_BOOL_VEC2', 'GL_TIMEOUT_IGNORED', 'GL_MAX_VARYING_VECTORS', 'GL_RENDERBUFFER_SAMPLES', 'GL_ONE', 'GL_RG', 'GL_COLOR_CLEAR_VALUE', 'GL_MAX_SAMPLES', 'GL_BUFFER_USAGE', 'GL_UNPACK_IMAGE_HEIGHT', 'GL_FLOAT_MAT3x2', 'GL_TRIANGLE_STRIP', 'GL_PROGRAM_BINARY_RETRIEVABLE_HINT', 'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING', 'GL_FLOAT_MAT3x4', 'GL_COLOR_ATTACHMENT28', 'GL_COLOR_ATTACHMENT29', 'GL_COLOR_ATTACHMENT24', 'GL_COLOR_ATTACHMENT25', 'GL_COLOR_ATTACHMENT26', 'GL_COLOR_ATTACHMENT27', 'GL_COLOR_ATTACHMENT20', 'GL_COLOR_ATTACHMENT21', 'GL_COLOR_ATTACHMENT22', 'GL_COLOR_ATTACHMENT23', 'GL_TRANSFORM_FEEDBACK_BUFFER', 'GL_BLUE', 'GL_VERTEX_ARRAY_BINDING', 'GL_UNSIGNED_SHORT_5_5_5_1', 'GL_TIMEOUT_EXPIRED', 'GL_COMPRESSED_RGB8_ETC2', 'GL_SIGNED_NORMALIZED', 'GL_STENCIL_FUNC', 'GL_MAX_TEXTURE_LOD_BIAS', 'GL_ALIASED_LINE_WIDTH_RANGE', 'GL_DECR', 'GL_BACK', 'GL_ES_VERSION_3_0', 'GL_TEXTURE_COMPARE_FUNC', 'GL_TRANSFORM_FEEDBACK_BUFFER_MODE', 'GL_INT', 'GL_COMPRESSED_SIGNED_RG11_EAC', 'GL_POLYGON_OFFSET_FILL', 'GL_MINOR_VERSION', 'GL_FRONT_AND_BACK', 'GL_R8', 'GL_RGB_INTEGER', 'GL_STENCIL', 'GL_SRGB', 'GL_GREEN_BITS', 'GL_SYNC_FENCE', 'GL_ONE_MINUS_CONSTANT_COLOR', 'GL_SHADING_LANGUAGE_VERSION', 'GL_RGB8_SNORM', 'GL_UNPACK_SKIP_PIXELS', 'GL_TEXTURE_IMMUTABLE_LEVELS', 'GL_FRAGMENT_SHADER', 'GL_UNSIGNED_INT_2_10_10_10_REV', 'GL_UNSIGNED_SHORT_4_4_4_4', 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS', 'GL_FRAGMENT_SHADER_DERIVATIVE_HINT', 'GL_NO_ERROR', 'GL_VIEWPORT', 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME', 'GL_BLEND_SRC_ALPHA', 'GL_DRAW_BUFFER6', 'GL_DRAW_BUFFER7', 'GL_DRAW_BUFFER4', 'GL_DRAW_BUFFER5', 'GL_DRAW_BUFFER2', 'GL_DRAW_BUFFER3', 'GL_DRAW_BUFFER0', 'GL_DRAW_BUFFER1', 'GL_UNIFORM_TYPE', 'GL_QUERY_RESULT_AVAILABLE', 'GL_DRAW_BUFFER8', 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT', 'GL_MAX_DRAW_BUFFERS', 'GL_KEEP', 'GL_DELETE_STATUS', 'GL_R32UI', 'GL_RGBA8_SNORM', 'GL_INT_SAMPLER_3D', 'GL_SRC_COLOR', 'GL_SAMPLER_BINDING', 'GL_DEPTH24_STENCIL8', 'GL_SAMPLE_BUFFERS', 'GL_MAJOR_VERSION', 'GL_STATIC_COPY', 'GL_ACTIVE_ATTRIBUTE_MAX_LENGTH', 'GL_EXTENSIONS', 'GL_UNIFORM_BUFFER_BINDING', 'GL_RGBA16UI', 'GL_COPY_READ_BUFFER_BINDING', 'GL_TEXTURE_COMPARE_MODE', 'GL_ANY_SAMPLES_PASSED', 'GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE', 'GL_DEPTH_BUFFER_BIT', 'GL_STENCIL_BACK_PASS_DEPTH_FAIL', 'GL_UNIFORM_BUFFER', 'GL_MAP_WRITE_BIT', 'GL_VERTEX_ATTRIB_ARRAY_POINTER', 'GL_ALIASED_POINT_SIZE_RANGE', 'GL_CCW', 'GL_MAP_INVALIDATE_BUFFER_BIT', 'GL_DEPTH_COMPONENT24', 'GL_UNSIGNED_INT_5_9_9_9_REV', 'GL_DEPTH_TEST', 'GL_SYNC_GPU_COMMANDS_COMPLETE', 'GL_VERTEX_ATTRIB_ARRAY_INTEGER', 'GL_MAX_FRAGMENT_UNIFORM_BLOCKS', 'GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE', 'GL_ACTIVE_UNIFORM_MAX_LENGTH', 'GL_STREAM_READ', 'GL_LINEAR', 'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN', 'GL_FUNC_SUBTRACT', 'GL_R32F', 'GL_MAX_VARYING_COMPONENTS', 'GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH', 'GL_IMPLEMENTATION_COLOR_READ_FORMAT', 'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING', 'GL_HALF_FLOAT', 'GL_COLOR_ATTACHMENT15', 'GL_COLOR_ATTACHMENT14', 'GL_HIGH_FLOAT', 'GL_DEPTH_RANGE', 'GL_GREATER', 'GL_CLAMP_TO_EDGE', 'GL_COLOR_ATTACHMENT13', 'GL_COLOR_ATTACHMENT12', 'GL_NEAREST', 'GL_VERTEX_ATTRIB_ARRAY_ENABLED', 'GL_COLOR_ATTACHMENT19', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER', 'GL_MAX_TEXTURE_IMAGE_UNITS', 'GL_RGB32F', 'GL_FLOAT_MAT2', 'GL_FLOAT_MAT3', 'GL_FRONT_FACE', 'GL_DEPTH', 'GL_FLOAT_MAT4', 'GL_RENDERBUFFER_GREEN_SIZE', 'GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE', 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT', 'GL_TEXTURE30', 'GL_TEXTURE31', 'GL_RG8I', 'GL_RGBA8I', 'GL_RG8UI', 'GL_DEPTH_CLEAR_VALUE', 'GL_BUFFER_MAP_POINTER', 'GL_RENDERBUFFER_BINDING', 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE', 'GL_STENCIL_REF', 'GL_MAX_3D_TEXTURE_SIZE', 'GL_R16UI', 'GL_COPY_WRITE_BUFFER_BINDING', 'GL_COPY_WRITE_BUFFER', 'GL_BLEND', 'GL_MIRRORED_REPEAT', 'GL_SAMPLER_CUBE_SHADOW', 'GL_TEXTURE_BINDING_3D', 'GL_UNSIGNED_SHORT', 'GL_MIN', 'GL_ONE_MINUS_DST_COLOR', 'GL_ONE_MINUS_SRC_COLOR', 'GL_TEXTURE', 'GL_COLOR_BUFFER_BIT', 'GL_DONT_CARE', 'GL_ACTIVE_UNIFORMS', 'GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2', 'GL_MAX_VERTEX_UNIFORM_VECTORS', 'GL_TEXTURE_BINDING_CUBE_MAP', 'GL_SAMPLER_2D', 'GL_INVALID_VALUE', 'GL_NEAREST_MIPMAP_NEAREST', 'GL_NUM_COMPRESSED_TEXTURE_FORMATS', 'GL_PACK_SKIP_ROWS', 'GL_TEXTURE_MAG_FILTER', 'GL_R8I', 'GL_TEXTURE1', 'GL_BLEND_EQUATION_RGB', 'GL_LINK_STATUS', 'GL_TEXTURE_MAX_LEVEL', 'GL_R32I', 'GL_BLEND_COLOR', 'GL_ALPHA_BITS', 'GL_BOOL_VEC4', 'GL_ONE_MINUS_CONSTANT_ALPHA', 'GL_NEAREST_MIPMAP_LINEAR', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z', 'GL_WAIT_FAILED', 'GL_UNIFORM_BLOCK_NAME_LENGTH', 'GL_MAX_TEXTURE_SIZE', 'GL_RG32F', 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY', 'GL_ARRAY_BUFFER', 'GL_DEPTH_COMPONENT16', 'GL_UNSIGNALED', 'GL_RGB32I', 'GL_BLEND_SRC_RGB', 'GL_FRAMEBUFFER_UNDEFINED', 'GL_SYNC_FLAGS', 'GL_FALSE', 'GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS', 'GL_ONE_MINUS_SRC_ALPHA', 'GL_RG32I', 'GL_RENDERBUFFER_INTERNAL_FORMAT', 'GL_NUM_SHADER_BINARY_FORMATS', 'GL_RGBA16I', 'GL_RGBA16F', 'GL_SAMPLE_ALPHA_TO_COVERAGE', 'GL_INT_SAMPLER_2D', 'GL_STENCIL_BITS', 'GL_STENCIL_PASS_DEPTH_FAIL', 'GL_RED', 'GL_MAX_ELEMENT_INDEX', 'GL_MAX_VERTEX_UNIFORM_BLOCKS', 'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS', 'GL_RGBA8UI', 'GL_GREEN', 'GL_INVALID_OPERATION', 'GL_RED_INTEGER', 'GL_NONE', 'GL_STENCIL_BACK_PASS_DEPTH_PASS', 'GL_COLOR_ATTACHMENT5', 'GL_FUNC_REVERSE_SUBTRACT', 'GL_COLOR_ATTACHMENT7', 'GL_COLOR_ATTACHMENT6', 'GL_COLOR_ATTACHMENT1', 'GL_COLOR_ATTACHMENT0', 'GL_COLOR_ATTACHMENT3', 'GL_COLOR_ATTACHMENT2', 'GL_UNIFORM_BLOCK_INDEX', 'GL_FRAMEBUFFER_DEFAULT', 'GL_COLOR_ATTACHMENT9', 'GL_COLOR_ATTACHMENT8', 'GL_COLOR_ATTACHMENT10', 'GL_FRONT', 'GL_SCISSOR_BOX', 'GL_UNIFORM_BLOCK_DATA_SIZE', 'GL_LEQUAL', 'GL_CULL_FACE_MODE', 'GL_MAX_FRAGMENT_UNIFORM_VECTORS', 'GL_NUM_EXTENSIONS', 'GL_UNIFORM_IS_ROW_MAJOR', 'GL_MAX_UNIFORM_BLOCK_SIZE', 'GL_BOOL', 'GL_MAX_COMBINED_UNIFORM_BLOCKS', 'GL_FRAMEBUFFER_BINDING', 'GL_UNSIGNED_INT_24_8', 'GL_COMPRESSED_TEXTURE_FORMATS', 'GL_ALPHA', 'GL_COLOR_WRITEMASK', 'GL_DST_COLOR', 'GL_UNSIGNED_INT', 'GL_DEPTH_FUNC', 'GL_ALWAYS', 'GL_TEXTURE_WRAP_S', 'GL_TEXTURE_WRAP_T', 'GL_INVALID_ENUM', 'GL_PROGRAM_BINARY_LENGTH', 'GL_STENCIL_BACK_VALUE_MASK', 'GL_INT_SAMPLER_2D_ARRAY', 'GL_COLOR_ATTACHMENT11', 'GL_DEPTH_COMPONENT', 'GL_SCISSOR_TEST', 'GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES', 'GL_SHADER_TYPE', 'GL_COMPARE_REF_TO_TEXTURE', 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE', 'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE', 'GL_TRUE', 'GL_TEXTURE_MIN_FILTER', 'GL_REPLACE', 'GL_BLUE_BITS', 'GL_RG_INTEGER', 'GL_TEXTURE_SWIZZLE_R', 'GL_VERTEX_ATTRIB_ARRAY_STRIDE', 'GL_EQUAL', 'GL_TEXTURE_SWIZZLE_G', 'GL_DEPTH_STENCIL_ATTACHMENT', 'GL_RENDERBUFFER_HEIGHT', 'GL_RG16UI', 'GL_DRAW_BUFFER12', 'GL_TEXTURE_SWIZZLE_A', 'GL_LOW_FLOAT', 'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS', 'GL_FLOAT_MAT4x3', 'GL_DRAW_BUFFER15', 'GL_DYNAMIC_COPY', 'GL_STENCIL_BACK_REF', 'GL_UNPACK_ALIGNMENT', 'GL_ALREADY_SIGNALED', 'GL_LINE_STRIP', 'GL_STREAM_COPY', 'GL_PACK_ROW_LENGTH', 'GL_NUM_SAMPLE_COUNTS', 'GL_MEDIUM_INT', 'GL_TEXTURE_CUBE_MAP', 'GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS', 'GL_COLOR', 'GL_RENDERBUFFER_DEPTH_SIZE', 'GL_DYNAMIC_READ', 'GL_PROGRAM_BINARY_FORMATS', 'GL_LOW_INT', 'GL_DEPTH_STENCIL', 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR', 'GL_MAX_VERTEX_OUTPUT_COMPONENTS', 'GL_POINTS', 'GL_COMPRESSED_RG11_EAC', 'GL_RENDERBUFFER_BLUE_SIZE', 'GL_UNIFORM_NAME_LENGTH', 'GL_FASTEST', 'GL_SYNC_CONDITION', 'GL_TEXTURE_2D', 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS', 'GL_MAP_INVALIDATE_RANGE_BIT', 'GL_TEXTURE23', 'GL_TEXTURE22', 'GL_TEXTURE21', 'GL_TEXTURE20', 'GL_TEXTURE27', 'GL_TEXTURE26', 'GL_TEXTURE25', 'GL_TEXTURE24', 'GL_R8_SNORM', 'GL_TEXTURE29', 'GL_TEXTURE28', 'GL_ELEMENT_ARRAY_BUFFER_BINDING', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z', 'GL_LINE_LOOP', 'GL_READ_BUFFER', 'GL_MAP_FLUSH_EXPLICIT_BIT', 'GL_PACK_SKIP_PIXELS', 'GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS', 'GL_SUBPIXEL_BITS', 'GL_SRGB8', 'GL_GEQUAL', 'GL_UNIFORM_BLOCK_BINDING', 'GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT', 'GL_LINE_WIDTH', 'GL_UNIFORM_OFFSET', 'GL_R16F', 'GL_REPEAT', 'GL_TRANSFORM_FEEDBACK', 'GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC', 'GL_UNSIGNED_INT_SAMPLER_CUBE', 'GL_COLOR_ATTACHMENT4', 'GL_UNIFORM_SIZE', 'GL_FUNC_ADD', 'GL_FLOAT_MAT4x2', 'GL_SHADER_SOURCE_LENGTH', 'GL_CURRENT_VERTEX_ATTRIB', 'GL_ARRAY_BUFFER_BINDING', 'GL_POLYGON_OFFSET_UNITS', 'GL_DYNAMIC_DRAW', 'GL_OUT_OF_MEMORY', 'GL_NICEST', 'GL_IMPLEMENTATION_COLOR_READ_TYPE', 'GL_UNPACK_ROW_LENGTH', 'GL_CURRENT_PROGRAM', 'GL_BUFFER_MAPPED', 'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS', 'GL_RASTERIZER_DISCARD', 'GL_NUM_PROGRAM_BINARY_FORMATS', 'GL_STREAM_DRAW', 'GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER', 'GL_MAX_UNIFORM_BUFFER_BINDINGS', 'GL_SIGNALED', 'GL_FRAMEBUFFER', 'GL_MEDIUM_FLOAT', 'GL_STENCIL_TEST', 'GL_R11F_G11F_B10F', 'GL_LUMINANCE_ALPHA', 'GL_PIXEL_UNPACK_BUFFER_BINDING', 'GL_INVERT', 'GL_STENCIL_BACK_FAIL', 'GL_POLYGON_OFFSET_FACTOR', 'GL_TRANSFORM_FEEDBACK_VARYINGS', 'GL_DEPTH_COMPONENT32F', 'GL_TRIANGLE_FAN', 'GL_SYNC_FLUSH_COMMANDS_BIT', 'GL_ONE_MINUS_DST_ALPHA', 'GL_DRAW_FRAMEBUFFER_BINDING', 'GL_MAX_ELEMENTS_VERTICES', 'GL_STENCIL_BACK_WRITEMASK', 'GL_INVALID_FRAMEBUFFER_OPERATION', 'GL_BUFFER_ACCESS_FLAGS', 'GL_COMPRESSED_RGBA8_ETC2_EAC', 'GL_UNIFORM_BUFFER_SIZE', 'GL_TRIANGLES', 'GL_SAMPLER_2D_ARRAY_SHADOW', 'GL_DEPTH32F_STENCIL8', 'GL_MAX_ARRAY_TEXTURE_LAYERS', 'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING', 'GL_UNIFORM_MATRIX_STRIDE', 'GL_MAX_SERVER_WAIT_TIMEOUT', 'GL_SRGB8_ALPHA8', 'GL_PACK_ALIGNMENT', 'GL_SAMPLER_2D_ARRAY', 'GL_RENDERER', 'GL_MAX_COLOR_ATTACHMENTS', 'GL_ACTIVE_UNIFORM_BLOCKS', 'GL_UNPACK_SKIP_IMAGES', 'GL_STENCIL_BACK_FUNC', 'GL_RGB16I', 'GL_ACTIVE_TEXTURE', 'GL_TEXTURE_BASE_LEVEL', 'GL_INTERLEAVED_ATTRIBS', 'GL_RGB16F', 'GL_COMPRESSED_SIGNED_R11_EAC', 'GL_UNSIGNED_INT_SAMPLER_3D', 'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH', 'GL_TEXTURE_WRAP_R', 'GL_INT_VEC4', 'GL_INT_VEC3', 'GL_INT_VEC2', 'GL_STENCIL_FAIL', 'GL_MAX_VERTEX_ATTRIBS', 'GL_CONDITION_SATISFIED', 'GL_TEXTURE_IMMUTABLE_FORMAT', 'GL_FRAMEBUFFER_UNSUPPORTED', 'GL_DST_ALPHA', 'GL_LESS', 'GL_MAX_CUBE_MAP_TEXTURE_SIZE', 'GL_RGB565', 'GL_TRANSFORM_FEEDBACK_BINDING', 'GL_RENDERBUFFER_WIDTH', 'GL_READ_FRAMEBUFFER_BINDING', 'GL_RGBA4', 'GL_DRAW_BUFFER10', 'GL_DRAW_BUFFER11', 'GL_RGBA8', 'GL_DRAW_BUFFER13', 'GL_DRAW_BUFFER14', 'GL_LUMINANCE', 'GL_INFO_LOG_LENGTH', 'GL_DEPTH_WRITEMASK', 'GL_PRIMITIVE_RESTART_FIXED_INDEX', 'GL_SRC_ALPHA_SATURATE', 'GL_RENDERBUFFER_STENCIL_SIZE', 'GL_CONSTANT_ALPHA', 'GL_R16I', 'GL_RG8_SNORM', 'GL_PIXEL_PACK_BUFFER', 'GL_STATIC_READ', 'GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2', 'GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER', 'GL_VALIDATE_STATUS', 'GL_MAP_READ_BIT', 'GL_STENCIL_CLEAR_VALUE', 'GL_STENCIL_BUFFER_BIT', 'GL_TEXTURE_SWIZZLE_B', 'GL_COLOR_ATTACHMENT17', 'GL_BLEND_EQUATION_ALPHA', 'GL_RGBA_INTEGER', 'GL_ACTIVE_ATTRIBUTES', 'GL_MAX_RENDERBUFFER_SIZE', 'GL_COLOR_ATTACHMENT31', 'GL_COLOR_ATTACHMENT30', 'GL_STENCIL_PASS_DEPTH_PASS', 'GL_INCR_WRAP', 'GL_RENDERBUFFER_ALPHA_SIZE', 'GL_HIGH_INT', 'GL_COLOR_ATTACHMENT16', 'GL_DECR_WRAP', 'GL_ATTACHED_SHADERS', 'GL_MAX_FRAGMENT_INPUT_COMPONENTS', 'GL_SAMPLE_COVERAGE_INVERT', 'GL_LINES', 'GL_TEXTURE18', 'GL_TEXTURE19', 'GL_TEXTURE16', 'GL_TEXTURE17', 'GL_TEXTURE14', 'GL_GENERATE_MIPMAP_HINT', 'GL_TEXTURE12', 'GL_TEXTURE13', 'GL_TEXTURE10', 'GL_UNPACK_SKIP_ROWS', 'GL_BLEND_DST_ALPHA', 'GL_RGB', 'GL_INT_SAMPLER_CUBE', 'GL_CURRENT_QUERY', 'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED', 'GL_RGB5_A1', 'GL_VERTEX_SHADER', 'GL_TRANSFORM_FEEDBACK_BUFFER_START', 'GL_MAX_PROGRAM_TEXEL_OFFSET', 'GL_SHADER_BINARY_FORMATS', 'GL_CONSTANT_COLOR', 'GL_RGBA32F', 'GL_RGBA32I', 'GL_VERTEX_ATTRIB_ARRAY_TYPE', 'GL_PIXEL_UNPACK_BUFFER', 'GL_LINEAR_MIPMAP_NEAREST', 'GL_STENCIL_WRITEMASK', 'GL_RG8', 'GL_RGB10_A2', 'GL_ES_VERSION_2_0', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE', 'GL_VERSION', 'GL_MAP_UNSYNCHRONIZED_BIT', 'GL_ZERO', 'GL_ELEMENT_ARRAY_BUFFER', 'GL_SYNC_STATUS', 'GL_BUFFER_MAP_LENGTH', 'GL_MAX_ELEMENTS_INDICES', 'GL_UNSIGNED_NORMALIZED', 'GL_SRC_ALPHA', 'GL_TEXTURE_3D', 'GL_FIXED', 'GL_RGB8', 'GL_NOTEQUAL', 'GL_UNIFORM_ARRAY_STRIDE', 'GL_FLOAT_32_UNSIGNED_INT_24_8_REV', 'GL_INCR', 'GL_CULL_FACE', 'GL_SAMPLE_COVERAGE_VALUE', 'GL_RENDERBUFFER_RED_SIZE', 'GL_MAX_VIEWPORT_DIMS', 'GL_RG32UI', 'GL_NEVER', 'GL_TEXTURE15', 'GL_STENCIL_VALUE_MASK', 'GL_DRAW_BUFFER9', 'GL_COMPILE_STATUS', 'GL_FRAMEBUFFER_COMPLETE', 'GL_TEXTURE11', 'GL_COPY_READ_BUFFER', 'GL_SHADER_COMPILER', 'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS', 'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS', 'GL_RGBA', 'GL_SHORT', 'GL_READ_FRAMEBUFFER', 'GL_CW', 'GL_MIN_PROGRAM_TEXEL_OFFSET', 'GL_UNSIGNED_BYTE', 'GL_MAX_VERTEX_UNIFORM_COMPONENTS', 'GL_VENDOR', 'GL_TEXTURE_2D_ARRAY', 'GL_UNSIGNED_INT_10F_11F_11F_REV', 'GL_TEXTURE_BINDING_2D', 'GL_OBJECT_TYPE', 'GL_R8UI', 'GL_STATIC_DRAW', 'GL_RENDERBUFFER', 'GL_FLOAT_MAT2x3', 'GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE', 'GL_FLOAT_MAT2x4', 'GL_RGB8I', 'GL_COLOR_ATTACHMENT18', 'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE', 'GL_TRANSFORM_FEEDBACK_ACTIVE', 'GL_SEPARATE_ATTRIBS', 'GL_SAMPLER_3D', 'GL_MAX', 'GL_STENCIL_INDEX8', 'GL_DEPTH_BITS', 'GL_RGB8UI', 'GL_INVALID_INDEX', 'GL_COMPRESSED_SRGB8_ETC2', 'GL_BLEND_DST_RGB', 'GL_SAMPLER_2D_SHADOW', 'GL_TEXTURE_BINDING_2D_ARRAY', 'GL_RG16F', 'GL_SAMPLER_CUBE', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL', 'GL_RED_BITS', 'GL_RG16I', 'GL_PIXEL_PACK_BUFFER_BINDING', 'GL_STENCIL_ATTACHMENT', 'GL_SAMPLE_COVERAGE', 'GL_ANY_SAMPLES_PASSED_CONSERVATIVE', 'GL_DRAW_FRAMEBUFFER', 'GL_RGB10_A2UI', 'GL_SAMPLES', 'GLchar', 'GLenum', 'GLboolean', 'GLbitfield', 'GLbyte', 'GLshort', 'GLint', 'GLint64', 'GLsizei', 'GLubyte', 'GLushort', 'GLuint', 'GLfloat', 'GLclampf', 'GLfixed', 'GLintptr', 'GLsizeiptr', 'GLclampx', 'void', 'GLvoid', 'GLsync']