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
             0.5,-0.5, 0,
             0.5, 0.5, 0,
            -0.5, 0.5, 0] )
        glGenBuffers(1,tmp)
        self.vbuff = tmp[0]
        glBindBuffer(GL_ARRAY_BUFFER,self.vbuff)
        glBufferData(GL_ARRAY_BUFFER,len(vdata)*4,vdata,GL_STATIC_DRAW)
        
        glEnableVertexAttribArray(Program.POSITION_INDEX)
        glVertexAttribPointer(Program.POSITION_INDEX,3,GL_FLOAT,False,3*4,0)
        
        glBindVertexArray(0)
        
    def draw(self,prog):
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES,0,6   )
        
