import Hexagon
import math3d
import Program

class Bullet(object):
    hexa = None
    def __init__(self,x,y,w):
        self.x = x
        self.y = y
        self.xpos = 0
        self.worldMat = math3d.scaling([0.25,0.25,0])*w
        self.wm = 0
        if Bullet.hexa == None:
            Bullet.hexa = Hexagon.Hexagon()

    def update(self,elapsed):

        self.wm = [self.x*elapsed,self.y,0]
        self.worldMat = self.worldMat*math3d.translation(self.wm)
        self.xpos = self.worldMat[3][0]



    def draw(self,prog):
        prog.setUniform("worldMatrix",self.worldMat)
        Bullet.hexa.draw(prog)