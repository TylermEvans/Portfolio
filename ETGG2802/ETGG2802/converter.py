def convert():
    cv = []
    cvt = []
    vn = []
    cf = []
    for L in open("cube.obj"):
        L=L.strip()
        if (len(L))==0:
            continue
        L=L.split(" ")
        if L[0].startswith("#"):
            pass
        elif L[0]==("v"):
            pt=[float(q) for q in L[1:]]
            cv.append(vec3(pt[0],pt[1],pt[2]))
        elif L[0]==("vt"):
            pt=[float(q) for q in L[1:]]
            cvt.append(vec2(pt[0],pt[1]))
        elif L[0]==("vn"):
            pt=
    maplist = []
    fp = open("map.txt")
    for line in fp:
        
