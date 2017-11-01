#pragma once
#include "Square.h"
#include "ImageTexture.h"
#include "math3d.h"
#include "Program.h"



class Bullet 
{
public:
	ImageTexture* tex;
	Square* square;
	vec3 pos;
	vec3 U;
	vec3 V;
	vec3 W;
	int radius;
	mat4 worldMat;
	vec2 bbsize;
	int life;
	
	Bullet(vec4 eye, vec4 U, vec4 V, int rad) 
	{
		
		
		square = new Square();
		this -> tex = new ImageTexture("ball.png");
		this->pos = vec3(eye.x,eye.y,eye.z);
		this->U = vec3(U.x,U.y,U.z);
		this->V = vec3(V.x, V.y, V.z);
		this->W = cross(this->U, this->V);
		this->radius = rad;
		this->worldMat = mat4(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
		this->bbsize = vec2(0.1, 0.1);
		this->life = 100;
		
		
		

	}
	void update(float elapsed) 
	{

		this->pos = this->pos + this->W* -1 * elapsed*0.01;
		this->worldMat = translation(this->pos)*translation(-0.25*this->V)*translation(0.2*this->U)*translation(-0.2*this->W);
		if (this->life > 0) 
		{
			this->life -= 1;
		}

		

	}
	void draw(Program* prog) 
	{
		
		prog -> setUniform("worldMatrix", this->worldMat);
		prog -> setUniform("tex",  this -> tex);
		prog -> setUniform("bbsize", this -> bbsize);
		square->draw(prog);



	}


};