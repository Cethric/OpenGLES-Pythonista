# coding: utf-8
"""
OpenGLES.Util.Physics.__init__.py
Helper script for handling physics related tasks
Note This uses Cannon.js for physics and if it cannot be
found it will atomatically download it
Attributes:
    LIB_DIR (str): The location to check for the Cannon.js file or to download it to.
"""
import os
import ui
import time
import json
import dialogs
import urllib2
import urlparse
import threading
import objc_util

from OpenGLES.GLKit.glkmath import vector3 as v3
from OpenGLES.GLKit.glkmath import matrix4 as m4
from OpenGLES.GLKit.glkmath import matrix3 as m3
from OpenGLES.GLKit.glkmath import quaternion as quat

LIB_DIR = __file__.replace("__init__.py", "")

def get_library(lib_name, url_path=None):
    """
    Check if a file exist otherwise try to download it
    Args:
        lib_name (str): The name of the library
        url_path (Optional[str]): If not none and file cannot be
                                  found download it from this location
    """
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
        """
        Handle object for most Physics related tasks
        Attributes:
            setup (bool): Are the libraries setup yet
            objects (dict): This id of an object and the position and rotation of it
            js (ui.WebView): A method to display infomation and handle the JSContext
        """
        self.setup = False
        self.objects = {}
        self.js = ui.WebView()
        self.js.width = 800
        self.js.height = 300
        self.js.delegate = self
        self.js.load_html(get_library('view.html'))
        
        while not self.setup:
            pass
        
    def webview_should_start_load(self, webview, url, nav_type):
        """
        Should a url be allowed to load.
        If it starts with 'python' no as this is a function
        Args:
            webview (ui.WebView): The view that wants to load
            url (str): the url to load
            nav_type (str): the type of navigation
        """
        if not 'python' in url:
            return True
        else:
            t = urlparse.parse_qs(url.replace("python://method?", ""))
            try:
                s = time.clock()
                func = getattr(self, t['name'][0])
                func(*t['param'])
                e = time.clock()
            except AttributeError as e:
                print e
                print url, t
            return False
    
    def ios_log(self, msg):
        """
        A javascript to python function for simple logging
        Args:
            msg (str): the message to print
        """
        print "BULLET-LOG:\t%s" % msg
        
    def ios_error(self, msg):
        """
        A javascript to python function for simple error logging
        Args:
            msg (str): the message to print
        """
        print "BULLET-ERROR:\t%s" % msg
        
    def object_pos(self, oid, x, y, z):
        """
        A javascript to python function to handle setting object position
        @TODO change values to ints and floats respectively
        Args:
            oid (str): the id of the object
            x (str): the x position
            y (str): the y position
            z (str): the z position
        """
        (oid,x,y,z) = int(oid), float(x), float(y), float(z)
        if oid in self.objects:
            self.objects[oid][0] = (x, y, z)
        else:
            self.objects[oid] = [(x,y,z), (0,0,0,0)]
    
    def object_rot(self, oid, w, x, y, z):
        """
        A javascript to python function to handle setting object rotation
        @TODO change values to ints and floats respectively
        Args:
            oid (str): the id of the object
            w (str): the w real value
            x (str): the x imaginary value
            y (str): the y imaginary value
            z (str): the z imaginary value
        """
        (oid,w,x,y,z) = int(oid), float(w), float(x), float(y), float(z)
        if oid in self.objects:
            self.objects[oid][1] = (w, x, y, z)
        else:
            self.objects[oid] = [(0,0,0), (w,x,y,z)]
            
    def object_json(self, jsonstring):
        try:
            data = json.loads(jsonstring)
            posl = len(data['pos'])
            rotl = len(data['rot'])
            for i in range(0, posl):
                pos = data['pos'][i]
                self.object_pos(i, *pos)
            for i in range(0, rotl):
                rot = data['rot'][i]
                self.object_rot(i, *rot)
        except Exception as e:
            print e
            
    def get_object_mat(self, oid):
        """
        A way of getting the matrix data of an object
        Args:
            oid (int): The id of the object
        Returns:
            (euclid.Matrix4): The model matrix of an MVP
        Raises:
            AttributeError: if the object cannot be found
        """
        if oid is None:
            return None
        if oid in self.objects:
            # quat = euclid.Quaternion(*self.objects[oid][1])
            axis = v3.GLKVector3Make(*self.objects[oid][1][1:])
            quaternion = quat.GLKQuaternionMakeWithAngleAndVector3Axis(self.objects[oid][1][0], axis)
            # mat = euclid.Matrix4.new_identity()
            mat = m4.GLKMatrix4MakeTranslation(*self.objects[oid][0])
            # mat.translate(*self.objects[oid][0])
            mat = m4.GLKMatrix4Multiply(mat, m4.GLKMatrix4MakeWithQuaternion(quaternion))
            # mat *= quat.get_matrix()
            return mat
        else:
            raise AttributeError, "Object with id '%s' does not exist" % oid
            
    def get_object_pos_rot(self, oid):
        if oid in self.objects:
            # quat = euclid.Quaternion(*self.objects[oid][1])
            axis = v3.GLKVector3Make(*self.objects[oid][0][0:3])
            quaternion = quat.GLKQuaternionMakeWithAngleAndVector3Axis(self.objects[oid][0][0], axis)
            # pos = euclid.Vector3(*self.objects[oid][0])
            pos = v3.GLKVector3Make(*self.objects[oid][0])
            return pos, quaternion
        return None, None
            
    def add_cube(self, x, y, z):
        """
        Add a cube physics object to the physics world
        Args:
            x (float): initial x position
            y (float): initial y position
            z (float): initial z position
        Returns:
            (int): the id of the new object
        """
        d = self.js.eval_js('add_cube(%f, %f, %f);' % (x, y, z))
        if d:
            oid = int(d)
            self.objects[oid] = [(x,y,z), (0,0,0,0)]
            return oid
        return None
            
    def add_camera(self, camera_object):
        # r = euclid.Quaternion().rotate_euler(0, camera_object.yaw, 0)
        r = quat.GLKQuaternionMakeWithMatrix3(m3.GLKMatrix3MakeYRotation(camera_object.yaw))
        p = camera_object.position
        d = self.js.eval_js('add_camera(%f,%f,%f, %f,%f,%f,%f, 0.5,0.5,0.5);' % (p.x,p.y,p.z, r.w,r.x,r.y,r.z))
        if d:
            oid = int(d)
            self.objects[oid] = [(p.x, p.y, p.z), (r.w,r.x,r.y,r.z)]
            return oid
        return None
        
    def webview_did_finish_load(self, webview):
        """
        If the libraries have not yet been setup then set them up
        """
        if not self.setup:
            self.setup = True
            self.js.eval_js(CANNON)
            self.js.eval_js(get_library('CannonHelpers.js'))
            self.js.eval_js("setup();")
            # self.js.eval_js("startUpdates();")
            print 'Setup Finished'
        
    def webview_did_fail_load(self, webview, error_code, error_msg):
        """
        Very simple error logging if the webview failed to load something
        """
        print error_code, error_msg
        

