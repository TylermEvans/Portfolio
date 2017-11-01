#pragma once

#include "Texture2D.h"
#include "Texture2DArray.h"
#include "math3d.h"
#include "util.h"
#include "CubeTexture.h"

class Program {
public:
	static const int POSITION_INDEX = 0;
	static const int TEXCOORD_INDEX = 1;
	static const int NORMAL_INDEX = 2;
	static const int TANGENT_INDEX = 3;
	static const int BITANGENT_INDEX = 4;
	static const int BONE_INDEX = 5;

	static Program* active;

	Program(const Program&) = delete;

	class Setter {
	public:
		string name;
		int loc;
		Setter(string n, int lo) {
			name = n;
			loc = lo;
		}
		Setter() {}

		virtual void set(float value) {
			throw runtime_error("Trying to set uniform " + name + " to a float");
		}
		virtual void set(const vec2& value) {
			throw runtime_error("Trying to set uniform " + name + " to a vec2");
		}
		virtual void set(const ivec2& value) {
			throw runtime_error("Trying to set uniform " + name + " to an ivec2");
		}
		virtual void set(const vec3& value) {
			throw runtime_error("Trying to set uniform " + name + " to a vec3");
		}
		virtual void set(const vec4& value) {
			throw runtime_error("Trying to set uniform " + name + " to a vec4");
		}
		virtual void set(const vector<float>& value) {
			throw runtime_error("Trying to set uniform " + name + " to a float array");
		}
		virtual void set(const vector<vec2>& value) {
			throw runtime_error("Trying to set uniform " + name + " to a vec2 array");
		}
		virtual void set(const vector<vec3>& value) {
			throw runtime_error("Trying to set uniform " + name + " to a vec3 array");
		}
		virtual void set(const vector<vec4>& value) {
			throw runtime_error("Trying to set uniform " + name + " to a vec4 array");
		}
		virtual void set(const vector<mat4>& value) {
			throw runtime_error("Trying to set uniform " + name + " to a mat4 array");
		}
		virtual void set(const mat4& value) {
			throw runtime_error("Trying to set uniform " + name + " to a mat4");
		}
		virtual void set(Texture* value) {
			throw runtime_error("Trying to set uniform " + name + " to a Texture");
		}
	};

	class FloatSetter : public Setter {
	public:
		FloatSetter(string name, int loc) : Setter(name, loc) {}
		void set(float v) override {
			glUniform1f(this->loc, v);
		}
	};

	class IntSetter : public Setter {
	public:
		IntSetter(string name, int loc) : Setter(name, loc) {}
		void set(float v) override {
			glUniform1i(this->loc, (int)v);
		}
	};

	class UIntSetter : public Setter {
	public:
		UIntSetter(string name, int loc) : Setter(name, loc) {}
		void set(float v) override {
			glUniform1ui(this->loc, (unsigned)v);
		}
	};

	class Vec2Setter : public Setter {
	public:
		Vec2Setter(string name, int loc) : Setter(name, loc) {}
		void set(const vec2& v) override {
			glUniform2f(this->loc, v.x, v.y);
		}
	};

	class IVec2Setter : public Setter {
	public:
		IVec2Setter(string name, int loc) : Setter(name, loc) {}
		void set(const ivec2& v) override {
			glUniform2i(this->loc, v.x, v.y);
		}
	};

	class Vec3Setter : public Setter {
	public:
		Vec3Setter(string name, int loc) : Setter(name, loc) {}
		void set(const vec3& v) override {
			glUniform3f(this->loc, v.x, v.y, v.z);
		}
	};

	class Vec4Setter : public Setter {
	public:
		Vec4Setter(string name, int loc) : Setter(name, loc) {}
		void set(const vec4& v) override {
			glUniform4f(this->loc, v.x, v.y, v.z, v.w);
		}
	};

