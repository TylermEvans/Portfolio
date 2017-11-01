import sys
from ctypes import *
import time
import pysdl2.sdl2 as sdl2
from pysdl2.sdl2.keycode import *
from glfuncs import *
from glconstants import *
import Square
import Hexagon
from Program import Program 

def debugcallback(source,typ, id_,severity, length, message, obj ):
    print(message)

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


prog = Program("vs.txt","fs.txt")
prog.use()

square = Square.Square()
hexagon = Hexagon.Hexagon()
    
keyset = set()
glClearColor(0.2,0.4,0.6,1.0)

r=0
ev=sdl2.SDL_Event()
prev = sdl2.SDL_GetTicks()
while 1:
    while 1:
        if not sdl2.SDL_PollEvent(byref(ev)):
            break
    
        if ev.type == sdl2.SDL_QUIT:
            sys.exit(0)
        elif ev.type == sdl2.SDL_KEYDOWN:
            k = ev.key.keysym.sym
            print("key down:",k)
            if k == SDLK_q:
                sys.exit(0)
            elif k == SDLK_1:
                if k not in keyset:
                    keyset.add(k)
            elif k == SDLK_2:
                if k not in keyset:
                    keyset.add(k)
        elif ev.type == sdl2.SDL_KEYUP:
            k = ev.key.keysym.sym
            print("key up:",k)
            keyset.discard(k)
        elif ev.type == sdl2.SDL_MOUSEBUTTONDOWN:
            print("mouse down:",ev.button.button,ev.button.x,ev.button.y)
        elif ev.type == sdl2.SDL_MOUSEBUTTONUP:
            print("mouse up:",ev.button.button,ev.button.x,ev.button.y)
        #elif ev.type == sdl2.SDL_MOUSEMOTION:
            #print("mouse move:",ev.motion.x,ev.motion.y)
    





    glClearColor(r,0.4,0.6,1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    if SDLK_1 in keyset:
        square.draw(prog)
    if SDLK_2 in keyset:
        hexagon.draw(prog)

    

    sdl2.SDL_GL_SwapWindow(win)
