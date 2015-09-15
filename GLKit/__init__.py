# coding: utf-8
import ui
import ctypes
import weakref
from objc_util import *

from OpenGLES.EAGL import *
from OpenGLES.Util import RenderCycle

__all__ = ["GLKView", "GLKViewDelegate", "setRenderEngine", "getRenderEngine"]

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/GLKit.framework").load()


GLKView_OBJC = ObjCClass('GLKView')

renderEngine = RenderCycle()

def setRenderEngine(engine):
    global renderEngine
    renderEngine = engine

def getRenderEngine():
    return renderEngine

game_initialised = False
def glkView_drawInRect_(_self, _cmd, _view, _rect):
    global game_initialised
    view = ObjCInstance(_view)
    if not game_initialised:
        try:
            renderEngine.setup(view.context())
            print "Game has been Initialised"
        finally:
            game_initialised = True
    renderEngine.render(view.context())
    
def glkViewControllerUpdate_(_self, _cmd, _controller):
    controller = ObjCInstance(_controller)
    renderEngine.update(controller.timeSinceLastUpdate())
    renderEngine.fps = controller.framesPerSecond()
    renderEngine.framesDisplayed = controller.framesDisplayed()

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
    
class TouchController(ui.View):
    def __init__(self, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)
        
        self.left_touch = {}
        self.right_touch = {}
        
        self.dir_move = [0,0]
        self.dir_look = [0,0]
        
        ui.delay(self.update_touch, 0.01)
        
    def update_touch(self):
        renderEngine.look_f(self.dir_look)
        renderEngine.move_f(self.dir_move)
        ui.delay(self.update_touch, 0.01)

    def touch_began(self, touch):
        if touch.location[0] > self.width / 2:
            self.right_touch[touch.touch_id] = touch.location
        else:
            self.left_touch[touch.touch_id] = touch.location

    def touch_moved(self, touch):
        b = 50
        if touch.touch_id in self.right_touch:
            mx = touch.location[0] - self.right_touch[touch.touch_id][0]
            my = touch.location[1] - self.right_touch[touch.touch_id][1]
            
            if mx < -b:
                #print "Strafe Left", mx + b
                self.dir_move[0] = 1
            elif mx > b:
                #print "Strafe Right", mx - b
                self.dir_move[0] = -1
            else:
                self.dir_move[0] = 0
                
            if my < -b:
                #print "Move Forward", my + b
                self.dir_move[1] = 1
            elif my > b:
                #print "Move Backward", my - b
                self.dir_move[1] = -1
            else:
                self.dir_move[1] = 0
                
        elif touch.touch_id in self.left_touch:
            mx = touch.location[0] - self.left_touch[touch.touch_id][0]
            my = touch.location[1] - self.left_touch[touch.touch_id][1]
            if mx < -b:
                #print "Look Left", mx + b
                self.dir_look[0] = 1
            elif mx > b:
                #print "Look Right", mx - b
                self.dir_look[0] = -1
            else:
                self.dir_look[0] = 0
                
            if my < -b:
                #print "Look Up", my + b
                self.dir_look[1] = 1
            elif my > b:
                #print "Look Down", my - b
                self.dir_look[1] = -1
            else:
                self.dir_look[1] = 0

    def touch_ended(self, touch):
        if touch.touch_id in self.right_touch:
            del self.right_touch[touch.touch_id]
            self.dir_move = [0,0]
        elif touch.touch_id in self.left_touch:
            del self.left_touch[touch.touch_id]
            self.dir_look = [0,0]

class GLKView(ui.View):
    @on_main_thread
    def __init__(self, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)
        print self.width, self.height
        self.name = "HELLO WORLD"
        frame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
        flex_width, flex_height = (1<<1), (1<<4)
        self.glview = GLKView_OBJC.alloc().initWithFrame_(frame).autorelease()
        self.glview.setDrawableDepthFormat_(2)
        self.glview.setAutoresizingMask_(flex_width|flex_height)
        self.vc = GKLViewController("Test GLES", self.glview)
        self.vcd = GLKViewControllerDelegate()
        self.vc.setDelegate_(self.vcd)
        self.glview.setEnableSetNeedsDisplay_(False)
        self.tc = TouchController(frame=(0,0,400,400))
        
    def present(self, *args, **kwargs):
        ui.View.present(self, *args, **kwargs)
        self_objc = ObjCInstance(self)
        if self.vc:
            self_objc.nextResponder().addChildViewController_(self.vc)
            self_objc.addSubview_(self.glview)
            frame = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
            self.glview.setFrame_(frame)
        else:
            raise RuntimeError("GLKViewController property ('vc') must not be None")
        
        self.tc.multitouch_enabled = True
        
        #self.glview.addSubview_(ObjCInstance(tc))
        self.add_subview(self.tc)
        self.tc.width = self.width
        self.tc.height = self.height
        
        self.tc.bring_to_front()
    def will_close(self):
        ui.cancel_delays()
        print "Tearing down GLES data"
        renderEngine.teardown()
        print "Goodbye"
        
    def updateToucher(self):
        print "Update Touch events"
        
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


if __name__ == "__main__":
    v = GLKView(frame=(0,0,800,600))
    d = GLKViewDelegate()
    vc = GKLViewController("GLKit Demo", v)
    vcd = GLKViewControllerDelegate()
    vc.delegate = vcd
    print v
    print d
    print vc
    print vcd