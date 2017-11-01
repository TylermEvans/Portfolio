#!/usr/bin/env python3


import sys


class Vector4:
    def __init__(self,x,y,z,w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
    def __str__(self):
        return "%f %f %f" % (self.x,self.y,self.z)
    
class Node:
    def __init__(self,name,parent,nodelist):
        self.idx=len(nodelist)
        nodelist.append(self)
        self.name=name
        self.ch=[]
        self.translation=None
        self.channels=[]
        self.end=None
        self.parent=parent
        
        #index = frame number
        #values = data for each channel for that frame as a tuple
        self.framedata=[]
        
    def parse(self,fp,nodelist):
        #assume fp is sitting just before the opening { of this
        #item's definition
        x=fp.readline()
        x=x.strip()
        assert x == "{"
        while 1:
            x=fp.readline()
            x=x.strip()
            lst=x.split()
            if lst[0] == "OFFSET":
                self.translation=Vector4( 
                    float(lst[1]),float(lst[2]),float(lst[3]),0.0)
                
            elif lst[0] == "CHANNELS":
                self.channels = lst[2:]
            elif lst[0] == "JOINT":
                b=Node(lst[1],self,nodelist)
                b.parse(fp,nodelist)
                self.ch.append(b)
            elif lst[0] == "End" and lst[1]== "Site":
                #location of the end effector
                fp.readline()   #{
                x=fp.readline().strip()
                lst=x.split()
                assert lst[0]=="OFFSET"
                self.end=Vector4(float(lst[1]),
                    float(lst[2]),
                    float(lst[3]),0.0)
                fp.readline()   #}
            elif lst[0] == "}":
                return 
            else:
                print("Got",lst)
                assert 0

def compute_maxdepth(n):
    if len(n.ch) == 0:
        return 1
    else:
        x=-1
        for c in n.ch:
            d = compute_maxdepth(c)
            if d > x:
                x=d
        return x+1
        
def read_armature_data(oc,fp):
    #parse a biovision bvh file
    nodelist = oc.bonelist
    nodemap = oc.bonemap
    
    assert fp.readline().strip() == "HIERARCHY"
    lst=fp.readline().strip().split()
    assert lst[0] == "ROOT"
    root = Node(lst[1],None,nodelist)
    root.parse(fp,nodelist)
    
    for n in nodelist:
        nodemap[n.name]=n.idx
        
    x=fp.readline().strip()
    assert x == "MOTION"
    lst=fp.readline().strip().split()
    assert lst[0] == "Frames:"
    numframes=int(lst[1])
    fp.readline()       #Frame Time
    #data follows
    #one line per frame
    for i in range(numframes):
        lst=fp.readline().strip().split()
        j=0
        for n in nodelist:
            L=[]
            for k in range(len(n.channels)):
                L.append(float(lst[j]))
                j+=1
            n.framedata.append(L)
    
    md = compute_maxdepth(root)
    oc.bonedepth = md

    #make sure it follows the format we expect
    return root
    
    assert len(nodelist[0].channels) == 6
    assert root.channels[0] == "Xposition"
    assert root.channels[1] == "Yposition"
    assert root.channels[2] == "Zposition"
    assert root.channels[3] == "Xrotation"
    assert root.channels[4] == "Yrotation"
    assert root.channels[5] == "Zrotation"
    for n in nodelist[1:]:
        assert len(n.channels) == 3
        assert n.channels[0] == "Xrotation"
        assert n.channels[1] == "Yrotation"
        assert n.channels[2] == "Zrotation"

class X:
    pass

def main():
    oc=X()
    oc.bonelist=[]
    oc.bonemap={}
    
    fp=open(sys.argv[1])
    root = read_armature_data(oc,fp)
    
#    print("digraph d {")
#    for b in oc.bonelist:
#        print('v%d [label="%s"];' % (b.idx,b.name))

    print(root.name,"is the root")
    for b in oc.bonelist:
        print(b.name,"has offset",b.translation)
        
    for b in oc.bonelist:
        for c in b.ch:
            print(c.name,"has parent",b.name)
    
    
            #print('v%d -> v%d;' % (b.idx,c.idx) )
    #print("}")

main()
