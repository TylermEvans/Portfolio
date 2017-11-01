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
import bullet
import Enemy

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








w = World.World("map.txt")

prog = Program("vs.txt","fs.txt")
prog.use()

cam = Camera()
cam.lookAt(vec3(4,0,-2),vec3(0,0,-1),vec3(0,1,0))


glClearColor(0.5,0.5,0.5,1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)

sdl2.SDL_SetRelativeMouseMode(True)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
glBlendEquation( GL_FUNC_ADD );




keys=set()
last=sdl2.SDL_GetTicks()
paused=False
ev=sdl2.SDL_Event()
angle=0
change = 0
TWOPI = 2.0*3.14159265358979323
elapsed = 0
b_list = []
e_list = []
e_list.append(Enemy.Enemy("robot.obj.mesh",math3d.vec3(5,-1,-6),1))
e_list.append(Enemy.Enemy("robot.obj.mesh",math3d.vec3(5,-1,-5),1))
e_list.append(Enemy.Enemy("robot.obj.mesh",math3d.vec3(8,-1,-7),1))
prog.setUniform("fogSetting",0)
fogStart = 0.5
fogEnd = 10
deltaFog = fogEnd - fogStart




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
                sdl2.SDL_Quit()
            if k == SDLK_0:
                prog.setUniform("fogSetting",0)
            if k == SDLK_1:
                prog.setUniform("fogSetting",1)
            if k == SDLK_2:
                prog.setUniform("fogSetting",2)
            if k == SDLK_3:
                prog.setUniform("fogSetting",3)
            
            
        elif ev.type == sdl2.SDL_KEYUP:
            k = ev.key.keysym.sym
            keys.discard(k)
        elif ev.type == sdl2.SDL_MOUSEMOTION:
            change = ev.motion.xrel
            cam.turn(-change*(0.001*elapsed))
        elif ev.type == sdl2.SDL_MOUSEBUTTONDOWN:
            b_list.append(bullet.Bullet(cam.eye,cam.U,cam.V,1))
                


    now = sdl2.SDL_GetTicks()
    elapsed = now-last
    last=now

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )


    if SDLK_w in keys:
        cam.walk(0.01*elapsed)
    if SDLK_d in keys:
        cam.strafe((0.01*elapsed),0,0)
    if SDLK_a in keys:
        cam.strafe((-0.01*elapsed),0,0)
    if SDLK_s in keys:
        cam.walk(-0.01*elapsed)
    for b in b_list:
        b.update(elapsed)

    for b in b_list:
        for e in e_list:
            vec = e.pos.xyz-b.pos.xyz
            distance = math3d.dot(vec,vec)
            if distance<(e.radius+b.radius)**2:
                e.alpha-=0.1

    for e in e_list:
        if e.alpha==0:
            e_list.remove(e)
    for b in b_list:
        if b.life<=0:
            b_list.remove(b)
    
    
    
    
    



    cam.draw(prog)
    
    
    prog.setUniform("light.position", vec3(cam.eye.x,cam.eye.y,cam.eye.z))
    prog.setUniform("light.color", vec3(1,1,1) )
    prog.setUniform("eyePos",vec3(cam.eye.x,cam.eye.y,cam.eye.z) )
    prog.setUniform("fogColor",vec4(0.5,0.5,0.5,1))
    prog.setUniform("fogStart", fogStart)
    prog.setUniform("deltaFog", deltaFog)
    prog.setUniform("density", 1)









    w.draw(prog)
   
    for e in e_list:
        e.draw(prog)
    for b in b_list:
        b.draw(prog)

    sdl2.SDL_GL_SwapWindow(win)
