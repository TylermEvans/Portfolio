
from math3d import *

def compute_tbn(vdata, tdata, triangles):
    #vdata = list of vertex positions (x,y,z coordinates)
    #tdata = list of texture coordinates (s,t tuples)
    #triangles = dictionary. Key = string, value = list of triangles
    #   Each triangle consists of three tuples
    #   Each tuple has a vertex index as its first entry
    #       and a texture coordinate index as its second entry
    #debugging_info is just a string that is printed when we find bad geometry

    #tangents. One per entry in vdata
    Tdata = []
    
    #bitangents
    Bdata = []
    
    #normals (smoothed)
    Ndata = []
    
    for i in range(len(vdata)):
        Tdata.append(vec3(0,0,0))
        Bdata.append(vec3(0,0,0))
        Ndata.append(vec3(0,0,0))
        
    for mtlname in triangles:    
        for T in triangles[mtlname]:
            qi = T[0][0]
            ri = T[1][0]
            si = T[2][0]
            
            q = vdata[qi]
            q = vec3(q[0],q[1],q[2])
            r = vdata[ri]
            r = vec3(r[0],r[1],r[2])
            s = vdata[si]
            s = vec3(s[0],s[1],s[2])

            try:
                N = normalize(cross(s-r,q-r))
            except ZeroDivisionError:
                print(mtlname,": Divide by zero: Degenerate triangles?",
                    q,r,s)
                N=vec3(0,1,0)
                
            Ndata[qi] = normalize(Ndata[qi]+N)
            Ndata[ri] = normalize(Ndata[ri]+N)
            Ndata[si] = normalize(Ndata[si]+N)
            
            
            qi1 = T[0][1]
            ri1 = T[1][1]
            si1 = T[2][1]
            qtex = tdata[qi1] 
            qtex = vec2(qtex[0],qtex[1])
            rtex = tdata[ri1]
            rtex = vec2(rtex[0],rtex[1])
            stex = tdata[si1]
            stex = vec2(stex[0],stex[1])
            
            r_ = r-q
            s_ = s-q
            r_tex = rtex-qtex
            s_tex = stex-qtex

            try:
                tmp = 1.0/(r_tex[0]*s_tex[1]-s_tex[0]*r_tex[1])
            except ZeroDivisionError:
                print(mtlname,": Warning: Bad texture coordinates (",
                    qtex,rtex,stex,"; bump mapping will be bad")
                tmp=1
                
            #row 0 of the R matrix
            R00 = tmp*s_tex[1]
            R01 = tmp*-r_tex[1]
            tanvec = vec3(
                R00*r_[0]+R01*s_[0],
                R00*r_[1]+R01*s_[1],
                R00*r_[2]+R01*s_[2]
            )
            try:
                Tdata[qi] = normalize(Tdata[qi] + tanvec)
                Tdata[ri] = normalize(Tdata[ri] + tanvec)
                Tdata[si] = normalize(Tdata[ri] + tanvec)
            except ZeroDivisionError:
                print(mtlname,": Zero length tangent")
                
            
    #gram-schmidt
    for i in range(len(Ndata)):
        try:
            N = Ndata[i]
            T = Tdata[i]
            N=normalize(N)
            T = T - dot(T,N)*N
            T=normalize(T)
            B = normalize( cross(N,T) )
            
        except ZeroDivisionError:
            print("Warning: Bad GS; bump mapping will be bad",
                "N=",Ndata[i],"T=",Tdata[i],"i=",i,
                "p=",vdata[i])
            T=vec3(1,0,0)
            B=vec3(0,1,0)
            N=vec3(0,0,1)
            
        Tdata[i] = T
        Bdata[i] = B
        Ndata[i] = N
            
    return Tdata,Bdata,Ndata
