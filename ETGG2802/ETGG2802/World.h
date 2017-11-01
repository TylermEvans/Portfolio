#pragma once

#include "Cube.h"
#include "math3d.h"
#include "Texture.h"
#include "Robot.h"
#include "SolidTexture.h"
#include "Mesh.h"
#include "ObjMesh.h"

class World{
    public:
    
    int numrows, numcols;
    vector<string> lines;
	vector<Robot*> robots;
    ObjMesh* cube;
	//Mesh* cube2;
	ObjMesh* floor;
	vector<mat4> cubemat;
	vector<vec3> cubepos;
	vector<vec3> robotpos;
	SolidTexture* stex;
	SolidTexture* etex;

    World(){
        ifstream fp("map3.txt");
        if(!fp)
            throw runtime_error("Cannot load map.txt");
            
        while(true){
            string s;
            getline(fp,s);
            if( fp.fail() )
                break;
            lines.push_back(s);
        }
		
        numrows = int(lines.size());
        numcols = int(lines[0].size());
		for (unsigned i = 0; i<lines.size(); ++i) {
			for (unsigned j = 0; j<lines[i].size(); ++j) {
				if (lines[i][j] == 'R') {
					lines[i][j] = ' ';
					robots.push_back(new Robot(vec3(float(j * 2)-10, 0, float(i * 2)-10)));
				}
			}
		}
        
		cube = new ObjMesh("cube.obj.mesh");
		//cube2 = new Mesh("cube2.obj.mesh");
		floor = new ObjMesh("floor2.obj.mesh");

		stex = new SolidTexture(0.5, 0.5, 0.5, 1);
		etex = new SolidTexture(0, 0, 0, 1);

        

		for (int r = 0; r<(int)this->lines.size(); ++r) {
			string& L = this->lines[r];
			for (int c = 0; c<(int)L.size(); ++c) {
				if (L[c] == '*') {
					cubemat.push_back(translation(vec3(float(c * 2)-10, 1.0f, float(r * 2)-10)));
						
				}
			}
		}
		for (int i = 0; i < cubemat.size(); i++) 
		{
			mat4 tmp = cubemat.at(i);
			vec3 vect = vec3(tmp[3][0], tmp[3][1], tmp[3][2]);
			cubepos.push_back(vect);
		}
		
		
    }
    
    void update(int elapsed,vec4 ppos, vector<vec3> cubepos){
        for( auto R : robots )
            R->update(elapsed , ppos,cubepos);
    }
    
    void draw(Program* prog){
        //FIXME: We could make this more efficient by building one big mesh...
        
       // prog->setUniform("tex",ceiltex);
       // for(int r=0;r<numrows;++r){
          //  for(int c=0;c<numcols;++c){
             //   prog->setUniform("worldMatrix",
                 //   translation(vec3(float(c*2),3,float(r*2))));
               // cube->draw(prog);
           // }
       // }
        
        
       prog->setUniform("worldMatrix",translation(vec3(-9,-1,40)));
	   floor->draw(prog);

	  
        for(int r=0;r<(int)this->lines.size();++r)
		{
            string& L = this->lines[r];
            for(int c=0;c<(int)L.size();++c)
			{
                if(L[c] == '*')
				{
                   
                    prog->setUniform("worldMatrix", 
                        translation(vec3(float(c*2)-10,1.0f,float(r*2)-10) ) );
                    cube->draw(prog);
                }
           }
        }
        
        
	
    }
	void robotdraw(Program* prog) 
	{

		for (auto R : robots) {
			R->draw(prog);
		}

	}
	
};

