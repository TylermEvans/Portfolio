import Mesh
import Program
import math3d

class Enemy(object):
    mesh = None
    def __init__(self,fname,pos,radius):
        self.alpha = 1
        self.pos = pos
        self.radius = radius
        if Enemy.mesh==None:
            Enemy.mesh = Mesh.Mesh(fname)
        self.worldMat = math3d.translation(self.pos)
        


        
    def draw(self,prog):
        prog.setUniform("vshader",0)
        prog.setUniform("fshader",0)
        prog.setUniform("alphaOffset",1-self.alpha)
        prog.setUniform("worldMatrix",self.worldMat)
        Enemy.mesh.draw(prog)
        
        
