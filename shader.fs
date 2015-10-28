varying lowp vec4 colorVarying;

uniform sampler2D test;

void main() {
    highp vec2 seed = vec2(1, 1);
    gl_FragColor = colorVarying * texture2D(test, vec2(0.5, 0.5));
}