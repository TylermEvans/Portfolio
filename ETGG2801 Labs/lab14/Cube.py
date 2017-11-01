from glfuncs import *
from glconstants import *
from Program import *
from Texture import *


class Cube:
    def __init__(self):
        tmp = array.array("I",[0])
        glGenVertexArrays(1,tmp)
        self.vao = tmp[0]

        glBindVertexArray(self.vao)

        glGenBuffers(1,tmp)
        self.vbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.vbuff)
        vdata = array.array('f',
            [
                -0.5,0.5,0,
                -0.5,-0.5,0,
                0.5,-0.5,0,
                0.5,0.5,0,
                -0.5,0.5,-1,
                -0.5,-0.5,-1,
                0.5,-0.5,-1,
                0.5,0.5,-1

            ]
        )

        glBufferData(GL_ARRAY_BUFFER,len(vdata)*4,vdata,GL_STATIC_DRAW)
        glEnableVertexAttribArray(Program.POSITION_INDEX)
        glVertexAttribPointer(Program.POSITION_INDEX,3,GL_FLOAT,False,3*4,0)

        #texture data
        tdata = array.array("f",[
            0,1,0,
            0,0,0,
            1,0,0,
            1,1,0,
            0,1,-1,
            0,0,-1,
            1,0,-1,
            1,1,-1
        ])
        glGenBuffers(1,tmp)
        self.tbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.tbuff)
        glBufferData(GL_ARRAY_BUFFER,len(tdata)*4,tdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.TEXCOORD_INDEX)
        glVertexAttribPointer(Program.TEXCOORD_INDEX,2,GL_FLOAT,False,2*4,0)

        idata = array.array("H",[
            0,1,3,
            1,2,3,
            3,2,7,
            7,2,6,
            4,0,7,
            7,6,4,
            6,5,4,
            4,5,0,
            5,1,0,
            5,1,6,
            1,2,6
        ])
        glGenBuffers(1,tmp)
        self.ibuff = tmp[0]
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.ibuff)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,len(idata)*2,idata,GL_STATIC_DRAW)

        glBindVertexArray(0)

        self.tex = ImageTexture("brick.png")

    def draw(self,prog):
        prog.setUniform("tex",self.tex)
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_SHORT, 0 )
