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



    def draw(self,prog):
        tex = ImageTexture("roof.png")
        tex2 = ImageTexture("brick.png")
        tex3 = ImageTexture("brickfloor.png")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                vec = math3d.vec3(1,0,0)
                self.worldMat = math3d.translation([j*2,0,0])*math3d.translation([0,0,-i*2])*math3d.axisRotation(vec,45)*math3d.translation([-10,0,0])*math3d.translation([0,-10,0])*math3d.translation([0,0,-12])
                prog.setUniform("worldMatrix",self.worldMat)
                if self.data[i][j] == "*":
                    c = Cube2.Cube2()
                    prog.setUniform("tex",tex)
                    c.draw(prog)
                if self.data[i][j] == ":":
                    c = Cube2.Cube2()
                    prog.setUniform("tex",tex2)
                    c.draw(prog)
                if self.data[i][j] == "?":
                    c = Cube2.Cube2()
                    prog.setUniform("tex",tex3)
                    c.draw(prog)







