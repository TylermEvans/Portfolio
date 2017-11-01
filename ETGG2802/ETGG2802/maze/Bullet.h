#pragma once
#include "Square.h"
#include "ImageTexture.h"
#include "math3d.h"
#include "BBProgram.h"

#define NULL 0;

class Bullet 
{
public:
	ImageTexture* tex;
	Square square;
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
		this->pos = vec3(eye.x,eye.y,eye.z);
		this->U = vec3(U.x,U.y,U.z);
		this->V = vec3(V.x, V.y, V.z);
		this->W = cross(this->U, this->V);
		this->radius = rad;
		this->worldMat = mat4(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
		this->bbsize = vec2(0.5, 0.5);
		this->life = 100;
		this->square = Square();
		this->tex = new ImageTexture("bullet.png");

	}
	void update(float elapsed) 
	{

		this->pos = this->pos + this->W*-1 * elapsed*0.003;
		this->worldMat = translation(this->pos);
		if (this->life > 0) 
		{
			this->life -= 1;
		}

	}
	void draw(BBProgram* prog) 
	{
		prog -> setUniform("worldMatrix", this->worldMat);
		prog -> setUniform("tex", this->tex);
		prog -> setUniform("bbsize", this->bbsize);
		this->square.draw(prog);



	}


};