	class FloatArraySetter : public Setter {
	public:
		unsigned size;
		FloatArraySetter(string name, int loc, int sz) : Setter(name, loc),
			size(sz) {}
		void set(const vector<float>& v) override {
			if (v.size() != size)
				throw runtime_error("Bad size: Got " + str(v.size()) + " but expected " + str(size));
			glUniform1fv(this->loc, size, (float*)&v[0]);
		}
	};

	class Vec2ArraySetter : public Setter {
	public:
		unsigned size;
		Vec2ArraySetter(string name, int loc, int sz) : Setter(name, loc),
			size(sz) {}
		void set(const vector<vec2>& v) override {
			if (v.size() != size)
				throw runtime_error("Bad size: Got " + str(v.size()) + " but expected " + str(size));
			glUniform2fv(this->loc, size, (float*)&v[0]);
		}
	};

	class Vec3ArraySetter : public Setter {
	public:
		unsigned size;
		Vec3ArraySetter(string name, int loc, int sz) : Setter(name, loc),
			size(sz) {}
		void set(const vector<vec3>& v) override {
			if (v.size() != size)
				throw runtime_error("Bad size: Got " + str(v.size()) + " but expected " + str(size));
			glUniform3fv(this->loc, size, (float*)&v[0]);
		}
	};


	class Vec4ArraySetter : public Setter {
	public:
		unsigned size;
		Vec4ArraySetter(string name, int loc, int sz) : Setter(name, loc),
			size(sz) {}
		void set(const vector<vec4>& v) override {
			if (v.size() != size)
				throw runtime_error("Bad size: Got " + str(v.size()) + " but expected " + str(size));
			glUniform4fv(this->loc, size, (float*)&v[0]);
		}
	};

	class Mat4ArraySetter : public Setter {
	public:
		unsigned size;
		Mat4ArraySetter(string name, int loc, int sz) : Setter(name, loc),
			size(sz) {}
		void set(const vector<mat4>& v) override {
			if (v.size() != size)
				throw runtime_error("Bad size: Got " + str(v.size()) + " but expected " + str(size));
			glUniformMatrix4fv(this->loc, size, true, (float*)&v[0]);
		}
	};

	class Mat4Setter : public Setter {
	public:
		Mat4Setter(string name, int loc) : Setter(name, loc) {}
		void set(const mat4& v) override {
			glUniformMatrix4fv(this->loc, 1, true, (float*)v._m);
		}
	};

	class Sampler2dSetter : public Setter {
	public:
		int unit;
		Sampler2dSetter(string name, int loc, int unit) : Setter(name, loc) {
			this->unit = unit;
		}
		void set(Texture* v) override {
			if (!dynamic_cast<Texture2D*>(v))
				throw runtime_error("Cannot convert to Texture2D");
			v->bind(this->unit);
			glUniform1i(this->loc, this->unit);
		}
	};

	class Sampler2dArraySetter : public Setter {
	public:
		int unit;
		Sampler2dArraySetter(string name, int loc, int unit) : Setter(name, loc) {
			this->unit = unit;
		}
		void set(Texture* v) override {
			if (!dynamic_cast<Texture2DArray*>(v))
				throw runtime_error("Cannot convert to Texture2DArray");
			v->bind(this->unit);
			glUniform1i(this->loc, this->unit);
		}
	};

	class SamplerCubeSetter : public Setter {
	public:
		int unit;
		SamplerCubeSetter(string name, int loc, int unit) : Setter(name, loc) {
			this->unit = unit;
		}
		void set(Texture* v) override {
			if (!dynamic_cast<CubeTexture*>(v))
				throw runtime_error("Texture is not a cube texture");
			v->bind(this->unit);
			glUniform1i(this->loc, this->unit);
		}
	};

	map<string, Setter*> setters;
	GLuint prog;
	string name;
	bool is_compute_shader;

	Program(string csfname) {
		init("", "", "", csfname, {});
	}

