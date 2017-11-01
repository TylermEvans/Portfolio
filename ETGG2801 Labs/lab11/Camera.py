from math3d import *

class Camera:
    def __init__(self):
        ah=45
        av=45
        hither=0.1
        yon=100
        self.projmatrix = mat4( 
            1/math.tan(math.radians(ah)),0,0,0,
            0,1/math.tan(math.radians(av)),0,0,
            0,0,1+2*yon/(hither-yon),-1,
            0,0,2*hither*yon/(hither-yon),0)

    def draw(self,prog):
        prog.setUniform("projMatrix",self.projmatrix)
