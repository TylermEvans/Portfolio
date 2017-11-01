import sys
from ctypes import *
import time
import pysdl2.sdl2 as sdl2
from pysdl2.sdl2.keycode import *
from glfuncs import *
from glconstants import *
import Square
from Program import Program 
import math3d
import Bullet
import Hexagon

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
    
    
glClearColor(0.0,0.0,0.0,1.0)
keys=set()
r=0
worldMatrix = math3d.scaling([0.25,0.25,1])
last=sdl2.SDL_GetTicks()
bullet_list = []
sqaure_x = 0.001
sqaure_y = 0.001
fire = False
ev=sdl2.SDL_Event()
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
            if k == SDLK_SPACE:
                fire = True
                bullet_list.append(Bullet.Bullet(0,0,worldMatrix))
        elif ev.type == sdl2.SDL_KEYUP:
            k = ev.key.keysym.sym
            keys.discard(k)
        elif ev.type == sdl2.SDL_MOUSEBUTTONDOWN:
            print("mouse down:",ev.button.button,ev.button.x,ev.button.y)
        elif ev.type == sdl2.SDL_MOUSEBUTTONUP:
            print("mouse up:",ev.button.button,ev.button.x,ev.button.y)
        #elif ev.type == sdl2.SDL_MOUSEMOTION:
            #print("mouse move:",ev.motion.x,ev.motion.y)

    now = sdl2.SDL_GetTicks()
    elapsed = now-last
    last=now 


    if SDLK_d in keys:
        worldMatrix = worldMatrix * math3d.translation([elapsed*0.001,0,0])
    if SDLK_a in keys:
        worldMatrix = worldMatrix * math3d.translation([-elapsed*0.001,0,0])
    if SDLK_w in keys:
        worldMatrix = worldMatrix * math3d.translation([0,elapsed*0.001,0])
    if SDLK_s in keys:
        worldMatrix = worldMatrix * math3d.translation([0,-elapsed*0.001,0])
    for bullet in bullet_list:
        bullet.update(elapsed)
        print(bullet.x)
    for bullet in bullet_list:
        if bullet.x >= 3:
            bullet_list.remove(bullet)



    glClear(GL_COLOR_BUFFER_BIT)
    prog.setUniform("worldMatrix",worldMatrix)
    square.draw(prog)
    for bullet in bullet_list:
        bullet.draw(prog)
    sdl2.SDL_GL_SwapWindow(win)
