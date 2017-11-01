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
        
    def isPowerOf2(self,x):
        return  ((x-1)&x) == 0
        
    def bind(self,unit):
        glActiveTexture(GL_TEXTURE0 + unit)
        glBindTexture(GL_TEXTURE_2D, self.tex)

class ImageTextureArray(Texture):
    def __init__(self,filenames):
        L=[]
        for filename in filenames:
            w,h,data,meta = png.read(filename)
            L.append( (w,h,data,meta) )

        alldata = bytes()
            
        for i in range(len(L)):
            if L[0][0] != L[i][0] or L[0][1] != L[i][1]:
                raise RuntimeError("Texture size mismatch")
            if L[0][3]["planes"] != L[i][3]["planes"]:
                raise RuntimeError("Texture depth mismatch")
            alldata += L[i][2]
                
        tmp = array.array("I",[0])
        glGenTextures(1,tmp)
        self.tex = tmp[0]

        glBindTexture(GL_TEXTURE_2D_ARRAY,self.tex)
        if meta["planes"] == 3:
            fmt=GL_RGB
        elif meta["planes"] == 4:
            fmt=GL_RGBA
        else:
            assert 0
            
        glTexImage3D(GL_TEXTURE_2D_ARRAY,0,
            GL_RGBA,w,h,len(L),0,GL_RGBA,GL_UNSIGNED_BYTE,alldata)
        
        if self.isPowerOf2(w) and self.isPowerOf2(h):
            glGenerateMipmap(GL_TEXTURE_2D_ARRAY)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_S,GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_T,GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
        else:
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D_ARRAY,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
            
        self.w=w
        self.h=h
       
    def setParameter(self,pname,pvalue):
        self.bind(0)
        glTexParameteri(GL_TEXTURE_2D_ARRAY,pname,pvalue)

    def isPowerOf2(self,x):
        return  ((x-1)&x) == 0
        
    def bind(self,unit):
        glActiveTexture(GL_TEXTURE0 + unit)
        glBindTexture(GL_TEXTURE_2D_ARRAY, self.tex)



class DataTexture(Texture2D):
    def __init__(self,w,h,channels,data=None):
        self.w=w
        self.h=h
        self.channels=channels

        tmp = array.array("I",[0])
        glGenTextures(1,tmp)
        self.tex = tmp[0]

        glBindTexture(GL_TEXTURE_2D,self.tex)
        
        if channels == 1:
            ifmt = GL_R32F
            fmt=GL_RED
        elif channels == 2:
            ifmt = GL_RG32F
            fmt=GL_RG
        elif channels == 3:
            ifmt = GL_RGB32F
            fmt = GL_RGB
        elif channels == 4:
            ifmt = GL_RGBA32F
            fmt = GL_RGBA
        else:
            assert 0
            
        glTexImage2D(GL_TEXTURE_2D,0,ifmt, w,h,0, fmt,GL_UNSIGNED_BYTE,None)
        self.fmt=fmt
        self.ifmt=ifmt
        
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)

        if data:
            self.update(data)
            
    def update(self,b):
        self.bind(0)
        
        if isinstance(b,bytes) or isinstance(b,bytearray):
            bsize = len(b)
        elif isinstance(b,array.array):
            bsize = len(b)*b.itemsize 
            b=b.tobytes()
        else:
            assert 0
            
        if bsize != self.w*self.h*self.channels*4:
            raise RuntimeError("Bad size: Expected "+
                str(self.w*self.h*self.channels*4)+"; got "+
                str(bsize))

        glTexSubImage2D(GL_TEXTURE_2D,0, 0,0,  self.w,self.h,
            self.fmt,GL_FLOAT,b)
        
    def bind(self,unit):
        glActiveTexture(GL_TEXTURE0 + unit)
        glBindTexture(GL_TEXTURE_2D, self.tex)
