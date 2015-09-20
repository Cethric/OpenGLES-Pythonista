# coding: utf-8
import objc_util
from objc_util import *
import ctypes
import euclid
import urlparse
import time
import ui

PHYSICS_DIR = __file__.replace("__init__.py", "")
BULLET_CODE = os.path.join(os.path.join(PHYSICS_DIR,"ammo.js"))
if os.path.exists(BULLET_CODE):
    with open(BULLET_CODE, "rb") as f:
        AMMO = f.read()
else:
    ammo_url = "https://raw.githubusercontent.com/kripken/ammo.js/master/builds/ammo.js"
    print "No Bullet engine (ammo.js file) found"
    print "Downloading one from '%s'" % ammo_url
    import urllib2
    try:
        f = urllib2.urlopen(ammo_url)
        AMMO = f.read()
        with open(BULLET_CODE, "wb") as r:
            r.write(AMMO)
    finally:
        f.close()
    print "ammo.js successfully downloaded"
    
BULLET_HTML = '''<!DOCTYPE html>
<html>
    <head>
        <title> Bullet Physics Hub </title>
        <script>
            function send_to_python(name, param) {
                var iframe = document.createElement("IFRAME");
                iframe.setAttribute("src", 'python://method?name=' + name + "&param=" + param);
                document.documentElement.appendChild(iframe);
                iframe.parentNode.removeChild(iframe);
                iframe = null;
            }
            
            console.log = function(log) {
                send_to_python("ios_log", log);
            }
            console.debug = function(log) {
                send_to_python("ios_debug", log);
            }
            console.info = function(log) {
                send_to_python("ios_info", log);
            }
            console.warn = function(log) {
                send_to_python("ios_warn", log);
            }
            console.error = function(log) {
                send_to_python("ios_error", log);
            }
            console.alert = function(prompt, msg) {
                send_to_python("ios_alert", prompt + ":" + msg);
            }
            window.onerror = (function(error, url, line, col, errorobj) {
               console.error(error + " at " + line + ":" + col);
            });
            console.log("logging activated");
            print = (function(arg) {
                send_to_python('ios_print', arg);
            });
            
            get_position = (function(id, pos) {
                send_to_python('_get_position', id + '#' + pos)
            })
            
            get_rotation = (function(id, pos) {
                send_to_python('_get_rotation', id + '#' + pos)
            })
        </script>
    </head>
    <body>
        <p> Bullet Physics test </p>
    </body>
</html>'''

PHYSICS_WORLD_LOAD = '''
var collisionConfiguration = new Ammo.btDefaultCollisionConfiguration();
var dispatcher = new Ammo.btCollisionDispatcher(collisionConfiguration);

var maxProxies = 16384;
var aabbmin = new Ammo.btVector3(-1000,-1000,-1000); // world size
var aabbmax = new Ammo.btVector3(1000,1000,1000);
var overlappingPairCache = new Ammo.btAxisSweep3(aabbmin, aabbmax, maxProxies);

var solver = new Ammo.btSequentialImpulseConstraintSolver();
var dynamicsWorld = new Ammo.btDiscreteDynamicsWorld(dispatcher, overlappingPairCache, solver, collisionConfiguration);
dynamicsWorld.setGravity(new Ammo.btVector3(0, -9.8, 0));

var bodies = [];

var groundShape = new Ammo.btBoxShape(new Ammo.btVector3(50, 50, 50));
var groundTransform = new Ammo.btTransform();
groundTransform.setIdentity();
groundTransform.setOrigin(new Ammo.btVector3(0, -56, 0));

(function() {
  var mass = 0;
  var isDynamic = mass !== 0;
  var localInertia = new Ammo.btVector3(0, 0, 0);

  if (isDynamic)
    groundShape.calculateLocalInertia(mass, localInertia);

  var myMotionState = new Ammo.btDefaultMotionState(groundTransform);
  var rbInfo = new Ammo.btRigidBodyConstructionInfo(mass, myMotionState, groundShape, localInertia);
  var body = new Ammo.btRigidBody(rbInfo);

  dynamicsWorld.addRigidBody(body);
  bodies.push(body);
})();
print(dynamicsWorld);
'''

