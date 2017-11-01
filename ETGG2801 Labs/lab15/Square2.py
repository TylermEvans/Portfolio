from glfuncs import *
from glconstants import *
from Program import Program
from Texture import *

import array

class Square:
    vao=None 
    
    def __init__(self):
        
        if not Square.vao:
            tmp = array.array("I",[0])
            glGenVertexArrays(1,tmp)
            Square.vao = tmp[0]
            
            glBindVertexArray(Square.vao)
            
            vdata = array.array("f",[
                -1, 1, 0,
                -1,-1, 0,
                 1,-1, 0, 
                 1, 1, 0
                ] )
            
            glGenBuffers(1,tmp)
            Square.vbuff = tmp[0]
            glBindBuffer(GL_ARRAY_BUFFER,Square.vbuff)
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
            Square.tbuff = tmp[0]
            glBindBuffer(GL_ARRAY_BUFFER,Square.tbuff)
            glBufferData(GL_ARRAY_BUFFER,len(tdata)*4,tdata,GL_STATIC_DRAW)
            
            glEnableVertexAttribArray(Program.TEXCOORD_INDEX)
            glVertexAttribPointer(Program.TEXCOORD_INDEX,2,GL_FLOAT,False,2*4,0)


            idata = array.array("H",[
                0,1,2,   0,2,3
            ])
            glGenBuffers(1,tmp)
            Square.ibuff = tmp[0]
            glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,Square.ibuff)
            glBufferData(GL_ELEMENT_ARRAY_BUFFER,len(idata)*2,idata,GL_STATIC_DRAW)
            
            glBindVertexArray(0)
            
        
    def draw(self,prog):
        glBindVertexArray(Square.vao)
        glDrawElements(GL_TRIANGLES,6, GL_UNSIGNED_SHORT, 0 )
        
