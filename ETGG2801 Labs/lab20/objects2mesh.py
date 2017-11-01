import tkinter.filedialog
import sys
import os
import array
if len(sys.argv)==1:
    infile = tkinter.filedialog.askopenfilename()
    if not infile:
        sys.exit(0)
else:
    infile = sys.argv[1]
outfile = infile+".mesh"
vertexdata = []
normaldata = []
texdata = []
triangles = []
T=[]
mtls = {None:{"count":0}}
omtl = None

fp = open(infile)
for line in fp:
    line = line.strip()
    if len(line)==0:
        pass
    elif line.startswith("#"):
        pass
    elif line.startswith("v "):
        lst = line.split()[1:]
        lst = [float(q) for q in lst]
        vertexdata.append(lst)
    elif line.startswith("vn "):
        lst = line.split()[1:]
        lst = [float(q) for q in lst]
        normaldata.append(lst)
    elif line.startswith("vt "):
        lst = line.split()[1:]
        lst = [float(q) for q in lst]
        texdata.append(lst)
    elif line.startswith("f "):
        lst = line.split()[1:]
        if len(lst)!=3:
            print("not triangle")
        else:
            T = []
            mtls[omtl]["count"] += 1
            for vspec in lst:
                vv = vspec.split('/')
                if len(vv)==1:
                    #vi
                    T.append((int(vv[0])-1,0,0))
                elif len(vv)==2:
                    T.append((int(vv[0])-1,int(vv[1])-1,0))
                
                else:
                    if len(vv[1])==0:
                        T.append((int(vv[0])-1,0,int(vv[2])-1))
                    else:
                        T.append((int(vv[0])-1,int(vv[1])-1,int(vv[2])-1))
            triangles.append(T)

    elif line.startswith("mtllib"):
        mfp = open(line[7:])
        for line in mfp:
            line = line.strip()
            if len(line) ==0:
                pass
            elif line[0]=="#":
                pass
            elif line.startswith("newmtl"):
                curmtl = line[7:]
                mtls[curmtl] = {"count":0}
            else:
                lst = line.split(" ",1)
                mtls[curmtl][lst[0]] = lst[1]                    
    elif line.startswith("usemtl"):
        omtl = line[7:]
    

indexmap = {}
otl = []
cat = []  
for T in triangles:
    for vi,ti,ni in T:       
        key = (vi,ti,ni)
        if key not in indexmap:
            indexmap[key] = len(cat)
            cat.append(key)
        otl.append(indexmap[key])

    
print(cat)
ofp = open(outfile,"wb")
ofp.write(b"mesh_01\n")
ofp.write(("num_vertices "+str(len(cat))+"\n").encode())
ofp.write(("num_triangles "+str(len(triangles))+"\n").encode())
maxc = 0
maxmtl = None
for mname in mtls:
    c = mtls[mname]["count"]
    if c>maxc:
        maxc = c
        maxmtl = mname

ofp.write(("texture_file "+mtls[maxmtl]["map_Kd"]).encode())
ofp.write(b"\n")
tmpv = []
tmpn = []
tmpt = []

for vi,ti,ni in cat: 
    tmpv.append(vertexdata[vi][0])
    tmpv.append(vertexdata[vi][1])
    tmpv.append(vertexdata[vi][2])
    tmpt.append(texdata[ti][0])
    tmpt.append(texdata[ti][1])
    tmpn.append(normaldata[ni][0])
    tmpn.append(normaldata[ni][1])
    tmpn.append(normaldata[ni][2])



ofp.write(b"vertices\n")
ofp.write(array.array("f", tmpv).tobytes())
ofp.write(b"\n")
ofp.write(b"normals\n")
ofp.write(array.array("f", tmpn).tobytes())
ofp.write(b"\n")
ofp.write(b"texcoords\n")
ofp.write(array.array("f", tmpt).tobytes())
ofp.write(b"\n")
ofp.write(b"indices\n")
ofp.write(array.array("I",otl).tobytes())
ofp.write(b"\n")
ofp.write(b"end\n")
ofp.close()
    
                                
            
        
        
