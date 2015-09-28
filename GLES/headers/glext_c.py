# Generated Files. DO NOT EDIT
# Generated on: 09/28/15 10:48:07
import ctypes
from objc_util import *
from GLConstants import *

DEBUG = 0
loaded = [0, 0]

# GLES Constants
GL_TEXTURE_CROP_RECT_OES = 0x00008b9d
GL_MATRIX_INDEX_ARRAY_SIZE_OES = 0x00008846
GL_OES_packed_depth_stencil = 0x00000001
GL_DEPTH_EXT = 0x00001801
GL_COLOR_EXT = 0x00001800
GL_QCOM_tiled_rendering = 0x00000001
GL_RGB16F_EXT = 0x0000881b
GL_CLIP_PLANE1_IMG = 0x00003001
GL_NV_fence = 0x00000001
GL_CLIP_PLANE3_IMG = 0x00003003
GL_OES_blend_subtract = 0x00000001
GL_IMG_texture_compression_pvrtc = 0x00000001
GL_SRGB_ALPHA_EXT = 0x00008c42
GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES = 0x0000851c
GL_REFLECTION_MAP_OES = 0x00008512
GL_COLOR_BUFFER_BIT7_QCOM = 0x00000080
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES = 0x00008518
GL_BLEND_DST_RGB_OES = 0x000080c8
GL_RENDERBUFFER_WIDTH_OES = 0x00008d42
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_APPLE = 0x00008d56
GL_DEPTH_BUFFER_BIT3_QCOM = 0x00000800
GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES = 0x0000898d
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES = 0x00008cd7
GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 0x00008c02
GL_CONTEXT_ROBUST_ACCESS_EXT = 0x000090f3
GL_QCOM_perfmon_global_mode = 0x00000001
GL_RGB32F_EXT = 0x00008815
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES = 0x00008cda
GL_CLIP_PLANE0_IMG = 0x00003000
GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES = 0x00008d68
GL_OES_single_precision = 0x00000001
GL_EXT_multisampled_render_to_texture = 0x00000001
GL_OES_texture_env_crossbar = 0x00000001
GL_WRITEONLY_RENDERING_QCOM = 0x00008823
GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT = 0x00008365
GL_TEXTURE_BINDING_EXTERNAL_OES = 0x00008d67
GL_NONE_OES = 0x00000000
GL_OES_texture_cube_map = 0x00000001
GL_OES_query_matrix = 0x00000001
GL_ALPHA32F_EXT = 0x00008816
GL_SYNC_FENCE_APPLE = 0x00009116
GL_DEPTH_COMPONENT24_OES = 0x000081a6
GL_FRAMEBUFFER_UNSUPPORTED_OES = 0x00008cdd
GL_RGBA32F_EXT = 0x00008814
GL_READ_FRAMEBUFFER_BINDING_APPLE = 0x00008caa
GL_LUMINANCE32F_EXT = 0x00008818
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES = 0x00008517
GL_MAP_UNSYNCHRONIZED_BIT_EXT = 0x00000020
GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 0x00008c00
GL_DRAW_FRAMEBUFFER_BINDING_APPLE = 0x00008ca6
GL_APPLE_texture_max_level = 0x00000001
GL_TEXTURE_HEIGHT_QCOM = 0x00008bd3
GL_RENDERBUFFER_OES = 0x00008d41
GL_FENCE_CONDITION_NV = 0x000084f4
GL_TEXTURE_CUBE_MAP_OES = 0x00008513
GL_EXT_multi_draw_arrays = 0x00000001
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 0x000083f0
GL_OES_fbo_render_mipmap = 0x00000001
GL_RECIP_ADD_SIGNED_ALPHA_IMG = 0x00008c05
GL_STENCIL_BUFFER_BIT5_QCOM = 0x00200000
GL_UNKNOWN_CONTEXT_RESET_EXT = 0x00008255
GL_OES_stencil_wrap = 0x00000001
GL_TEXTURE_BINDING_CUBE_MAP_OES = 0x00008514
GL_READ_FRAMEBUFFER_APPLE = 0x00008ca8
GL_SYNC_FLUSH_COMMANDS_BIT_APPLE = 0x00000001
GL_TEXTURE_INTERNAL_FORMAT_QCOM = 0x00008bd5
GL_STENCIL_BUFFER_BIT2_QCOM = 0x00040000
GL_RENDERBUFFER_HEIGHT_OES = 0x00008d43
GL_TEXTURE_ALPHA_MODULATE_IMG = 0x00008c06
GL_NORMAL_MAP_OES = 0x00008511
GL_LUMINANCE8_ALPHA8_EXT = 0x00008045
GL_MAX_EXT = 0x00008008
GL_MAX_VERTEX_UNITS_OES = 0x000086a4
GL_DEPTH_BUFFER_BIT7_QCOM = 0x00008000
GL_TEXTURE_LOD_BIAS_EXT = 0x00008501
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES = 0x00008519
GL_TEXTURE_FORMAT_QCOM = 0x00008bd6
GL_MODULATE_COLOR_IMG = 0x00008c04
GL_RENDERBUFFER_BINDING_OES = 0x00008ca7
GL_EXT_texture_compression_dxt1 = 0x00000001
GL_OES_extended_matrix_palette = 0x00000001
GL_STENCIL_BUFFER_BIT1_QCOM = 0x00020000
GL_RENDERBUFFER_STENCIL_SIZE_OES = 0x00008d55
GL_SYNC_OBJECT_APPLE = 0x00008a53
GL_SRGB8_ALPHA8_EXT = 0x00008c43
GL_BLEND_SRC_ALPHA_OES = 0x000080cb
GL_MULTISAMPLE_BUFFER_BIT2_QCOM = 0x04000000
GL_MAX_SERVER_WAIT_TIMEOUT_APPLE = 0x00009111
GL_OES_blend_equation_separate = 0x00000001
GL_MULTISAMPLE_BUFFER_BIT3_QCOM = 0x08000000
GL_RENDERBUFFER_DEPTH_SIZE_OES = 0x00008d54
GL_MATRIX_INDEX_ARRAY_STRIDE_OES = 0x00008848
GL_WEIGHT_ARRAY_OES = 0x000086ad
GL_BUFFER_ACCESS_OES = 0x000088bb
GL_OES_matrix_get = 0x00000001
GL_LUMINANCE8_EXT = 0x00008040
GL_OES_EGL_image_external = 0x00000001
GL_RGB10_EXT = 0x00008052
GL_EXT_map_buffer_range = 0x00000001
GL_CONDITION_SATISFIED_APPLE = 0x0000911c
GL_OES_stencil4 = 0x00000001
GL_BLEND_EQUATION_ALPHA_OES = 0x0000883d
GL_FUNC_ADD_OES = 0x00008006
GL_DEPTH_COMPONENT16_OES = 0x000081a5
GL_WEIGHT_ARRAY_POINTER_OES = 0x000086ac
GL_EXT_blend_minmax = 0x00000001
GL_MAX_CLIP_PLANES_IMG = 0x00000d32
GL_STENCIL_BUFFER_BIT0_QCOM = 0x00010000
GL_BLEND_DST_ALPHA_OES = 0x000080ca
GL_STENCIL_INDEX1_OES = 0x00008d46
GL_TEXTURE_DEPTH_QCOM = 0x00008bd4
GL_RENDERBUFFER_BLUE_SIZE_OES = 0x00008d52
GL_OES_byte_coordinates = 0x00000001
GL_MAX_SAMPLES_APPLE = 0x00008d57
GL_COLOR_BUFFER_BIT4_QCOM = 0x00000010
GL_RENDERBUFFER_GREEN_SIZE_OES = 0x00008d51
GL_WRITE_ONLY_OES = 0x000088b9
GL_IMG_read_format = 0x00000001
GL_OES_blend_func_separate = 0x00000001
GL_MULTISAMPLE_BUFFER_BIT7_QCOM = 0x80000000
GL_BGRA_EXT = 0x000080e1
GL_OES_depth24 = 0x00000001
GL_MULTISAMPLE_BUFFER_BIT6_QCOM = 0x40000000
GL_FENCE_STATUS_NV = 0x000084f3
GL_TEXTURE_OBJECT_VALID_QCOM = 0x00008bdb
GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG = 0x00008c01
GL_LUMINANCE_ALPHA16F_EXT = 0x0000881f
GL_OES_stencil1 = 0x00000001
GL_AMD_compressed_ATC_texture = 0x00000001
GL_OES_matrix_palette = 0x00000001
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES = 0x00008cd2
GL_FACTOR_ALPHA_MODULATE_IMG = 0x00008c07
GL_MIRRORED_REPEAT_OES = 0x00008370
GL_RENDERBUFFER_RED_SIZE_OES = 0x00008d50
GL_QCOM_writeonly_rendering = 0x00000001
GL_TEXTURE_GEN_MODE_OES = 0x00002500
GL_COLOR_BUFFER_BIT3_QCOM = 0x00000008
GL_WEIGHT_ARRAY_BUFFER_BINDING_OES = 0x0000889e
GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG = 0x00008c03
GL_UNSIGNALED_APPLE = 0x00009118
GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES = 0x0000898e
GL_STENCIL_ATTACHMENT_OES = 0x00008d20
GL_OBJECT_TYPE_APPLE = 0x00009112
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES = 0x0000851a
GL_RENDERBUFFER_SAMPLES_EXT = 0x00008cab
GL_APPLE_framebuffer_multisample = 0x00000001
GL_RENDERBUFFER_ALPHA_SIZE_OES = 0x00008d53
GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE = 0x00009117
GL_SIGNALED_APPLE = 0x00009119
GL_RGBA8_OES = 0x00008058
GL_APPLE_sync = 0x00000001
GL_EXT_robustness = 0x00000001
GL_ALL_COMPLETED_NV = 0x000084f2
GL_SYNC_STATUS_APPLE = 0x00009114
GL_BLEND_EQUATION_RGB_OES = 0x00008009
GL_MULTISAMPLE_BUFFER_BIT0_QCOM = 0x01000000
GL_RESET_NOTIFICATION_STRATEGY_EXT = 0x00008256
GL_UNSIGNED_INT_24_8_OES = 0x000084fa
GL_CLIP_PLANE5_IMG = 0x00003005
GL_INCR_WRAP_OES = 0x00008507
GL_MAX_SAMPLES_IMG = 0x00009135
GL_OES_framebuffer_object = 0x00000001
GL_MAP_READ_BIT_EXT = 0x00000001
GL_DEPTH_BUFFER_BIT6_QCOM = 0x00004000
GL_COLOR_BUFFER_BIT6_QCOM = 0x00000040
GL_RGB10_A2_EXT = 0x00008059
GL_MAP_FLUSH_EXPLICIT_BIT_EXT = 0x00000010
GL_COLOR_BUFFER_BIT0_QCOM = 0x00000001
GL_WEIGHT_ARRAY_TYPE_OES = 0x000086a9
GL_EXT_read_format_bgra = 0x00000001
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES = 0x00008cd6
GL_DEPTH_BUFFER_BIT0_QCOM = 0x00000100
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES = 0x00008cd3
GL_FRAMEBUFFER_COMPLETE_OES = 0x00008cd5
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT = 0x00008d56
GL_LOSE_CONTEXT_ON_RESET_EXT = 0x00008252
GL_QCOM_extended_get2 = 0x00000001
GL_WEIGHT_ARRAY_STRIDE_OES = 0x000086aa
GL_TEXTURE_IMMUTABLE_FORMAT_EXT = 0x0000912f
GL_STATE_RESTORE = 0x00008bdc
GL_DEPTH_BUFFER_BIT4_QCOM = 0x00001000
GL_DEPTH_ATTACHMENT_OES = 0x00008d00
GL_TEXTURE_GEN_STR_OES = 0x00008d60
GL_FRAMEBUFFER_BINDING_OES = 0x00008ca6
GL_WEIGHT_ARRAY_SIZE_OES = 0x000086ab
GL_MATRIX_INDEX_ARRAY_TYPE_OES = 0x00008847
GL_3DC_XY_AMD = 0x000087fa
GL_MIN_EXT = 0x00008007
GL_OES_depth32 = 0x00000001
GL_ALPHA8_EXT = 0x0000803c
GL_STENCIL_INDEX4_OES = 0x00008d47
GL_CLIP_PLANE2_IMG = 0x00003002
GL_FRAMEBUFFER_OES = 0x00008d40
GL_APPLE_texture_2D_limited_npot = 0x00000001
GL_INNOCENT_CONTEXT_RESET_EXT = 0x00008254
GL_OES_EGL_image = 0x00000001
GL_BLEND_EQUATION_OES = 0x00008009
GL_STENCIL_BUFFER_BIT3_QCOM = 0x00080000
GL_TEXTURE_TARGET_QCOM = 0x00008bda
GL_VERTEX_ARRAY_BINDING_OES = 0x000085b5
GL_MAX_PALETTE_MATRICES_OES = 0x00008842
GL_DEPTH_BUFFER_BIT1_QCOM = 0x00000200
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT = 0x00008210
GL_RENDERBUFFER_SAMPLES_APPLE = 0x00008cab
GL_TIMEOUT_IGNORED_APPLE = 0xffffffffffffffff
GL_DECR_WRAP_OES = 0x00008508
GL_EXT_texture_lod_bias = 0x00000001
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES = 0x00008cd9
GL_TEXTURE_FILTER_CONTROL_EXT = 0x00008500
GL_EXT_sRGB = 0x00000001
GL_EXT_texture_filter_anisotropic = 0x00000001
GL_OES_texture_mirrored_repeat = 0x00000001
GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES = 0x0000898f
GL_RGB565_OES = 0x00008d62
GL_RGB5_A1_OES = 0x00008057
GL_OES_rgb8_rgba8 = 0x00000001
GL_RENDERBUFFER_INTERNAL_FORMAT_OES = 0x00008d44
GL_IMG_multisampled_render_to_texture = 0x00000001
GL_MAP_INVALIDATE_BUFFER_BIT_EXT = 0x00000008
GL_COLOR_BUFFER_BIT5_QCOM = 0x00000020
GL_MATRIX_INDEX_ARRAY_OES = 0x00008844
GL_ADD_BLEND_IMG = 0x00008c09
GL_ETC1_RGB8_OES = 0x00008d64
GL_WAIT_FAILED_APPLE = 0x0000911d
GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES = 0x00008b9e
GL_DEPTH_BUFFER_BIT5_QCOM = 0x00002000
GL_NO_RESET_NOTIFICATION_EXT = 0x00008261
GL_MAX_TEXTURE_LOD_BIAS_EXT = 0x000084fd
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT = 0x00008d6c
GL_SYNC_FLAGS_APPLE = 0x00009115
GL_DEPTH_BUFFER_BIT2_QCOM = 0x00000400
GL_EXT_texture_storage = 0x00000001
GL_OES_required_internalformat = 0x00000001
GL_IMG_user_clip_plane = 0x00000001
GL_MATRIX_PALETTE_OES = 0x00008840
GL_COLOR_BUFFER_BIT1_QCOM = 0x00000002
GL_DOT3_RGBA_IMG = 0x000086af
GL_AMD_compressed_3DC_texture = 0x00000001
GL_BGRA_IMG = 0x000080e1
GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG = 0x00008365
GL_RGB8_OES = 0x00008051
GL_OES_element_index_uint = 0x00000001
GL_RENDERBUFFER_SAMPLES_IMG = 0x00009133
GL_STENCIL_INDEX8_OES = 0x00008d48
GL_OES_draw_texture = 0x00000001
GL_MAX_SAMPLES_EXT = 0x00008d57
GL_PERFMON_GLOBAL_MODE_QCOM = 0x00008fa0
GL_OES_mapbuffer = 0x00000001
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG = 0x00009134
GL_UNSIGNED_INT = 0x00001405
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 0x000083f1
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES = 0x00008cd1
GL_MATRIX_INDEX_ARRAY_POINTER_OES = 0x00008849
GL_OES_compressed_ETC1_RGB8_texture = 0x00000001
GL_FRAGMENT_ALPHA_MODULATE_IMG = 0x00008c08
GL_ALREADY_SIGNALED_APPLE = 0x0000911a
GL_MULTISAMPLE_BUFFER_BIT1_QCOM = 0x02000000
GL_BUFFER_MAPPED_OES = 0x000088bc
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 0x000084ff
GL_TEXTURE_IMAGE_VALID_QCOM = 0x00008bd8
GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD = 0x000087ee
GL_TEXTURE_WIDTH_QCOM = 0x00008bd2
GL_LUMINANCE_ALPHA32F_EXT = 0x00008819
GL_INVALID_FRAMEBUFFER_OPERATION_OES = 0x00000506
GL_OES_fixed_point = 0x00000001
GL_RGBA4_OES = 0x00008056
GL_CURRENT_PALETTE_MATRIX_OES = 0x00008843
GL_EXT_texture_format_BGRA8888 = 0x00000001
GL_DRAW_FRAMEBUFFER_APPLE = 0x00008ca9
GL_BUFFER_MAP_POINTER_OES = 0x000088bd
GL_COLOR_BUFFER_BIT2_QCOM = 0x00000004
GL_3DC_X_AMD = 0x000087f9
GL_MAP_INVALIDATE_RANGE_BIT_EXT = 0x00000004
GL_QCOM_extended_get = 0x00000001
GL_MAP_WRITE_BIT_EXT = 0x00000002
GL_TEXTURE_NUM_LEVELS_QCOM = 0x00008bd9
GL_FIXED_OES = 0x0000140c
GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT = 0x00008366
GL_DEPTH_COMPONENT32_OES = 0x000081a7
GL_STENCIL_BUFFER_BIT7_QCOM = 0x00800000
GL_STENCIL_BUFFER_BIT4_QCOM = 0x00100000
GL_DEPTH24_STENCIL8_OES = 0x000088f0
GL_APPLE_copy_texture_levels = 0x00000001
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES = 0x00008516
GL_TEXTURE_MAX_ANISOTROPY_EXT = 0x000084fe
GL_GUILTY_CONTEXT_RESET_EXT = 0x00008253
GL_ARM_rgba8 = 0x00000001
GL_BLEND_SRC_RGB_OES = 0x000080c9
GL_MULTISAMPLE_BUFFER_BIT4_QCOM = 0x10000000
GL_FUNC_SUBTRACT_OES = 0x0000800a
GL_MULTISAMPLE_BUFFER_BIT5_QCOM = 0x20000000
GL_LUMINANCE16F_EXT = 0x0000881e
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES = 0x00008cd0
GL_TIMEOUT_EXPIRED_APPLE = 0x0000911b
GL_STENCIL_BUFFER_BIT6_QCOM = 0x00400000
GL_BGRA8_EXT = 0x000093a1
GL_ATC_RGB_AMD = 0x00008c92
GL_TEXTURE_SAMPLES_IMG = 0x00009136
GL_CLIP_PLANE4_IMG = 0x00003004
GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES = 0x00008515
GL_IMG_texture_env_enhanced_fixed_function = 0x00000001
GL_TEXTURE_MAX_LEVEL_APPLE = 0x0000813d
GL_TEXTURE_TYPE_QCOM = 0x00008bd7
GL_TEXTURE_EXTERNAL_OES = 0x00008d65
GL_STENCIL_EXT = 0x00001802
GL_APPLE_texture_format_BGRA8888 = 0x00000001
GL_QCOM_driver_control = 0x00000001
GL_EXT_discard_framebuffer = 0x00000001
GL_ALPHA16F_EXT = 0x0000881c
GL_SRGB_EXT = 0x00008c40
GL_FUNC_REVERSE_SUBTRACT_OES = 0x0000800b
GL_COLOR_ATTACHMENT0_OES = 0x00008ce0
GL_SYNC_CONDITION_APPLE = 0x00009113
GL_OES_stencil8 = 0x00000001
GL_MAX_RENDERBUFFER_SIZE_OES = 0x000084e8
GL_DEPTH_STENCIL_OES = 0x000084f9
GL_OES_vertex_array_object = 0x00000001
GL_ATC_RGBA_EXPLICIT_ALPHA_AMD = 0x00008c93

