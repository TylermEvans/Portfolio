import Square2
import math3d
import Program
import Texture
import time
from glfuncs import *
from glconstants import *

class Bullet(object):
    square = None
    tex = None
    def __init__(self,eye,U,V,radius):
        self.pos = eye
        self.U = U
        self.V = V
        self.W = math3d.cross(self.U,self.V)
        self.radius = radius
        if Bullet.square == None:
            Bullet.square = Square2.Square()
        if Bullet.tex == None:
            Bullet.tex = Texture.ImageTexture("spell.png")
        self.worldMat = 0
        self.bbsize = math3d.vec2(0.5,0.5)
        self.life = 100

        
       
        

    def update(self,elapsed):
        self.pos = self.pos+self.W*-1*elapsed*0.003
        self.worldMat = math3d.translation(self.pos)
        if self.life>0:
            self.life-=1
        
    





    def draw(self,prog):
        prog.setUniform("worldMatrix",self.worldMat)
        prog.setUniform("tex", Bullet.tex)
        prog.setUniform("bbsize",self.bbsize)
        prog.setUniform("vshader",1.0)
        prog.setUniform("fshader",1.0)
        Bullet.square.draw(prog)
