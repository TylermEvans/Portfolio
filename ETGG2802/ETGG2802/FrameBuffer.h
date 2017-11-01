#pragma once

#include "Texture2D.h"
#include "CubeTexture.h"

//abstract base class
class RenderTarget {
public:

	RenderTarget(const RenderTarget&) = delete;

	//tells which RT is currently active, or null if none
	static RenderTarget* active_target;

	//saved viewport (the one that was active before we switched
	//to this RT
	static int saved_viewport[4];

	//textures which belong to this render target.
	//Might be 2d or cube
	vector<Texture*> textures;
	Texture* texture;                 //alias for textures[0]

									  //called by subclasses: Determine if it's ok to bind this rt
	void checkOkToBind() {
		if (active_target)
			throw runtime_error("Another FBO is already bound");
		for (unsigned i = 0; i<textures.size(); ++i) {
			if (textures[i]->on_units.size() != 0) {
				for (int j : textures[i]->on_units) {
					if (Texture::active_textures[j] != textures[i]) {
						//internal consistency error
						assert(0);
					}
				}
				throw runtime_error("This FBO has textures that are active");
			}
		}
	}


	void unbind() {
		if (active_target != this)
			throw runtime_error("This FBO is not bound");
		active_target = NULL;
		for (unsigned i = 0; i<textures.size(); ++i)
			textures[i]->part_of_active_fbo = false;
		glBindFramebuffer(GL_FRAMEBUFFER, 0);
		glViewport(saved_viewport[0], saved_viewport[1],
			saved_viewport[2], saved_viewport[3]);
	}

	//only the subclasses are useful for creation, so we forbid creation of
	//the RenderTarget directly
protected:
	RenderTarget() {}
};



class Framebuffer2D : public RenderTarget {
public:

	int width, height;                   //size of FBO
	int fbo;                            //GL identifier
	Texture2D* depthtexture;            //depth texture (z buffer) + stencil
	vector<GLuint> drawbuffers;

	Framebuffer2D(int width, int height) {
		init(width, height, GL_RGBA, GL_UNSIGNED_BYTE, 1);
	}

	Framebuffer2D(int width, int height, int count) {
		init(width, height, GL_RGBA, GL_UNSIGNED_BYTE, count);
	}

	Framebuffer2D(int width, int height, int count, int format, int type) {
		init(width, height, format, type, count);
	}

	void init(int width, int height, int format, int type, int count) {

		this->width = width;
		this->height = height;

		textures.resize(count);
		for (int i = 0; i<count; ++i) {
			textures[i] = new Texture2D();
			textures[i]->bind(0);
			glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
			textures[i]->unbind(0);
		}
		texture = textures[0];

		depthtexture = new Texture2D();
		depthtexture->bind(0);
		glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH24_STENCIL8, width, height, 0, GL_DEPTH_STENCIL, GL_UNSIGNED_INT_24_8, NULL);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
		depthtexture->unbind(0);

		GLuint tmp[1];
		glGenFramebuffers(1, tmp);
		fbo = tmp[0];
		glBindFramebuffer(GL_FRAMEBUFFER, fbo);
		for (int i = 0; i<count; ++i) {
			assert(textures[i]->tex != 0);
			glFramebufferTexture(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0 + i, textures[i]->tex, 0);
		}
		glFramebufferTexture(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, depthtexture->tex, 0);

		int complete = glCheckFramebufferStatus(GL_FRAMEBUFFER);
		if (complete != GL_FRAMEBUFFER_COMPLETE) {
			throw runtime_error("Framebuffer is not complete: " + str(complete));
		}

		glBindFramebuffer(GL_FRAMEBUFFER, 0);

		for (int i = 0; i<count; ++i)
			drawbuffers.push_back(GL_COLOR_ATTACHMENT0 + i);

	}

	void bind() {
		if (active_target != NULL) {
			active_target->unbind();
		}
		checkOkToBind();
		for (unsigned i = 0; i<textures.size(); ++i) {
			assert(!textures[i]->part_of_active_fbo);
			textures[i]->part_of_active_fbo = true;
		}
		active_target = this;
		glBindFramebuffer(GL_FRAMEBUFFER, fbo);
		glGetIntegerv(GL_VIEWPORT, saved_viewport);
		glViewport(0, 0, width, height);
		glDrawBuffers(drawbuffers.size(), &drawbuffers[0]);
	}
};

class FramebufferCube : public RenderTarget {
public:

	int size;                       //size of FBO sides; width = height
	int fbos[6];                    //one fbo for each side of cube map
	Texture2D* depthtextures[6];

	FramebufferCube(int size) {
		init(size, GL_RGBA, GL_UNSIGNED_BYTE);
	}

	FramebufferCube(int width, int height, int format, int type) {
		init(size, format, type);
	}

	void init(int size, int format, int type) {
		this->size = size;
		texture = new CubeTexture();
		textures.push_back(texture);
		texture->bind(0);
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
		glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

		for (int j = 0; j<6; ++j) {
			int target = GL_TEXTURE_CUBE_MAP_POSITIVE_X + j;
			glTexImage2D(target, 0, format, size, size, 0, format, type, NULL);

			GLuint tmp[1];
			glGenFramebuffers(1, tmp);
			fbos[j] = tmp[0];

			glBindFramebuffer(GL_FRAMEBUFFER, fbos[j]);

			glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
				target, texture->tex, 0);

			depthtextures[j] = new Texture2D();
			depthtextures[j]->bind(0);   //binds to the 2d attachment point, not the cube point
			glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH24_STENCIL8, size, size, 0,
				GL_DEPTH_STENCIL, GL_UNSIGNED_INT_24_8, NULL);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
			glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
			glFramebufferTexture(GL_FRAMEBUFFER,
				GL_DEPTH_STENCIL_ATTACHMENT, depthtextures[j]->tex, 0);

			int complete = glCheckFramebufferStatus(GL_FRAMEBUFFER);
			if (complete != GL_FRAMEBUFFER_COMPLETE) {
				throw  runtime_error("Framebuffer is not complete: " + str(complete));
			}

			glBindFramebuffer(GL_FRAMEBUFFER, 0);

		}

	}

	//face should be GL_TEXTURE_CUBE_MAP_{POSITIVE,NEGATIVE}_{X,Y,Z}
	void bind(int face) {
		if (active_target != NULL)
			active_target->unbind();
		checkOkToBind();
		active_target = this;
		for (unsigned i = 0; i<textures.size(); ++i)
			textures[i]->part_of_active_fbo = true;
		int idx = face - GL_TEXTURE_CUBE_MAP_POSITIVE_X;
		glBindFramebuffer(GL_FRAMEBUFFER, fbos[idx]);
		glGetIntegerv(GL_VIEWPORT, saved_viewport);
		glViewport(0, 0, size, size);
	}
};