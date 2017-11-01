#pragma once

#include "ppng.h"
#include "util.h"
#include "Texture2DArray.h"

//Array of 2D textures; data is drawn from files
class ImageTextureArray: public Texture2DArray {
    public:
    ImageTextureArray(const vector<string>& filenames){
        w=-1;
        h=-1;
        numslices=0;
        
        int numplanes;
        vector<uint8_t> alldata;
        
        for( string filename : filenames ){
            int w,h;
            vector<uint8_t> data;
            map<string,int> meta;
            png_read(filename,w,h,data,meta);
            if( this->w == -1 ){
                this->w=w;
                this->h=h;
                numplanes = meta["planes"];
            }
            else{
                if( this->w != w || this->h != h )
                    throw runtime_error("Size mismatch: "+filename );
                if( numplanes != meta["planes"] )
                    throw runtime_error("Format mismatch: "+filename);
            }
            ++numslices;
            alldata.insert( alldata.end(), data.begin(), data.end() );
        }

     
        glBindTexture(GL_TEXTURE_2D_ARRAY,this->tex);
        int fmt;
        if(numplanes == 3 )
            fmt=GL_RGB;
        else if(numplanes == 4 )
            fmt=GL_RGBA;
        else
            throw runtime_error("Bad planes");
            
        glTexImage3D(GL_TEXTURE_2D_ARRAY,0,
            GL_RGBA,w,h,numslices,0,fmt,GL_UNSIGNED_BYTE,&(alldata[0]));
        
        if(isPowerOf2(w) and isPowerOf2(h)){
            glGenerateMipmap(GL_TEXTURE_2D_ARRAY);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_S,GL_REPEAT);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_T,GL_REPEAT);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
        } else {
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
        }
    }
    
};

