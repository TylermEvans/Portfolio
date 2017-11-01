#pragma once

#include "math3d.h"
#include "Mesh.h"
#include <math.h>



class Robot{
    public:
    static Mesh* mesh;
    vec3 pos;
	mat4 worldMat;
	vec3 up = vec3(0,1,0);
	int rad = 1;
	double speed = 0.0003;
	float frame = 1;
    Robot(vec3 pos){
		if (mesh == NULL) {
			mesh = new Mesh("robot.ms3d.mesh");
		}
       
        this->pos=pos;
		this -> worldMat = translation(this->pos);
		
		
		
    }
    void draw(Program* prog){
        prog->setUniform("worldMatrix", this->worldMat);
		prog->setUniform("frame", this->frame);
        Robot::mesh->draw(prog);
    }
	float lookAt(vec4 ppos) 
	{
		vec3 tmp = ppos.xyz() - this->pos;
		tmp = normalize(tmp);
		float angle = atan2f(tmp.z, tmp.x);
		return -angle + (M_PI);

	}
	void update(int elapsed, vec4 ppos, vector<vec3> cubepos )
	{
		
		float theta = lookAt(ppos);
		vec3 tmp = ppos.xyz() - this->pos;
		float dist = dot(tmp, tmp);
		if (dist < pow(5, 2))
		{
			
			
			


			float oldpos_x = this->pos.x;
			float oldpos_z = this->pos.z;

			if (ppos.x > this->pos.x && ppos.z > this->pos.z) 
			{
				
				this->pos = this->pos + vec3(1, 0, 1)*speed*elapsed;
				this->frame += .7;
				if (this->frame >= 15){
					this->frame = 3;
				}
				if (collision(this->pos.x, this->pos.z, cubepos) == true)
				{
					this->pos.x = oldpos_x;
					this->pos.z = oldpos_z;
				}


			}
			if (ppos.x < this->pos.x && ppos.z < this->pos.z) 
			{
				this->pos = this->pos + vec3(-1, 0, -1)*speed*elapsed;
				this->frame += .7;
				if (this->frame >= 15) {
					this->frame = 3;
				}
				if (collision(this->pos.x, this->pos.z, cubepos) == true)
				{
					this->pos.x = oldpos_x;
					this->pos.z = oldpos_z;
				}

			}
			if (ppos.x < this->pos.x && ppos.z > this->pos.z) 
			{
				this->pos = this->pos + vec3(-1, 0, 1)*speed*elapsed;
				this->frame += .7;
				if (this->frame >= 15) {
					this->frame = 3;
				}
				if (collision(this->pos.x, this->pos.z, cubepos) == true)
				{
					this->pos.x = oldpos_x;
					this->pos.z = oldpos_z;
				}



			}
			if (ppos.x > this->pos.x && ppos.z < this->pos.z) 
			{
				this->pos = this->pos + vec3(1, 0, -1)*speed*elapsed;
				this->frame += .7;
				if (this->frame >= 15) {
					this->frame = 3;
				}
				if (collision(this->pos.x, this->pos.z, cubepos) == true)
				{
					this->pos.x = oldpos_x;
					this->pos.z = oldpos_z;
				}

			}
			
			
			this->worldMat =  axisRotation(this->up, theta) * translation(this->pos);
		}
		else
		{
			this->frame = 0;

		}

		
	}
};

        
        