ADD_SPHERE = '''
(function() {
  var colShape = new Ammo.btSphereShape(%f);
  
  var startTransform = new Ammo.btTransform();
  startTransform.setIdentity();
  
  var mass = %f;
  var isDynamic = mass !== 0;
  var localInertia = new Ammo.btVector3(0, 0, 0);

  if (isDynamic) {
    colShape.calculateLocalInertia(mass, localInertia);
  }
  
  startTransform.setOrigin(new Ammo.btVector3(%f, %f, %f));
  
  var myMotionState = new Ammo.btDefaultMotionState(startTransform);
  var rbInfo = new Ammo.btRigidBodyConstructionInfo(mass, myMotionState, colShape, localInertia);
  var body = new Ammo.btRigidBody(rbInfo);

  dynamicsWorld.addRigidBody(body);
  bodies.push(body);
})();
var l = bodies.length - 1;
l
'''

ADD_BOX = '''
(function() {
  var size = %f;
  var colShape = new Ammo.btBoxShape(new Ammo.btVector3(size, size, size));
  
  var startTransform = new Ammo.btTransform();
  startTransform.setIdentity();
  
  var mass = %f;
  var isDynamic = mass !== 0;
  var localInertia = new Ammo.btVector3(0, 0, 0);

  if (isDynamic) {
    colShape.calculateLocalInertia(mass, localInertia);
  }
  
  startTransform.setOrigin(new Ammo.btVector3(%f, %f, %f));
  
  var myMotionState = new Ammo.btDefaultMotionState(startTransform);
  var rbInfo = new Ammo.btRigidBodyConstructionInfo(mass, myMotionState, colShape, localInertia);
  var body = new Ammo.btRigidBody(rbInfo);

  dynamicsWorld.addRigidBody(body);
  bodies.push(body);
})();
var l = bodies.length - 1;
l
'''

ADD_SHAPE = '''
(function() {
  var colShape = _shape;
  
  var startTransform = new Ammo.btTransform();
  startTransform.setIdentity();
  
  var mass = %f;
  var isDynamic = mass !== 0;
  var localInertia = new Ammo.btVector3(0, 0, 0);

  if (isDynamic) {
    colShape.calculateLocalInertia(mass, localInertia);
  }
  
  startTransform.setOrigin(new Ammo.btVector3(%f, %f, %f));
  
  var myMotionState = new Ammo.btDefaultMotionState(startTransform);
  var rbInfo = new Ammo.btRigidBodyConstructionInfo(mass, myMotionState, colShape, localInertia);
  var body = new Ammo.btRigidBody(rbInfo);

  dynamicsWorld.addRigidBody(body);
  bodies.push(body);
})();
var l = bodies.length - 1;
l
'''

GET_POSITION = '''
var id = %s;
var body = bodies[id];
if (body.getMotionState()) {
    var trans = new Ammo.btTransform();
    body.getMotionState().getWorldTransform(trans);
    get_position(id, [trans.getOrigin().x(), trans.getOrigin().y(),trans.getOrigin().z()]);
}
'''

GET_ROTATION = '''
var body = bodies[%s];
if (body.getMotionState()) {
    var trans = new Ammo.btTransform();
    body.getMotionState().getWorldTransform(trans);
    get_rotation(id, [trans.getRotation().w(), trans.getRotation().x(),trans.getRotation().y(), trans.getRotation().z()]);
}
'''

