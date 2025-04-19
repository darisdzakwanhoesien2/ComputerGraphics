#version 120

attribute vec3 vertexPosition_modelspace;
attribute vec2 vertexUV;

uniform mat4 mvp;

varying vec2 UV;

void main() {
    gl_Position = mvp * vec4(vertexPosition_modelspace, 1.0);
    UV = vertexUV;
}
