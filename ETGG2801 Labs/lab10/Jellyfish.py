
import Program
import math3d
import random
import jelTex




class Jellyfish(object):
    jelTex = None
    def __init__(self):
        self.x = random.uniform(-0.9,0.9)
        self.y = random.uniform(-0.9,0.9)
        self.pos = math3d.vec3(self.x,self.y,0)
        self.dir = math3d.vec3(random.uniform(-0.001,0.001),random.uniform(-0.001,0.001),0)
        self.init_pos = [self.x,self.y,0]
        self.worldMat = 0
        if Jellyfish.jelTex==None:
            Jellyfish.jelTex = jelTex.jelTex()

    def update(self,elapsed):

        if self.pos[0]>=1:
            self.pos[0] = 1
            self.dir[0]*=-1
        if self.pos[0]<=-1:
            self.pos[0] = -1
            self.dir[0]*=-1
        if self.pos[1]>=1:
            self.pos[1] = 1
            self.dir[1]*=-1
        if self.pos[1]<=-1:
            self.pos[1] = -1
            self.dir[1]*=-1


        self.pos = self.pos+self.dir*elapsed
        self.worldMat =math3d.translation(self.init_pos)*math3d.scaling([0.25,0.25,0])*math3d.translation(self.pos)




    def draw(self,prog):
        prog.setUniform("worldMatrix",self.worldMat)
        Jellyfish.jelTex.draw(prog)
