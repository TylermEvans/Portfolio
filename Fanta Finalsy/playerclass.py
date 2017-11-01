import random
import pygame
import time


class player(object):
    def __init__(self,start_x,start_y):
        self.x=start_x
        self.y=start_y
        self.level=1
        self.xp=0
        self.nextlevel=50
        self.oldlevel=50
        self.maxhp=100
        self.hp=self.maxhp
        self.hplevelup=10
        self.maxmp=50
        self.mp=self.maxmp
        self.mplevelup=5
        self.damage=10
        self.damagelevelup=2
        self.skillset=[]
        self.alive=True
        self.goalX=self.x
        self.goalY=self.y
        self.speed=1
        self.collision=["Wall","Wall2","Water","Water2","Water3","MTN","BWall","DBWall","Statue","Trash"]
        self.dungeon="Dungeon"
        self.town="Town"
        self.steps=0
        self.freg=0
        self.pressing=False
        self.animTimer = time.time()
        self.walkAnimImages = []
        self.walkAnimImages.append(pygame.image.load("danny.png"))
        self.walkAnimImages.append(pygame.image.load("dannywalkR1.png"))
        self.walkAnimImages.append(pygame.image.load("dannywalkR2.png"))
        self.walkAnimFrame = 0
        self.direction = "R"
        self.isMoving = False
        self.animUpdatePeriod=0.05
        self.level=1
        self.xp=0
        self.nextlevel=50
        self.oldlevel=50
        self.maxhp=100
        self.hp=self.maxhp
        self.hplevelup=10
        self.maxmp=50
        self.mp=self.maxmp
        self.mplevelup=5
        self.damage=10
        self.damagelevelup=2
        self.skillset=[]
        self.alive=True
        self.turn=False
        self.attacking=False
        self.weapon="None"
        self.armor="None"
    def leveling(self):
        if self.xp>=self.nextlevel:
            self.oldlevel=self.nextlevel
            self.nextlevel=self.oldlevel+50*(self.level-1)
            self.level+=1
            self.maxhp+=self.hplevelup
            self.maxmp+=self.mplevelup
            self.damage+=self.damagelevelup
    def move(self,map,pressing,shop,p1,p2,p3,p4):
        elapsedTime = time.time() - self.animTimer
        if self.isMoving and elapsedTime > self.animUpdatePeriod:
            self.walkAnimFrame += 1
            self.animTimer = time.time()
            if self.walkAnimFrame > 2:
                self.walkAnimFrame = 0

        pygame.event.pump()
        key = pygame.key.get_pressed()
        old_x=self.x
        old_y=self.y
        if self.x<self.goalX:
            self.x+=self.speed

        if self.x>self.goalX:
            self.x-=self.speed

        if self.y<self.goalY:
            self.y+=self.speed

        if self.y>self.goalY:
            self.y-=self.speed

        if self.pressing==False:

            if key[pygame.K_a]:
                self.pressing=True
                self.goalX =(self.x//32)*32-16
                self.steps+=2
                self.direction = "L"
                self.isMoving = True
            elif key[pygame.K_d]:
                self.pressing=True
                self.goalX = (self.x//32)*32+48
                self.steps+=2
                self.direction = "R"
                self.isMoving = True
            elif key[pygame.K_w]:
                self.pressing=True
                self.goalY =(self.y//32)*32-16
                self.steps+=2
            elif key[pygame.K_s]:
                    self.pressing=True
                    self.goalY = (self.y//32)*32+48
                    self.steps+=2
            else:
                self.isMoving=False
        self.freq=1800
        collision_set=map.getCollisionSetCircle(self.x,self.y,32)
        if len(collision_set)>0:
            for collide_tile in collision_set:
                if collide_tile.mapEntryKey=="Trash":
                    shop.openShop(p1,p2,p3,p4)










        if old_x!=self.x:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collide_tile in collision_set:
                    if collide_tile.mapEntryKey in self.collision:
                        self.x=old_x
                        break

        if old_y!=self.y:
            collision_set=map.getCollisionSetCircle(self.x,self.y,15)
            if len(collision_set)>0:
                for collide_tile in collision_set:
                    if collide_tile.mapEntryKey in self.collision:
                        self.y=old_y
                        break

    def render(self,screen):
        #pygame.draw.circle(screen,(r,g,b),(int(self.x),int(self.y)),16,0)
        if self.isMoving == False:
            self.walkAnimFrame=0   # idle state
        curFrameSurf = self.walkAnimImages[self.walkAnimFrame]
        if self.direction == "R":
            screen.blit(curFrameSurf,(self.x-16,self.y-16))
        else:
            screen.blit(pygame.transform.flip(curFrameSurf,True,False),(self.x-16,self.y-16))

class mounty(player):
    def modify(self,weapon,armor,*potions):
        self.maxhp+=50
        self.maxmp-=20
        self.hplevelup+=5
        self.damage+=5
        self.mplevelup-=2
        self.damagelevelup-=1
        self.hp=self.maxhp
        self.mp=self.maxmp
        self.char="Mounty"
        self.weapon=weapon
        self.armor=armor
        self.items=[]
        for i in potions:
            self.items.append(i)
class bard(player):
    def modify(self,weapon,armor,*potions):
        self.maxhp-=90
        self.maxmp-=45
        self.hplevelup-=9
        self.damage-=9
        self.mplevelup-=4
        self.damagelevelup+=5
        self.hp=self.maxhp
        self.mp=self.maxmp
        self.weapon=weapon
        self.armor=armor
        self.char="Useless Bard"
        self.items=[]
        for i in potions:
            self.items.append(i)
class ranger(player):
    def modify(self,weapon,armor,*potions):
        self.maxmp-=10
        self.hplevelup+=2
        self.damage+=2
        self.mplevelup-=1
        self.damagelevelup
        self.hp=self.maxhp
        self.mp=self.maxmp
        self.weapon=weapon
        self.armor=armor
        self.char="Ranger"
        self.items=[]
        for i in potions:
            self.items.append(i)
class magician(player):
    def modify(self,weapon,armor,*potions):
        self.maxhp-=50
        self.maxmp+=40
        self.hplevelup-=5
        self.damage-=5
        self.mplevelup+=5
        self.damagelevelup-=1
        self.hp=self.maxhp
        self.mp=self.maxmp
        self.weapon=weapon
        self.armor=armor
        self.char="Magican"
        self.items=[]
        for i in potions:
            self.items.append(i)


