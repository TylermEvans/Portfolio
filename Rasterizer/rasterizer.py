import pygame
import time
import random
import math3d
#Initialization

pygame.init()
#Variables
screen=pygame.display.set_mode((800,600))
trans=math3d.translate(True,400,300,1)
scale=math3d.scale(True,50,50,50)
rotate=math3d.rotateX(True,-90)
rotate2=math3d.rotateY(True,180)
rotate3=math3d.rotate(True,180)
#Creates Polymeshes
sun=math3d.Polymesh("sun.obj","sun.mtl")
ship=math3d.Polymesh("ship.obj","ship.mtl")
ship2=math3d.Polymesh("ship.obj","ship.mtl")
saturn=math3d.Polymesh("saturn.obj","saturn.mtl")
saturn.children.append(ship2)
sun.children.append(saturn)
sun.children.append(ship)

#Polymesh lsit
polymesh=[]
polymesh.append(sun)
t=180
r=0
s=0
m=0
k=0
old_pos=[0,0]
game=True
#Game Loop
while game==True:
    #Keys and variable updates
    screen.fill((0,0,0))
    pygame.event.pump()
    key = pygame.key.get_pressed()
    [mx,my]= pygame.mouse.get_pos()
    mpos=[mx,my]
    lb=pygame.mouse.get_pressed()[0]
    offsetX=mpos[0]-old_pos[0]
    offsetY=mpos[1]-old_pos[1]
    old_pos=mpos
    r-=5
    s+=10
    m-=5
    k-=20

    #Key presses
    if key[pygame.K_ESCAPE]:
        game=False
    if lb==True:
        t=t+offsetX
        rotate2=math3d.rotateY(True,t)

    #Transformations
    transformation=scale*rotate*rotate2*trans
    sun.Mtransform=transformation
    ship.Mtransform=(math3d.scale(True,0.2,0.2,0.2)*math3d.rotateX(True,90)*math3d.translate(True,3,0,0)*math3d.rotateY(True,r))
    ship2.Mtransform=(math3d.scale(True,0.1,0.1,0.1)*math3d.rotateX(True,90)*math3d.translate(True,2.3,0,0)*math3d.rotateY(True,k))
    saturn.Mtransform=(math3d.scale(True,0.7,0.7,0.7)*math3d.rotateX(True,s)*math3d.translate(True,-4,0,0)*math3d.rotateY(True,m))
    polymesh[0].render(screen,math3d.MatrixN(4,4,(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1)))


    #Quit
    pygame.display.flip()
pygame.quit()

