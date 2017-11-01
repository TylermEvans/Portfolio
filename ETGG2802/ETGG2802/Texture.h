#pragma once

#include "ppng.h"
#include "util.h"

class Texture {
public:

	Texture(const Texture&) = delete;

	//texture identifier
	GLuint tex = 0;

	//type of texture
	GLenum type = 0;

	//list of texture units this texture is active on.
	set<int> on_units;

	bool part_of_active_fbo = false;
	//which textures are active on which texture units.
	//We limit it to 128 units.
	static Texture* active_textures[128];

	virtual ~Texture() {}

	static bool isPowerOf2(int x) {
		return  ((x - 1)&x) == 0;
	}

	void bind(int unit) {
		assert(tex != 0);
		assert(type != 0);
		glActiveTexture(GL_TEXTURE0 + unit);
		glBindTexture(type, this->tex);
		if (active_textures[unit])
			active_textures[unit]->on_units.erase(unit);
		on_units.insert(unit);
		active_textures[unit] = this;
	}

	void unbind(int unit) {
		glActiveTexture(GL_TEXTURE0 + unit);
		glBindTexture(type, 0);
		on_units.erase(unit);
		active_textures[unit] = NULL;
	}

	void unbind() {
		for (int u : on_units) {
			glActiveTexture(GL_TEXTURE0 + u);
			glBindTexture(type, 0);
			active_textures[u] = NULL;
		}
		on_units.clear();
	}

protected:
	Texture(GLenum ty) : type(ty) {
		GLuint tmp[1];
		glGenTextures(1, tmp);
		this->tex = tmp[0];
	}


};

