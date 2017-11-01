#!/usr/bin/env python3

import xml.dom.minidom
import xml.etree.ElementTree
import sys
#import json
import re



        
class Param:
    pass
    def __repr__(self):
        return str(self.__dict__)+"\n"
 

extensionrex=re.compile(r"gl[_A-Za-z0-9]+([A-Z]{2,})")
#ARB|SUN|EXT|NV|AMD|QCOM|ATI|INTEL|APPLE|IBM|OES|KHR|SGI|MESA|ANGLE|GREMEDY|3DFX|IMG)")

specialfuncs=set()


def output_c_prologue(c):
    print(r"""
#ifdef WIN32
#include <windows.h>
#else
#include <dlfcn.h>
#endif
#include "glcorearb.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdexcept>
#include <cstdio>

using namespace std;

static void* mygetprocaddr(const char* funcname){
    void* x = 0;
    
#ifdef WIN32
    static HMODULE gllib = 0;
    if (!gllib) {
        gllib = LoadLibraryA("opengl32.dll");
        if (!gllib)
            throw runtime_error("Cannot load GL library");
    }
    typedef void* (__stdcall *GLT)(LPCSTR);
    static GLT wglgpa;    
    if( !wglgpa ){
        wglgpa = (GLT) GetProcAddress(gllib,"wglGetProcAddress");
        if(!wglgpa)
            throw runtime_error("Cannot find wglGetProcAddress");
    }
    
    x = (void*) wglgpa(funcname);
    
    if (!x || x == (void*)1 || x == (void*)2 || x == (void*)3 || x == (void*)-1)
        x = 0;
        
    if(!x)
        x = (void*)GetProcAddress(gllib, funcname);
        
#else   
    static void* gllib = 0;
    if(!gllib){
        gllib = dlopen("libGL.so", RTLD_NOW);
        if (!gllib)
            throw runtime_error("Cannot load GL library");
    }
    x = dlsym(gllib, funcname);
#endif

    if (!x)
        throw runtime_error(string("Could not load function ")+funcname);
        
    return x;
  
}

""",file=c)

   
   
def get_require_and_removed_features(root):
    remove=set()
    require=set()
    for feature in root.iter("feature"):
        if feature.attrib["api"] == "gl" and float(feature.attrib["number"]) >= 1.0:
            for R in feature.iter("require"):
                if "profile" in R.attrib and R.attrib["profile"] != "core":
                    continue
                for C in R.iter("command"):
                    require.add(C.attrib["name"])

    for feature in root.iter("feature"):
        for R in feature.iter("remove"):
            if "profile" in R.attrib and R.attrib["profile"] == "core":
                for command in R.iter("command"):
                    remove.add(command.attrib["name"])
    return require,remove

#def collect_text(n):
#    tmp=[]
#    n.normalize()       #join adjacent Text nodes to one node
#    tmp.append(n.text)
#    for c in n.childNodes:
#        if n.nodeType == TEXT_NODE:
#            tmp.append(n.data)
#        else:
#            tmp.append(collect_text(c))
#    return "".join(tmp)
    
#def process_typedefs(root,typemap):
#    #process the typedefs
#    for types in root.iter("types"):    
#        for type_ in types.iter("type"):
#            txt = collect_text(type_)
#            print(txt)
            
def process_function_definition(command,proto,require,remove,allfuncnames):
    
    #get function's return type. The text
    #and tail fields would hold const or pointer items

    #return type, as a C type
    returntype = ""
    if proto.text:
        returntype += proto.text
    if proto[0].tag == "ptype":
        if proto[0].text:
            returntype += proto[0].text
        if proto[0].tail:
            returntype += proto[0].tail

    returntype = returntype.strip()

    #function name
    fname = proto.find("name").text

    if extensionrex.match(fname) or fname in remove or fname in specialfuncs or fname not in require:
        return None,None,None
    
    #print("~~~~~~~~~~",fname,"~~~~~~~~~~~~")

    allfuncnames.append(fname)
    
    paramlist=[]
    for param in command.findall("param"):
        
        ptype = ""
        
        tmp = param.text 
        if tmp != None:
            const = tmp.strip()
        else:
            const=None
        
        pointer=""    
        tmp = param.find("ptype")
        if tmp != None:
            ptype += tmp.text.strip()
            if tmp.tail:
                pointer = tmp.tail.strip()
            
        if "len" in param.attrib:
            isarray=True
            arraylen = param.attrib["len"]
        else:
            isarray=False
            arraylen=None

        #make sure const didn't capture more than it should
        if const == "const":
            pass
        elif not const:
            pass
        else:
            if ptype or pointer:
                print (ptype,pointer,const)
                assert 0

            if const == "const void *":
                const="const"
                ptype = "void"
                pointer = "*"
            elif const == "void *":
                const=None
                ptype="void"
                pointer="*"
            elif const == "void**" or const == "void **":
                const=None
                ptype="void"
                pointer="**"
            elif const == "const void **" or const == "const void *const*":
                const="const"
                ptype="void"
                pointer="**"
            else:
                print("Bad const:")
                print("const=",const)
                print(ptype)
                print(pointer)
                assert 0

            
        if pointer == "*const*":
            pointer="**"
        
        #the name of the parameter, as recorded in the gl.xml file    
        name = param.find("name")
        
        try:
            P = Param()
            P.name = name.text+"_"
            P.ptype = ptype  #parameter type, as a C type
            P.isarray = isarray 
            P.arraylen = arraylen 
            P.const = const
            P.pointer = pointer
            paramlist.append(P)
        except AttributeError:
            print("fname=",fname)
            print("name=",name)
            print("ptype=",ptype)
            print(name.text)
            print(ptype.text)
            raise
    #endfor each parameter
    
    return returntype, fname, paramlist
    
    

