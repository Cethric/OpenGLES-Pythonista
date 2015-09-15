# coding: utf-8
# NOTE
# For this function to work the current working
# directory must be set to the same directory as all
# the GLES header files
import ast
import os
import re
import copy
import time
import datetime

headers = ["gl.h", "glext.h", "gl2.h", "gl2ext.h", "gl2platform.h", "gl3.h", "gl31.h", "gl3platform.h"]

VERBOSITY = 0

def download_header_files(force_download=False):
    if not os.path.exists(os.path.join(os.getcwd(), headers[0])) or force_download:
        if VERBOSITY >= 0:
            print "Downloading headers..."
        import urllib2
        for header in headers:
            if '2' in header:
                url = 'https://www.khronos.org/registry/gles/api/GLES2/%s'
            elif '3' in header:
                url = 'https://www.khronos.org/registry/gles/api/GLES3/%s'
            else:
                url = 'https://www.khronos.org/registry/gles/api/GLES/%s'
            try:
                if VERBOSITY >= 1:
                    print "Downloading: '%s'... Please wait" % (url%header)
                f = urllib2.urlopen(url % header)
                with open(os.path.join(os.getcwd(), header), "w") as h:
                    h.write(f.read())
                if VERBOSITY >= 1:
                    print "Done"
            finally:
                f.close()
        if VERBOSITY >= 0:
            print "Finished downloading headers"
            
def build_constants_file():
    with open('GLConstants.py', "wb") as f:
        f.write("import ctypes\n")
        f.write("GLchar = ctypes.c_char\n")
        f.write("GLenum = ctypes.c_uint32\n")
        f.write("GLboolean = ctypes.c_uint8\n")
        f.write("GLbitfield = ctypes.c_uint32\n")
        f.write("GLbyte = ctypes.c_int8\n")
        f.write("GLshort = ctypes.c_int16\n")
        f.write("GLint = ctypes.c_int32\n")
        f.write("GLint64 = ctypes.c_int64\n")
        f.write("GLsizei = ctypes.c_int32\n")
        f.write("GLubyte = ctypes.c_uint8\n")
        f.write("GLushort = ctypes.c_uint16\n")
        f.write("GLuint = ctypes.c_uint32\n")
        f.write("GLfloat = ctypes.c_float\n")
        f.write("GLclampf = ctypes.c_float\n")
        f.write("GLfixed = ctypes.c_int32\n")
        f.write("GLintptr = ctypes.c_int32\n")
        f.write("GLsizeiptr = ctypes.c_int32\n")
        f.write("GLclampx = ctypes.c_int\n")
        f.write("void = ctypes.c_void_p\n")
        f.write("GLvoid = ctypes.c_void_p\n")
        f.write("GLsync = None\n\n")

