#pragma once

#include "ppng.h"
#include "util.h"
#include "Texture.h"

//Generic type for 2D array textures. Never directly instantiated.
class Texture2DArray : public Texture{
    public:
    int w,h;
    int numslices;

    protected:
    Texture2DArray(): Texture(GL_TEXTURE_2D_ARRAY) {}

};


