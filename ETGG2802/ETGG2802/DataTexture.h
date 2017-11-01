#pragma once

#include "ppng.h"
#include "util.h"
#include <vector>
#include "math3d.h"
#include "Texture2D.h"


class DataTexture : public Texture2D {
public:
	GLenum ifmt, fmt;
	int w, h;
	int numcomponents;
	DataTexture(const vector<vec4>& data, int width, int height) {
		init(width, height, (float*)&data[0], 4, data.size());
	}
	DataTexture(const vector<vec3>& data, int width, int height) {
		init(width, height, (float*)&data[0], 3, data.size());
	}
	DataTexture(const vector<vec2>& data, int width, int height) {
		init(width, height, (float*)&data[0], 2, data.size());
	}
	DataTexture(const vector<float>& data, int width, int height) {
		init(width, height, &data[0], 1, data.size());
	}
	void init(int w, int h, const float* p, int numcomponents, int numitems) {
		this->w = w;
		this->h = h;
		this->numcomponents = numcomponents;
		if (numcomponents == 1) {
			ifmt = GL_R32F;
			fmt = GL_RED;
		}
		else if (numcomponents == 2) {
			ifmt = GL_RG32F;
			fmt = GL_RG;
		}
		else if (numcomponents == 3) {
			ifmt = GL_RGB32F;
			fmt = GL_RGB;
		}
		else if (numcomponents == 4) {
			ifmt = GL_RGBA32F;
			fmt = GL_RGBA;
		}
		else
			assert(0);

		bind(0);
		glTexImage2D(GL_TEXTURE_2D, 0, ifmt, w, h, 0, fmt, GL_UNSIGNED_BYTE, NULL);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
		if (p)
			update(p, numcomponents*numitems);
	}

	void update(const vector<float>& f) {
		if (numcomponents != 1)
			throw runtime_error("Component count mismatch: Created with " + str(numcomponents));
		update(&f[0], f.size());
	}
	void update(const vector<vec2>& f) {
		if (numcomponents != 2)
			throw runtime_error("Component count mismatch: Created with " + str(numcomponents));
		update((float*)&f[0], f.size() * 2);
	}
	void update(const vector<vec3>& f) {
		if (numcomponents != 3)
			throw runtime_error("Component count mismatch: Created with " + str(numcomponents));
		update((float*)&f[0], f.size() * 3);
	}
	void update(const vector<vec4>& f) {
		if (numcomponents != 4)
			throw runtime_error("Component count mismatch: Created with " + str(numcomponents));
		update((float*)&f[0], f.size() * 4);
	}
	void update(const float* p, int numfloats) {
		bind(0);
		glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, w, h, fmt, GL_FLOAT, p);
	}
};

