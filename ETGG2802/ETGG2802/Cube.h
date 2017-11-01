#pragma once


class Cube{
    public:
    
    int numindices;
    GLuint vao;
	vec3 pos;
	int radius;
	

    
    Cube(){

		
        
        //since we have different texture coordinates in different
        //faces, we need to replicate the vertices...
        float vdata[] = {
            //front
            -1,-1,1,    1,-1,1,     1,1,1,      -1,1,1,
            //left
            -1,-1,-1,   -1,-1,1,    -1,1,1,     -1,1,-1,
            //right
            1,-1,1,     1,-1,-1,    1,1,-1,     1,1,1,
            //back
            1,-1,-1,    -1,-1,-1,   -1,1,-1,    1,1,-1,
            //top
            -1,1,1,     1,1,1,      1,1,-1,     -1,1,-1,
            //bottom
            -1,-1,-1,   1,-1,-1,    1,-1,1,     -1,-1,1
        };
        
        
        float tdata[] = {
            0,0,    1,0,   1,1,   0,1,
            0,0,    1,0,   1,1,   0,1,
            0,0,    1,0,   1,1,   0,1,
            0,0,    1,0,   1,1,   0,1,
            0,0,    1,0,   1,1,   0,1,
            0,0,    1,0,   1,1,   0,1
        };

        float ndata[] = {
            0,0,1,  0,0,1,  0,0,1,  0,0,1, 
            -1,0,0, -1,0,0, -1,0,0, -1,0,0,
            1,0,0,  1,0,0,  1,0,0,  1,0,0,
            0,0,-1, 0,0,-1, 0,0,-1, 0,0,-1,
            0,1,0,  0,1,0,  0,1,0,  0,1,0,
            0,-1,0, 0,-1,0, 0,-1,0, 0,-1,0
        };
            
        unsigned short idata[] = {
            0,1,2,      0,2,3,
            4,5,6,      4,6,7,
            8,9,10,     8,10,11,
            12,13,14,   12,14,15,
            16,17,18,   16,18,19,
            20,21,22,   20,22,23
        };
        
        this->numindices = sizeof(idata)/sizeof(idata[0]);
        
        GLuint tmp[1];
        glGenVertexArrays(1,tmp);
        this->vao = tmp[0];

        glBindVertexArray(this->vao);
        
        glGenBuffers(1,tmp);
        GLuint vbuff = tmp[0];
        glBindBuffer(GL_ARRAY_BUFFER,vbuff);
        glBufferData(GL_ARRAY_BUFFER,sizeof(vdata),vdata,GL_STATIC_DRAW);
        glEnableVertexAttribArray(Program::POSITION_INDEX);
        glVertexAttribPointer(Program::POSITION_INDEX,3,GL_FLOAT,false,3*4,0);
        
        glGenBuffers(1,tmp);
        GLuint tbuff = tmp[0];
        glBindBuffer(GL_ARRAY_BUFFER,tbuff);
        glBufferData(GL_ARRAY_BUFFER,sizeof(tdata),tdata,GL_STATIC_DRAW);
        glEnableVertexAttribArray(Program::TEXCOORD_INDEX);
        glVertexAttribPointer(Program::TEXCOORD_INDEX,2,GL_FLOAT,false,2*4,0);

        glGenBuffers(1,tmp);
        GLuint nbuff = tmp[0];
        glBindBuffer(GL_ARRAY_BUFFER,nbuff);
        glBufferData(GL_ARRAY_BUFFER,sizeof(ndata),ndata,GL_STATIC_DRAW);
        glEnableVertexAttribArray(Program::NORMAL_INDEX);
        glVertexAttribPointer(Program::NORMAL_INDEX,3,GL_FLOAT,false,3*4,0);
        
        glGenBuffers(1,tmp);
        GLuint ibuff = tmp[0];
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,ibuff);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,sizeof(idata),idata,GL_STATIC_DRAW);
 
        glBindVertexArray(0);
    }
    
    void draw(Program* prog){
        glBindVertexArray(this->vao);
        glDrawElements(GL_TRIANGLES, this->numindices, GL_UNSIGNED_SHORT, 0 );
    }
};
