#!/usr/bin/env python3

import struct
import sys
import array
from math3d import *
import bumpmap
try:
    import tkinter.filedialog
except ImportError:
    pass


def qmul(q,r):
    w = q.w*r.w - dot(q.xyz , r.xyz )
    xyz = q.w*r.xyz + r.w*q.xyz + cross( q.xyz , r.xyz )
    return vec4(xyz.x, xyz.y, xyz.z, w)

def main(fname):

    #spec from ms3d site: http://www.chumba.ch/chumbalum-soft/files/ms3dsdk184.zip
    #MS3D itself is shareware, but there's no license information anywhere in the spec
    #or in its zipfile.

    #header: 14 bytes
    # char: MS3D000000
    # version: int: should be 4
    #num vertices, as a short
    #Next are the vertices. Each one is 15 bytes. 
    #   flags: selected, selected2, or hidden: 1 byte
    #   x,y,z (floats)
    #   bone id (byte, -1=none)
    #   reference count (byte)
    #num triangles, as a short
    #Triangles: 70 bytes each, repeated numtriangles times
    #   flags: short: selected, selected2, hidden
    #   index0, index1, index2 (shorts)
    #   normals: x,y,z,  x,y,z,  x,y,z  (floats)
    #   tex coord s: 3 floats
    #   tex coord t: 3 floats
    #   smoothing group (byte, 1-32)
    #   group index, byte
    #num groups, short
    #Then data for each group
    #   flags (byte), s, s2, h
    #   name (32 bytes)
    #   num triangles (short)
    #   triangle indices: numtriangles of them, shorts
    #   material index, byte, -1=none
    #num materials, short
    #   name, 32 chars
    #   ambient (4 floats)
    #   diffuse (4 floats)
    #   specular (4 floats)
    #   emit (4 floats)
    #   shiny (float) 0-128
    #   transparency (0-1), float
    #   mode, byte, 0,1,2 -- not used
    #   texture file (128 bytes)
    #   alpha file (128 bytes)
    #animation fps (float)
    #current time (float)
    #total frames (int)
    #num joints (short)
    #data for each joint:
    #   flags: byte: s, d
    #   name: 32 bytes
    #   parent name, 32 bytes
    #   rotation: 3 floats  ("local reference matrix")
    #   position: 3 floats
    #       From Blender MS3d importer:
    #       rotation[2] = z axis rotation, [1]=y axis rotation, [0]=x axis rotation
    #       Importer multiplies in order z*y*x, but it probably
    #       also considers points to be postmultiplied
    #       Local matrix transform with mesh points =
    #           translation * rotation * point
    #   num keyframes for rotation: short
    #   num keyframes for translation: short
    #   Then data for all the rotation keyframes:
    #       time: float
    #       rotation (angles, for x, y, and z): floats  
    #   Then data for all the translation keyframes
    #       time: float
    #       position: 3 floats
    #How to apply:
    #   v' = v * "inverse of local reference matrix" * translation_data[i] * rotation_data[i]
    #Older files apparently end here.
    #If we have a newer file, there will be a subversion here: int, always 1
    #num group comments, int
    #Then the comments. No indication as to how we know the end of a comment
    #   Perhaps it's null terminated?
    #integer: 1 if model comments exist
    #Then the model comment, if present, with some unspecified length.
    #Then a "sub-version" number. Call it S.
    #Then num_vertices instances of additional info:
    #   bone ids: 3 bytes: Joint index, or -1 if unused. Call this array B.
    #   weights: 3 bytes:
    #       First element is weight of bone specified the vertex structure
    #           given earlier in the file
    #       Second element is the weight of the bone in B[0]
    #       Third element is the weight of the bone in B[1]
    #       The weight of bone in B[2] is not given explicitly,
    #           but the weights of all the bones must sum to 1,
    #           so we can calculate it from the three weights we do have.
    #   If S==2: We have an integer here that is "extra information",
    #       but the meaning of it is not specified.
    #Integer subversion.
    #Joint colors: num_joints * 3 floats
    #Integer: subversion
    #Joint size, as a float
    #Transparency: How rendering should be done (z buffer, depth sorting, etc.): int
    #Alpha reference value: float
    #End of file.

    def Int():
        b=fp.read(4)
        return struct.unpack("I",b)[0]
    def Short():
        b=fp.read(2)
        return struct.unpack("H",b)[0]
    def Byte():
        return fp.read(1)[0]
    def Float():
        return struct.unpack("f",fp.read(4))[0]
    def String(num):
        tmp=fp.read(num)
        tmps=""
        for b in tmp:
            if b == 0:
                return tmps
            tmps += chr(b)
        return tmps
    def Comment():
        c=""
        while 1:
            x=fp.read(1)
            print("Comment byte:",x)
            if x == '':
                return c
            if x[0] == 0:
                return c
            c += chr(x[0])
            
        
    fp=open(fname,"rb")


    class Tmp:
        pass
       
    sig = fp.read(10)
    assert sig == b"MS3D000000"
    version = Int()
    assert version == 4
    numverts = Short()
    vertices=[]
    for flags,x,y,z,boneid,refcount in struct.iter_unpack("<b3fbb",fp.read(15*numverts)):
        vertices.append( (x,y,z,boneid) )
        
    numtris = Short()
    #normals=[]
    #texes=[]
    faces=[]
    for flags,i0,i1,i2,nx0,ny0,nz0,nx1,ny1,nz1,nx2,ny2,nz2,s0,s1,s2,t0,t1,t2,sgroup,gidx in struct.iter_unpack("<H3H3f3f3f3f3fbb",fp.read(70*numtris)):
        tmp=Tmp()
        faces.append(tmp)
        tmp.i0=i0
        tmp.i1=i1
        tmp.i2=i2
        tmp.n0 = (nx0,ny0,nz0)
        tmp.n1 = (nx1,ny1,nz1)
        tmp.n2 = (nx2,ny2,nz2)
        tmp.tx0 = (s0,1-t0)
        tmp.tx1 = (s1,1-t1)
        tmp.tx2 = (s2,1-t2)
        tmp.gidx = gidx
        tmp.groups=set()
        
    numgroups = Short()
    groups=[]
    for i in range(numgroups):
        tmp=Tmp()
        tmp.flags=Byte()
        tmp.name=String(32)
        print("Group name:",tmp.name)
        tmp.numtris=Short()
        b = fp.read(tmp.numtris*2)
        TI = struct.unpack( str(tmp.numtris)+"H",b )
        #we may sort the triangles later, so the indices in
        #TI won't be valid once that's done
        for ti in TI:
            faces[ti].groups.add(i)
        tmp.mtlindex = Byte()
        tmp.comment=b""
        groups.append(tmp)
        

    nummaterials = Short()
    materials=[]
    for i in range(nummaterials):
        tmp=Tmp()
        tmp.name = String(32)
        tmp.ambient = struct.unpack("4f",fp.read(4*4) )
        tmp.diffuse = struct.unpack("4f",fp.read(4*4) )
        tmp.specular = struct.unpack("4f",fp.read(4*4) )
        tmp.emit = struct.unpack("4f",fp.read(4*4) )
        tmp.shiny = struct.unpack("f",fp.read(4))[0]
        tmp.alpha = struct.unpack("f",fp.read(4))[0]
        Byte()  #mode: Not used
        t = String(128)
        t=t.split("/")[-1].split("\\")[-1]
        if t.find(".jpg") != -1:
            print("Note: Replacing jpeg texture with png")
            t=t.replace(".jpg",".png")
        tmp.texfile = t
        tmp.alphafile = String(128)
        tmp.count=0     #for counting how many faces use this material
        materials.append(tmp)


    for f in faces:
        g = f.gidx
        m = groups[g].mtlindex
        materials[m].count += 1

    tmp=[]
    for i in range(len(materials)):
        tmp.append( (materials[i].count,i) )
    tmp.sort()
    most_used_material = tmp[-1][1]


    fps = Float()
    print("FPS:",fps)
    currenttime = Float()
    print("Current time:",currenttime)
    num_frames = Int()
    print("num_frames:",num_frames)
    print("Computed max time:",num_frames/fps)



    def interpolate(L):
        #use linear interpolation to fill in entries of L that are None
        #Assumes each element of L is a list.
        
        for i in range(len(L)):
            if L[i] == None:
                j=i
                while L[j] == None:
                    j+=1
                #rotationF[i...j] are all None
                #use linear interpolation.
                #FIXME: Is this right?
                start = L[i-1]
                end = L[j]
                numsteps = j-i
                for k in range(i,j):
                    Q=[0,0,0]
                    for m in range(len(start)):
                        Q[m] = start[m] + (k-i+1)/(numsteps+1) * (end[m]-start[m])
                    L[k] = Q
                        
    numjoints = Short()
    joints = []
    for ji in range(numjoints):
        tmp=Tmp()
        joints.append(tmp)
        Byte()      #flags
        tmp.name = String(32)
        tmp.parentname = String(32)
        
        #this is the "local reference matrix"
        rx,ry,rz = struct.unpack("3f", fp.read(4*3))
        if abs(rx) < 1E-6:
            rx=0
        if abs(ry) < 1E-6:
            ry=0
        if abs(rz) < 1E-6:
            rz=0
        tmp.rotation = (rx,ry,rz)
        tmp.translation = struct.unpack("3f", fp.read(4*3))
        
        tmp.numRkeys = Short()
        tmp.numTkeys = Short()
        tmp.rotations=[]
        tmp.translations=[]
        tmp.matrices=[]
        tmp.quaternions=[]
        for i in range(tmp.numRkeys):
            time,rx,ry,rz = struct.unpack("4f",fp.read(4*4) )
            
            frame1 = time*fps
            frame = round(frame1)
            if abs(frame-frame1) > 0.001:
                print(frame1,frame)
                assert 0
            tmp.rotations.append( (time,frame,rx,ry,rz) )
        
        tmp.rotationF = []
        for time,frame,rx,ry,rz in tmp.rotations:
            frame=frame-1
            while frame > len(tmp.rotationF):
                tmp.rotationF.append(None)
            tmp.rotationF.append( [rx,ry,rz] )
            
        while len(tmp.rotationF) < num_frames:
            tmp.rotationF.append( None )

        interpolate(tmp.rotationF)
        
        for i in range(tmp.numTkeys):
            time,tx,ty,tz = struct.unpack("4f",fp.read(4*4) )
            frame1 = time*fps
            frame = round(frame1)
            if abs(frame-frame1) > 0.001:
                print(frame1,frame)
                assert 0
            tmp.translations.append( (time,frame,tx,ty,tz) )
            
        tmp.translationF = []
        for time,frame,tx,ty,tz in tmp.translations:
            frame -= 1
            if tx != 0 or ty != 0 or tz != 0:
                pass
            while frame > len(tmp.translationF):
                tmp.translationF.append(None)
            tmp.translationF.append( (tx,ty,tz) )

        interpolate(tmp.translationF)
        
        while len(tmp.translationF) < num_frames:
            tmp.translationF.append( tmp.translationF[-1] )

        assert len(tmp.rotationF) == len(tmp.translationF)
               

    jointnames={}
    for i in range(len(joints)):
        jointnames[joints[i].name] = i
        
    num_bones = len(joints)
    for j in joints:
        if len(j.parentname) == 0:
            j.parentindex=-1
        else:
            j.parentindex = jointnames[j.parentname]

    for ji in range(len(joints)):
        M = mat4.identity()
        i=ji
        while i != -1:
            R = joints[i].rotation
            T = joints[i].translation

            rx,ry,rz=R
                
            M = M * (
                axisRotation( vec3(1,0,0), rx) *
                axisRotation( vec3(0,1,0), ry) *
                axisRotation( vec3(0,0,1), rz) *
                translation( vec3(T[0],T[1],T[2]) )  
            )
            i = joints[i].parentindex
        
        joints[ji].head = (vec4(0,0,0,1) * M).xyz
        joints[ji].headMatrix = M
        
    for j in joints:
        for i in range(len(j.rotationF)):
            
            M = mat4.identity()
            M = translation( vec3(-1*j.head[0], -1*j.head[1],-1*j.head[2]) )
            
            axis = vec4(1,0,0,0)*j.headMatrix
            angle =  j.rotationF[i][0]
            M = M * axisRotation( axis , angle )
            co = math.cos(angle/2)
            si = math.sin(angle/2)
            qx = vec4( si*axis.xyz, co )
            
            axis = vec4(0,1,0,0)*j.headMatrix
            angle = j.rotationF[i][1]
            M = M * axisRotation( axis , angle  )
            co = math.cos(angle/2)
            si = math.sin(angle/2)
            qy = vec4( si*axis.xyz, co )
            
            axis = vec4(0,0,1,0)*j.headMatrix
            angle = j.rotationF[i][2] 
            M = M * axisRotation( axis , angle )
            co = math.cos(angle/2)
            si = math.sin(angle/2)
            qz = vec4( si*axis.xyz, co )
            
            M = M * translation( vec3(
                j.translationF[i][0], 
                j.translationF[i][1],
                j.translationF[i][2]))
            M = M * translation(vec3(j.head[0], j.head[1], j.head[2]))
            j.matrices.append(M)
            
            q = qmul( qz, qmul(qy,qx) )
            j.quaternions.append(q)
        
        
        
    print(len(joints),"bones")    


    #Older files apparently end here.

    fpos = fp.tell()
    fp.seek(0,2)
    fsize = fp.tell()
    if fsize != fpos:
        print("File has additional data")
        fp.seek(fpos)
        subversion = Int()
        assert subversion == 1
        numgroupcomments = Int()
        print(numgroupcomments,"group comments")
        print(numgroups,"groups")
        for i in range(numgroupcomments):
            comnum = Int()
            comlength = Int()
            comdata = fp.read(comlength)
            print("Comment:",comnum,":",comdata)
            groups[i].comment = comdata
        modcomments = Int()
        assert modcomments == 0 or modcomments == 1
        if modcomments == 1:
            comnum=Int()
            comlength=Int()
            comdata = fp.read(comlength)
            print("Model comment:",comdata)
        else:
            print("No model comments")
            
        subversion = Int()
        print("Subversion:",subversion)
        #Then a "sub-version" number. Call it S.
        #Then num_vertices instances of additional info:
        #   bone ids: 3 bytes: Joint index, or -1 if unused. Call this array B.
        #   weights: 3 bytes:
        #       First element is weight of bone specified the vertex structure
        #           given earlier in the file
        #       Second element is the weight of the bone in B[0]
        #       Third element is the weight of the bone in B[1]
        #       The weight of bone in B[2] is not given explicitly,
        #           but the weights of all the bones must sum to 1,
        #           so we can calculate it from the three weights we do have.
        #   If S==2: We have an integer here that is "extra information",
        #       but the meaning of it is not specified.
        #Integer subversion.
        #Joint colors: num_joints * 3 floats
        #Integer: subversion
        #Joint size, as a float
        #Transparency: How rendering should be done (z buffer, depth sorting, etc.): int
        #Alpha reference value: float
        #End of file.




        
    else:
        print("File does not have extra data; stopping")



    vertexdata=vertices
    texturedata=[]
    normaldata=[]
    tmap={}
    nmap={}
    #group the faces by material
    triangles_by_group={}
    for f in faces:
        T=[ [f.i0,None,None] , [f.i1,None,None], [f.i2,None,None] ]
        
        tmp = [f.n0,f.n1,f.n2]
        for ii in range(3):
            nn = tmp[ii]
            if nn not in nmap:
                nmap[nn] = len(normaldata)
                normaldata.append(nn)
            T[ii][2] = nmap[nn]
        
        tmp = [f.tx0,f.tx1,f.tx2]
        for ii in range(3):
            nn = tmp[ii]
            if nn not in tmap:
                tmap[nn] = len(texturedata)
                texturedata.append(nn)
            T[ii][1] = tmap[nn]
        
        gid = f.gidx
        if gid not in triangles_by_group:
            triangles_by_group[gid]=[]
            
        triangles_by_group[gid].append( T )


            
    tangentdata, bitangentdata, smoothnormals = bumpmap.compute_tbn( vertexdata, texturedata, triangles_by_group )

    vmap={}     #key=vi,ti,ni  Value=index in vdata/tdata/ndata/etc.
    numv=0
    
    #there will be numv items in each of these
    vdata=[]    #vertex positions: vec3
    tdata=[]    #tex coords: vec2
    ndata=[]    #normals: vec3
    Tdata=[]    #tangents: vec3
    Bdata=[]    #bitangents: vec3
    bdata=[]    #bone data: float (one per vertex)
    idata=[]    #indices: three per triangle

    allgroups = list(sorted(triangles_by_group.keys()))
    
    for gid in allgroups:
        for T in triangles_by_group[gid]:
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
                    bdata += [vertexdata[vi][3]]
                    
                idata.append( vmap[key] )
            
    #output
    #mesh format
    ofp=open(fname+".mesh","wb")
    ofp.write(b"mesh_01sbr\n")
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
 
    #bone ownership
    tmp = array.array("f",bdata)
    ofp.write(b"boneowner\n")
    ofp.write(tmp.tobytes())
    ofp.write(b"\n")
     
    ofp.write(( "numbones "+str(len(joints))+"\n").encode())

    tmp=[]
    for j in range(len(joints)):
        tmp += [joints[j].head[0],joints[j].head[1],joints[j].head[2]]
    tmp=array.array("f",tmp)
    assert len(tmp) == num_bones*3
    b = tmp.tobytes()
    ofp.write( b"boneheads\n")
    ofp.write(b)
    ofp.write(b"\n")

    tmp=[]
    for j in range(len(joints)):
        tmp.append( joints[j].parentindex )
    tmp=array.array("f",tmp)
    assert len(tmp) == len(joints)
    b = tmp.tobytes()
    ofp.write( b"boneparents\n" )
    ofp.write(b)
    ofp.write(b"\n")

    ofp.write( ("numframes "+str(num_frames)+"\n").encode() )

    tmp=[]
    for j in joints:
        for x,y,z in j.rotationF:
            tmp += [x,y,z,0]
    tmp=array.array("f",tmp)
    assert len(tmp) == num_frames*num_bones*4
    b = tmp.tobytes()
    ofp.write( b"rotations\n")
    ofp.write(b)
    ofp.write(b"\n")

    tmp=[]
    for j in joints:
        for x,y,z in j.translationF:
            tmp += [x,y,z,0]
    tmp=array.array("f",tmp)
    assert len(tmp) == num_frames * num_bones * 4
    b = tmp.tobytes()
    ofp.write( b"translations\n")
    ofp.write(b)
    ofp.write(b"\n")

    tmp=[]
    for j in joints:
        for M in j.matrices:
            for row in range(4):
                for col in range(4):
                    tmp.append(M[row][col])
    tmp = array.array('f',tmp)
    assert len(tmp) == num_frames * num_bones * 16
    b = tmp.tobytes()
    ofp.write( b"matrices\n")
    ofp.write(b)
    ofp.write(b"\n")

    tmp=[]
    for j in joints:
        for Q in j.quaternions:
            tmp.append(Q.x)
            tmp.append(Q.y)
            tmp.append(Q.z)
            tmp.append(Q.w)
    tmp = array.array('f',tmp)
    assert len(tmp) == num_frames * num_bones * 4
    b = tmp.tobytes()
    ofp.write( b"quaternions\n")
    ofp.write(b)
    ofp.write(b"\n")


    start=0
    for gid in allgroups:
        g = groups[gid]
        m = materials[g.mtlindex]
        
        name = g.name.replace(" ","_")
        if g.comment:
            name += g.comment.decode()
        if len(name) == 0:
            name="?"
            
        num = len(triangles_by_group[gid]) * 3
        ofp.write( ("material %d %d %s " % (start,num,name)).encode())
        ofp.write( ("%f %f %f " % (m.diffuse[0],   m.diffuse[1],   m.diffuse[2])  ).encode() )
        if m.texfile:
            ofp.write( ("map_Kd "+m.texfile+" ").encode() )
        if m.alphafile:
            #we'll use the alpha map for the bump map...
            ofp.write( ("map_Bump "+m.alphafile+" ").encode() )
        #FIXME: what about reflection or specular or emission maps?
        ofp.write(b"\n")
        start += num
        
        
        
    #~ for gid in facegids:
        #~ nf = len(faces_by_group[gid])
        #~ g=groups[gid]
        #~ m = materials[g.mtlindex]
        #~ ofp.write( ("material %d %d " % (start,nf*3) ).encode() )
        #~ if g.comment:
            #~ ofp.write( g.comment.replace(b" ",b"_")  )
        
        #~ ofp.write( g.name.replace(" ","_").encode() )
        #~ ofp.write( (" %f %f %f " % (m.diffuse[0],   m.diffuse[1],   m.diffuse[2]) ).encode() )
 
        #~ ofp.write(b"\n")
        
        #~ start += nf*3
        
    ofp.write(b"\nend\n")

    ofp.close()



if len(sys.argv) == 1:
    infile = tkinter.filedialog.askopenfilename()
    if not infile:
        sys.exit(0)
    main(infile)
else:
    for x in sys.argv[1:]:
        main(x)
