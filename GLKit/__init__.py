# coding: utf-8
import ui
import ctypes
import weakref
from objc_util import *

from OpenGLES.EAGL import *
from OpenGLES.Util import RenderCycle

GLKView_OBJC = ObjCClass('GLKView')

renderEngine = RenderCycle()
    
def glSetup(context):
    pass

def glkView_drawInRect_(_self, _cmd, _view, _rect):
    view = ObjCInstance(_view)
    renderEngine.render(view.context())
    
def glkViewControllerUpdate_(_self, _cmd, _controller):
    controller = ObjCInstance(_controller)
    renderEngine.update(controller.timeSinceLastUpdate())

GLKViewDelegate_Class = create_objc_class('GLKViewDelegate_Class', methods=[glkView_drawInRect_], protocols=['GLKViewDelegate'])

GLKViewControllerDelegate_Class = create_objc_class('GLKViewControllerDelegate_Class', methods=[glkViewControllerUpdate_], protocols='GLKViewControllerDelegate')

def GLKViewDelegate():
    return GLKViewDelegate_Class.alloc().init()
    
def GLKViewControllerDelegate():
    return GLKViewControllerDelegate_Class.alloc().init()
        
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
    return glvc

class GLKView(ui.View):
    @on_main_thread
    def __init__(self, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)
        frame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
        flex_width, flex_height = (1<<1), (1<<4)
        self.glview = GLKView_OBJC.alloc().initWithFrame_(frame).autorelease()
        self.glview.setAutoresizingMask_(flex_width|flex_height)
        self.vc = GKLViewController("Test GLES", self.glview)
        self.vcd = GLKViewControllerDelegate()
        self.vc.setDelegate_(self.vcd)
        self.glview.setEnableSetNeedsDisplay_(False)
        
    def present(self, *args, **kwargs):
        ui.View.present(self, *args, **kwargs)
        self_objc = ObjCInstance(self)
        
        if self.vc:
            self_objc.nextResponder().addChildViewController_(self.vc)
            self_objc.addSubview_(self.glview)
            frame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
            self.glview.setFrame_(frame)
            renderEngine.setup(self.getContext()._context)
        else:
            raise RuntimeError("GLKViewController property ('vc') must not be None")
        
    def setContext(self, context):
        self.glview.setContext_(context._context)
        
    def getContext(self):
        return EAGLContext(None, self.glview.context)
        
    context = property(getContext, setContext, None, "The EAGL context")
    
    def setDelegate(self, delegate):
        self.glview.setDelegate_(delegate)
        
    def getDelegate(self):
        return self.glview.delegate
        
    delegate = property(getDelegate, setDelegate, None, "GLKViewDelegate")

__all__ = ["GLKView", "GLKViewDelegate", "renderEngine"]
if __name__ == "__main__":
    v = GLKView(None, None)
    d = GLKViewDelegate()
    vc = GKLViewController("GLKit Demo", v)
    vcd = GLKViewControllerDelegate()
    vc.delegate = vcd
    print v
    print d
    print vc
    print vcd