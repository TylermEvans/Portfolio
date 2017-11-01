from glfuncs import *
from glconstants import *
from Program import Program
from Texture import ImageTexture
import array
class jelTex:

    def __init__(self):
        tmp = array.array("I",[0])
        glGenVertexArrays(1,tmp)
        self.vao = tmp[0]

        glBindVertexArray(self.vao)

        vdata = array.array("f",[
            -0.5, 0.5, 0,
            -0.5,-0.5, 0,
             0.5,-0.5, 0,
             0.5, 0.5, 0
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
            1,1
        ])
        glGenBuffers(1,tmp)
        self.tbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.tbuff)
        glBufferData(GL_ARRAY_BUFFER,len(tdata)*4,tdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.TEXCOORD_INDEX)
        glVertexAttribPointer(Program.TEXCOORD_INDEX,2,GL_FLOAT,False,2*4,0)

        idata = array.array("H",[
            0,1,2,   0,2,3
        ])
        glGenBuffers(1,tmp)
        self.ibuff = tmp[0]
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.ibuff)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,len(idata)*2,idata,GL_STATIC_DRAW)

        glBindVertexArray(0)

        self.tex = ImageTexture("jelly.png")

    def draw(self,prog):
        prog.setUniform("tex",self.tex)
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES,6, GL_UNSIGNED_SHORT, 0 )