# GL Functions
try:
    def glBlendEquationSeparateOES(modeRGB, modeAlpha, modeRGB_t=GLenum, modeAlpha_t=GLenum):
        restype = None
        argtypes = [modeRGB_t, modeAlpha_t]
        cfunc = c.glBlendEquationSeparateOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(modeRGB, modeAlpha)
    # Check if the function actually exists
    f = c.glBlendEquationSeparateOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendFuncSeparateOES(srcRGB, dstRGB, srcAlpha, dstAlpha, srcRGB_t=GLenum, dstRGB_t=GLenum, srcAlpha_t=GLenum, dstAlpha_t=GLenum):
        restype = None
        argtypes = [srcRGB_t, dstRGB_t, srcAlpha_t, dstAlpha_t]
        cfunc = c.glBlendFuncSeparateOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(srcRGB, dstRGB, srcAlpha, dstAlpha)
    # Check if the function actually exists
    f = c.glBlendFuncSeparateOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBlendEquationOES(mode, mode_t=GLenum):
        restype = None
        argtypes = [mode_t]
        cfunc = c.glBlendEquationOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mode)
    # Check if the function actually exists
    f = c.glBlendEquationOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexsOES(x, y, z, width, height, x_t=GLshort, y_t=GLshort, z_t=GLshort, width_t=GLshort, height_t=GLshort):
        restype = None
        argtypes = [x_t, y_t, z_t, width_t, height_t]
        cfunc = c.glDrawTexsOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z, width, height)
    # Check if the function actually exists
    f = c.glDrawTexsOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexiOES(x, y, z, width, height, x_t=GLint, y_t=GLint, z_t=GLint, width_t=GLint, height_t=GLint):
        restype = None
        argtypes = [x_t, y_t, z_t, width_t, height_t]
        cfunc = c.glDrawTexiOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z, width, height)
    # Check if the function actually exists
    f = c.glDrawTexiOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexxOES(x, y, z, width, height, x_t=GLfixed, y_t=GLfixed, z_t=GLfixed, width_t=GLfixed, height_t=GLfixed):
        restype = None
        argtypes = [x_t, y_t, z_t, width_t, height_t]
        cfunc = c.glDrawTexxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z, width, height)
    # Check if the function actually exists
    f = c.glDrawTexxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexsvOES(param0, param0_t=GLshort):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glDrawTexsvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glDrawTexsvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexivOES(param0, param0_t=GLint):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glDrawTexivOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glDrawTexivOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexxvOES(param0, param0_t=GLfixed):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glDrawTexxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glDrawTexxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexfOES(x, y, z, width, height, x_t=GLfloat, y_t=GLfloat, z_t=GLfloat, width_t=GLfloat, height_t=GLfloat):
        restype = None
        argtypes = [x_t, y_t, z_t, width_t, height_t]
        cfunc = c.glDrawTexfOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z, width, height)
    # Check if the function actually exists
    f = c.glDrawTexfOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDrawTexfvOES(param0, param0_t=GLfloat):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glDrawTexfvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glDrawTexfvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glEGLImageTargetTexture2DOES(target, image, target_t=GLenum, image_t=GLeglImageOES):
        restype = None
        argtypes = [target_t, image_t]
        cfunc = c.glEGLImageTargetTexture2DOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, image)
    # Check if the function actually exists
    f = c.glEGLImageTargetTexture2DOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glEGLImageTargetRenderbufferStorageOES(target, image, target_t=GLenum, image_t=GLeglImageOES):
        restype = None
        argtypes = [target_t, image_t]
        cfunc = c.glEGLImageTargetRenderbufferStorageOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, image)
    # Check if the function actually exists
    f = c.glEGLImageTargetRenderbufferStorageOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glAlphaFuncxOES(func, ref, func_t=GLenum, ref_t=GLclampx):
        restype = None
        argtypes = [func_t, ref_t]
        cfunc = c.glAlphaFuncxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(func, ref)
    # Check if the function actually exists
    f = c.glAlphaFuncxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClearColorxOES(red, green, blue, alpha, red_t=GLclampx, green_t=GLclampx, blue_t=GLclampx, alpha_t=GLclampx):
        restype = None
        argtypes = [red_t, green_t, blue_t, alpha_t]
        cfunc = c.glClearColorxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glClearColorxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClearDepthxOES(depth, depth_t=GLclampx):
        restype = None
        argtypes = [depth_t]
        cfunc = c.glClearDepthxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(depth)
    # Check if the function actually exists
    f = c.glClearDepthxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClipPlanexOES(plane, param0, plane_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [plane_t, param0_t]
        cfunc = c.glClipPlanexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(plane, param0)
    # Check if the function actually exists
    f = c.glClipPlanexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glColor4xOES(red, green, blue, alpha, red_t=GLfixed, green_t=GLfixed, blue_t=GLfixed, alpha_t=GLfixed):
        restype = None
        argtypes = [red_t, green_t, blue_t, alpha_t]
        cfunc = c.glColor4xOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(red, green, blue, alpha)
    # Check if the function actually exists
    f = c.glColor4xOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDepthRangexOES(zNear, zFar, zNear_t=GLclampx, zFar_t=GLclampx):
        restype = None
        argtypes = [zNear_t, zFar_t]
        cfunc = c.glDepthRangexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(zNear, zFar)
    # Check if the function actually exists
    f = c.glDepthRangexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFogxOES(pname, param, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [pname_t, param_t]
        cfunc = c.glFogxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glFogxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFogxvOES(pname, param0, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [pname_t, param0_t]
        cfunc = c.glFogxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glFogxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFrustumxOES(left, right, bottom, top, zNear, zFar, left_t=GLfixed, right_t=GLfixed, bottom_t=GLfixed, top_t=GLfixed, zNear_t=GLfixed, zFar_t=GLfixed):
        restype = None
        argtypes = [left_t, right_t, bottom_t, top_t, zNear_t, zFar_t]
        cfunc = c.glFrustumxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glFrustumxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetClipPlanexOES(pname, eqn, pname_t=GLenum, eqn_t=(GLfixed * 4)):
        restype = None
        argtypes = [pname_t, eqn_t]
        cfunc = c.glGetClipPlanexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, eqn)
    # Check if the function actually exists
    f = c.glGetClipPlanexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetFixedvOES(pname, param0, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [pname_t, param0_t]
        cfunc = c.glGetFixedvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetFixedvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetLightxvOES(light, pname, param0, light_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [light_t, pname_t, param0_t]
        cfunc = c.glGetLightxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param0)
    # Check if the function actually exists
    f = c.glGetLightxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetMaterialxvOES(face, pname, param0, face_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [face_t, pname_t, param0_t]
        cfunc = c.glGetMaterialxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param0)
    # Check if the function actually exists
    f = c.glGetMaterialxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexEnvxvOES(env, pname, param0, env_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [env_t, pname_t, param0_t]
        cfunc = c.glGetTexEnvxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(env, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexEnvxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexParameterxvOES(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
        cfunc = c.glGetTexParameterxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexParameterxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLightModelxOES(pname, param, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [pname_t, param_t]
        cfunc = c.glLightModelxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glLightModelxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLightModelxvOES(pname, param0, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [pname_t, param0_t]
        cfunc = c.glLightModelxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glLightModelxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLightxOES(light, pname, param, light_t=GLenum, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [light_t, pname_t, param_t]
        cfunc = c.glLightxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param)
    # Check if the function actually exists
    f = c.glLightxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLightxvOES(light, pname, param0, light_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [light_t, pname_t, param0_t]
        cfunc = c.glLightxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(light, pname, param0)
    # Check if the function actually exists
    f = c.glLightxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLineWidthxOES(width, width_t=GLfixed):
        restype = None
        argtypes = [width_t]
        cfunc = c.glLineWidthxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(width)
    # Check if the function actually exists
    f = c.glLineWidthxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLoadMatrixxOES(param0, param0_t=GLfixed):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glLoadMatrixxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glLoadMatrixxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMaterialxOES(face, pname, param, face_t=GLenum, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [face_t, pname_t, param_t]
        cfunc = c.glMaterialxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param)
    # Check if the function actually exists
    f = c.glMaterialxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMaterialxvOES(face, pname, param0, face_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [face_t, pname_t, param0_t]
        cfunc = c.glMaterialxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(face, pname, param0)
    # Check if the function actually exists
    f = c.glMaterialxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMultMatrixxOES(param0, param0_t=GLfixed):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glMultMatrixxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glMultMatrixxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMultiTexCoord4xOES(target, s, t, r, q, target_t=GLenum, s_t=GLfixed, t_t=GLfixed, r_t=GLfixed, q_t=GLfixed):
        restype = None
        argtypes = [target_t, s_t, t_t, r_t, q_t]
        cfunc = c.glMultiTexCoord4xOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, s, t, r, q)
    # Check if the function actually exists
    f = c.glMultiTexCoord4xOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glNormal3xOES(nx, ny, nz, nx_t=GLfixed, ny_t=GLfixed, nz_t=GLfixed):
        restype = None
        argtypes = [nx_t, ny_t, nz_t]
        cfunc = c.glNormal3xOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(nx, ny, nz)
    # Check if the function actually exists
    f = c.glNormal3xOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glOrthoxOES(left, right, bottom, top, zNear, zFar, left_t=GLfixed, right_t=GLfixed, bottom_t=GLfixed, top_t=GLfixed, zNear_t=GLfixed, zFar_t=GLfixed):
        restype = None
        argtypes = [left_t, right_t, bottom_t, top_t, zNear_t, zFar_t]
        cfunc = c.glOrthoxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glOrthoxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glPointParameterxOES(pname, param, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [pname_t, param_t]
        cfunc = c.glPointParameterxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param)
    # Check if the function actually exists
    f = c.glPointParameterxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glPointParameterxvOES(pname, param0, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [pname_t, param0_t]
        cfunc = c.glPointParameterxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glPointParameterxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glPointSizexOES(size, size_t=GLfixed):
        restype = None
        argtypes = [size_t]
        cfunc = c.glPointSizexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size)
    # Check if the function actually exists
    f = c.glPointSizexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glPolygonOffsetxOES(factor, units, factor_t=GLfixed, units_t=GLfixed):
        restype = None
        argtypes = [factor_t, units_t]
        cfunc = c.glPolygonOffsetxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(factor, units)
    # Check if the function actually exists
    f = c.glPolygonOffsetxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glRotatexOES(angle, x, y, z, angle_t=GLfixed, x_t=GLfixed, y_t=GLfixed, z_t=GLfixed):
        restype = None
        argtypes = [angle_t, x_t, y_t, z_t]
        cfunc = c.glRotatexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(angle, x, y, z)
    # Check if the function actually exists
    f = c.glRotatexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glSampleCoveragexOES(value, invert, value_t=GLclampx, invert_t=GLboolean):
        restype = None
        argtypes = [value_t, invert_t]
        cfunc = c.glSampleCoveragexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(value, invert)
    # Check if the function actually exists
    f = c.glSampleCoveragexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glScalexOES(x, y, z, x_t=GLfixed, y_t=GLfixed, z_t=GLfixed):
        restype = None
        argtypes = [x_t, y_t, z_t]
        cfunc = c.glScalexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z)
    # Check if the function actually exists
    f = c.glScalexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexEnvxOES(target, pname, param, target_t=GLenum, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [target_t, pname_t, param_t]
        cfunc = c.glTexEnvxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexEnvxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexEnvxvOES(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
        cfunc = c.glTexEnvxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexEnvxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexParameterxOES(target, pname, param, target_t=GLenum, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [target_t, pname_t, param_t]
        cfunc = c.glTexParameterxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glTexParameterxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexParameterxvOES(target, pname, param0, target_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [target_t, pname_t, param0_t]
        cfunc = c.glTexParameterxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param0)
    # Check if the function actually exists
    f = c.glTexParameterxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTranslatexOES(x, y, z, x_t=GLfixed, y_t=GLfixed, z_t=GLfixed):
        restype = None
        argtypes = [x_t, y_t, z_t]
        cfunc = c.glTranslatexOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, z)
    # Check if the function actually exists
    f = c.glTranslatexOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsRenderbufferOES(renderbuffer, renderbuffer_t=GLuint):
        restype = GLboolean
        argtypes = [renderbuffer_t]
        cfunc = c.glIsRenderbufferOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(renderbuffer)
    # Check if the function actually exists
    f = c.glIsRenderbufferOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindRenderbufferOES(target, renderbuffer, target_t=GLenum, renderbuffer_t=GLuint):
        restype = None
        argtypes = [target_t, renderbuffer_t]
        cfunc = c.glBindRenderbufferOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, renderbuffer)
    # Check if the function actually exists
    f = c.glBindRenderbufferOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteRenderbuffersOES(n, renderbuffers, n_t=GLsizei, renderbuffers_t=ctypes.POINTER(GLuint)):
        restype = None
        argtypes = [n_t, renderbuffers_t]
        cfunc = c.glDeleteRenderbuffersOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, renderbuffers)
    # Check if the function actually exists
    f = c.glDeleteRenderbuffersOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenRenderbuffersOES(n, renderbuffers, n_t=GLsizei, renderbuffers_t=ctypes.POINTER(GLuint)):
        restype = None
        argtypes = [n_t, renderbuffers_t]
        cfunc = c.glGenRenderbuffersOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, renderbuffers)
    # Check if the function actually exists
    f = c.glGenRenderbuffersOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorageOES(target, internalformat, width, height, target_t=GLenum, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [target_t, internalformat_t, width_t, height_t]
        cfunc = c.glRenderbufferStorageOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, internalformat, width, height)
    # Check if the function actually exists
    f = c.glRenderbufferStorageOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetRenderbufferParameterivOES(target, pname, params, target_t=GLenum, pname_t=GLenum, params_t=ctypes.POINTER(GLint)):
        restype = None
        argtypes = [target_t, pname_t, params_t]
        cfunc = c.glGetRenderbufferParameterivOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, params)
    # Check if the function actually exists
    f = c.glGetRenderbufferParameterivOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsFramebufferOES(framebuffer, framebuffer_t=GLuint):
        restype = GLboolean
        argtypes = [framebuffer_t]
        cfunc = c.glIsFramebufferOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(framebuffer)
    # Check if the function actually exists
    f = c.glIsFramebufferOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindFramebufferOES(target, framebuffer, target_t=GLenum, framebuffer_t=GLuint):
        restype = None
        argtypes = [target_t, framebuffer_t]
        cfunc = c.glBindFramebufferOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, framebuffer)
    # Check if the function actually exists
    f = c.glBindFramebufferOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteFramebuffersOES(n, framebuffers, n_t=GLsizei, framebuffers_t=ctypes.POINTER(GLuint)):
        restype = None
        argtypes = [n_t, framebuffers_t]
        cfunc = c.glDeleteFramebuffersOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, framebuffers)
    # Check if the function actually exists
    f = c.glDeleteFramebuffersOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenFramebuffersOES(n, framebuffers, n_t=GLsizei, framebuffers_t=ctypes.POINTER(GLuint)):
        restype = None
        argtypes = [n_t, framebuffers_t]
        cfunc = c.glGenFramebuffersOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, framebuffers)
    # Check if the function actually exists
    f = c.glGenFramebuffersOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCheckFramebufferStatusOES(target, target_t=GLenum):
        restype = GLenum
        argtypes = [target_t]
        cfunc = c.glCheckFramebufferStatusOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glCheckFramebufferStatusOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFramebufferRenderbufferOES(target, attachment, renderbuffertarget, renderbuffer, target_t=GLenum, attachment_t=GLenum, renderbuffertarget_t=GLenum, renderbuffer_t=GLuint):
        restype = None
        argtypes = [target_t, attachment_t, renderbuffertarget_t, renderbuffer_t]
        cfunc = c.glFramebufferRenderbufferOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, renderbuffertarget, renderbuffer)
    # Check if the function actually exists
    f = c.glFramebufferRenderbufferOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFramebufferTexture2DOES(target, attachment, textarget, texture, level, target_t=GLenum, attachment_t=GLenum, textarget_t=GLenum, texture_t=GLuint, level_t=GLint):
        restype = None
        argtypes = [target_t, attachment_t, textarget_t, texture_t, level_t]
        cfunc = c.glFramebufferTexture2DOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, textarget, texture, level)
    # Check if the function actually exists
    f = c.glFramebufferTexture2DOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetFramebufferAttachmentParameterivOES(target, attachment, pname, params, target_t=GLenum, attachment_t=GLenum, pname_t=GLenum, params_t=ctypes.POINTER(GLint)):
        restype = None
        argtypes = [target_t, attachment_t, pname_t, params_t]
        cfunc = c.glGetFramebufferAttachmentParameterivOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, attachment, pname, params)
    # Check if the function actually exists
    f = c.glGetFramebufferAttachmentParameterivOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenerateMipmapOES(target, target_t=GLenum):
        restype = None
        argtypes = [target_t]
        cfunc = c.glGenerateMipmapOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glGenerateMipmapOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glUnmapBufferOES(target, target_t=GLenum):
        restype = GLboolean
        argtypes = [target_t]
        cfunc = c.glUnmapBufferOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target)
    # Check if the function actually exists
    f = c.glUnmapBufferOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetBufferPointervOES(target, pname, params, target_t=GLenum, pname_t=GLenum, params_t=GLvoid):
        restype = None
        argtypes = [target_t, pname_t, params_t]
        cfunc = c.glGetBufferPointervOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, params)
    # Check if the function actually exists
    f = c.glGetBufferPointervOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCurrentPaletteMatrixOES(matrixpaletteindex, matrixpaletteindex_t=GLuint):
        restype = None
        argtypes = [matrixpaletteindex_t]
        cfunc = c.glCurrentPaletteMatrixOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(matrixpaletteindex)
    # Check if the function actually exists
    f = c.glCurrentPaletteMatrixOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glLoadPaletteFromModelViewMatrixOES(void, void_t=ctypes.c_void_p):
        restype = None
        argtypes = [void_t]
        cfunc = c.glLoadPaletteFromModelViewMatrixOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glLoadPaletteFromModelViewMatrixOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMatrixIndexPointerOES(size, type, stride, param0, size_t=GLint, type_t=GLenum, stride_t=GLsizei, param0_t=GLvoid):
        restype = None
        argtypes = [size_t, type_t, stride_t, param0_t]
        cfunc = c.glMatrixIndexPointerOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size, type, stride, param0)
    # Check if the function actually exists
    f = c.glMatrixIndexPointerOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glWeightPointerOES(size, type, stride, param0, size_t=GLint, type_t=GLenum, stride_t=GLsizei, param0_t=GLvoid):
        restype = None
        argtypes = [size_t, type_t, stride_t, param0_t]
        cfunc = c.glWeightPointerOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(size, type, stride, param0)
    # Check if the function actually exists
    f = c.glWeightPointerOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glQueryMatrixxOES(mantissa, exponent, mantissa_t=(GLfixed * 16), exponent_t=(GLint * 16)):
        restype = GLbitfield
        argtypes = [mantissa_t, exponent_t]
        cfunc = c.glQueryMatrixxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(mantissa, exponent)
    # Check if the function actually exists
    f = c.glQueryMatrixxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDepthRangefOES(zNear, zFar, zNear_t=GLclampf, zFar_t=GLclampf):
        restype = None
        argtypes = [zNear_t, zFar_t]
        cfunc = c.glDepthRangefOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(zNear, zFar)
    # Check if the function actually exists
    f = c.glDepthRangefOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFrustumfOES(left, right, bottom, top, zNear, zFar, left_t=GLfloat, right_t=GLfloat, bottom_t=GLfloat, top_t=GLfloat, zNear_t=GLfloat, zFar_t=GLfloat):
        restype = None
        argtypes = [left_t, right_t, bottom_t, top_t, zNear_t, zFar_t]
        cfunc = c.glFrustumfOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glFrustumfOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glOrthofOES(left, right, bottom, top, zNear, zFar, left_t=GLfloat, right_t=GLfloat, bottom_t=GLfloat, top_t=GLfloat, zNear_t=GLfloat, zFar_t=GLfloat):
        restype = None
        argtypes = [left_t, right_t, bottom_t, top_t, zNear_t, zFar_t]
        cfunc = c.glOrthofOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(left, right, bottom, top, zNear, zFar)
    # Check if the function actually exists
    f = c.glOrthofOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClipPlanefOES(plane, param0, plane_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [plane_t, param0_t]
        cfunc = c.glClipPlanefOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(plane, param0)
    # Check if the function actually exists
    f = c.glClipPlanefOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetClipPlanefOES(pname, eqn, pname_t=GLenum, eqn_t=(GLfloat * 4)):
        restype = None
        argtypes = [pname_t, eqn_t]
        cfunc = c.glGetClipPlanefOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, eqn)
    # Check if the function actually exists
    f = c.glGetClipPlanefOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClearDepthfOES(depth, depth_t=GLclampf):
        restype = None
        argtypes = [depth_t]
        cfunc = c.glClearDepthfOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(depth)
    # Check if the function actually exists
    f = c.glClearDepthfOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexGenfOES(coord, pname, param, coord_t=GLenum, pname_t=GLenum, param_t=GLfloat):
        restype = None
        argtypes = [coord_t, pname_t, param_t]
        cfunc = c.glTexGenfOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param)
    # Check if the function actually exists
    f = c.glTexGenfOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexGenfvOES(coord, pname, param0, coord_t=GLenum, pname_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [coord_t, pname_t, param0_t]
        cfunc = c.glTexGenfvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param0)
    # Check if the function actually exists
    f = c.glTexGenfvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexGeniOES(coord, pname, param, coord_t=GLenum, pname_t=GLenum, param_t=GLint):
        restype = None
        argtypes = [coord_t, pname_t, param_t]
        cfunc = c.glTexGeniOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param)
    # Check if the function actually exists
    f = c.glTexGeniOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexGenivOES(coord, pname, param0, coord_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [coord_t, pname_t, param0_t]
        cfunc = c.glTexGenivOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param0)
    # Check if the function actually exists
    f = c.glTexGenivOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexGenxOES(coord, pname, param, coord_t=GLenum, pname_t=GLenum, param_t=GLfixed):
        restype = None
        argtypes = [coord_t, pname_t, param_t]
        cfunc = c.glTexGenxOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param)
    # Check if the function actually exists
    f = c.glTexGenxOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexGenxvOES(coord, pname, param0, coord_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [coord_t, pname_t, param0_t]
        cfunc = c.glTexGenxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param0)
    # Check if the function actually exists
    f = c.glTexGenxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexGenfvOES(coord, pname, param0, coord_t=GLenum, pname_t=GLenum, param0_t=GLfloat):
        restype = None
        argtypes = [coord_t, pname_t, param0_t]
        cfunc = c.glGetTexGenfvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexGenfvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexGenivOES(coord, pname, param0, coord_t=GLenum, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [coord_t, pname_t, param0_t]
        cfunc = c.glGetTexGenivOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexGenivOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetTexGenxvOES(coord, pname, param0, coord_t=GLenum, pname_t=GLenum, param0_t=GLfixed):
        restype = None
        argtypes = [coord_t, pname_t, param0_t]
        cfunc = c.glGetTexGenxvOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(coord, pname, param0)
    # Check if the function actually exists
    f = c.glGetTexGenxvOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glBindVertexArrayOES(array, array_t=GLuint):
        restype = None
        argtypes = [array_t]
        cfunc = c.glBindVertexArrayOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(array)
    # Check if the function actually exists
    f = c.glBindVertexArrayOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteVertexArraysOES(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
        cfunc = c.glDeleteVertexArraysOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glDeleteVertexArraysOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenVertexArraysOES(n, param0, n_t=GLsizei, param0_t=GLuint):
        restype = None
        argtypes = [n_t, param0_t]
        cfunc = c.glGenVertexArraysOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(n, param0)
    # Check if the function actually exists
    f = c.glGenVertexArraysOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsVertexArrayOES(array, array_t=GLuint):
        restype = GLboolean
        argtypes = [array_t]
        cfunc = c.glIsVertexArrayOES
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(array)
    # Check if the function actually exists
    f = c.glIsVertexArrayOES
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glCopyTextureLevelsAPPLE(destinationTexture, sourceTexture, sourceBaseLevel, sourceLevelCount, destinationTexture_t=GLuint, sourceTexture_t=GLuint, sourceBaseLevel_t=GLint, sourceLevelCount_t=GLsizei):
        restype = None
        argtypes = [destinationTexture_t, sourceTexture_t, sourceBaseLevel_t, sourceLevelCount_t]
        cfunc = c.glCopyTextureLevelsAPPLE
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(destinationTexture, sourceTexture, sourceBaseLevel, sourceLevelCount)
    # Check if the function actually exists
    f = c.glCopyTextureLevelsAPPLE
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorageMultisampleAPPLE(param0, param1, param2, param3, param4, param0_t=GLenum, param1_t=GLsizei, param2_t=GLenum, param3_t=GLsizei, param4_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t, param4_t]
        cfunc = c.glRenderbufferStorageMultisampleAPPLE
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3, param4)
    # Check if the function actually exists
    f = c.glRenderbufferStorageMultisampleAPPLE
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glResolveMultisampleFramebufferAPPLE(void, void_t=ctypes.c_void_p):
        restype = None
        argtypes = [void_t]
        cfunc = c.glResolveMultisampleFramebufferAPPLE
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glResolveMultisampleFramebufferAPPLE
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetInteger64vAPPLE(pname, param0, pname_t=GLenum, param0_t=GLint64):
        restype = None
        argtypes = [pname_t, param0_t]
        cfunc = c.glGetInteger64vAPPLE
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(pname, param0)
    # Check if the function actually exists
    f = c.glGetInteger64vAPPLE
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDiscardFramebufferEXT(target, numAttachments, param0, target_t=GLenum, numAttachments_t=GLsizei, param0_t=GLenum):
        restype = None
        argtypes = [target_t, numAttachments_t, param0_t]
        cfunc = c.glDiscardFramebufferEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, numAttachments, param0)
    # Check if the function actually exists
    f = c.glDiscardFramebufferEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFlushMappedBufferRangeEXT(target, offset, length, target_t=GLenum, offset_t=GLintptr, length_t=GLsizeiptr):
        restype = None
        argtypes = [target_t, offset_t, length_t]
        cfunc = c.glFlushMappedBufferRangeEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, offset, length)
    # Check if the function actually exists
    f = c.glFlushMappedBufferRangeEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorageMultisampleEXT(param0, param1, param2, param3, param4, param0_t=GLenum, param1_t=GLsizei, param2_t=GLenum, param3_t=GLsizei, param4_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t, param4_t]
        cfunc = c.glRenderbufferStorageMultisampleEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3, param4)
    # Check if the function actually exists
    f = c.glRenderbufferStorageMultisampleEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFramebufferTexture2DMultisampleEXT(param0, param1, param2, param3, param4, param5, param0_t=GLenum, param1_t=GLenum, param2_t=GLenum, param3_t=GLuint, param4_t=GLint, param5_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t, param4_t, param5_t]
        cfunc = c.glFramebufferTexture2DMultisampleEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3, param4, param5)
    # Check if the function actually exists
    f = c.glFramebufferTexture2DMultisampleEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMultiDrawArraysEXT(param0, param1, param2, param3, param0_t=GLenum, param1_t=GLint, param2_t=GLsizei, param3_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t]
        cfunc = c.glMultiDrawArraysEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3)
    # Check if the function actually exists
    f = c.glMultiDrawArraysEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glMultiDrawElementsEXT(param0, param1, param2, param3, param4, param0_t=GLenum, param1_t=GLsizei, param2_t=GLenum, param3_t=ctypes.POINTER(GLvoid), param4_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t, param4_t]
        cfunc = c.glMultiDrawElementsEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3, param4)
    # Check if the function actually exists
    f = c.glMultiDrawElementsEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetGraphicsResetStatusEXT(void, void_t=ctypes.c_void_p):
        restype = GLenum
        argtypes = [void_t]
        cfunc = c.glGetGraphicsResetStatusEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(void)
    # Check if the function actually exists
    f = c.glGetGraphicsResetStatusEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glReadnPixelsEXT(x, y, width, height, format, type, bufSize, voiddata, x_t=GLint, y_t=GLint, width_t=GLsizei, height_t=GLsizei, format_t=GLenum, type_t=GLenum, bufSize_t=GLsizei, voiddata_t=ctypes.c_void_p):
        restype = None
        argtypes = [x_t, y_t, width_t, height_t, format_t, type_t, bufSize_t, voiddata_t]
        cfunc = c.glReadnPixelsEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, width, height, format, type, bufSize, voiddata)
    # Check if the function actually exists
    f = c.glReadnPixelsEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetnUniformfvEXT(program, location, bufSize, floatparams, program_t=GLuint, location_t=GLint, bufSize_t=GLsizei, floatparams_t=float):
        restype = None
        argtypes = [program_t, location_t, bufSize_t, floatparams_t]
        cfunc = c.glGetnUniformfvEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, location, bufSize, floatparams)
    # Check if the function actually exists
    f = c.glGetnUniformfvEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetnUniformivEXT(program, location, bufSize, param0, program_t=GLuint, location_t=GLint, bufSize_t=GLsizei, param0_t=GLint):
        restype = None
        argtypes = [program_t, location_t, bufSize_t, param0_t]
        cfunc = c.glGetnUniformivEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, location, bufSize, param0)
    # Check if the function actually exists
    f = c.glGetnUniformivEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexStorage1DEXT(target, levels, internalformat, width, target_t=GLenum, levels_t=GLsizei, internalformat_t=GLenum, width_t=GLsizei):
        restype = None
        argtypes = [target_t, levels_t, internalformat_t, width_t]
        cfunc = c.glTexStorage1DEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, levels, internalformat, width)
    # Check if the function actually exists
    f = c.glTexStorage1DEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexStorage2DEXT(target, levels, internalformat, width, height, target_t=GLenum, levels_t=GLsizei, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [target_t, levels_t, internalformat_t, width_t, height_t]
        cfunc = c.glTexStorage2DEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, levels, internalformat, width, height)
    # Check if the function actually exists
    f = c.glTexStorage2DEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTexStorage3DEXT(target, levels, internalformat, width, height, depth, target_t=GLenum, levels_t=GLsizei, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei, depth_t=GLsizei):
        restype = None
        argtypes = [target_t, levels_t, internalformat_t, width_t, height_t, depth_t]
        cfunc = c.glTexStorage3DEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, levels, internalformat, width, height, depth)
    # Check if the function actually exists
    f = c.glTexStorage3DEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTextureStorage1DEXT(texture, target, levels, internalformat, width, texture_t=GLuint, target_t=GLenum, levels_t=GLsizei, internalformat_t=GLenum, width_t=GLsizei):
        restype = None
        argtypes = [texture_t, target_t, levels_t, internalformat_t, width_t]
        cfunc = c.glTextureStorage1DEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture, target, levels, internalformat, width)
    # Check if the function actually exists
    f = c.glTextureStorage1DEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTextureStorage2DEXT(texture, target, levels, internalformat, width, height, texture_t=GLuint, target_t=GLenum, levels_t=GLsizei, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei):
        restype = None
        argtypes = [texture_t, target_t, levels_t, internalformat_t, width_t, height_t]
        cfunc = c.glTextureStorage2DEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture, target, levels, internalformat, width, height)
    # Check if the function actually exists
    f = c.glTextureStorage2DEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTextureStorage3DEXT(texture, target, levels, internalformat, width, height, depth, texture_t=GLuint, target_t=GLenum, levels_t=GLsizei, internalformat_t=GLenum, width_t=GLsizei, height_t=GLsizei, depth_t=GLsizei):
        restype = None
        argtypes = [texture_t, target_t, levels_t, internalformat_t, width_t, height_t, depth_t]
        cfunc = c.glTextureStorage3DEXT
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture, target, levels, internalformat, width, height, depth)
    # Check if the function actually exists
    f = c.glTextureStorage3DEXT
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClipPlanefIMG(param0, param1, param0_t=GLenum, param1_t=GLfloat):
        restype = None
        argtypes = [param0_t, param1_t]
        cfunc = c.glClipPlanefIMG
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1)
    # Check if the function actually exists
    f = c.glClipPlanefIMG
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glClipPlanexIMG(param0, param1, param0_t=GLenum, param1_t=GLfixed):
        restype = None
        argtypes = [param0_t, param1_t]
        cfunc = c.glClipPlanexIMG
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1)
    # Check if the function actually exists
    f = c.glClipPlanexIMG
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glRenderbufferStorageMultisampleIMG(param0, param1, param2, param3, param4, param0_t=GLenum, param1_t=GLsizei, param2_t=GLenum, param3_t=GLsizei, param4_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t, param4_t]
        cfunc = c.glRenderbufferStorageMultisampleIMG
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3, param4)
    # Check if the function actually exists
    f = c.glRenderbufferStorageMultisampleIMG
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFramebufferTexture2DMultisampleIMG(param0, param1, param2, param3, param4, param5, param0_t=GLenum, param1_t=GLenum, param2_t=GLenum, param3_t=GLuint, param4_t=GLint, param5_t=GLsizei):
        restype = None
        argtypes = [param0_t, param1_t, param2_t, param3_t, param4_t, param5_t]
        cfunc = c.glFramebufferTexture2DMultisampleIMG
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2, param3, param4, param5)
    # Check if the function actually exists
    f = c.glFramebufferTexture2DMultisampleIMG
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDeleteFencesNV(param0, param1, param0_t=GLsizei, param1_t=GLuint):
        restype = None
        argtypes = [param0_t, param1_t]
        cfunc = c.glDeleteFencesNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1)
    # Check if the function actually exists
    f = c.glDeleteFencesNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGenFencesNV(param0, param1, param0_t=GLsizei, param1_t=GLuint):
        restype = None
        argtypes = [param0_t, param1_t]
        cfunc = c.glGenFencesNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1)
    # Check if the function actually exists
    f = c.glGenFencesNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glIsFenceNV(param0, param0_t=GLuint):
        restype = GLboolean
        argtypes = [param0_t]
        cfunc = c.glIsFenceNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glIsFenceNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glTestFenceNV(param0, param0_t=GLuint):
        restype = GLboolean
        argtypes = [param0_t]
        cfunc = c.glTestFenceNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glTestFenceNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetFenceivNV(param0, param1, param2, param0_t=GLuint, param1_t=GLenum, param2_t=GLint):
        restype = None
        argtypes = [param0_t, param1_t, param2_t]
        cfunc = c.glGetFenceivNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1, param2)
    # Check if the function actually exists
    f = c.glGetFenceivNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glFinishFenceNV(param0, param0_t=GLuint):
        restype = None
        argtypes = [param0_t]
        cfunc = c.glFinishFenceNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0)
    # Check if the function actually exists
    f = c.glFinishFenceNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glSetFenceNV(param0, param1, param0_t=GLuint, param1_t=GLenum):
        restype = None
        argtypes = [param0_t, param1_t]
        cfunc = c.glSetFenceNV
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, param1)
    # Check if the function actually exists
    f = c.glSetFenceNV
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetDriverControlsQCOM(param0, size, param1, param0_t=GLint, size_t=GLsizei, param1_t=GLuint):
        restype = None
        argtypes = [param0_t, size_t, param1_t]
        cfunc = c.glGetDriverControlsQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, size, param1)
    # Check if the function actually exists
    f = c.glGetDriverControlsQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glGetDriverControlStringQCOM(driverControl, bufSize, param0, param1, driverControl_t=GLuint, bufSize_t=GLsizei, param0_t=GLsizei, param1_t=GLchar):
        restype = None
        argtypes = [driverControl_t, bufSize_t, param0_t, param1_t]
        cfunc = c.glGetDriverControlStringQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(driverControl, bufSize, param0, param1)
    # Check if the function actually exists
    f = c.glGetDriverControlStringQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glEnableDriverControlQCOM(driverControl, driverControl_t=GLuint):
        restype = None
        argtypes = [driverControl_t]
        cfunc = c.glEnableDriverControlQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(driverControl)
    # Check if the function actually exists
    f = c.glEnableDriverControlQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glDisableDriverControlQCOM(driverControl, driverControl_t=GLuint):
        restype = None
        argtypes = [driverControl_t]
        cfunc = c.glDisableDriverControlQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(driverControl)
    # Check if the function actually exists
    f = c.glDisableDriverControlQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetTexturesQCOM(param0, maxTextures, param1, param0_t=GLuint, maxTextures_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [param0_t, maxTextures_t, param1_t]
        cfunc = c.glExtGetTexturesQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, maxTextures, param1)
    # Check if the function actually exists
    f = c.glExtGetTexturesQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetBuffersQCOM(param0, maxBuffers, param1, param0_t=GLuint, maxBuffers_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [param0_t, maxBuffers_t, param1_t]
        cfunc = c.glExtGetBuffersQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, maxBuffers, param1)
    # Check if the function actually exists
    f = c.glExtGetBuffersQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetRenderbuffersQCOM(param0, maxRenderbuffers, param1, param0_t=GLuint, maxRenderbuffers_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [param0_t, maxRenderbuffers_t, param1_t]
        cfunc = c.glExtGetRenderbuffersQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, maxRenderbuffers, param1)
    # Check if the function actually exists
    f = c.glExtGetRenderbuffersQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetFramebuffersQCOM(param0, maxFramebuffers, param1, param0_t=GLuint, maxFramebuffers_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [param0_t, maxFramebuffers_t, param1_t]
        cfunc = c.glExtGetFramebuffersQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, maxFramebuffers, param1)
    # Check if the function actually exists
    f = c.glExtGetFramebuffersQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetTexLevelParameterivQCOM(texture, face, level, pname, param0, texture_t=GLuint, face_t=GLenum, level_t=GLint, pname_t=GLenum, param0_t=GLint):
        restype = None
        argtypes = [texture_t, face_t, level_t, pname_t, param0_t]
        cfunc = c.glExtGetTexLevelParameterivQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(texture, face, level, pname, param0)
    # Check if the function actually exists
    f = c.glExtGetTexLevelParameterivQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtTexObjectStateOverrideiQCOM(target, pname, param, target_t=GLenum, pname_t=GLenum, param_t=GLint):
        restype = None
        argtypes = [target_t, pname_t, param_t]
        cfunc = c.glExtTexObjectStateOverrideiQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, pname, param)
    # Check if the function actually exists
    f = c.glExtTexObjectStateOverrideiQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetTexSubImageQCOM(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, param0, target_t=GLenum, level_t=GLint, xoffset_t=GLint, yoffset_t=GLint, zoffset_t=GLint, width_t=GLsizei, height_t=GLsizei, depth_t=GLsizei, format_t=GLenum, type_t=GLenum, param0_t=GLvoid):
        restype = None
        argtypes = [target_t, level_t, xoffset_t, yoffset_t, zoffset_t, width_t, height_t, depth_t, format_t, type_t, param0_t]
        cfunc = c.glExtGetTexSubImageQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, param0)
    # Check if the function actually exists
    f = c.glExtGetTexSubImageQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetBufferPointervQCOM(target, param0, target_t=GLenum, param0_t=GLvoid):
        restype = None
        argtypes = [target_t, param0_t]
        cfunc = c.glExtGetBufferPointervQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(target, param0)
    # Check if the function actually exists
    f = c.glExtGetBufferPointervQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetShadersQCOM(param0, maxShaders, param1, param0_t=GLuint, maxShaders_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [param0_t, maxShaders_t, param1_t]
        cfunc = c.glExtGetShadersQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, maxShaders, param1)
    # Check if the function actually exists
    f = c.glExtGetShadersQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetProgramsQCOM(param0, maxPrograms, param1, param0_t=GLuint, maxPrograms_t=GLint, param1_t=GLint):
        restype = None
        argtypes = [param0_t, maxPrograms_t, param1_t]
        cfunc = c.glExtGetProgramsQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(param0, maxPrograms, param1)
    # Check if the function actually exists
    f = c.glExtGetProgramsQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtIsProgramBinaryQCOM(program, program_t=GLuint):
        restype = GLboolean
        argtypes = [program_t]
        cfunc = c.glExtIsProgramBinaryQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program)
    # Check if the function actually exists
    f = c.glExtIsProgramBinaryQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glExtGetProgramBinarySourceQCOM(program, shadertype, param0, param1, program_t=GLuint, shadertype_t=GLenum, param0_t=GLchar, param1_t=GLint):
        restype = None
        argtypes = [program_t, shadertype_t, param0_t, param1_t]
        cfunc = c.glExtGetProgramBinarySourceQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(program, shadertype, param0, param1)
    # Check if the function actually exists
    f = c.glExtGetProgramBinarySourceQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glStartTilingQCOM(x, y, width, height, preserveMask, x_t=GLuint, y_t=GLuint, width_t=GLuint, height_t=GLuint, preserveMask_t=GLbitfield):
        restype = None
        argtypes = [x_t, y_t, width_t, height_t, preserveMask_t]
        cfunc = c.glStartTilingQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(x, y, width, height, preserveMask)
    # Check if the function actually exists
    f = c.glStartTilingQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

