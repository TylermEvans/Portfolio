import pygame
import time
import random



class Enemy(object):
    def __init__(self,start_x,start_y,timeout):
        self.x=start_x
        self.y=start_y
        self.gravity=2
        self.grav=True
        self.brick=["brick.vine1","brick.vine2","brick.vine3","brick.vine4","rock.red1","rock.red2","rock.red3","rock.red4","brick.brown1","brick.brown2","brick.brown3","brick.brown4"]
        self.ladder=["ladder.top","ladder.mid","ladder.bot"]
        self.chain=["hchain.center","hchain.right","hchain.left"]
        self.chest="chest.type1"
        self.steel=["steel.block1","steel.block2","steel.block3"]
        self.direction=-.9
        self.time_out=timeout


    def move(self,px,py,map):

        old_x=self.x#x key movement and bounding x
        old_y=self.y

        collision_set=map.getCollisionSetCircle(self.x,self.y,14)

        if self.x>785:
            self.x=785
        if self.x<15:
            self.x=15


        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey in self.ladder and py > self.y:
                    self.grav=False
                    self.y+=1



        if len(collision_set)>0:
            for collidetile in collision_set:
                if collidetile.mapEntryKey in self.ladder and py < self.y:
                    self.grav = False
                    self.x=collidetile.mapTileCenterX
                    self.y-=1



        if len(collision_set)==0:#gravity
            self.y+=3






        if self.y!=old_y:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.brick:
                        self.y=old_y
                        break

        if self.y!=old_y:# ground collision
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.steel:
                        self.y=old_y
                        break




        if self.y==old_y:
            self.x+=self.direction


        if self.x!=old_x:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.steel:
                        self.x=old_x
                        break




        if self.x!=old_x:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collidetile in collision_set:
                    if collidetile.mapEntryKey in self.brick:
                        self.x=old_x
                        break




        if int(py)!=int(self.y):
            if old_x>self.x-.1 and old_x<self.x+.1:
                self.direction*=-1

        if int(self.y)<int(py)+5 and int(self.y)>int(py)-5:
            if px>self.x:
                self.direction=.9
            else:
                self.direction=-.9

        if len(self.time_out)>0:
            for tile in self.time_out:
                (colX,rowY,t)=tile
                if t<time.time()-10:
                    if self.x>colX*32 and self.x<colX*32+32 and self.y>rowY*32 and self.y<rowY*32+32:
                        self.x=random.randint(50,740)
                        self.y=0












    def render(self,screen):
        alien=pygame.image.load("alien.png")
        screen.blit(alien,(self.x-16,self.y-16))
