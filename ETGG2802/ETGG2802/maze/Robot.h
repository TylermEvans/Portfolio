#pragma once

#include "math3d.h"
#include "Mesh.h"

class Robot{
    public:
    static Mesh* mesh;
    vec3 pos;
    Robot(vec3 pos){
        if( mesh == NULL )
            mesh = new Mesh("robot.obj.mesh");
        this->pos=pos;
    }
    void draw(Program* prog){
        prog->setUniform("worldMatrix", translation(this->pos));
        Robot::mesh->draw(prog);
    }
    void update(int elapsed){
    }
    
};

        
        
