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
print = (function(arg) {
    send_to_python('ios_print', arg);
});

console.log("logging activated");

var world = null;
var timeforotp = 0;

var cansetup = false;

function setup() {
    if (cansetup==false) {
        world = new CANNON.World();
        world.gravity.set(0, -20, 0);
        world.broadphase = new CANNON.NaiveBroadphase();
        world.solver.iterations = 10;
        
        var groundShape = new CANNON.Plane();
        var groundBody = new CANNON.Body({ mass: 0 });
        groundBody.addShape(groundShape);
        groundBody.quaternion.setFromAxisAngle(new CANNON.Vec3(1,0,0),-Math.PI/2);
        world.addBody(groundBody);
        cansetup = true;
    }
}

var intervalID = null;
var intervalID2 = null;

function sendObjectData() {
    var start = new Date().getTime();
    var pos = []
    var rot = []
    for (var body in world.bodies) {
        var vec = world.bodies[body].position;
        var quat = world.bodies[body].quaternion;
        pos.push([vec.x, vec.y, vec.z]);
        rot.push([quat.w, quat.x, quat.y, quat.z]);
    }
    var data = {}
    data.pos = pos
    data.rot = rot
    send_to_python('object_json', JSON.stringify(data));
    var end = new Date().getTime();
    // console.log(end - start)
    timeforotp = end - start;
}

var ts = 0;
var tabid = 0;
var sw = 0;

function selectTab(tab_id) {
    var body_info = document.getElementById('body_info');
    var body = world.bodies[tab_id];
    var pos = body.position;
    var quat = body.quaternion;
    body_info.innerHTML = '<p> Body: ' + tab_id + '</p>';
    body_info.innerHTML += '<p> Position (x,y,z): ' + pos.x.toFixed(2) + ', ' + pos.y.toFixed(2) + ', ' + pos.z.toFixed(2) + '</p>';
    body_info.innerHTML += '<p> Rotation (w,x,y,z): ' + quat.w.toFixed(2) + ', ' + quat.x.toFixed(2) + ', ' + quat.y.toFixed(2) + ', ' + quat.z.toFixed(2) + '</p>';
    
}

function addToBodyMenu(body_id) {
    var body_menu = document.getElementById('body_menu');
    body_menu.innerHTML += '<button onclick="tabid = ' + body_id + ';">' + body_id + '</button>';
}

function updateBulletView() {
    var time_s = document.getElementById('time_s');
    time_s.innerHTML = 'Time Spent Updating (ms): ' + ts;
    time_s.innerHTML += '<br>Time Spent Sending to python (ms): ' + timeforotp;
    var tot_bodies = document.getElementById('tot_bodies');
    tot_bodies.innerHTML = 'Total Number of objects in the world: ' + world.bodies.length;
    // if (sw == 20) {
    //     tabid += 1;
    //     sw = 0;
    // } else {
    //     sw += 1;
    // }
    // if (tabid == world.bodies.length) {
    //     tabid = 1;
    // }
    selectTab(tabid);
}

var last = 0;

function __update() {
    var start = new Date().getTime();
    world.step(1.0 / 30.0, start - last, 9);
    last = start;
    // sendObjectData();
    // intervalID = setTimeout(__update, 0.0001);
    updateBulletView();
    var end = new Date().getTime();
    ts = end - start;
}

var fid = 0;

function add_cube(x, y, z) {
    var shape = new CANNON.Box(new CANNON.Vec3(0.5,0.5,0.5));
    var body = new CANNON.Body({mass:1});
    body.addShape(shape);
    // body.angularVelocity.set(0,10,0);
    body.angularDamping = 0.5;
    body.position.set(x, y, z)
    world.addBody(body);
    fid += 1;
    addToBodyMenu(fid);
    return fid;
}

function add_camera(px,py,pz, qw,qx,qy,qz, w,h,d) {
    var shape = new CANNON.Box(new CANNON.Vec3(w,h,d));
    var body = new CANNON.Body({mass:16});
    body.addShape(shape);
    body.angularDamping = 0.5;
    body.position.set(px,py,pz);
    body.quaternion.set(qw,qx,qy,qz);
    world.addBody(body);
    fid += 1;
    addToBodyMenu(fid);
    return fid;
}

function set_object_pos(oid, px, py, pz) {
    var body = world.bodies[oid];
    body.position.set(px, py, pz);
}
function set_object_rot(oid, qw, qx, qy, qz) {
    var body = world.bodies[oid];
    body.quaternion.set(qw,qx,qy,qz);
}

function startUpdates() {
    // intervalID = setTimeout(__update, 0.0001);
    last = new Date().getTime();
    intervalID = setInterval(__update, 1 / 180.0);
    intervalID2 = setInterval(sendObjectData, 1 / 120.0);
    // __update()
}

function done() {
    // clearTimeout(intervalID);
    clearInterval(intervalID);
    clearInterval(intervalID2);
    console.log("Shutting simulation down");
}