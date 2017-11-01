import pygame
class enemy(object):
    def __init__(self,num):
        self.hp=0
        self.mp=0
        self.damage=0
        self.size=0
        self.skills=[]
        self.image=None
        self.alive=True
        self.num=num
    def render(self,screen,position):
        self.image=pygame.image.load(self.imagename)
        ix=self.image.get_width()
        iy=self.image.get_height()
        self.image=pygame.transform.scale(self.image,(int(ix*(self.size*.8)),int(iy*self.size*.9)))
        screen.blit(self.image,position)
class fistsnake(enemy):
    def modify(self):
        self.hp+=25
        self.damage+=5
        self.size+=2
        self.enemyname="FISTSNAKE"+str(self.num)
        self.gold=10
        self.xp=20
        self.imagename="fist snake.png"
class snakefist(enemy):
    def modify(self):
        self.hp+=60
        self.damage+=10
        self.size+=4
        self.enemyname="SNAKEFIST"+str(self.num)
        self.gold=50
        self.imagename="snakefists.png"
        self.xp=50
class fistspider(enemy):
    def modify(self):
        self.hp+=120
        self.damage+=15
        self.size+=5
        self.enemyname="FISTSPIDER"+str(self.num)
        self.gold=400
        self.imagename="spiderfist.png"
        self.xp=200
class iratepigeon(enemy):
    def modify(self):
        self.hp+=40
        self.damage+=9
        self.size+=2
        self.enemyname="IRATEPIGEON"+str(self.num)
        self.imagename="iratepigeon.png"
        self.gold=60
        self.xp=60
class wheelchair(enemy):
    def modify(self):
        self.hp+=150
        self.damage+=14
        self.size+=4
        self.enemyname="WHEELCHAIR"+str(self.num)
        self.imagename="wheelchair.png"
        self.gold=300
        self.xp=100
class ireland(enemy):
    def modify(self):
        self.hp+=1000
        self.damage+=50
        self.size+=5
        self.enemyname="IRELAND"+str(self.num)
        self.imagename="ireland.png"
        self.xp=2000
        self.gold=2000
