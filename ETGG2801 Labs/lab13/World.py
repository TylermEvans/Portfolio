import Program
import Cube2
import math3d
from Texture import ImageTexture


class World(object):
    def __init__(self,filename):
        self.map = filename
        self.worldMat = 0
        self.data = []
        fp = open(filename,"r")
        for i in fp:
            self.data.append(i)
        self.c_list = []
        self.tex = ImageTexture("brick.png")
        self.tex2 = ImageTexture("roof.png")
        self.tex3 = ImageTexture("brickfloor.png")
        self.c = Cube2.Cube2()





    def draw(self,prog):

        prog.setUniform("tex",self.tex)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == "*":
                    self.worldMat = math3d.translation([j*2,0,-i*2])
                    prog.setUniform("worldMatrix",self.worldMat)
                    self.c.draw(prog)
        prog.setUniform("tex",self.tex2)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.worldMat = math3d.translation([j*2,2,-i*2])
                prog.setUniform("worldMatrix",self.worldMat)
                self.c.draw(prog)
        prog.setUniform("tex",self.tex3)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.worldMat = math3d.translation([j*2,-2,-i*2])
                prog.setUniform("worldMatrix",self.worldMat)
                self.c.draw(prog)











