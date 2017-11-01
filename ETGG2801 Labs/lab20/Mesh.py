import array
from glfuncs import *
from glconstants import *
from Program import Program
from Texture import *

class Mesh(object):
    def __init__(self,fname):
        vdata = 0
        tdata = 0
        ndata = 0
        idata = 0
        fp = open(fname,"rb")
        line = fp.readline().decode().strip()
        assert line=="mesh_01"
        while 1:
            line = fp.readline().decode().strip()
            if line=="end":
                break
            elif line.startswith("num_vertices"):
                lst = line.split()
                self.numv=int(lst[1])
            elif line.startswith("num_triangles"):
                lst = line.split()
                self.numt = int(lst[1])
            elif line.startswith("texture_file"):
                lst = line.split()
                self.tex = ImageTexture(lst[1])
            elif line.startswith("vertices"):
                numbytes = self.numv*3*4
                self.vdata = fp.read(numbytes)
            elif line.startswith("normals"):
                numbytes = self.numv*3*4
                self.ndata = fp.read(numbytes)
            elif line.startswith("texcoords"):
                numbytes = self.numv*2*4
                self.tdata = fp.read(numbytes)
            elif line.startswith("indices"):
                numbytes = self.numt*3*4
                self.idata = fp.read(numbytes)
            
        
        tmp = array.array("I",[0])
        glGenVertexArrays(1,tmp)
        self.vao = tmp[0]

        glBindVertexArray(self.vao)
        #vertex
        glGenBuffers(1,tmp)
        self.vbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.vbuff)
        glBufferData(GL_ARRAY_BUFFER,len(self.vdata),self.vdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.POSITION_INDEX)
        glVertexAttribPointer(Program.POSITION_INDEX,3,GL_FLOAT,False,3*4,0)


        #tex
        glGenBuffers(1,tmp)
        self.tbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.tbuff)
        glBufferData(GL_ARRAY_BUFFER,len(self.tdata),self.tdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.TEXCOORD_INDEX)
        glVertexAttribPointer(Program.TEXCOORD_INDEX,2,GL_FLOAT,False,2*4,0)
        # normal
        assert len(self.ndata) == len(self.vdata)

        glGenBuffers(1, tmp)
        self.nbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER, self.nbuff)
        glBufferData(GL_ARRAY_BUFFER, len(self.ndata) , self.ndata, GL_STATIC_DRAW)
        glEnableVertexAttribArray(Program.NORMAL_INDEX)
        glVertexAttribPointer(Program.NORMAL_INDEX, 3, GL_FLOAT, False, 3 * 4, 0)
        #indices
        glGenBuffers(1,tmp)
        self.ibuff = tmp[0]
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.ibuff)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,len(self.idata),self.idata,GL_STATIC_DRAW)

        glBindVertexArray(0)

    def draw(self,prog):
        prog.setUniform("tex",self.tex)
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES,self.numt*3, GL_UNSIGNED_INT, 0 )