try:
    def glEndTilingQCOM(preserveMask, preserveMask_t=GLbitfield):
        restype = None
        argtypes = [preserveMask_t]
        cfunc = c.glEndTilingQCOM
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc(preserveMask)
    # Check if the function actually exists
    f = c.glEndTilingQCOM
    del f
    loaded[0] += 1
except AttributeError as e:
    loaded[1] += 1
    if DEBUG > 0:
        print 'could not load the function'
        print e

print 'Loaded %i functions and failed to load %i functions of %i functions in the header glext.h' % (loaded[0], loaded[1], sum(loaded))
__all__ = ['glBlendEquationSeparateOES', 'glBlendFuncSeparateOES', 'glBlendEquationOES', 'glDrawTexsOES', 'glDrawTexiOES', 'glDrawTexxOES', 'glDrawTexsvOES', 'glDrawTexivOES', 'glDrawTexxvOES', 'glDrawTexfOES', 'glDrawTexfvOES', 'glEGLImageTargetTexture2DOES', 'glEGLImageTargetRenderbufferStorageOES', 'glAlphaFuncxOES', 'glClearColorxOES', 'glClearDepthxOES', 'glClipPlanexOES', 'glColor4xOES', 'glDepthRangexOES', 'glFogxOES', 'glFogxvOES', 'glFrustumxOES', 'glGetClipPlanexOES', 'glGetFixedvOES', 'glGetLightxvOES', 'glGetMaterialxvOES', 'glGetTexEnvxvOES', 'glGetTexParameterxvOES', 'glLightModelxOES', 'glLightModelxvOES', 'glLightxOES', 'glLightxvOES', 'glLineWidthxOES', 'glLoadMatrixxOES', 'glMaterialxOES', 'glMaterialxvOES', 'glMultMatrixxOES', 'glMultiTexCoord4xOES', 'glNormal3xOES', 'glOrthoxOES', 'glPointParameterxOES', 'glPointParameterxvOES', 'glPointSizexOES', 'glPolygonOffsetxOES', 'glRotatexOES', 'glSampleCoveragexOES', 'glScalexOES', 'glTexEnvxOES', 'glTexEnvxvOES', 'glTexParameterxOES', 'glTexParameterxvOES', 'glTranslatexOES', 'glIsRenderbufferOES', 'glBindRenderbufferOES', 'glDeleteRenderbuffersOES', 'glGenRenderbuffersOES', 'glRenderbufferStorageOES', 'glGetRenderbufferParameterivOES', 'glIsFramebufferOES', 'glBindFramebufferOES', 'glDeleteFramebuffersOES', 'glGenFramebuffersOES', 'glCheckFramebufferStatusOES', 'glFramebufferRenderbufferOES', 'glFramebufferTexture2DOES', 'glGetFramebufferAttachmentParameterivOES', 'glGenerateMipmapOES', 'glUnmapBufferOES', 'glGetBufferPointervOES', 'glCurrentPaletteMatrixOES', 'glLoadPaletteFromModelViewMatrixOES', 'glMatrixIndexPointerOES', 'glWeightPointerOES', 'glQueryMatrixxOES', 'glDepthRangefOES', 'glFrustumfOES', 'glOrthofOES', 'glClipPlanefOES', 'glGetClipPlanefOES', 'glClearDepthfOES', 'glTexGenfOES', 'glTexGenfvOES', 'glTexGeniOES', 'glTexGenivOES', 'glTexGenxOES', 'glTexGenxvOES', 'glGetTexGenfvOES', 'glGetTexGenivOES', 'glGetTexGenxvOES', 'glBindVertexArrayOES', 'glDeleteVertexArraysOES', 'glGenVertexArraysOES', 'glIsVertexArrayOES', 'glCopyTextureLevelsAPPLE', 'glRenderbufferStorageMultisampleAPPLE', 'glResolveMultisampleFramebufferAPPLE', 'glGetInteger64vAPPLE', 'glDiscardFramebufferEXT', 'glFlushMappedBufferRangeEXT', 'glRenderbufferStorageMultisampleEXT', 'glFramebufferTexture2DMultisampleEXT', 'glMultiDrawArraysEXT', 'glMultiDrawElementsEXT', 'glGetGraphicsResetStatusEXT', 'glReadnPixelsEXT', 'glGetnUniformfvEXT', 'glGetnUniformivEXT', 'glTexStorage1DEXT', 'glTexStorage2DEXT', 'glTexStorage3DEXT', 'glTextureStorage1DEXT', 'glTextureStorage2DEXT', 'glTextureStorage3DEXT', 'glClipPlanefIMG', 'glClipPlanexIMG', 'glRenderbufferStorageMultisampleIMG', 'glFramebufferTexture2DMultisampleIMG', 'glDeleteFencesNV', 'glGenFencesNV', 'glIsFenceNV', 'glTestFenceNV', 'glGetFenceivNV', 'glFinishFenceNV', 'glSetFenceNV', 'glGetDriverControlsQCOM', 'glGetDriverControlStringQCOM', 'glEnableDriverControlQCOM', 'glDisableDriverControlQCOM', 'glExtGetTexturesQCOM', 'glExtGetBuffersQCOM', 'glExtGetRenderbuffersQCOM', 'glExtGetFramebuffersQCOM', 'glExtGetTexLevelParameterivQCOM', 'glExtTexObjectStateOverrideiQCOM', 'glExtGetTexSubImageQCOM', 'glExtGetBufferPointervQCOM', 'glExtGetShadersQCOM', 'glExtGetProgramsQCOM', 'glExtIsProgramBinaryQCOM', 'glExtGetProgramBinarySourceQCOM', 'glStartTilingQCOM', 'glEndTilingQCOM', 'GL_TEXTURE_CROP_RECT_OES', 'GL_MATRIX_INDEX_ARRAY_SIZE_OES', 'GL_OES_packed_depth_stencil', 'GL_DEPTH_EXT', 'GL_COLOR_EXT', 'GL_QCOM_tiled_rendering', 'GL_RGB16F_EXT', 'GL_CLIP_PLANE1_IMG', 'GL_NV_fence', 'GL_CLIP_PLANE3_IMG', 'GL_OES_blend_subtract', 'GL_IMG_texture_compression_pvrtc', 'GL_SRGB_ALPHA_EXT', 'GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES', 'GL_REFLECTION_MAP_OES', 'GL_COLOR_BUFFER_BIT7_QCOM', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES', 'GL_BLEND_DST_RGB_OES', 'GL_RENDERBUFFER_WIDTH_OES', 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_APPLE', 'GL_DEPTH_BUFFER_BIT3_QCOM', 'GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES', 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES', 'GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG', 'GL_CONTEXT_ROBUST_ACCESS_EXT', 'GL_QCOM_perfmon_global_mode', 'GL_RGB32F_EXT', 'GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES', 'GL_CLIP_PLANE0_IMG', 'GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES', 'GL_OES_single_precision', 'GL_EXT_multisampled_render_to_texture', 'GL_OES_texture_env_crossbar', 'GL_WRITEONLY_RENDERING_QCOM', 'GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT', 'GL_TEXTURE_BINDING_EXTERNAL_OES', 'GL_NONE_OES', 'GL_OES_texture_cube_map', 'GL_OES_query_matrix', 'GL_ALPHA32F_EXT', 'GL_SYNC_FENCE_APPLE', 'GL_DEPTH_COMPONENT24_OES', 'GL_FRAMEBUFFER_UNSUPPORTED_OES', 'GL_RGBA32F_EXT', 'GL_READ_FRAMEBUFFER_BINDING_APPLE', 'GL_LUMINANCE32F_EXT', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES', 'GL_MAP_UNSYNCHRONIZED_BIT_EXT', 'GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG', 'GL_DRAW_FRAMEBUFFER_BINDING_APPLE', 'GL_APPLE_texture_max_level', 'GL_TEXTURE_HEIGHT_QCOM', 'GL_RENDERBUFFER_OES', 'GL_FENCE_CONDITION_NV', 'GL_TEXTURE_CUBE_MAP_OES', 'GL_EXT_multi_draw_arrays', 'GL_COMPRESSED_RGB_S3TC_DXT1_EXT', 'GL_OES_fbo_render_mipmap', 'GL_RECIP_ADD_SIGNED_ALPHA_IMG', 'GL_STENCIL_BUFFER_BIT5_QCOM', 'GL_UNKNOWN_CONTEXT_RESET_EXT', 'GL_OES_stencil_wrap', 'GL_TEXTURE_BINDING_CUBE_MAP_OES', 'GL_READ_FRAMEBUFFER_APPLE', 'GL_SYNC_FLUSH_COMMANDS_BIT_APPLE', 'GL_TEXTURE_INTERNAL_FORMAT_QCOM', 'GL_STENCIL_BUFFER_BIT2_QCOM', 'GL_RENDERBUFFER_HEIGHT_OES', 'GL_TEXTURE_ALPHA_MODULATE_IMG', 'GL_NORMAL_MAP_OES', 'GL_LUMINANCE8_ALPHA8_EXT', 'GL_MAX_EXT', 'GL_MAX_VERTEX_UNITS_OES', 'GL_DEPTH_BUFFER_BIT7_QCOM', 'GL_TEXTURE_LOD_BIAS_EXT', 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES', 'GL_TEXTURE_FORMAT_QCOM', 'GL_MODULATE_COLOR_IMG', 'GL_RENDERBUFFER_BINDING_OES', 'GL_EXT_texture_compression_dxt1', 'GL_OES_extended_matrix_palette', 'GL_STENCIL_BUFFER_BIT1_QCOM', 'GL_RENDERBUFFER_STENCIL_SIZE_OES', 'GL_SYNC_OBJECT_APPLE', 'GL_SRGB8_ALPHA8_EXT', 'GL_BLEND_SRC_ALPHA_OES', 'GL_MULTISAMPLE_BUFFER_BIT2_QCOM', 'GL_MAX_SERVER_WAIT_TIMEOUT_APPLE', 'GL_OES_blend_equation_separate', 'GL_MULTISAMPLE_BUFFER_BIT3_QCOM', 'GL_RENDERBUFFER_DEPTH_SIZE_OES', 'GL_MATRIX_INDEX_ARRAY_STRIDE_OES', 'GL_WEIGHT_ARRAY_OES', 'GL_BUFFER_ACCESS_OES', 'GL_OES_matrix_get', 'GL_LUMINANCE8_EXT', 'GL_OES_EGL_image_external', 'GL_RGB10_EXT', 'GL_EXT_map_buffer_range', 'GL_CONDITION_SATISFIED_APPLE', 'GL_OES_stencil4', 'GL_BLEND_EQUATION_ALPHA_OES', 'GL_FUNC_ADD_OES', 'GL_DEPTH_COMPONENT16_OES', 'GL_WEIGHT_ARRAY_POINTER_OES', 'GL_EXT_blend_minmax', 'GL_MAX_CLIP_PLANES_IMG', 'GL_STENCIL_BUFFER_BIT0_QCOM', 'GL_BLEND_DST_ALPHA_OES', 'GL_STENCIL_INDEX1_OES', 'GL_TEXTURE_DEPTH_QCOM', 'GL_RENDERBUFFER_BLUE_SIZE_OES', 'GL_OES_byte_coordinates', 'GL_MAX_SAMPLES_APPLE', 'GL_COLOR_BUFFER_BIT4_QCOM', 'GL_RENDERBUFFER_GREEN_SIZE_OES', 'GL_WRITE_ONLY_OES', 'GL_IMG_read_format', 'GL_OES_blend_func_separate', 'GL_MULTISAMPLE_BUFFER_BIT7_QCOM', 'GL_BGRA_EXT', 'GL_OES_depth24', 'GL_MULTISAMPLE_BUFFER_BIT6_QCOM', 'GL_FENCE_STATUS_NV', 'GL_TEXTURE_OBJECT_VALID_QCOM', 'GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG', 'GL_LUMINANCE_ALPHA16F_EXT', 'GL_OES_stencil1', 'GL_AMD_compressed_ATC_texture', 'GL_OES_matrix_palette', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES', 'GL_FACTOR_ALPHA_MODULATE_IMG', 'GL_MIRRORED_REPEAT_OES', 'GL_RENDERBUFFER_RED_SIZE_OES', 'GL_QCOM_writeonly_rendering', 'GL_TEXTURE_GEN_MODE_OES', 'GL_COLOR_BUFFER_BIT3_QCOM', 'GL_WEIGHT_ARRAY_BUFFER_BINDING_OES', 'GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG', 'GL_UNSIGNALED_APPLE', 'GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES', 'GL_STENCIL_ATTACHMENT_OES', 'GL_OBJECT_TYPE_APPLE', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES', 'GL_RENDERBUFFER_SAMPLES_EXT', 'GL_APPLE_framebuffer_multisample', 'GL_RENDERBUFFER_ALPHA_SIZE_OES', 'GL_SYNC_GPU_COMMANDS_COMPLETE_APPLE', 'GL_SIGNALED_APPLE', 'GL_RGBA8_OES', 'GL_APPLE_sync', 'GL_EXT_robustness', 'GL_ALL_COMPLETED_NV', 'GL_SYNC_STATUS_APPLE', 'GL_BLEND_EQUATION_RGB_OES', 'GL_MULTISAMPLE_BUFFER_BIT0_QCOM', 'GL_RESET_NOTIFICATION_STRATEGY_EXT', 'GL_UNSIGNED_INT_24_8_OES', 'GL_CLIP_PLANE5_IMG', 'GL_INCR_WRAP_OES', 'GL_MAX_SAMPLES_IMG', 'GL_OES_framebuffer_object', 'GL_MAP_READ_BIT_EXT', 'GL_DEPTH_BUFFER_BIT6_QCOM', 'GL_COLOR_BUFFER_BIT6_QCOM', 'GL_RGB10_A2_EXT', 'GL_MAP_FLUSH_EXPLICIT_BIT_EXT', 'GL_COLOR_BUFFER_BIT0_QCOM', 'GL_WEIGHT_ARRAY_TYPE_OES', 'GL_EXT_read_format_bgra', 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES', 'GL_DEPTH_BUFFER_BIT0_QCOM', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES', 'GL_FRAMEBUFFER_COMPLETE_OES', 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT', 'GL_LOSE_CONTEXT_ON_RESET_EXT', 'GL_QCOM_extended_get2', 'GL_WEIGHT_ARRAY_STRIDE_OES', 'GL_TEXTURE_IMMUTABLE_FORMAT_EXT', 'GL_STATE_RESTORE', 'GL_DEPTH_BUFFER_BIT4_QCOM', 'GL_DEPTH_ATTACHMENT_OES', 'GL_TEXTURE_GEN_STR_OES', 'GL_FRAMEBUFFER_BINDING_OES', 'GL_WEIGHT_ARRAY_SIZE_OES', 'GL_MATRIX_INDEX_ARRAY_TYPE_OES', 'GL_3DC_XY_AMD', 'GL_MIN_EXT', 'GL_OES_depth32', 'GL_ALPHA8_EXT', 'GL_STENCIL_INDEX4_OES', 'GL_CLIP_PLANE2_IMG', 'GL_FRAMEBUFFER_OES', 'GL_APPLE_texture_2D_limited_npot', 'GL_INNOCENT_CONTEXT_RESET_EXT', 'GL_OES_EGL_image', 'GL_BLEND_EQUATION_OES', 'GL_STENCIL_BUFFER_BIT3_QCOM', 'GL_TEXTURE_TARGET_QCOM', 'GL_VERTEX_ARRAY_BINDING_OES', 'GL_MAX_PALETTE_MATRICES_OES', 'GL_DEPTH_BUFFER_BIT1_QCOM', 'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT', 'GL_RENDERBUFFER_SAMPLES_APPLE', 'GL_TIMEOUT_IGNORED_APPLE', 'GL_DECR_WRAP_OES', 'GL_EXT_texture_lod_bias', 'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES', 'GL_TEXTURE_FILTER_CONTROL_EXT', 'GL_EXT_sRGB', 'GL_EXT_texture_filter_anisotropic', 'GL_OES_texture_mirrored_repeat', 'GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES', 'GL_RGB565_OES', 'GL_RGB5_A1_OES', 'GL_OES_rgb8_rgba8', 'GL_RENDERBUFFER_INTERNAL_FORMAT_OES', 'GL_IMG_multisampled_render_to_texture', 'GL_MAP_INVALIDATE_BUFFER_BIT_EXT', 'GL_COLOR_BUFFER_BIT5_QCOM', 'GL_MATRIX_INDEX_ARRAY_OES', 'GL_ADD_BLEND_IMG', 'GL_ETC1_RGB8_OES', 'GL_WAIT_FAILED_APPLE', 'GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES', 'GL_DEPTH_BUFFER_BIT5_QCOM', 'GL_NO_RESET_NOTIFICATION_EXT', 'GL_MAX_TEXTURE_LOD_BIAS_EXT', 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT', 'GL_SYNC_FLAGS_APPLE', 'GL_DEPTH_BUFFER_BIT2_QCOM', 'GL_EXT_texture_storage', 'GL_OES_required_internalformat', 'GL_IMG_user_clip_plane', 'GL_MATRIX_PALETTE_OES', 'GL_COLOR_BUFFER_BIT1_QCOM', 'GL_DOT3_RGBA_IMG', 'GL_AMD_compressed_3DC_texture', 'GL_BGRA_IMG', 'GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG', 'GL_RGB8_OES', 'GL_OES_element_index_uint', 'GL_RENDERBUFFER_SAMPLES_IMG', 'GL_STENCIL_INDEX8_OES', 'GL_OES_draw_texture', 'GL_MAX_SAMPLES_EXT', 'GL_PERFMON_GLOBAL_MODE_QCOM', 'GL_OES_mapbuffer', 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG', 'GL_UNSIGNED_INT', 'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT', 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES', 'GL_MATRIX_INDEX_ARRAY_POINTER_OES', 'GL_OES_compressed_ETC1_RGB8_texture', 'GL_FRAGMENT_ALPHA_MODULATE_IMG', 'GL_ALREADY_SIGNALED_APPLE', 'GL_MULTISAMPLE_BUFFER_BIT1_QCOM', 'GL_BUFFER_MAPPED_OES', 'GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT', 'GL_TEXTURE_IMAGE_VALID_QCOM', 'GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD', 'GL_TEXTURE_WIDTH_QCOM', 'GL_LUMINANCE_ALPHA32F_EXT', 'GL_INVALID_FRAMEBUFFER_OPERATION_OES', 'GL_OES_fixed_point', 'GL_RGBA4_OES', 'GL_CURRENT_PALETTE_MATRIX_OES', 'GL_EXT_texture_format_BGRA8888', 'GL_DRAW_FRAMEBUFFER_APPLE', 'GL_BUFFER_MAP_POINTER_OES', 'GL_COLOR_BUFFER_BIT2_QCOM', 'GL_3DC_X_AMD', 'GL_MAP_INVALIDATE_RANGE_BIT_EXT', 'GL_QCOM_extended_get', 'GL_MAP_WRITE_BIT_EXT', 'GL_TEXTURE_NUM_LEVELS_QCOM', 'GL_FIXED_OES', 'GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT', 'GL_DEPTH_COMPONENT32_OES', 'GL_STENCIL_BUFFER_BIT7_QCOM', 'GL_STENCIL_BUFFER_BIT4_QCOM', 'GL_DEPTH24_STENCIL8_OES', 'GL_APPLE_copy_texture_levels', 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES', 'GL_TEXTURE_MAX_ANISOTROPY_EXT', 'GL_GUILTY_CONTEXT_RESET_EXT', 'GL_ARM_rgba8', 'GL_BLEND_SRC_RGB_OES', 'GL_MULTISAMPLE_BUFFER_BIT4_QCOM', 'GL_FUNC_SUBTRACT_OES', 'GL_MULTISAMPLE_BUFFER_BIT5_QCOM', 'GL_LUMINANCE16F_EXT', 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES', 'GL_TIMEOUT_EXPIRED_APPLE', 'GL_STENCIL_BUFFER_BIT6_QCOM', 'GL_BGRA8_EXT', 'GL_ATC_RGB_AMD', 'GL_TEXTURE_SAMPLES_IMG', 'GL_CLIP_PLANE4_IMG', 'GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES', 'GL_IMG_texture_env_enhanced_fixed_function', 'GL_TEXTURE_MAX_LEVEL_APPLE', 'GL_TEXTURE_TYPE_QCOM', 'GL_TEXTURE_EXTERNAL_OES', 'GL_STENCIL_EXT', 'GL_APPLE_texture_format_BGRA8888', 'GL_QCOM_driver_control', 'GL_EXT_discard_framebuffer', 'GL_ALPHA16F_EXT', 'GL_SRGB_EXT', 'GL_FUNC_REVERSE_SUBTRACT_OES', 'GL_COLOR_ATTACHMENT0_OES', 'GL_SYNC_CONDITION_APPLE', 'GL_OES_stencil8', 'GL_MAX_RENDERBUFFER_SIZE_OES', 'GL_DEPTH_STENCIL_OES', 'GL_OES_vertex_array_object', 'GL_ATC_RGBA_EXPLICIT_ALPHA_AMD', 'GLchar', 'GLenum', 'GLboolean', 'GLbitfield', 'GLbyte', 'GLshort', 'GLint', 'GLint64', 'GLsizei', 'GLubyte', 'GLushort', 'GLuint', 'GLfloat', 'GLclampf', 'GLfixed', 'GLintptr', 'GLsizeiptr', 'GLclampx', 'void', 'GLvoid', 'GLsync', 'GLeglImageOES', 'GLDEBUGPROCKHR', 'GLuint64']