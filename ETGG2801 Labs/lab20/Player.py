import math3d

class Player(object):
    def __init__(self,pos,radius,V,U):
        self.pos = pos
        self.radius = radius
        self.V = V
        self.U = U
        self.W = math3d.cross(self.V,self.U)
        
    def walk(amt,cam):
        m = math3d.translation(-amt*self.W)
        self.eye = self.eye*m
        cam.compute_view_matrix()
        
    def turn(self,angle):
        m = math3d.axisRotation(self.V,angle)
        self.U = self.U*m
        self.W = self.W*m
        cam.compute_view_matrix()
    
