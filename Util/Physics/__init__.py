# coding: utf-8
import os
import ui
import time
import dialogs
import urllib2
import urlparse
import euclid

LIB_DIR = __file__.replace("__init__.py", "")

def get_library(lib_name, url_path=None):
    lib_file = os.path.join(LIB_DIR, lib_name)
    if os.path.exists(lib_file):
        with open(lib_file, 'rb') as f:
            data = f.read()
    else:
        if url_path:
            print "Could not find: '%s'.\nDownloading it from %s" % (lib_name, url_path)
            f = urllib2.urlopen(url_path)
            data = f.read()
            with open(lib_file, "wb") as r:
                r.write(data)
        else:
            data = ""
            print "Could not find '%s' and could not download it. Assuming it does not exist" % lib_name
    return data

CANNON = get_library('Cannon.js', 'https://raw.githubusercontent.com/schteppe/cannon.js/master/build/cannon.min.js')


class CannonJS(object):
    def __init__(self):
        self.setup = False
        self.objects = {}
        
        self.js = ui.WebView()
        self.js.width = 700
        self.js.height = 300
        self.js.delegate = self
        self.js.load_html(get_library('view.html'))
        
        while not self.setup:
            pass
        
    def webview_should_start_load(self, webview, url, nav_type):
        if not 'python' in url:
            return True
        else:
            t = urlparse.parse_qs(url.replace("python://method?", ""))
            try:
                func = getattr(self, t['name'][0])
                func(*t['param'])
            except AttributeError as e:
                print e
                print url, t
            return False
            
    def ios_log(self, args):
        print "BULLET-LOG:\t%s" % args
        
    def ios_error(self, args):
        print "BULLET-ERROR:\t%s" % args
        
    def object_pos(self, oid, x, y, z):
        (oid,x,y,z) = int(oid), float(x), float(y), float(z)
        if oid in self.objects:
            self.objects[oid][0] = (x, y, z)
        else:
            self.objects[oid] = [(x,y,z), (0,0,0,0)]
    
    def object_rot(self, oid, w, x, y, z):
        (oid,w,x,y,z) = int(oid), float(w), float(x), float(y), float(z)
        if oid in self.objects:
            self.objects[oid][1] = (w, x, y, z)
        else:
            self.objects[oid] = [(0,0,0), (w,x,y,z)]
            
    def get_object_mat(self, oid):
        if oid in self.objects:
            quat = euclid.Quaternion(*self.objects[oid][1])
            mat = euclid.Matrix4.new_identity()
            mat.translate(*self.objects[oid][0])
            mat *= quat.get_matrix()
            return mat
        else:
            raise AttributeError, "Object with id '%s' does not exist" % oid
            
    def add_cube(self, x, y, z):
        oid = int(self.js.eval_js('add_cube(%f, %f, %f);' % (x, y, z)))
        self.objects[oid] = [(x,y,z), (0,0,0,0)]
        return oid
        
    def webview_did_finish_load(self, webview):
        if not self.setup:
            self.js.eval_js(CANNON)
            self.js.eval_js(get_library('CannonHelpers.js'))
            self.js.eval_js("setup();")
            self.js.eval_js("startUpdates();")
            self.setup = True
            print 'Setup Finished'
        
    def webview_did_fail_load(self, webview, error_code, error_msg):
        print error_code, error_msg
        

PhysicsWorld = CannonJS()

__all__ = ["PhysicsWorld"]
        
if __name__ == '__main__':
    c = PhysicsWorld
    import OpenGLES.Util.Model as Model
    m = Model.XMLModel("../../test_model.xml")
    # oid = c.add_cube(0, 0, 0)
    for x in range(-10, 10, 4):
        for y in range(10, 14, 4):
            for z in range(-10, 10, 4):
                oid = c.add_cube(x,y,z)  # yes I know only the last ```oid``` will be saved
    i = 0
    while i < 1000:
        start = time.clock()
        print c.get_object_mat(oid)
        i += 1
        end = time.clock()
        print end - start
    
    c.js.eval_js('done')