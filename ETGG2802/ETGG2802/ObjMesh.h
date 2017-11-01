#pragma once 
#include "Program.h"
#include "SolidTexture.h"
#include "ImageTexture.h"
#include "DataTexture.h"

class ObjMesh {
public:

	string filename;
	class Material {
	public:
		string name;
		Texture* texture = NULL;
		Texture* emitmap = NULL;
		Texture* specularmap = NULL;
		Texture* reflmap = NULL;
		Texture* bumpmap = NULL;
	};
	vector<Material> materials;
	vector<pair<int, int> > groups;
	int numvertices;
	int numindices;
	int numframes;
	int numbones;
	GLuint vao;

	ObjMesh(string filename) {

		this->filename = filename;

		ifstream fp(filename, ios::binary);
		if (!fp)
			throw runtime_error("Cannot open file " + filename);

		string line;

		getline(fp, line);

		if (line != "mesh_01sb")
		{
			throw runtime_error("Incorrect mesh format: " + line + "; expected mesh_01sbr");
		}
		

		GLuint tmp[1];
		glGenVertexArrays(1, tmp);
		this->vao = tmp[0];
		glBindVertexArray(this->vao);


		while (true) {
			getline(fp, line);
			if (fp.fail()) {
				assert(0);
			}
			istringstream iss(line);
			cout << line << endl;
			string word;
			iss >> word;

			if (iss.fail()) {
			}
			else if (word == "num_vertices")
				iss >> this->numvertices;
			else if (word == "num_indices")
				iss >> this->numindices;
			else if (word == "positions") {
				vector<char> pdata;
				pdata.resize(this->numvertices * 4 * 3);
				fp.read(&pdata[0], pdata.size());
				glGenBuffers(1, tmp);
				GLuint vbuff = tmp[0];
				glBindBuffer(GL_ARRAY_BUFFER, vbuff);
				glBufferData(GL_ARRAY_BUFFER, pdata.size(), &pdata[0], GL_STATIC_DRAW);
				glEnableVertexAttribArray(Program::POSITION_INDEX);
				glVertexAttribPointer(Program::POSITION_INDEX, 3, GL_FLOAT, false, 3 * 4, 0);
			}
			else if (word == "texcoords") {
				vector<char> tdata;
				tdata.resize(this->numvertices * 4 * 2);
				fp.read(&tdata[0], tdata.size());
				glGenBuffers(1, tmp);
				GLuint tbuff = tmp[0];
				glBindBuffer(GL_ARRAY_BUFFER, tbuff);
				glBufferData(GL_ARRAY_BUFFER, tdata.size(), &tdata[0], GL_STATIC_DRAW);
				glEnableVertexAttribArray(Program::TEXCOORD_INDEX);
				glVertexAttribPointer(Program::TEXCOORD_INDEX, 2, GL_FLOAT, false, 2 * 4, 0);
			}
			else if (word == "normals") {
				vector<vec3> ndata;
				ndata.resize(this->numvertices);
				fp.read((char*)&ndata[0], ndata.size() * sizeof(ndata[0]));
				glGenBuffers(1, tmp);
				GLuint nbuff = tmp[0];
				glBindBuffer(GL_ARRAY_BUFFER, nbuff);
				glBufferData(GL_ARRAY_BUFFER, ndata.size() * sizeof(ndata[0]), &ndata[0], GL_STATIC_DRAW);
				glEnableVertexAttribArray(Program::NORMAL_INDEX);
				glVertexAttribPointer(Program::NORMAL_INDEX, 3, GL_FLOAT, false, 3 * 4, 0);
			}
			else if (word == "tangents") {
				vector<char> tandata;
				tandata.resize(this->numvertices * 4 * 3);
				fp.read(&tandata[0], tandata.size());
				glGenBuffers(1, tmp);
				GLuint tanbuff = tmp[0];
				glBindBuffer(GL_ARRAY_BUFFER, tanbuff);
				glBufferData(GL_ARRAY_BUFFER, tandata.size(), &tandata[0], GL_STATIC_DRAW);
				glEnableVertexAttribArray(Program::TANGENT_INDEX);
				glVertexAttribPointer(Program::TANGENT_INDEX, 3, GL_FLOAT, false, 3 * 4, 0);
			}
			else if (word == "bitangents") {
				vector<char> bitandata;
				bitandata.resize(this->numvertices * 4 * 3);
				fp.read(&bitandata[0], bitandata.size());
				glGenBuffers(1, tmp);
				GLuint bitanbuff = tmp[0];
				glBindBuffer(GL_ARRAY_BUFFER, bitanbuff);
				glBufferData(GL_ARRAY_BUFFER, bitandata.size(), &bitandata[0], GL_STATIC_DRAW);
				glEnableVertexAttribArray(Program::BITANGENT_INDEX);
				glVertexAttribPointer(Program::BITANGENT_INDEX, 3, GL_FLOAT, false, 3 * 4, 0);
			}
			else if (word == "indices") {
				vector<char> idata;
				idata.resize(this->numindices * 4);
				fp.read(&idata[0], idata.size());
				glGenBuffers(1, tmp);
				GLuint ibuff = tmp[0];
				glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuff);
				glBufferData(GL_ELEMENT_ARRAY_BUFFER, idata.size(), &idata[0], GL_STATIC_DRAW);

			}
			else if (word == "material") {
				int start, num;
				string mtlname;
				float Kdr, Kdg, Kdb;
				iss >> start >> num >> mtlname >> Kdr >> Kdg >> Kdb;
				Material m;
				m.name = mtlname;
				while (1) {
					string key, value;
					iss >> key >> value;

					if (iss.fail())
						break;

					if (key == "map_Kd")
						m.texture = new ImageTexture(value);
					else if (key == "map_Ks")
						m.specularmap = new ImageTexture(value);
					else if (key == "map_Ke")
						m.emitmap = new ImageTexture(value);
					else if (key == "refl")
						m.reflmap = new ImageTexture(value);
					else if (key == "map_Bump")
						m.bumpmap = new ImageTexture(value);
				}

				if (!m.texture)
					m.texture = new SolidTexture(Kdr, Kdg, Kdb, 1.0);
				if (!m.specularmap)
					m.specularmap = new SolidTexture(1, 1, 1, 1);
				if (!m.emitmap)
					m.emitmap = new SolidTexture(0, 0, 0, 1);
				if (!m.reflmap)
					m.reflmap = new SolidTexture(0, 0, 0, 1);
				if (!m.bumpmap)
					m.bumpmap = new SolidTexture(0.5, 0.5, 1.0, 1.0);

				materials.push_back(m);
				groups.push_back(make_pair(start, num));
			}
			else if (word == "end")
				break;
			else {
				cerr << "Unknown word: " << word << "\n";
				assert(0);
			}
		}

		glBindVertexArray(0);

	}

	void draw(Program* prog) {
		glBindVertexArray(this->vao);
		for (unsigned i = 0; i<groups.size(); ++i) {
			prog->setUniform("tex", materials[i].texture);
			prog->setUniform("etex", materials[i].emitmap);
			prog->setUniform("stex", materials[i].specularmap);
			prog->setUniform("rtex", materials[i].reflmap);
			prog->setUniform("bumpmap", materials[i].bumpmap);
			glDrawElements(GL_TRIANGLES, groups[i].second, GL_UNSIGNED_INT,
				reinterpret_cast<GLvoid*>(groups[i].first * 4));
		}
		prog->checkUninitialized();
	}
};