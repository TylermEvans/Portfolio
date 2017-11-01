#pragma once

#include "ppng.h"
#include "util.h"
#include "CubeTexture.h"

class ImageCubeTexture : public CubeTexture {

public:

	//+-X, +-Y, +-Z
	ImageCubeTexture(const vector<string>& filenames) {
		if (filenames.size() != 6)
			throw runtime_error("Bad size for filenames");

		bind(0);
		this->size = 0;

		for (int m = 0; m<6; ++m) {

			vector<uint8_t> pdata;
			map<string, int> meta;

			int w, h;
			png_read(filenames[m], w, h, pdata, meta);

			int bytesperpixel = meta["planes"];
			int fmt;
			if (bytesperpixel == 3)
				fmt = GL_RGB;
			else if (bytesperpixel == 4)
				fmt = GL_RGBA;
			else
				assert(0);


			vector<uint8_t> pix;
			pix.resize(pdata.size());

			//need to flip vertically
			int i = 0;
			for (int row = 0; row<h; ++row) {
				int j = (h - row - 1)*w*bytesperpixel;
				for (int k = 0; k<w; ++k) {
					for (int n = 0; n<bytesperpixel; ++n) {
						pix[j++] = pdata[i++];
					}
				}
			}

			if (w != h)
				throw runtime_error("Cube map images must be square");

			if (this->size != 0 && this->size != w)
				throw runtime_error("Mismatched sizes");
			else
				this->size = w;

			glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + m,
				0, GL_RGBA, size, size, 0, fmt, GL_UNSIGNED_BYTE,
				&pix[0]);
		}


		if (isPowerOf2(size)) {
			glGenerateMipmap(GL_TEXTURE_CUBE_MAP);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_REPEAT);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_REPEAT);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
		}
		else {
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
			glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
		}
	}
};
