#version 120

// Attributes (no layout qualifiers in GLSL 120)
attribute vec3 vertexPosition;
attribute vec2 vertexUV;
attribute vec3 vertexNormal;

// Varying variables passed to fragment shader
varying vec2 UV;
varying vec3 FragV;
varying vec3 FragL;
varying vec3 FragN;

// Uniforms
uniform mat4 MVP;
uniform mat4 M;
uniform mat4 V;
uniform vec4 lightPosition;
uniform float lightBool;
uniform vec3 planetColor;

void main() {
    gl_Position = MVP * vec4(vertexPosition, 1.0);

    vec4 p = V * M * vec4(vertexPosition, 1.0);
    FragL = lightPosition.xyz - p.xyz;
    FragN = lightBool * (V * M * vec4(vertexNormal, 0.0)).xyz;
    FragV = -p.xyz;

    UV = vertexUV;
}
