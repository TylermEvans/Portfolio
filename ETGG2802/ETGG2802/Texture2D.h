#pragma once

#include "ppng.h"
#include "util.h"
#include "Texture.h"

//Generic 2D texture. This is never directly instantiated.
class Texture2D : public Texture {
public:
	int w, h;

	Texture2D() : Texture(GL_TEXTURE_2D) {}

protected:
	Texture2D(const Texture2D&) = delete;
};

