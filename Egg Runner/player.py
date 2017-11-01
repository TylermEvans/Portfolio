import math
import collide
import dicttool
import pygame
import random
import time
t=time.time()
colX=0
rowY=0
key=0
class Player(object):
    def __init__(self,start_x,start_y):
        self.spawnx=start_x
        self.spawny=start_y
        self.x=start_x
        self.y=start_y
        self.lives=5
        self.score=0
        self.treasure=0
        self.gravity=5
        self.grav=True
        self.next_level=False
        self.game_over=False
        self.level=1
        self.brick=["brick.vine1","brick.vine2","brick.vine3","brick.vine4","rock.red1","rock.red2","rock.red3","rock.red4","brick.brown1","brick.brown2","brick.brown3","brick.brown4"]
        self.ladder=["ladder.top","ladder.mid","ladder.bot"]
        self.chain=["hchain.center","hchain.right","hchain.left"]
        self.chest="egg"
        self.steel=["steel.block1","steel.block2","steel.block3"]
        self.trap="trap.door"
        self.time_out=[]
        self.animetimer=time.time()
        self.walkingImg=[]
        self.walkingImg.append(pygame.image.load("danny.png"))
        self.walkingImg.append(pygame.image.load("dannywalkR1.png"))
        self.walkingImg.append(pygame.image.load("dannywalkR2.png"))
        self.walkingframe=0
        self.dir="R"
        self.moving=False
        self.animeupdate=0.05
        self.otherImg=[]
        self.otherImg.append(pygame.image.load("dannyDigR.png"))
        self.otherImg.append(pygame.image.load("dannyDigL.png"))
        self.climbImg=[]
        self.climbImg.append(pygame.image.load("dannyclimb1.png"))
        self.climbImg.append(pygame.image.load("dannyclimb2.png"))
        self.digL=False
        self.digR=False
        self.climb=False








    def move(self,map,ex,ey):
        elapsedtime=time.time()-self.animetimer
        if self.moving and elapsedtime>self.animeupdate:
            self.walkingframe+=1
            self.animetimer=time.time()
            if self.walkingframe>2:
                self.walkingframe=0




        pygame.event.pump()
        keysPressed = pygame.key.get_pressed()



        old_x=self.x#x key movement and bounding x
        old_y=self.y
        if keysPressed[pygame.K_a]:
            self.x-=2
            self.dir="L"
            self.moving=True
        elif keysPressed[pygame.K_d]:
            self.x+=2
            self.dir="R"
            self.moving=True
        else:
            self.moving=False

        if keysPressed[pygame.K_s]:
            self.y+=2

        if self.x>=785:
            self.x=785
        if self.x<15:
            self.x=15
        if self.y<=16:
            self.y=16
        if self.y>=785:
            self.y=785




        collision_set=map.getCollisionSetCircle(self.x,self.y,16)


        if len(collision_set)==0 and self.grav==True:
            self.y+=self.gravity




        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey in self.ladder and keysPressed[pygame.K_w]:
                    self.grav=False
                    self.x=collidetile.mapTileCenterX
                    self.y-=2




                if collidetile.mapEntryKey in self.ladder and keysPressed[pygame.K_s]:
                    self.grav=False
                    self.x=collidetile.mapTileCenterX
                    self.y+=2


        else:
            self.grav=True


        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile in self.chain and keysPressed[pygame.K_a]:
                    self.grav=False
                    self.x-=2
                if collidetile in self.chain and keysPressed[pygame.K_d]:
                    self.grav=False
                    self.x+=2
        else:
            self.grav=True


        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey==self.chest:
                    map.setTileMapEntry(collidetile.mapCol,collidetile.mapRow,None)
                    self.treasure-=1
                    self.score+=250

        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey=="trap.door":
                    map.setTileMapEntry(collidetile.mapCol,collidetile.mapRow,None)

        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey in self.brick and keysPressed[pygame.K_LEFT]:
                    self.digL=True
                    colX=collidetile.mapCol-1
                    rowY=collidetile.mapRow
                    t=time.time()
                    map.setTileMapEntry(collidetile.mapCol-1,collidetile.mapRow,None)
                    self.time_out.append((colX,rowY,t))
                else:
                    self.digL=False



        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey in self.brick and keysPressed[pygame.K_RIGHT]:
                    self.digR=True
                    colX=collidetile.mapCol+1
                    rowY=collidetile.mapRow
                    t=time.time()
                    map.setTileMapEntry(collidetile.mapCol+1,collidetile.mapRow,None)
                    self.time_out.append((colX,rowY,t))
                else:
                    self.digR=False





        if len(self.time_out)>0:
            for tile in self.time_out:
                (colX,rowY,t)=tile
                if t<time.time()-10:
                    map.setTileMapEntry(colX,rowY,self.brick[0])
                    self.time_out.remove(tile)
                    if self.x>colX*32 and self.x<colX*32+32 and self.y>rowY*32 and self.y<rowY*32+32:
                        self.lives-=1
                        self.x=self.spawnx
                        self.y=self.spawny

        if collide.collideCircles(self.x,self.y,16,ex,ey,16):
            self.lives-=1
            self.x=self.spawnx
            self.y=self.spawny

        if self.y!=old_y:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.steel:
                        self.y=old_y
                        break

        if self.x!=old_x:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.steel:
                        self.x=old_x
                        break

        if self.y!=old_y:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.brick:
                        self.y=old_y
                        break



        if self.x!=old_x:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.brick:
                        self.x=old_x
                        break



        if self.y<=30 and self.treasure==0:# next level statement
            self.next_level=True
        else:
            self.next_level=False

        if self.lives==0:
            self.game_over=True





    def render(self,screen):
        if self.moving==False:
            self.walkingframe=0
        currentFrame=self.walkingImg[self.walkingframe]
        if self.dir=="R":
            screen.blit(currentFrame,(self.x-16,self.y-16))
        else:
            screen.blit(pygame.transform.flip(currentFrame,True,False),(self.x-16,self.y-16))
        if self.digL==True:
            screen.blit(self.otherImg[1],(self.x-16,self.y-16))
        if self.digR==True:
            screen.blit(self.otherImg[0],(self.x-16,self.y-16))







