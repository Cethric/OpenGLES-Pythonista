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

function setup() {
    world = new CANNON.World();
    world.gravity.set(0, -9.8, 0);
    world.broadphase = new CANNON.NaiveBroadphase();
    world.solver.iterations = 10;
    
    var groundShape = new CANNON.Plane();
    var groundBody = new CANNON.Body({ mass: 0 });
    groundBody.addShape(groundShape);
    groundBody.quaternion.setFromAxisAngle(new CANNON.Vec3(1,0,0),-Math.PI/2);
    world.addBody(groundBody);
}

var intervalID = null;
var intervalID2 = null;

var BLOCK_SIZE = 5;
var curr_id = 0;

function sendObjectData() {
    var start = new Date().getTime();
    var i = curr_id;
    while (i < curr_id+BLOCK_SIZE) {
        if (i > (world.bodies.length-1)) {
            curr_id = 0;
            break;
        }
        var body = world.bodies[i];
        var vec = body.position;
        var quat = body.quaternion;
        send_to_python('object_pos', i+'&param='+vec.x+'&param='+vec.y+'&param='+vec.z);
        send_to_python('object_rot', i+'&param='+quat.w+'&param='+quat.x+'&param='+quat.y+'&param='+quat.z);
        i += 1;
    }
    curr_id += BLOCK_SIZE;
    // for (var id in world.bodies) {
    //     var body = world.bodies[id];
    //     var vec = body.position;
    //     var quat = body.quaternion;
    //     send_to_python('object_pos', id+'&param='+vec.x+'&param='+vec.y+'&param='+vec.z);
    //     send_to_python('object_rot', id+'&param='+quat.w+'&param='+quat.x+'&param='+quat.y+'&param='+quat.z);
    // }
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
    body_info.innerHTML += '<p> Position (x,y,z): ' + pos.x + ', ' + pos.y + ', ' + pos.z + '</p>';
    body_info.innerHTML += '<p> Rotation (w,x,y,z): ' + quat.w + ', ' + quat.x + ', ' + quat.y + ', ' + quat.z + '</p>';
    
}

function addToBodyMenu(body_id) {
    var body_menu = document.getElementById('body_menu');
    body_menu.innerHTML += '<button onclick="tabid = ' + body_id + ';">' + body_id + '</button>';
}

function updateBulletView() {
    var time_s = document.getElementById('time_s');
    time_s.innerHTML = 'Time Spent Updating (ms): ' + ts;
    time_s.innerHTML += '<br>Time Spent Sending to python (ms): ' + timeforotp;
    time_s.innerHTML += '&nbsp;&nbsp;Block Size:&nbsp;' + BLOCK_SIZE;
    var tot_bodies = document.getElementById('tot_bodies');
    tot_bodies.innerHTML = 'Total Number of objects in the world: ' + world.bodies.length;
    if (sw == 20) {
        tabid += 1;
        sw = 0;
    } else {
        sw += 1;
    }
    if (tabid == world.bodies.length) {
        tabid = 1;
    }
    selectTab(tabid);
}

function __update() {
    var start = new Date().getTime();
    world.step(1.0 / 120.0);
    // sendObjectData();
    // intervalID = setTimeout(__update, 0.0001);
    updateBulletView();
    var end = new Date().getTime();
    ts = end - start;
}

function add_cube(x, y, z) {
    var shape = new CANNON.Box(new CANNON.Vec3(1,1,1));
    var body = new CANNON.Body({mass:1});
    body.addShape(shape);
    body.angularVelocity.set(0,10,0);
    body.angularDamping = 0.5;
    body.position.set(x, y, z)
    world.addBody(body);
    addToBodyMenu(world.bodies.length - 1);
    return world.bodies.length - 1;
}

function startUpdates() {
    // intervalID = setTimeout(__update, 0.0001);
    intervalID = setInterval(__update, 1 / 120.0);
    intervalID2 = setInterval(sendObjectData, 1 / 60);
    // __update()
}

function done() {
    // clearTimeout(intervalID);
    clearInterval(intervalID);
    clearInterval(intervalID2);
    console.log("Shutting simulation down");
}