#version 120

attribute vec3 vertexPosition;
attribute vec3 vertexColor;

varying vec3 fragmentColor;

uniform mat4 mvp;
uniform float time;

void main() {
    float angle = time * 2.0;
    mat4 rotationY = mat4(
        cos(angle), 0.0, sin(angle), 0.0,
        0.0, 1.0, 0.0, 0.0,
        -sin(angle), 0.0, cos(angle), 0.0,
        0.0, 0.0, 0.0, 1.0
    );
    gl_Position = mvp * rotationY * vec4(vertexPosition, 1.0);
    fragmentColor = vertexColor;
}
