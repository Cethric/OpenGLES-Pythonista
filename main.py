# coding: utf-8
import EAGL
import GLES
import GLKit

import os
for x,y,z in os.walk("/System/Library/Frameworks/OpenGLES.framework"):
    print x,y,z

reload(EAGL)
reload(GLES)
reload(GLKit)


if __name__ == "__main__":
    view = GLKit.GLKView.GLKView()
    view.width = 400
    view.height = 400
    eaglContext = EAGL.EAGLContext()
    view.setContext(eaglContext)
    view.present("sheet")
    view.set_needs_display()