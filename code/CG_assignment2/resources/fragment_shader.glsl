#version 120

varying vec3 fragmentColor;
uniform float time;

void main() {
    vec3 psychedelicColor = vec3(
        sin(fragmentColor.r * 3.14 + time) * 0.5 + 0.5,
        sin(fragmentColor.g * 3.14 + time * 1.5) * 0.5 + 0.5,
        sin(fragmentColor.b * 3.14 + time * 2.0) * 0.5 + 0.5
    );
    gl_FragColor = vec4(psychedelicColor, 1.0);
}