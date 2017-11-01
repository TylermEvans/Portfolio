import math3d


a = math3d.vec3(0,1,0)
b = math3d.vec3(-1,-1,1)
c = math3d.vec3(1,-1,1)

u = b-a
v = c-a
t = math3d.cross(u,v)
z = math3d.normalize(t)
print(z)

