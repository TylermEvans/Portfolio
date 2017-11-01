import pygame
import random
class mainmap(object):
    def __init__(self,width,height,screen):
        self.row=width
        self.col=height
        self.screen=screen
        self.maplist=[]
class map(object):
    def __init__(self,row,col,width,height,screen):
        self.row=row
        self.col=col
        self.w=width
        self.h=height
        self.maptiles=[]
        self.screen=screen
    def render(self):
        screenw=self.screen.get_width()
        screenh=self.screen.get_height()
        width=screenw/self.w
        height=screenh/self.h
        for i in range(0,len(self.maptiles)):
            j=self.maptiles[i]
            pygame.draw.rect(self.screen,j.info,(int(j.x)*width,int(j.y)*height,width,height),0)
            
            
        
class tile(object):
    def __init__(self,x,y,info):
        self.x=x
        self.y=y
        self.info=info

while __name__=="__main__":
    pygame.init()
    mx=10
    my=10
    screen=pygame.display.set_mode((800,600),pygame.SWSURFACE,24) 
    map1=mainmap(5,5,screen)
    for i in range(0,map1.row):
        for j in range(0,map1.col):
            map1.maplist.append(map(j,i,mx,my,map1.screen))
    for i in range(0,len(map1.maplist)):
        j=map1.maplist[i]
        for x in range(0,j.w):
            for y in range(0,j.h):
                j.maptiles.append(tile(x,y,(random.randint(0,255),random.randint(0,255),random.randint(0,255))))

    game=True
    row=0
    col=0
    pressing=False
    while game==True:
        pygame.event.pump()
        press=pygame.key.get_pressed()
        for i in range(0,len(map1.maplist)):
            q=map1.maplist[i]
            if q.row==row and q.col==col:
                q.render()
        if press[pygame.K_ESCAPE]==True:
            game=False
        if press[pygame.K_d]==True and pressing==False:
            pressing=True
            row+=1
            if row>map1.row:
                row=0
        if press[pygame.K_s]==True and pressing==False:
            pressing=True
            col+=1
            if col>map1.col:
                col=0
        if press[pygame.K_a]==True and pressing==False:
            pressing=True
            row-=1
            if row<0:
                row=map1.row
        if press[pygame.K_w]==True and pressing==False:
            pressing=True
            col-=1
            if col<0:
                col=map1.col
        if press[pygame.K_w]==False and press[pygame.K_a]==False and press[pygame.K_s]==False and press[pygame.K_d]==False:
            pressing=False
        
        pygame.display.flip()
    
    
        
                        
