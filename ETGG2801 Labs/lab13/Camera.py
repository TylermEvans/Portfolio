import math3d
import math
class Camera:
    def __init__(self,**kw):
        self.fov_h = kw.get("fov",45)
        self.hither = kw.get("hither",0.1)
        self.yon = kw.get("yon",1000)
        self.aspect_ratio = kw.get("aspect_ratio",1)
        self.fov_v = 1.0/self.aspect_ratio * self.fov_h
        self.U = math3d.vec3(0,0,0)
        self.V = math3d.vec3(0,0,0)
        self.W = math3d.vec3(0,0,0)
        self.eye = math3d.vec3(0,0,0)
        self.compute_proj_matrix()
        self.compute_view_matrix()


    def compute_proj_matrix(self):
        self.projmatrix = math3d.mat4(
            1/math.tan(math.radians(self.fov_h)),0,0,0,
            0,1/math.tan(math.radians(self.fov_v)),0,0,
            0,0,1+2*self.yon/(self.hither-self.yon),-1,
            0,0,2*self.hither*self.yon/(self.hither-self.yon),0)

    def compute_view_matrix(self):
        self.viewmatrix = math3d.mat4(1,0,0,0,
                                      0,1,0,0,
                                      0,0,1,0,
                                      -self.eye.x,-self.eye.y,-self.eye.z,1)*math3d.mat4(self.U.x,self.V.x,self.W.x,0,
                                                                                       self.U.y,self.V.y,self.W.y,0,
                                                                                       self.U.z,self.V.z,self.W.z,0,
                                                                                       0,0,0,1)


    def draw(self,prog):
        prog.setUniform("projMatrix",self.projmatrix)
        prog.setUniform("viewMatrix",self.viewmatrix)
    def lookAt(self,eye,coi,up):
        self.eye = math3d.vec4(eye.xyz,1)
        look = math3d.normalize(math3d.vec4(coi.xyz,1)-math3d.vec4(eye.xyz,1))
        up = math3d.vec4(up.xyz,0)
        self.W = -look
        self.U = math3d.cross(look,up)
        self.V = math3d.cross(self.U,look)
        self.compute_view_matrix()
    def walk(self,amount):
        m = math3d.translation(-amount*self.W)
        self.eye = self.eye*m
        self.compute_view_matrix()
    def strafe(self,amounth,amountv,amountf):
        m = math3d.translation(amounth*self.U)*math3d.translation(amountv*self.V)*math3d.translation(amountf*self.W)
        self.eye = self.eye*m
        self.compute_view_matrix()
    def turn(self,angle):
        m = math3d.axisRotation(self.V,angle)
        self.U = self.U*m
        self.W = self.W*m
        self.compute_view_matrix()