_PhysicsWorld = None # CannonJS()
        
def resetPhysicsWorld():
    print "Resetting physics world"
    global _PhysicsWorld
    del _PhysicsWorld
    _PhysicsWorld = None
    # PhysicsWorld = CannonJS()
    getPhysicsWorld()
    
def getPhysicsWorld():
    global _PhysicsWorld
    if _PhysicsWorld is None:
        print 'Setting up new Physics World'
        _PhysicsWorld = CannonJS()
    return _PhysicsWorld
    
def setPhysicsWorld(newWorld):
    _PhysicsWorld = newWorld

__all__ = ["resetPhysicsWorld", "getPhysicsWorld", "setPhysicsWorld"]
        
if __name__ == '__main__':
    c = getPhysicsWorld()
    c.js.present()
    import OpenGLES.Util.Model as Model
    m = Model.XMLModel("../../test_model.xml")
    # oid = c.add_cube(0, 0, 0)
    for x in range(-10, 10, 4):
        for y in range(10, 14, 4):
            for z in range(-10, 10, 4):
                oid = c.add_cube(x,y,z)  # yes I know only the last ```oid``` will be saved
    c.js.eval_js('startUpdates()')
    c.js.wait_modal()
    c.js.eval_js('done();')
    i = 0
    while i < 1000:
        start = time.clock()
        print c.get_object_mat(1)
        i += 1
        end = time.clock()
    #     # print end - start