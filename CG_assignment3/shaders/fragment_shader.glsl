#version 120

// Varying from vertex shader
varying vec2 UV;
varying vec3 FragV;
varying vec3 FragL;
varying vec3 FragN;

// Uniforms
uniform mat4 M;
uniform mat4 V;
uniform vec4 lightPosition;
uniform vec3 planetColor;
uniform sampler2D sampler;

uniform vec3 diffuseAlbedo;  // No default value in GLSL 120
uniform vec3 specularAlbedo;

void main() {
    vec3 n = normalize(FragN);
    vec3 l = normalize(FragL);
    vec3 v = normalize(FragV);
    vec3 r = reflect(-l, n);

    vec4 textureColor = texture2D(sampler, UV);

    vec3 diffuse = max(dot(l, n), 0.0) * textureColor.rgb;
    vec3 specular = pow(max(dot(r, v), 0.0), 12.0) * specularAlbedo;

    vec4 ambient = vec4(0.1, 0.1, 0.1, 0.8);
    vec3 finalColor = ambient.rgb * textureColor.rgb + diffuse + specular;

    gl_FragColor = vec4(finalColor, 1.0);
}
