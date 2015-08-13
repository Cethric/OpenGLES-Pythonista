# coding: utf-8
import ast
import re
import time
import datetime

headers = ["gl.h", "glext.h", "gl2.h", "gl2ext.h", "gl2platform.h", "gl3.h", "gl31.h", "gl3platform.h"]
for header in headers:
    constants = {}
    functions = []
    print "Parsing header: %s" % header
    with open(header, "r") as infile:
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
        
        #print re.findall(r'(GL_APICALL)', text)
        for call, return_type, name, value in re.findall(r'(GL_API|GL_APICALL)\s+(\w+)\s+GL_APIENTRY\s+(\w+)\s+(.*)', text):
            if not ("sync" in name or "sync" in value or "Sync" in name):
                value = value.replace("(", "").replace(");", "")
                values = value.split(", ")
                func = "    %s = c.%s\n" % (name, name)
                v = [x.replace("const ", "").split(" ")[0] for x in values]
                va = []
                for i in v:
                    if i == "void":
                        i = "ctypes.c_void_p"
                    if i.endswith("*"):
                        i = i.replace("*", "")
                        i = "ctypes.POINTER(%s)" % i
                    va.append(i)
                return_type = return_type if return_type != "void" else "None"
                func += "    %s.restype = %s\n" % (name, return_type)
                func += "    %s.argtypes = %s\n" % (name, str(va))
                func = func.replace("'", "")
                functions.append(func)
    print "%i Functions in %s" % (len(functions), header)
    
    print "Saving Python File"
    print "%i Items to save" % len(constants)
    with open(header.replace(".h", "_c.py"), "w") as f:
        f.write("# Generated Files. DO NOT EDIT\n")
        f.write("# Generated on: %s\n" % time.strftime("%x %X"))
        f.write("import ctypes\n")
        f.write("from objc_util import *\n")
        f.write("DEBUG = False\n\n")
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
        f.write("# GLES Constants\n")
        for k,v in constants.iteritems():
            f.write("%s = %s\n" % (k, v))
        f.write("\n# GL Functions\n")
        for fu in functions:
            f.write("try:\n")
            f.write(fu)
            f.write("except AttributeError as e:\n")
            f.write("    if DEBUG:\n")
            f.write("        print 'could not load the function'\n")
            f.write("        print e\n\n")