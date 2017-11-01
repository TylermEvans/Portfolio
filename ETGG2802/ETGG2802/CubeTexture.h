#pragma once

#include "ppng.h"
#include "util.h"
#include "Texture.h"

class CubeTexture : public Texture {
public:
	int size;
	CubeTexture() : Texture(GL_TEXTURE_CUBE_MAP) {}
};
