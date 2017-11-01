#pragma once

#include "ppng.h"
#include "util.h"
#include "Texture2D.h"

class SolidTexture : public Texture2D {
public:
	//fmt = GL_FLOAT or GL_UNSIGNED_BYTE
	int fmt;

	SolidTexture(float r, float g, float b, float a) : SolidTexture(GL_UNSIGNED_BYTE, r, g, b, a) {}

	SolidTexture(int fmt, float r, float g, float b, float a) {
		this->fmt = fmt;
		if (fmt != GL_UNSIGNED_BYTE && fmt != GL_FLOAT)
			throw runtime_error("Bad format");

		GLuint tmp[1];
		glGenTextures(1, tmp);
		this->tex = tmp[0];

		bind(0);
		glTexImage2D(GL_TEXTURE_2D,
			0,
			(fmt == GL_FLOAT) ? GL_RGBA32F : GL_RGBA,
			1, 1, 0,
			GL_RGBA,
			fmt,
			NULL);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
		if (fmt == GL_FLOAT) {
			float f[] = { r,g,b,a };
			glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 1, 1, GL_RGBA, fmt, f);
		}
		else {
			uint8_t bb[] = { (uint8_t)(r * 255), (uint8_t)(g * 255), (uint8_t)(b * 255), (uint8_t)(a * 255) };
			glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 1, 1, GL_RGBA, fmt, bb);
		}
	}
};
