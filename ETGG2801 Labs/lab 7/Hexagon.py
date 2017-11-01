from glfuncs import *
from glconstants import *
from Program import Program
import array

class Hexagon:

    def __init__(self):
        tmp = array.array("I",[0])
        glGenVertexArrays(1,tmp)
        self.vao = tmp[0]

        glBindVertexArray(self.vao)

        vdata = array.array("f",[ 0.0,0.0,0.0,
                                 0.25,0.5,0.0,
                                -0.25,0.5,0.0,
                                 0.0,0.0,0.0,
                                 0.5,0.0,0.0,
                                 0.25,0.5,0.0,
                                 0.0,0.0,0.0,
                                 0.25,-0.5,0.0,
                                 0.5,0.0,0.0,
                                 0.0,0.0,0.0,
                                 -0.25,-0.5,0.0,
                                 0.25,-0.5,0.0,
                                 0.0,0.0,0.0,
                                 -0.5,0.0,0.0,
                                 -0.25,-0.5,0.0,
                                 0.0,0.0,0.0,
                                 -0.25,0.5,0.0,
                                 -0.5,0.0,0.0 ] )
        
        glGenBuffers(1,tmp)
        self.vbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.vbuff)
        glBufferData(GL_ARRAY_BUFFER,len(vdata)*4,vdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.POSITION_INDEX)
        glVertexAttribPointer(Program.POSITION_INDEX,3,GL_FLOAT,False,3*4,0)

        cdata = array.array("f",[
            1,1,1,#1
            0,0,0,#2
            0,0,0,#3
            1,1,1,#4
            0,0,0,#5
            0,0,0,#6
            1,1,1,#7
            0,0,0,#8
            0,0,0,#9
            1,1,1,#10
            0,0,0,#11
            0,0,0,#12
            1,1,1,#13
            0,0,0,#14
            0,0,0,#15
            1,1,1,#16
            0,0,0,#17
            0,0,0#18
        ])
        glGenBuffers(1,tmp)
        self.cbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.cbuff)
        glBufferData(GL_ARRAY_BUFFER,len(cdata)*4,cdata,GL_STATIC_DRAW)

        glEnableVertexAttribArray(Program.COLOR_INDEX)
        glVertexAttribPointer(Program.COLOR_INDEX,3,GL_FLOAT,False,3*4,0)

        glBindVertexArray(0)

    def draw(self,prog):
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES,0,18)

