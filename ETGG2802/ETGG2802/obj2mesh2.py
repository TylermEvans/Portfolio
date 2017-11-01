#!/usr/bin/env python3

import sys
import array
from math3d import *
from bumpmap2 import *

try:
    import tkinter.filedialog
except ImportError:
    pass


def main():
            
    #get input and output file names
    if len(sys.argv) == 1:
        infile = tkinter.filedialog.askopenfilename()
        if not infile:
            return
        convert(infile)
        
    else:
        for infile in sys.argv[1:]:
            convert(infile)
        
def convert(infile):
    outfile = infile+".mesh"
    
    #vertex data will be a list of vec3's
    vertexdata = [] 
    
    #list of vec2's
    texturedata = [] 
    
    #list of vec3's
    normaldata = []
    
    #key = material name, value = list of triangles. 
    #Each triangle consists of three 
    #(vertex index, texture index, normal index, material index) tuples
    triangles = {} 
    
    #materials. Key = material name; value = dictionary
    mdict = {} 
    
    #current material
    currmtl=None

    for L in open(infile):
        L=L.strip()
        
        if len(L) == 0:
            continue
            
        L = L.split(" ")
        
        if L[0].startswith("#"):
            pass
        elif L[0] == "o" :
            currobj = L[1]
        elif L[0] == "v" :
            #a vertex (xyz) specification
            pt = [float(q) for q in L[1:]]
            vertexdata.append(vec3(pt[0],pt[1],pt[2]))
        elif L[0] == "vt" :
            #texture coordinate
            pt = [float(q) for q in L[1:]]
            texturedata.append(vec2(pt[0],pt[1]))
        elif L[0] == "vn":
            #normal
            pt = [float(q) for q in L[1:]]
            normaldata.append( vec3(pt[0],pt[1],pt[2]) )
        elif L[0] == "f" :
            #face (triangle)
            
            V = L[1:]
            if len(V) != 3:
                print("Warning: Non-triangles present:",len(V),"vertices") 
                continue 
            
            #t=the current triangle
            t=[] 
            for vspec in V:
                #four formats possible: vi  vi//ni  vi/ti  vi/ti/ni
                tmp = vspec.split("/") 
                
                #obj uses one-based indexing, so we must subtract one here
                vi=int(tmp[0])-1 
                
                #if no texture coordinate, make one up
                if len(tmp) < 2 or len(tmp[1]) == 0:
                    ti=0
                else:
                    ti = int(tmp[1])-1 
                    
                if len(tmp) < 3 or len(tmp[2]) == 0:
                    ni=0
                else:
                    ni = int(tmp[2])-1
                    
                t.append( (vi,ti,ni) )
            
            triangles[currmtl].append(t) 
            
        elif L[0] == "mtllib" :
            #material library; must parse it
            ML = open(L[1]).readlines()
            
            #look at each material and store information about it
            for m in ML:
                m=m.strip()
                if len(m) == 0:
                    continue
                    
                #important: only split once in case we have a
                #parameter with a space in it
                m=m.strip().split(" ",1)
                
                if m[0].startswith("#"):
                    pass
                elif m[0] == "newmtl" :
                    mname = m[1] 
                    mdict[mname]={"count":0}
                else:
                    mdict[mname][m[0]] = m[1]
        elif L[0] == "usemtl" :
            #change currently active material
            currmtl = L[1]
            if currmtl not in triangles:
                triangles[currmtl]=[]
        elif L[0] == 'l' or L[0] == 's':
            pass
        else:
            print("Note: Skipping",L)
    
    
    #first, determine how many unique vertices we'll have
    vmap={}     #key=vi,ti,ni  Value=index in vdata
    numv=0
    vdata=[]
    tdata=[]
    ndata=[]
    idata=[]   
    Tdata=[]    #tangents
    Bdata=[]    #bitangents
    
    
    
    #just for informational purposes
    numshared=0
    
    allmaterials = sorted(triangles.keys())

    
    tangentdata,bitangentdata,smoothednormaldata = compute_tbn(vertexdata,texturedata,triangles)

    for mtlname in allmaterials:
        for T in triangles[mtlname]:
            #T will be a list of three vi,ti,ni tuples
            assert len(T) == 3
            for vi,ti,ni in T:
                key = (vi,ti,ni)
                if key not in vmap:
                    #first time we've seen this vertex, so add it
                    #to our vertex list and our dictionary
                    vmap[key]=numv
                    numv+=1
                    vdata += [vertexdata[vi][0], vertexdata[vi][1], vertexdata[vi][2] ]
                    tdata += [texturedata[ti][0], texturedata[ti][1] ]
                    ndata += [normaldata[ni][0],normaldata[ni][1], normaldata[ni][2]]
                    #ndata += [smoothednormaldata[vi][0], smoothednormaldata[vi][1], smoothednormaldata[vi][2]]
                    Tdata += [tangentdata[vi][0], tangentdata[vi][1], tangentdata[vi][2]]
                    Bdata += [bitangentdata[vi][0], bitangentdata[vi][1], bitangentdata[vi][2]]
                else:
                    numshared+=1  #only for curiosity :-)
                    
                idata.append( vmap[key] )
        
        
        
    
    
    #information for the user
    print(len(vdata)//3,"vertices") 
    print(len(idata),"indices")
    print(numshared,"shared")
    
    ofp = open(outfile,"wb")
    ofp.write(b"mesh_01sb\n") 
    ofp.write( ("num_vertices "+str(len(vdata)//3)+"\n").encode() ) 
    ofp.write( ("num_indices "+str(len(idata))+"\n").encode() ) 

    #positions
    tmp = array.array("f",vdata)
    ofp.write(b"positions\n")
    ofp.write(tmp.tobytes())
    ofp.write(b"\n")
    
    #texture coordinates
    tmp = array.array("f",tdata)
    ofp.write(b"texcoords\n")
    ofp.write(tmp.tobytes())
    ofp.write(b"\n")

    #normals
    tmp = array.array("f",ndata)
    ofp.write(b"normals\n")
    ofp.write(tmp.tobytes())
    
    ofp.write(b"\n")

    #tangents
    tmp = array.array("f",Tdata)
    
    print("\n")
    
    ofp.write(b"tangents\n")
    ofp.write(tmp.tobytes())
    ofp.write(b"\n")

    #bitangents
    tmp = array.array("f",Bdata)
    ofp.write(b"bitangents\n")
    
    ofp.write(tmp.tobytes())
    ofp.write(b"\n")

    #always 4 bytes per index
    tmp = array.array("I",idata)
    ofp.write(b"indices\n")
    ofp.write(tmp.tobytes()) 
    ofp.write(b"\n")
    
    #give index ranges for each material
    start=0
    for mtlname in allmaterials:
        num = len(triangles[mtlname]) * 3
        ofp.write( ("material %d %d %s %s" % (start,num,mtlname,mdict[mtlname]["Kd"]) ).encode() )
        for k in mdict[mtlname]:
            if k.startswith("map_") or k == "refl":
                ofp.write( (" "+k+" "+mdict[mtlname][k]).encode() )
        ofp.write(b"\n")
        start += num
    
    ofp.write(b"\nend\n") 
    ofp.close()


main()
