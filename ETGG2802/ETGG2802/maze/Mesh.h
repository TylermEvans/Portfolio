#include "Program.h"
#include "Texture.h"

class Mesh{
    public:
    
    string filename;
    Texture2D* texture;
    int numvertices;
    int numindices;
    GLuint vao;
    
    Mesh(string filename){
        
        this->filename = filename;
        this->texture=NULL;
        
        ifstream fp(filename,ios::binary);
        if(!fp)
            throw runtime_error("Cannot open file "+filename);
            
        string line;
        
        getline(fp,line);
        
        if(line != "mesh_01" )
            throw runtime_error("Incorrect mesh format: "+line);
            
        GLuint tmp[1];
        glGenVertexArrays(1,tmp);
        this->vao = tmp[0];
        glBindVertexArray(this->vao);

        
        while(true){
            getline(fp,line);
            if( fp.fail() ){
                assert(0);
            }
            istringstream iss(line);
            string word;
            iss >> word;
            cout << line << "\n";
            
            if( iss.fail() ){
            }
            else if( word == "num_vertices" )
                iss >> this->numvertices;
            else if( word == "num_indices")
                iss >> this->numindices;
            else if( word == "texture_file"){
                string texf;
                getline(iss,texf);
                while( texf[0] == ' ')
                    texf = texf.substr(1);
                this->texture = new ImageTexture(texf);
            }
            else if( word == "positions"){
                vector<vec3> pdata;
                pdata.resize(this->numvertices);
                fp.read((char*)&pdata[0],pdata.size()*sizeof(pdata[0]));
                glGenBuffers(1,tmp);
                GLuint vbuff = tmp[0];
                glBindBuffer(GL_ARRAY_BUFFER,vbuff);
                glBufferData(GL_ARRAY_BUFFER,pdata.size()*sizeof(pdata[0]),&pdata[0],GL_STATIC_DRAW);
                glEnableVertexAttribArray(Program::POSITION_INDEX);
                glVertexAttribPointer(Program::POSITION_INDEX,3,GL_FLOAT,false,3*4,0);
            }
            else if( word == "texcoords"){
                vector<vec2> tdata;
                tdata.resize(this->numvertices);
                fp.read((char*)&tdata[0],tdata.size()*sizeof(tdata[0]));
                glGenBuffers(1,tmp);
                GLuint tbuff = tmp[0];
                glBindBuffer(GL_ARRAY_BUFFER,tbuff);
                glBufferData(GL_ARRAY_BUFFER,tdata.size()*sizeof(tdata[0]),&tdata[0],GL_STATIC_DRAW);
                glEnableVertexAttribArray(Program::TEXCOORD_INDEX);
                glVertexAttribPointer(Program::TEXCOORD_INDEX,2,GL_FLOAT,false,2*4,0);
            }
            else if( word == "normals"){
                vector<vec3> ndata;
                ndata.resize(this->numvertices);
                fp.read((char*)&ndata[0],ndata.size()*sizeof(ndata[0]));
                glGenBuffers(1,tmp);
                GLuint nbuff = tmp[0];
                glBindBuffer(GL_ARRAY_BUFFER,nbuff);
                glBufferData(GL_ARRAY_BUFFER,ndata.size()*sizeof(ndata[0]),&ndata[0],GL_STATIC_DRAW);
                glEnableVertexAttribArray(Program::NORMAL_INDEX);
                glVertexAttribPointer(Program::NORMAL_INDEX,3,GL_FLOAT,false,3*4,0);
            }
            else if( word == "bytes_per_index"){
                int bytes_per_index;
                iss >> bytes_per_index;
                if( bytes_per_index != 4 )
                    throw runtime_error("Expected 4 bytes per index");
            }
            else if( word == "indices"){
                vector<uint32_t> idata;
                idata.resize(this->numindices);
                fp.read((char*)&idata[0],idata.size()*sizeof(idata[0]));
                glGenBuffers(1,tmp);
                GLuint ibuff = tmp[0];
                glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,ibuff);
                glBufferData(GL_ELEMENT_ARRAY_BUFFER,idata.size()*sizeof(idata[0]),&idata[0],GL_STATIC_DRAW);

            }
            else if( word == "end")
                break;
            else{
                cerr << word << "\n";
                assert(0);
            }
        }
 
        glBindVertexArray(0);
    }

    void draw(Program* prog){
        if(this->texture)
            prog->setUniform("tex",this->texture);
        glBindVertexArray(this->vao);
        glDrawElements(GL_TRIANGLES, this->numindices, GL_UNSIGNED_INT,0);
        prog->checkUninitialized();
    }
};
        
