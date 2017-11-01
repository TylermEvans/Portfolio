from glfuncs import *
from glconstants import *
import png
import array

class Texture:
    pass
    
class Texture2D(Texture):
    pass

class ImageTexture(Texture2D):
    def __init__(self,filename):
        w,h,data,meta = png.read(filename)

        tmp = array.array("I",[0])
        glGenTextures(1,tmp)
        self.tex = tmp[0]

        glBindTexture(GL_TEXTURE_2D,self.tex)
        if meta["planes"] == 3:
            fmt=GL_RGB
        elif meta["planes"] == 4:
            fmt=GL_RGBA
        else:
            assert 0
            
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,w,h,0,fmt,GL_UNSIGNED_BYTE,data)
        
        if self.isPowerOf2(w) and self.isPowerOf2(h):
            glGenerateMipmap(GL_TEXTURE_2D)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        else:
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
            
        self.w=w
        self.h=h

    def setParameter(self,p,v):
        glBindTexture(GL_TEXTURE_2D,self.tex)
        glTexParameteri(GL_TEXTURE_2D,p,v)
        
    def isPowerOf2(self,x):
        return  ((x-1)&x) == 0
        
    def bind(self,unit):
        glActiveTexture(GL_TEXTURE0 + unit)
        glBindTexture(GL_TEXTURE_2D, self.tex)
