import sys
from ctypes import *
import time
import pysdl2.sdl2 as sdl2
from pysdl2.sdl2.keycode import *
from glfuncs import *
from glconstants import *
from Square import *
from Program import *
from math3d import * 
from Texture import *
from Pyramid import *
from Camera import *
import Cube
import World
import Cube2

def debugcallback(source,typ, id_,severity, length, message, obj ):
    print(message)

def ranges_overlap(a,b,  c,d):
    return  (c<b and d>a ) or (a<d and b>c)

sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
win = sdl2.SDL_CreateWindow( b"ETGG",20,20, 512,512, sdl2.SDL_WINDOW_OPENGL)
if not win:
    print("Could not create window")
    raise RuntimeError()

sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_STENCIL_SIZE, 8)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION,3)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION,3)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_FLAGS,sdl2.SDL_GL_CONTEXT_DEBUG_FLAG)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
rc = sdl2.SDL_GL_CreateContext(win)
if not rc:
    print("Cannot create GL context")
    raise RuntimeError()
    
glDebugMessageControl(GL_DONT_CARE,GL_DONT_CARE,GL_DONT_CARE, 0, None, 1 )
glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS)
glDebugMessageCallback(debugcallback,None)





tex = ImageTexture("spiral.png")
tex2 = ImageTexture("brick.png")
w = World.World("map.txt")
prog = Program("vs.txt","fs.txt")
prog.use()

cam = Camera()

glClearColor(0.2,0.4,0.6,1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)


keys=set()
last=sdl2.SDL_GetTicks()
paused=False
ev=sdl2.SDL_Event()
angle=0
TWOPI = 2.0*3.14159265358979323
while 1:
    while 1:
        if not sdl2.SDL_PollEvent(byref(ev)):
            break
    
        if ev.type == sdl2.SDL_QUIT:
            sys.exit(0)
        elif ev.type == sdl2.SDL_KEYDOWN:
            k = ev.key.keysym.sym
            keys.add(k)
            if k == SDLK_q:
                sys.exit(0)
        elif ev.type == sdl2.SDL_KEYUP:
            k = ev.key.keysym.sym
            keys.discard(k)
        elif ev.type == sdl2.SDL_MOUSEBUTTONDOWN:
            print("mouse down:",ev.button.button,ev.button.x,ev.button.y)
        elif ev.type == sdl2.SDL_MOUSEBUTTONUP:
            print("mouse up:",ev.button.button,ev.button.x,ev.button.y)

    now = sdl2.SDL_GetTicks()
    elapsed = now-last
    last=now 

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    
    cam.draw(prog)

    w.draw(prog)

    sdl2.SDL_GL_SwapWindow(win)
