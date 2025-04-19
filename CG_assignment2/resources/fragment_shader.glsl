#version 120

varying vec2 UV;
uniform sampler2D texture_sampler;
uniform float time;

void main() {
    vec4 texColor = texture2D(texture_sampler, UV);
    vec3 invertedColor = vec3(1.0) - texColor.rgb;

    vec3 psychedelicColor = vec3(
        sin(invertedColor.r * 3.14 + time) * 0.5 + 0.5,
        sin(invertedColor.g * 3.14 + time * 1.5) * 0.5 + 0.5,
        sin(invertedColor.b * 3.14 + time * 2.0) * 0.5 + 0.5
    );

    gl_FragColor = vec4(psychedelicColor, texColor.a);
}