def main():
    root = xml.etree.ElementTree.parse("glspec/gl.xml")

    for x in root.iter("comment"):
        copyrt = x.text 
        break

    #glconstants=open("glconstants.h","w")
    #print("/*Data from gl.xml, which has this copyright:",file=glconstants)
    #print( copyrt.replace("\n","\n#"), file=glconstants)
    #print("*/",file=glconstants)

    #for enums in root.iter("enums"):
    #    for enum in enums.iter("enum"):
    #        print("static const GLenum ",enum.attrib["name"],"=",enum.attrib["value"],";",
    #            file=glconstants)
    #glconstants.close()
    
    c = open("glfuncs.cpp","w")
    h = open("glfuncs.h","w")
    
    for x in [c,h]:
        print("/*Data from gl.xml, which has this copyright:",file=x)
        print( copyrt.replace("\n","\n#"), file=x)
        print("*/",file=x)
        
    print("#pragma once",file=h)
    print('#include "glcorearb.h"',file=h)
    
    print('#include "glfuncs.h"',file=c)
    
    output_c_prologue(c)
    
    #get required and removed features
    require,remove = get_require_and_removed_features(root)
    
    #process_typedefs(root,typemap)
    
    #all the GL functions we are working with
    allfuncnames=[]

    #iterate over all GL functions
    for commands in root.iter("commands"):
        for command in commands.iter("command"):
            
            proto = command.find("proto")

            returntype, fname, paramlist = process_function_definition(command,proto,require,remove,allfuncnames)
            
            if returntype == None and fname == None and paramlist == None:
                continue
                
            #debugging
            xmlfuncspec = xml.etree.ElementTree.tostring(command).decode()
            
            output_c_function_code( c, h, fname, returntype, paramlist, xmlfuncspec)
            
    c.close()
    h.close()

    sys.exit(0)
    

def output_c_function_code(cfile,hfile,fname,returntype,paramlist,xmlfuncspec):
    
    for f in [cfile,hfile]:
        print(returntype,fname,"(",file=f,end="")
    
        flag=0
        for P in paramlist:
            if flag:
                print(",",file=f,end=" ")
            flag=1
            if P.const:
                print(P.const,end=" ",file=f)
            print(P.ptype,file=f,end=" ")
            if P.pointer:
                print(P.pointer,file=f,end=" ")
            print(P.name,file=f,end=" ")
        print(")",file=f,end="")
    
    print(";",file=hfile)
    print("{",file=cfile)
    
    #for debugging
    print("    /*",xmlfuncspec,"*/",file=cfile)

    proctype = "PFN"+fname.upper()+"PROC"
    print("    static",proctype,"glfunc;",file=cfile)
    print("    if(!glfunc)",file=cfile)
    print('        glfunc = (',proctype,') mygetprocaddr("'+fname+'");',file=cfile)
    
    #call GL function
    if returntype != "void":
        print("    "+returntype+" retval = ",file=cfile,end="")
    else:
        print("    ",file=cfile,end="")
    print("glfunc(",end="",file=cfile)

    #pass parameters to GL function
    for i in range(len(paramlist)):
        if i > 0 :
            print(", ",end="",file=cfile)
            
        print(paramlist[i].name,file=cfile,end="")
        
    print(");",file=cfile)
    
    #return the data
    if returntype == "void":
        print("    return;",file=cfile)
    else:
        print("    return retval;",file=cfile)
    print("}",file=cfile)


if __name__ == "__main__":
    main()
    
