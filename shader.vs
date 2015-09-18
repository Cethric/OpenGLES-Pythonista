attribute vec4 position;

varying lowp vec4 colorVarying;
uniform mat4 M;
uniform mat4 V;
uniform mat4 P;

void main() {
    mat4 MVP = P * V * M;
    colorVarying = vec4(1.0,0.0,0.0,1.0);
    
    // gl_Position = MVP * position;
    gl_Position = (V * M) * position;
}