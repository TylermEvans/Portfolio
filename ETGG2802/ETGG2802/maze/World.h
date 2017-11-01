#pragma once

#include "Cube.h"
#include "math3d.h"
#include "Texture.h"
#include "Robot.h"

class World{
    public:
    
    int numrows, numcols;
    vector<string> lines;
    vector<Robot*> robots;
    Cube* cube;
    ImageTexture* bricks;
    ImageTexture* floortex;
    ImageTexture* ceiltex;
    
    World(){
        ifstream fp("map.txt");
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
        
        cube = new Cube();
        bricks = new ImageTexture("bricks2.png");
        floortex = new ImageTexture("floor.png");
        ceiltex = new ImageTexture("ceiling.png");

        for(unsigned i=0;i<lines.size();++i){
            for(unsigned j=0;j<lines[i].size();++j){
                if( lines[i][j] == 'R' ){
                    lines[i][j] = ' ';
                    robots.push_back( new Robot( vec3(float(j*2),0,float(i*2)) ) );
                }
            }
        }
    }
    
    void update(int elapsed){
        for( auto R : robots )
            R->update(elapsed);
    }
    
    void draw(Program* prog){
        
        //FIXME: We could make this more efficient by building one big mesh...
        
        prog->setUniform("tex",ceiltex);
        for(int r=0;r<numrows;++r){
            for(int c=0;c<numcols;++c){
                prog->setUniform("worldMatrix",
                    translation(vec3(float(c*2),3,float(r*2))));
                cube->draw(prog);
            }
        }
        prog->setUniform("tex",floortex);
        prog->setUniform("worldMatrix",mat4::identity());
        for(int r=0;r<numrows;++r){
            for(int c=0;c<numcols;++c){
                prog->setUniform("worldMatrix",
                    translation(vec3(float(c*2),-1,float(r*2) )));
                cube->draw(prog);
            }
        }
        prog->setUniform("tex",bricks);
        for(int r=0;r<(int)this->lines.size();++r){
            string& L = this->lines[r];
            for(int c=0;c<(int)L.size();++c){
                if(L[c] == '*'){
                    prog->setUniform("tex",this->bricks);
                    prog->setUniform("worldMatrix", 
                        translation(vec3(float(c*2),1.0f,float(r*2)) ) );
                    cube->draw(prog);
                }
            }
        }
        
        for(auto R : robots ){
            R->draw(prog);
        }
    }
};

