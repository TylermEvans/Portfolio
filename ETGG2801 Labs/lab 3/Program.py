from glfuncs import *
from glconstants import *
import array
class Program:
    POSITION_INDEX = 0
    
    def __init__(self,vsfname,fsfname):
        tmp = array.array("I",[0])
        
        vs = self.make_shader(vsfname, GL_VERTEX_SHADER)
        fs = self.make_shader(fsfname, GL_FRAGMENT_SHADER)
        prog = glCreateProgram()
        glAttachShader(prog,vs)
        glAttachShader(prog,fs)
        glBindAttribLocation(prog,Program.POSITION_INDEX, "a_position")
        
        glLinkProgram(prog)
        infolog = bytearray(4096)
        glGetProgramInfoLog(prog,len(infolog),tmp,infolog)
        if tmp[0] > 0:
            infolog = infolog[:tmp[0]].decode()
            print("Linking",vsfname,"+",fsfname,":")
            print(infolog)
        glGetProgramiv( prog, GL_LINK_STATUS, tmp )
        if not tmp[0]:
            raise RuntimeError("Could not link shaders")
        self.prog = prog

    def use(self):
        glUseProgram(self.prog)
        Program.active = self
        
    def make_shader(self, filename, shadertype ):
        shaderdata = open(filename).read()
        s = glCreateShader( shadertype )
        glShaderSource( s,1,[shaderdata],None)
        glCompileShader( s )
        infolog = bytearray(4096)
        tmp = array.array("I",[0])
        glGetShaderInfoLog( s, len(infolog), tmp, infolog)
        if tmp[0] > 0 :
            infolog = infolog[:tmp[0]].decode()
            print("When compiling",shadertype,filename,":")
            print(infolog)
        glGetShaderiv( s, GL_COMPILE_STATUS, tmp )
        if not tmp[0]:
            raise RuntimeError("Cannot compile "+filename)
        return s
