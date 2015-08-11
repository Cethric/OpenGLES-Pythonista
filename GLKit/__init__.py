# coding: utf-8
import ctypes
from objc_util import *

from OpenGLES.EAGL import *

GLKView_OBJC = ObjCClass('GLKView')
UIBarButtonItem = ObjCClass('UIBarButtonItem')

class GLKView(object):
    @on_main_thread
    def __init__(self, context, delegate):
        frame = CGRect(CGPoint(0, 0), CGSize(800, 600))
        self.glview = GLKView_OBJC.alloc().initWithFrame_(frame).autorelease()
        
    def setContext(self, context):
        self.glkview.setContext_(context._context)
        
    def getContext(self):
        return EAGLContext(None, self.glkview.getContext_())
        
    context = property(getContext, setContext, None, "The EAGL context")
    
    def setDelegate(self, delegate):
        self.glkview.setDelegate_(delegate._delegate)
        
    def getDelegate(self):
        return self.glkview.delegate
        
    delegate = property(getDelegate, setDelegate, None, "GLKViewDelegate")
    

def draw():
    print "Draw"

def glkView_drawInRect_(_self, _cmd, view, rect):
    draw()
    

GLKViewDelegate_Class = create_objc_class('GLKViewDelegate', methods=[glkView_drawInRect_], protocols=['GLKViewDelegate'])

def GLKViewDelegate():
    return GLKViewDelegate_Class.alloc().init()
        
GLKViewController_OBJC = ObjCClass('GLKViewController')
def dismiss(_self, _cmd):
    self = ObjCInstance(_self)
    self.view().delegate().release()
    self.view().setDelegate_(None)
    self.dismissViewControllerAnimated_completion_(True, None)
GKLViewController_Class = create_objc_class('GKLViewController_Class', GLKViewController_OBJC, methods=[dismiss])

def GKLViewController(title, glview):
    glvc = GKLViewController_Class.alloc().initWithNibName_bundle_(None, None).autorelease()
    glvc.setTitle_(title)
    glvc.setView_(glview)
    
    done_b = UIBarButtonItem.alloc().initWithTitle_style_target_action_('Done', 2, glvc, 'dismiss').autorelease()
    glvc.navigationItem().setRightBarButtonItem_(done_b)
    
    return glvc

__all__ = ["GLKView", "GLKViewDelegate", "GKLViewController", "draw"]
if __name__ == "__main__":
    v = GLKView(None, None)
    d = GLKViewDelegate.alloc().init()
    print d
    print GKLViewController("GLKit Demo", v)