	Program(string vsfname, string fsfname, const vector<string>& outputs) {
		init(vsfname, "", fsfname, "", outputs);
	}

	Program(string vsfname, string gsfname, string fsfname, const vector<string>& outputs) {
		init(vsfname, gsfname, fsfname, "", outputs);
	}

	void init(string vsfname, string gsfname, string fsfname, string csfname, const vector<string>& outputs) {

		if (csfname.length() > 0)
			is_compute_shader = true;
		else
			is_compute_shader = false;

		this->name = vsfname + " " + gsfname + " " + fsfname + " " + csfname;

		GLint tmp[1];

		GLuint vs = 0;
		if (vsfname.length() > 0)
			vs = this->make_shader(vsfname, GL_VERTEX_SHADER);
		GLuint gs = 0;
		if (gsfname.length() > 0)
			gs = this->make_shader(gsfname, GL_GEOMETRY_SHADER);
		GLuint fs = 0;
		if (fsfname.length() > 0)
			fs = this->make_shader(fsfname, GL_FRAGMENT_SHADER);
		GLuint cs = 0;
		if (csfname.length() > 0)
			cs = this->make_shader(csfname, GL_COMPUTE_SHADER);

		prog = glCreateProgram();
		if (vs)
			glAttachShader(prog, vs);
		if (gs)
			glAttachShader(prog, gs);
		if (fs)
			glAttachShader(prog, fs);
		if (cs)
			glAttachShader(prog, cs);

		glBindAttribLocation(prog, Program::POSITION_INDEX, "a_position");
		glBindAttribLocation(prog, Program::TEXCOORD_INDEX, "a_texcoord");
		glBindAttribLocation(prog, Program::NORMAL_INDEX, "a_normal");
		glBindAttribLocation(prog, Program::TANGENT_INDEX, "a_tangent");
		glBindAttribLocation(prog, Program::BITANGENT_INDEX, "a_bitangent");
		glBindAttribLocation(prog, Program::BONE_INDEX, "a_boneidx");

		for (unsigned i = 0; i<outputs.size(); ++i)
			glBindFragDataLocation(prog, i, outputs[i].c_str());

		glLinkProgram(prog);
		char infolog[4096];
		GLsizei isize;
		glGetProgramInfoLog(prog, sizeof(infolog), &isize, infolog);
		if (isize > 0) {
			cout << "Linking " << this->name << ":\n";
			cout << infolog;
		}

		glGetProgramiv(prog, GL_LINK_STATUS, tmp);
		if (!tmp[0])
			throw runtime_error("Could not link shaders");

		for (string x : outputs) {
			int loc = glGetFragDataLocation(prog, x.c_str());
			if (loc == -1)
				throw runtime_error("Shader " + fsfname + " does not have output " + x);
		}

		int texcounter = 0;
		glGetProgramiv(prog, GL_ACTIVE_UNIFORMS, tmp);
		GLuint numuniforms = tmp[0];
		for (GLuint i = 0; i<numuniforms; ++i) {
			GLint type_[1];
			GLint size[1];
			GLint le[1];
			char namea[256];
			glGetActiveUniformsiv(prog, 1, &i, GL_UNIFORM_TYPE, type_);
			glGetActiveUniformsiv(prog, 1, &i, GL_UNIFORM_SIZE, size);
			glGetActiveUniformName(prog, i, sizeof(namea), le, namea);
			string name = namea;
			int loc = glGetUniformLocation(prog, name.c_str());
			uninitialized.insert(name);
			if (size[0] == 1) {
				switch (type_[0]) {
				case GL_INT:
					setters[name] = new IntSetter(name, loc);
					break;
				case GL_UNSIGNED_INT:
					setters[name] = new UIntSetter(name, loc);
					break;
				case GL_FLOAT:
					setters[name] = new FloatSetter(name, loc);
					break;
				case GL_INT_VEC2:
					setters[name] = new IVec2Setter(name, loc);
					break;
				case GL_FLOAT_VEC2:
					setters[name] = new Vec2Setter(name, loc);
					break;
				case GL_FLOAT_VEC3:
					setters[name] = new Vec3Setter(name, loc);
					break;
				case GL_FLOAT_VEC4:
					setters[name] = new Vec4Setter(name, loc);
					break;
				case GL_SAMPLER_2D:
					setters[name] = new Sampler2dSetter(name, loc, texcounter);
					texcounter += 1;
					break;
				case GL_SAMPLER_2D_ARRAY:
					setters[name] = new Sampler2dArraySetter(name, loc, texcounter);
					texcounter += 1;
					break;
				case GL_SAMPLER_CUBE:
					setters[name] = new SamplerCubeSetter(name, loc, texcounter);
					texcounter += 1;
					break;
				case GL_FLOAT_MAT4:
					setters[name] = new Mat4Setter(name, loc);
					break;
				default:
					throw runtime_error(string("Don't know about type of ") + name);
				}
			}
			else {
				switch (type_[0]) {
				case GL_FLOAT:
					setters[name] = new FloatArraySetter(name, loc, size[0]);
					break;
				case GL_FLOAT_VEC2:
					setters[name] = new Vec2ArraySetter(name, loc, size[0]);
					break;
				case GL_FLOAT_VEC3:
					setters[name] = new Vec3ArraySetter(name, loc, size[0]);
					break;
				case GL_FLOAT_VEC4:
					setters[name] = new Vec4ArraySetter(name, loc, size[0]);
					break;
				case GL_FLOAT_MAT4:
					setters[name] = new Mat4ArraySetter(name, loc, size[0]);
					break;
				default:
					throw runtime_error(string("Don't know about type of ") + name);
				}
			}
		}
	}

