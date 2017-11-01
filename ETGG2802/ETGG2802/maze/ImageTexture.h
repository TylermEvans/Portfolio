#pragma once

#include "ppng.h"
#include "util.h"
#include "Texture2D.h"

//Texture with data from an image file.
class ImageTexture: public Texture2D {
    public:

    string filename;
    int depth;      //8 or 16 bits
    int planes;     //1 (grayscale), 3 (rgb), 4 (rgba)
    
    ImageTexture(string filename){
        
        vector<uint8_t> data;
        map<string,int> meta;
        
        this->filename = filename;
        
        png_read(filename,w,h,data,meta);
        
        glBindTexture(GL_TEXTURE_2D,this->tex);
        GLenum efmt;    //external format
        GLenum ifmt;    //internal format
        depth = meta["depth"];
        planes = meta["planes"];
        
        //PNG is big-endian...This only matters
        //for 16 bit images
        glPixelStorei(GL_UNPACK_SWAP_BYTES,GL_TRUE);

        //size of external data being passed in
        GLenum esize = ( (depth == 16) ? GL_UNSIGNED_SHORT : GL_UNSIGNED_BYTE );
        
        switch(planes){
            case 1:
                efmt = GL_RED;
                ifmt = ((depth==16) ? GL_R16 : GL_RED);
                break;
            case 3:
                efmt=GL_RGB;
                //no RGB16 format, so we use RGBA16 and waste RAM
                ifmt = ((depth==16) ? GL_RGBA16 : GL_RGB);
                break;
            case 4:
                efmt=GL_RGBA;
                ifmt = ((depth==16) ? GL_RGBA16 : GL_RGBA);
                break;
            default:
                throw runtime_error(filename+": Bad planes");
        }
           
        glTexImage2D(GL_TEXTURE_2D,0,ifmt,w,h,0,efmt,esize,&data[0]);
        
        if(depth == 8 && this->isPowerOf2(w) && this->isPowerOf2(h) ){
            glGenerateMipmap(GL_TEXTURE_2D);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
        } else{
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
        }            
    }
    
};