def build_gl_header_file():
    for header in headers:
        constants = {}
        functions = []
        if VERBOSITY >= 0:
            print "Parsing header: %s" % header
        with open(os.path.join(os.getcwd(), header), "r") as infile:
            text = infile.read()
            for name, value in re.findall(r'#define\s+(\w+)\s+(.*)', text):
                value = value if value != "0xFFFFFFFFFFFFFFFFull" else "0xFFFFFFFFFFFFFFFF"
                value = value if value != "0xFFFFFFFFu" else "0xFFFFFFFF"
                try:
                    constants[name] = "{0:#0{1}x}".format(ast.literal_eval(value),10)
                except Exception as e:
                    pass

            for name, value in re.findall(r'#typedef\s+(\w+)\s+(.*)', text):
                print name, value
            
            arg_names = []
            for call, return_type, name, value in re.findall(r'(GL_API|GL_APICALL)'
                                                              '\s+(\w+)\s+GL_APIENTRY'
                                                              '\s+(\w+)\s+(.*)', text):
                if not ("sync" in name or "sync" in value or "Sync" in name):
                    arg_names.append(name)
                    value = value.replace("(", "").replace(");", "")
                    values = value.split(", ")
                    v = [x.replace("const ", "")
                          .split(" ")[0] for x in values]
                    agn = []
                    agn2 = []
                    try:
                        agn = [x.replace("const ", "")
                                .replace(" *", "")
                                .replace("*", "")
                                .split(" ")[-1] for x in values]
                        agn2 = copy.deepcopy(agn)
                        agn2.append('argtypes_p=None')
                    except IndexError as e:
                        if VERBOSITY >= 2:
                            print e
                    va = []
                    for i in v:
                        if i == "void":
                            i = "ctypes.c_void_p"
                        if i.endswith("*"):
                            i = i.replace("*", "")
                            i = "ctypes.POINTER(%s)" % i
                        va.append(i)
                    return_type = return_type if return_type != "void" else "None"
                    
                    argva = 0
                    for a in agn:
                        if 'GL' in a:
                            agn[agn.index(a)] = 'param%s' % argva
                            agn2[agn2.index(a)] = 'param%s' % argva
                            argva += 1
                        if '[' in a and ']' in a:
                            try:
                                (lb, rb) = a.index('[')+1, a.index(']')
                                i = agn.index(a)
                                asize = a[lb:rb]
                                oldcmd = agn[i].strip("[1234567890]")
                                agn[i] = oldcmd
                                agn2[i] = oldcmd
                                va[i] = "(%s * %i)" % (va[i], int(asize))
                                if VERBOSITY >= 1:
                                    print "Limited Array Object Support"
                            except ValueError as e:
                                if VERBOSITY >= 2:
                                    print e
                            argva += 1
                    func = '''    def {funcname}({arg_names1}):
        restype = {return_type}
        if argtypes_p:
            argtypes = argtypes_p
        else:
            argtypes = [{argument_types}]
        cfunc = c.{funcname}
        cfunc.restype = restype
        cfunc.argtypes = argtypes
        return cfunc({arg_names})
    # Check if the function actually exists
    f = c.{funcname}
    del f
    '''
                    func = func.format(
                                *[],
                                **{
                                    'funcname': name,
                                    'return_type': return_type,
                                    'argument_types': ', '.join(va),
                                    'arg_names': ', '.join(agn),
                                    'arg_names1': ', '.join(agn2),
                                })
                    func = func.replace("'", "")
                    functions.append(func)
                else:
                    if VERBOSITY >= 1:
                        print "Sync functions are not currently supported. Function name '%s'" % name
        if VERBOSITY >= 1:
            print "%i Functions in %s" % (len(functions), header)
            print "Saving Python File"
            print "%i Items to save" % len(constants)
        with open(header.replace(".h", "_c.py"), "w") as f:
            f.write("# Generated Files. DO NOT EDIT\n")
            f.write("# Generated on: %s\n" % time.strftime("%x %X"))
            f.write("import ctypes\n")
            f.write("from objc_util import *\n")
            f.write("from GLConstants import *\n\n")
            f.write("DEBUG = 1\n")
            f.write("loaded = [0, 0]\n\n")
            f.write("# GLES Constants\n")
            for k,v in constants.iteritems():
                f.write("%s = %s\n" % (k, v))
            f.write("\n# GL Functions\n")
            for fu in functions:
                f.write("try:\n")
                f.write(fu)
                f.write("loaded[0] += 1\n")
                f.write("except AttributeError as e:\n")
                f.write("    loaded[1] += 1\n")
                f.write("    if DEBUG > 1:\n")
                f.write("        print 'could not load the function'\n")
                f.write("        print e\n\n")
            f.write("print 'Loaded %i functions and failed\\n'\\\n"
                    "      'to load %i functions of %i functions in\\n'\\\n"
                    "      'the header " + header +"' % (loaded[0], loaded[1], sum(loaded))\n")
            f.write("__all__ = [%s]" % ", ".join(arg_names))
        execfile(header.replace(".h", "_c.py"))
        if VERBOSITY >= 0:
            print "Finished parsing header %s" % header
        
def main():
    download_header_files()
    build_constants_file()
    build_gl_header_file()
    
if __name__ == "__main__":
    main()