	set<string> warned;
	set<string> uninitialized;

	template<typename T>
	void setUniform(string name, T value) {
		if (Program::active != this)
			throw runtime_error("Cannot set uniform on non-active program");

		uninitialized.erase(name);

		if (this->setters.find(name) != setters.end()) {
			this->setters[name]->set(value);
		}
		else {
			if (warned.find(name) == warned.end()) {
				cout << this->name << ": No such uniform " << name << "\n";
				if (this->setters.find(name + "[0]") != this->setters.end())
					throw runtime_error("It looks like you should use " + name + "[0]");
				warned.insert(name);
			}
		}
	}


	void checkUninitialized() {
		for (const string& s : uninitialized) {
			cout << "Uninitialized uniform: " << s << "\n";
		}
	}

	void use() {
		glUseProgram(this->prog);
		Program::active = this;
	}

	void dispatch(int xs, int ys, int zs) {
		if (active != this)
			throw runtime_error("Cannot dispatch() a non-active program");
		if (!is_compute_shader)
			throw runtime_error("Cannot dispatch() a non-compute shader");
		glDispatchCompute(xs, ys, zs);
		glMemoryBarrier(GL_ALL_BARRIER_BITS);
	}

	GLuint make_shader(string filename, GLenum shadertype) {
		ifstream in(filename.c_str());
		if (!in) {
			throw runtime_error("Cannot open file " + filename);
		}
		string shaderdata;
		getline(in, shaderdata, '\0');
		GLuint s = glCreateShader(shadertype);
		const char* x[] = { shaderdata.c_str() };
		glShaderSource(s, 1, x, NULL);
		glCompileShader(s);
		char infolog[4096];
		GLint tmp[1];
		glGetShaderInfoLog(s, sizeof(infolog), tmp, infolog);
		if (tmp[0] > 0) {
			cout << "When compiling " << filename << ":";
			cout << infolog;
		}
		glGetShaderiv(s, GL_COMPILE_STATUS, tmp);
		if (!tmp[0])
			throw runtime_error("Cannot compile " + filename);
		return s;
	}
};
