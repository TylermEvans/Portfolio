from glfuncs import *
from glconstants import *
from Program import Program
import array

class Square:

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

        cdata = array.array("f",[
            1,1,0,
            1,1,0,
            1,1,0,
            1,1,0
        ])

        glGenBuffers(1,tmp)
        self.cbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.cbuff)
        glBufferData(GL_ARRAY_BUFFER,len(cdata)*4,cdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.COLOR_INDEX)
        glVertexAttribPointer(Program.COLOR_INDEX,3,GL_FLOAT,False,3*4,0)

        idata = array.array("H",[
            0,1,2,   0,2,3
        ])
        glGenBuffers(1,tmp)
        self.ibuff = tmp[0]
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.ibuff)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,len(idata)*2,idata,GL_STATIC_DRAW)

        glBindVertexArray(0)

    def draw(self,prog):
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES,6, GL_UNSIGNED_SHORT, 0 )