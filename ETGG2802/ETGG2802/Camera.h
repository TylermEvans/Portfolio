#pragma once

#include "math3d.h"
#include "Program.h"
#include "Mesh.h"


class Camera {
public:

	float fov_h;
	float hither;
	float yon;
	float aspect_ratio;
	float fov_v;
	vec4 eye;
	vec4 U, V, W;
	mat4 projmatrix;
	mat4 viewmatrix;
    mat4 worldMatrix;
	vec4 gunpos;
	float angle  = 135;
	float frame = 0;
	Mesh * gun;

	Camera() {
		fov_h = 45;
		hither = 0.1f;
		yon = 100.0f;
		aspect_ratio = 1.0f;
		fov_v = 1.0f / aspect_ratio*fov_h;
		eye = vec4(0, 0, 0, 1);
		U = vec4(1, 0, 0, 0);
		V = vec4(0, 1, 0, 0);
		W = vec4(0, 0, 1, 0);
		vec4 gunpos = eye;
		this->gun = new Mesh("gunball.blend.ms3d.mesh");
		this->compute_proj_matrix();
		this->compute_view_matrix();

	}

	void compute_proj_matrix() {
		this->projmatrix = mat4(
			1 / tan(radians(this->fov_h)), 0, 0, 0,
			0, 1 / tan(radians(this->fov_v)), 0, 0,
			0, 0, 1 + 2 * this->yon / (this->hither - this->yon), -1,
			0, 0, 2 * this->hither*this->yon / (this->hither - this->yon), 0);
	}
	void compute_view_matrix() {
		this->viewmatrix =
			translation(-1 * this->eye) *
			mat4(U.x, V.x, W.x, 0,
				U.y, V.y, W.y, 0,
				U.z, V.z, W.z, 0,
				0, 0, 0, 1);
	}

	void draw(Program* prog) {
		prog->setUniform("projMatrix", this->projmatrix);
		prog->setUniform("viewMatrix", this->viewmatrix);
		
		prog->setUniform("eyePos", this->eye.xyz());
		
		
	}

	void turn(float  a) {
		this -> angle += a;
		mat4 M = axisRotation(this->V, a);
		this->U = this->U*M;
		this->W = this->W*M;
		this->compute_view_matrix();
	}

	void tilt(float a) {
		this->angle += a;
		mat4 M = axisRotation(this->U, a);
		this->V = this->V*M;
		this->W = this->W*M;
		this->compute_view_matrix();
	}

	void walk(float a) {
		
		this->eye = this->eye + -a * this->W;
		this->compute_view_matrix();
	}

	void strafe(float x, float y, float z) {
		this->eye = this->eye + x*U + y*V + -z*W;
		this->compute_view_matrix();
	}

	void look_at(vec3 eye, vec3 coi, vec3 up) {
		this->eye = vec4(eye.x, eye.y, eye.z, 1.0);
		vec3 tmp = eye - coi;
		vec3 W = normalize(tmp);
		vec3 U = normalize(cross(up, W));
		vec3 V = normalize(cross(W, U));
		this->U = vec4(U, 0);
		this->V = vec4(V, 0);
		this->W = vec4(W, 0);
		this->compute_view_matrix();
	}
	void gundraw(Program* prog) 
	{

		prog->setUniform("frame", this->frame);
		prog->setUniform("worldMatrix", this->worldMatrix);
		this->gun->draw(prog);


	}
	void gunupdate(bool firing) 
	{
		this->gunpos = eye;
		if (firing){
			this->frame += 5;
			if (this->frame >= 76) 
			{
				this->frame = 0;
			}
		}
		mat4 slide = translation(0.1 * this->U) * translation(-0.15 * this->V) * translation(-0.2 * this -> W);
		this->worldMatrix = scaling(0.05, 0.05, 0.05)*axisRotation(this->V, this->angle) * translation(this->gunpos)*slide;
	}
};