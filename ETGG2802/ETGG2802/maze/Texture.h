#pragma once

//Texture base class. This is never directly instantiated.
class Texture{
    public:
    
    //forbid copy construction or assignment.
    Texture(const Texture&) = delete;
    
    //texture identifier
    GLuint tex;
    
    //type of texture: GL_TEXTURE_2D, GL_TEXTURE_3D, etc.
    GLenum type;
    
    virtual ~Texture(){}

    static bool isPowerOf2(int x){
        return  ((x-1)&x) == 0;
    }
    
    
    void bind(int unit){
        glActiveTexture(GL_TEXTURE0 + unit);
        glBindTexture(type, this->tex);
    }
    
    void unbind(int unit){
        glActiveTexture(GL_TEXTURE0 + unit);
        glBindTexture(type, 0);
    }

    void setParameter(GLenum pname, int pvalue){
        this->bind(0);
        glTexParameteri(type,pname,pvalue);
    }
    
    protected:
    Texture(GLenum ty) : type(ty) {
        GLuint tmp[1];
        glGenTextures(1,tmp);
        this->tex = tmp[0];

    }
};
  
