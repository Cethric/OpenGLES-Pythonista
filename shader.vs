attribute vec4 position;

varying lowp vec4 colorVarying;
uniform mat4 M;
uniform mat4 V;
uniform mat4 P;

void main() {
    mat4 MVP = P * V * M;
    colorVarying = vec4(0.5,0.5,0.5,1.0) * M;
    
    gl_Position = MVP * position;
}