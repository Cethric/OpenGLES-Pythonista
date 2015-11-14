varying lowp vec4 colorVarying;

uniform sampler2D test;

void main() {
    gl_FragColor = colorVarying; // * texture2D(test, vec2(0.5, 0.5));
}