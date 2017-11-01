import Program
import Cube
import math3d


class World(object):
    def __init__(self,filename):
        self.map = filename
        self.worldMat = 0
        self.data = []
        fp = open(filename,"r")
        for i in fp:
            self.data.append(i)




    def draw(self,prog):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j]=="*":
                    vec = math3d.vec3(1,0,0)
                    self.worldMat = math3d.translation([j,0,0])*math3d.translation([0,0,-i])*math3d.axisRotation(vec,180)*math3d.translation([-6,0,0])*math3d.translation([0,-2,0])*math3d.translation([0,0,-20])
                    prog.setUniform("worldMatrix",self.worldMat)
                    c = Cube.Cube()
                    c.draw(prog)