class Bullet(object):
    def __init__(self):
        self.setup = False
        self.wv = ui.WebView()
        self.wv.delegate = self
        self.wv.load_html(BULLET_HTML)
        self.frame = (0,0,0,0)
        self.ids = []
        self.objdata = {}
        
        self.can_check = False
        # self.wv.present("sheet")
        
    def webview_should_start_load(self, webview, url, nav_type):
        r = not 'python' in url
        if not r:
            url = url.replace("python://method?", "")
            qs = urlparse.parse_qs(url)
            funcname = qs['name'][0]
            args = qs['param'][0]
            func = None
            try:
                func = getattr(self, funcname)
            except Exception as e:
                print "Function", funcname, "Does not exist"
            if func:
                func(args)
        return r
    
    def ios_log(self, args):
        print "BULLET-LOG:", args
        
    def ios_print(self, args):
        print "BULLET:", args
        
    def ios_error(self, args):
        print "BULLET-ERROR:", args
    
    def _get_position(self, args):
        args = args.split("#")
        self.objdata[int(args[0])][0] = [float(x) for x in args[1].split(",")]
        self.can_check = True
        
    def _get_rotation(self, args):
        args = args.split("#")
        self.objdata[int(args[0])][1] = [float(x) for x in args[1].split(",")]
        self.can_check = True
        
    def webview_did_finish_load(self, webview):
        if not self.setup:
            self.wv.evaluate_javascript(AMMO)
            self.wv.evaluate_javascript(PHYSICS_WORLD_LOAD)
            self.setup = True
        print "Functions can be called now"
        
    def webview_did_fail_load(self, webview, error_code, error_msg):
        print error_code, error_msg
        
    def add_object(self, vert, mass=1, pos=[0,0,0], convex=False):
        tris = len(vert) / 3
        if convex:
            self.wv.evaluate_javascript("var _shape = new Ammo.btConvexHullShape();")
            for x in range(0, tris, 3):
                v = vert[x:x+3]
                self.wv.evaluate_javascript("_shape.addPoint(new Ammo.btVector3(%f, %f, %f));" % (v[0], v[1], v[2]))
        else:
            self.wv.evaluate_javascript("var _mesh = new Ammo.btTriangleMesh();")
            for x in range(0, tris, 9):
                v = vert[x:x+9]
                (x1,y1,z1) = v[0:3]
                (x2,y2,z2) = v[3:6]
                (x3,y3,z3) = v[6:9]
                self.wv.evaluate_javascript("_mesh.addTriangle(new Ammo.btVector3(%f, %f, %f), new Ammo.btVector3(%f, %f, %f), new Ammo.btVector3(%f, %f, %f))" % tuple(v))
            self.wv.evaluate_javascript("var _shape = new Ammo.btBvhTriangleMeshShape(_mesh, true);")
        oid = self.wv.evaluate_javascript(ADD_SHAPE % (mass, pos[0], pos[1], pos[2]))
        self.ids.append(oid)
        self.objdata[int(oid)] = [(0,0,0), (0,0,0,0)]
        return oid
        
    def add_sphere(self, mass=1, pos=[0,0,0], radius=1):
        oid = self.wv.evaluate_javascript(ADD_SPHERE % (radius, mass, pos[0], pos[1], pos[2]))
        self.ids.append(oid)
        self.objdata[int(oid)] = [(0,0,0), (0,0,0,0)]
        return oid
        
    def add_box(self, mass=1, pos=[0,0,0], size=1):
        oid = self.wv.evaluate_javascript(ADD_BOX % (size, mass, pos[0], pos[1], pos[2]))
        self.ids.append(oid)
        self.objdata[int(oid)] = [(0,0,0), (0,0,0,0)]
        return oid
        
    def step_simulation(self, step, maxSubStep=1, fixTimeStep=1/60.0):
        start = time.clock()
        s = "dynamicsWorld.stepSimulation(%f, %f, %f)" % (step, maxSubStep, fixTimeStep)
        self.wv.evaluate_javascript(s)
        end = time.clock()
        print "step_simulation", end - start
        
    def get_object_pos(self, i=0):
        start = time.clock()
        self.can_check = False
        self.wv.evaluate_javascript(GET_POSITION % i)
        while not self.can_check:
            pass
        vpos = euclid.Vector3()
        if not int(i) in self.objdata:
            return vpos
        pos = self.objdata[int(i)][0]
        vpos.x = pos[0]
        vpos.y = pos[1]
        vpos.z = pos[2]
        end = time.clock()
        # print "get_object_pos", end - start
        return vpos
        
    def get_object_rot(self, i=0):
        start = time.clock()
        self.can_check = False
        self.wv.evaluate_javascript(GET_ROTATION % i)
        while not self.can_check:
            pass
            
        qrot = euclid.Quaternion()
        if not int(i) in self.objdata:
            return qrot
            
        rot = self.objdata[int(i)][1]
        qrot.w = rot[0]
        qrot.x = rot[1]
        qrot.y = rot[2]
        qrot.z = rot[3]
        end = time.clock()
        # print "get_object_rot", end - start
        return qrot
    
    def set_object_pos(self, i, pos):
        self.wv.evaluate_javascript("")
        
PhysicsWorld = Bullet()
while not PhysicsWorld.setup:
    pass
    
__all__ = ['PhysicsWorld']
        
if __name__ == "__main__":
    p = PhysicsWorld
    p.add_sphere(1, [0,20,0])
    import OpenGLES.Util.Model as Model
    m = Model.XMLModel("../../test_model.xml")
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    i = p.add_object(m.frames[m.frame], 10, [0,30,0])
    for _ in range(0, 10):
        p.step_simulation(1/60.0, 10)
        pos = p.get_object_pos(i)
        rot = p.get_object_rot(i)
        mat = euclid.Matrix4()
        mat.translate(pos.x, pos.y, pos.z)
        mat = mat * rot.get_matrix()
        print mat 