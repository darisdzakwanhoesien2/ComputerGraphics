#version 330 core

// Interpolated values from the vertex shaders
in vec2 uv;

// Ouput data
out vec3 color;

// Values that stay constant for the whole mesh.
uniform sampler2D texture_sampler;

void main(){

	// Output color = color of the texture at the specified UV
	color = texture(texture_sampler, uv).rgb;
}