from glfuncs import *
from glconstants import *
from Program import Program
from Texture import ImageTexture
import array
class Cube2:

    def __init__(self):
        tmp = array.array("I",[0])
        glGenVertexArrays(1,tmp)
        self.vao = tmp[0]

        glBindVertexArray(self.vao)

        vdata = array.array("f",[
            -1,1,1,
            -1,-1,1,
            1,-1,1,
            1,1,1,

            -1,1,1,
            -1,-1,1,
            -1,-1,-1,
            -1,1,-1,


            1,1,1,
            1,-1,1,
            1,-1,-1,
            1,1,-1,

            -1,1,-1,
            -1,-1,-1,
            1,-1,-1,
            1,1,-1,

            -1,1,1,
            1,1,1,
            1,1,-1,
            -1,1,-1,

            -1,-1,1,
            1,-1,1,
            1,-1,-1,
            -1,-1,-1








            ] )

        glGenBuffers(1,tmp)
        self.vbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.vbuff)
        glBufferData(GL_ARRAY_BUFFER,len(vdata)*4,vdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.POSITION_INDEX)
        glVertexAttribPointer(Program.POSITION_INDEX,3,GL_FLOAT,False,3*4,0)

        tdata = array.array("f",[
            0,1,
            0,0,
            1,0,
            1,1,

            0,1,
            0,0,
            1,0,
            1,1,

            0,1,
            0,0,
            1,0,
            1,1,

            0,1,
            0,0,
            1,0,
            1,1,

            0,1,
            0,0,
            1,0,
            1,1,

            0,1,
            0,0,
            1,0,
            1,1
        ])
        glGenBuffers(1,tmp)
        self.tbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.tbuff)
        glBufferData(GL_ARRAY_BUFFER,len(tdata)*4,tdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.TEXCOORD_INDEX)
        glVertexAttribPointer(Program.TEXCOORD_INDEX,2,GL_FLOAT,False,2*4,0)

        ndata = array.array("f", [
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,

            -1, 0, 0,
            -1, 0, 0,
            -1, 0, 0,
            -1, 0, 0,

            1, 0, 0,
            1, 0, 0,
            1, 0, 0,
            1, 0, 0,

            0, 0, -1,
            0, 0, -1,
            0, 0, -1,
            0, 0, -1,

            0, 1, 0,
            0, 1, 0,
            0, 1, 0,
            0, 1, 0,

            0, -1, 0,
            0, -1, 0,
            0, -1, 0,
            0, -1, 0
        ])
        assert len(ndata) == len(vdata)

        glGenBuffers(1, tmp)
        self.nbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER, self.nbuff)
        glBufferData(GL_ARRAY_BUFFER, len(ndata) * 4, ndata, GL_STATIC_DRAW)
        glEnableVertexAttribArray(Program.NORMAL_INDEX)
        glVertexAttribPointer(Program.NORMAL_INDEX, 3, GL_FLOAT, False, 3 * 4, 0)

        idata = array.array("H",[
            0,1,2,   0,2,3,
            7,6,5,   7,5,4,
            8,9,10,  8,10,11,
            12,13,14, 12,14,15,
            16,17,18, 16,18,19,
            20,21,22, 20,22,23



        ])
        glGenBuffers(1,tmp)
        self.ibuff = tmp[0]
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.ibuff)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,len(idata)*2,idata,GL_STATIC_DRAW)

        glBindVertexArray(0)

        self.tex = 0






    def draw(self,prog):

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES,36, GL_UNSIGNED_SHORT, 0 )


