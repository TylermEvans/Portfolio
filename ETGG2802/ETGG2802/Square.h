#pragma once

class Square
{

	public:
		int numindices;
		GLuint vao;

	Square() 
	{

		float vdata[] = {
			-1,1,0,
			-1,-1,0,
			1,-1,0,
			1,1,0
		};

		float tdata[] = {
			0,1,
			0,0,
			1,0,
			1,1

		};

		unsigned short idata[] = {
			0,1,2, 0,2,3
		};

		

		GLuint tmp[1];
		glGenVertexArrays(1, tmp);
		this->vao = tmp[0];

		glBindVertexArray(this->vao);

		glGenBuffers(1, tmp);
		GLuint vbuff = tmp[0];
		glBindBuffer(GL_ARRAY_BUFFER, vbuff);
		glBufferData(GL_ARRAY_BUFFER, sizeof(vdata), vdata, GL_STATIC_DRAW);
		glEnableVertexAttribArray(Program::POSITION_INDEX);
		glVertexAttribPointer(Program::POSITION_INDEX, 3, GL_FLOAT, false, 3 * 4, 0);




		glGenBuffers(1, tmp);
		GLuint tbuff = tmp[0];
		glBindBuffer(GL_ARRAY_BUFFER, tbuff);
		glBufferData(GL_ARRAY_BUFFER, sizeof(tdata), tdata, GL_STATIC_DRAW);
		glEnableVertexAttribArray(Program::TEXCOORD_INDEX);
		glVertexAttribPointer(Program::TEXCOORD_INDEX, 2, GL_FLOAT, false, 2 * 4, 0);

		glGenBuffers(1, tmp);
		GLuint ibuff = tmp[0];
		glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuff);
		glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(idata), idata, GL_STATIC_DRAW);

		glBindVertexArray(0);


	}

	void draw(Program* prog) 
	{
		
		glBindVertexArray(this->vao);
		glDrawElements(GL_TRIANGLES, 6 , GL_UNSIGNED_SHORT, 0);
		
	}

};
