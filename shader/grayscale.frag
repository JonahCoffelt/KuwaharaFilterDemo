#version 330 core

layout (location = 0) out vec4 fragColor;


in vec2 uv;

uniform sampler2D screenTexture;

float grayscale(vec3 color) {
    return dot(color.rgb, vec3(0.299, 0.587, 0.114));
}

void main()
{
    // Sample from the texture
    vec4 color = texture(screenTexture, uv);
    // Calculate the grayscale
    color.rgb = vec3(grayscale(color.rgb));
    fragColor = color;
}