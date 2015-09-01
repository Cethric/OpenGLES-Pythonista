# coding: utf-8
import objc_util
from objc_util import *
import ctypes
import euclid
import time

ObjCClass("NSBundle").bundleWithPath_("/System/Library/Frameworks/JavaScriptCore.framework").load()
    
JSContext = ObjCClass("JSContext")
context = JSContext.new()

def error_func(_self, _context, _error):
    print "JAVASCRIPT ERROR"
    print ObjCInstance(_error)
    
eb = ObjCBlock(error_func, None, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p])
context.setExceptionHandler_(eb)

context.evaluateScript_("function print(args){return args;}")

with open("/private/var/mobile/Containers/Shared/AppGroup/877D6E00-D22C-4407-9A69-C27FA4B9356A/Documents/site-packages/OpenGLES/Util/Physics/ammo.js", "rb") as f:
    AMMO = f.read()
context.evaluateScript_(AMMO)

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
var body = bodies[%s];
if (body.getMotionState()) {
    var trans = new Ammo.btTransform();
    body.getMotionState().getWorldTransform(trans);
    [trans.getOrigin().x(), trans.getOrigin().y(),trans.getOrigin().z()]
}
'''

GET_ROTATION = '''
var body = bodies[%s];
if (body.getMotionState()) {
    var trans = new Ammo.btTransform();
    body.getMotionState().getWorldTransform(trans);
    [trans.getRotation().w(), trans.getRotation().x(),trans.getRotation().y(), trans.getRotation().z()]
}
'''

context.evaluateScript_(PHYSICS_WORLD_LOAD)

@on_main_thread        
def add_object(vert, mass=1, pos=[0,0,0], convex=False):
    global context
    tris = len(vert) / 3
    if convex:
        context.evaluateScript_("var _shape = new Ammo.btConvexHullShape();")
        for x in range(0, tris, 3):
            v = vert[x:x+3]
            context.evaluateScript_("_shape.addPoint(new Ammo.btVector3(%f, %f, %f));" % (v[0], v[1], v[2]))
    else:
        context.evaluateScript_("var _mesh = new Ammo.btTriangleMesh();")
        for x in range(0, tris, 9):
            v = vert[x:x+9]
            (x1,y1,z1) = v[0:3]
            (x2,y2,z2) = v[3:6]
            (x3,y3,z3) = v[6:9]
            context.evaluateScript_("_mesh.addTriangle(new Ammo.btVector3(%f, %f, %f), new Ammo.btVector3(%f, %f, %f), new Ammo.btVector3(%f, %f, %f))" % tuple(v))
            
        context.evaluateScript_("var _shape = new Ammo.btBvhTriangleMeshShape(_mesh, true);")
        
    return context.evaluateScript_(ADD_SHAPE % (mass, pos[0], pos[1], pos[2]))

@on_main_thread
def add_sphere(mass=1, pos=[0,0,0], radius=1):
    global context
    return context.evaluateScript_(ADD_SPHERE % (radius, mass, pos[0], pos[1], pos[2]))

@on_main_thread
def add_box(mass=1, pos=[0,0,0], size=1):
    global context
    return context.evaluateScript_(ADD_BOX % (size, mass, pos[0], pos[1], pos[2]))

@on_main_thread    
def step_simulation(step, maxSubStep=1, fixTimeStep=1/60.0):
    #start = time.clock()
    global context
    s = "dynamicsWorld.stepSimulation(%f, %f, %f)" % (step, maxSubStep, fixTimeStep)
    try:
        context.evaluateScript_(s)
    except Exception as e:
        print s
        print e
    #end = time.clock()
    #print end - start
        
@on_main_thread
def get_object_pos(i=0):
    global context
    vpos = euclid.Vector3()
    p = context.evaluateScript_(GET_POSITION % i).toArray()
    if p:
        pos = [x.doubleValue() for x in p]
        vpos.x = pos[0]
        vpos.y = pos[1]
        vpos.z = pos[2]
    return vpos

@on_main_thread
def get_object_rot(i=0):
    global context
    qrot = euclid.Quaternion()
    rota = context.evaluateScript_(GET_ROTATION % i).toArray()
    if rota:
        rot = [x.doubleValue() for x in rota]
        qrot.w = rot[0]
        qrot.x = rot[1]
        qrot.y = rot[2]
        qrot.z = rot[3]
    return qrot
    
@on_main_thread
def set_object_pos(i, pos):
    global context
    
__all__ = ("add_object", "add_sphere", "step_simulation", "get_object_pos", "get_object_rot")
        
if __name__ == "__main__":
    add_sphere(1, [0,20,0])
    import OpenGLES.Util.Model as Model
    m = Model.XMLModel("../../test_model.xml")
    i = add_object(m.frames[m.frame], 10, [0,30,0])
    print i
    
    for _ in range(0, 365):
        step_simulation(1/60.0, 10)
        pos = get_object_pos(i)
        rot = get_object_rot(i)
        print rot
        mat = euclid.Matrix4()
        mat.translate(pos.x, pos.y, pos.z)
        mat = mat * rot.get_matrix()
        print mat 