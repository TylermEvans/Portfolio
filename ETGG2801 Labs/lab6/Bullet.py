import Hexagon
import math3d
import Program


class Bullet(object):
    hexa = None
    def __init__(self,x,y,w):
        self.x = x
        self.y = y
        self.worldMat = 0
        self.movVec = 0
        self.rotate = 0
        self.w = w

        if Bullet.hexa == None:
            Bullet.hexa = Hexagon.Hexagon()

    def update(self,elapsed):
        self.rotate+=1
        self.x = self.x + elapsed*0.003
        self.movVec = [self.x,self.y,0]
        self.worldMat =  math3d.scaling([0.10,0.10,1]) * math3d.axisRotation(math3d.vec3(0,0,1),self.rotate) * math3d.translation([self.w[3][0],self.w[3][1],self.w[3][2]]) * math3d.translation(self.movVec)






    def draw(self,prog):
        prog.setUniform("worldMatrix",self.worldMat)
        Bullet.hexa.draw(prog)