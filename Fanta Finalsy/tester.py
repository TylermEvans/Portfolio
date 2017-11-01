import pygame
import time
import random
import dicttool
import combattest
import playerclass
import GameItems



class Sound(object):
    def __init__(self,filename):
        pygame.mixer.init()
        self.sound=pygame.mixer.Sound(filename)



class Town(object):
    def __init__(self,map):
        self.col=1
        self.row=2
        self.map=map
        self.list=["1,1T.txt","1,2BM.txt","2,1T.txt","2,2DD.txt"]
        self.enter=False
        self.exit=False
        self.collide=["DBWall"]
    def render(self,player,world):

        collision_set=self.map.getCollisionSetCircle(player.x,player.y,15)
        if len(collision_set)>0:
            for collide_tile in collision_set:
                if collide_tile.mapEntryKey=="Town":
                    self.enter=True


        if self.enter==True and self.col==1 and self.row==2:
            self.map.loadMap(self.list[2])


        if player.y>599 and self.enter==True and self.row==2:
            self.exit=True
            player.y=500
        else:
            self.exit=False

        if self.exit==True:
            self.enter=False
            self.map.loadMap(world.collist[1])

        if self.enter==True:
            if player.y<0:
                self.row-=1
                player.y=596
            if player.y>599:
                self.row+=1
                player.y=4
            if player.x>799:
                self.col+=1
                player.x=5
            if player.x<0:
                self.col-=1
                player.x=796


            if self.row==1 and self.col==1:
                self.map.loadMap(self.list[0])

            if self.row==2 and self.col==2:
                self.map.loadMap(self.list[1])

            if self.row==1 and self.col==2:
                self.map.loadMap(self.list[3])





class World(object):
    def __init__(self,map):
        self.col=1
        self.row=1
        self.map=map
        self.collist=["1,1.txt","2,1.txt","3,1.txt"]
        self.rowlist=["1,2.txt","1,3.txt"]
        self.colrowlist=["2,2.txt","2,3.txt","2,4.txt","3,4.txt","3,3.txt","3,2.txt"]

    def move(self,player,town):
        if town.enter==False:
            if player.x>799:
                player.x=2
                self.col+=1

            if player.x<0:
                player.x=797
                self.col-=1

            if player.y>599:
                player.y=2
                self.row+=1

            if player.y<0:
                player.y=597
                self.row-=1

            if self.col>3 and self.row==1:
                self.col=1
                self.row=1

            if self.col<1 and self.row==1:
                self.col=3
                self.row=1

            if self.col>3 and self.row==2:
                self.col=1
                self.row=2

            if self.col<1 and self.row==2:
                self.col=3
                self.row=2

            if self.col>3 and self.row==3:
                self.col=1
                self.row=3

            if self.col<1 and self.row==3:
                self.col=3
                self.row=3

            if self.col>3 and self.row==4:
                self.col=1
                self.row=4

            if self.col<1 and self.row==4:
                self.col=3
                self.row=4

            if self.col==1 and self.row>4:
                self.col=1
                self.row=1

            if self.col==1 and self.row<1:
                self.col=1
                self.row=4

            if self.col==2 and self.row>4:
                self.col=2
                self.row=1

            if self.col==2 and self.row<1:
                self.col=2
                self.row=4

            if self.col==3 and self.row>4:
                self.col=3
                self.row=1

            if self.col==3 and self.row<1:
                self.col=3
                self.row=4








    def render(self):
        if self.col==1 and self.row==1:
            self.map.loadMap(self.collist[0])

        if self.col==2 and self.row==1:
            self.map.loadMap(self.collist[1])

        if self.col==3 and self.row==1:
            self.map.loadMap(self.collist[2])

        if self.col==1 and self.row==2:
            self.map.loadMap(self.colrowlist[4])

        if self.col==1 and self.row==3:
            self.map.loadMap(self.rowlist[1])

        if self.col==2 and self.row==2:
            self.map.loadMap(self.colrowlist[0])
        if self.col==3 and self.row==2:
            self.map.loadMap(self.colrowlist[1])

        if self.col==2 and self.row==3:
            self.map.loadMap(self.colrowlist[2])

        if self.col==3 and self.row==3:
            self.map.loadMap(self.colrowlist[3])

        if self.col==2 and self.row==4:
            self.map.loadMap(self.colrowlist[4])

        if self.col==3 and self.row==4:
            self.map.loadMap(self.colrowlist[5])





pygame.init()
screen=pygame.display.set_mode((800,600))
def fontwrite(x,y,string,color=(0,0,0)):
    font_Pygame=pygame.font.SysFont("Arial",24)
    screen.blit(font_Pygame.render(string,True,color),(x,y))
world=World(dicttool.TileMap(screen))
world.map.loadTileTypes("map1tiles.txt")
world.map.loadMap("1,1.txt")
town=Town(world.map)
fight1=combattest.fight(screen)
shield=combattest.armor(1)
dagger=combattest.weapon(1)
p1=playerclass.mounty(400,400)
p1.modify(dagger,shield,combattest.potion("HP",10),combattest.potion("RES",1))
p2=playerclass.ranger(400,400)
p2.modify(dagger,shield,combattest.potion("HPMP",20))
p3=playerclass.magician(400,400)
p3.modify(dagger,shield,combattest.potion("MP",10))
p4=playerclass.bard(400,400)
p4.modify(dagger,shield,combattest.potion("RES",1))
start_x=30
start_y=118
game=False
startscreen=True
press=True
gold=1000
shop=GameItems.Shop(gold,p1,p2,p3,p4)
bag1=combattest.bag()
location=1


if startscreen==True:
    sound=Sound("beep.wav")
    pygame.mixer.music.load("Skeltal.mp3")
    pygame.mixer.music.play()
while startscreen==True:



    screen.fill((0,0,0))
    pygame.event.pump()
    key=pygame.key.get_pressed()
    if key[pygame.K_s]:
        sound.sound.play()
        start_y=start_y+50


    if key[pygame.K_w]:
        sound.sound.play()
        start_y=start_y-50
    if start_y<118:
        start_y=118

    if start_y>168:
        start_y=168


    fontObj = pygame.font.SysFont("Arial", 20)
    
    img=pygame.image.load("fanta.png")
    new_img=pygame.transform.scale(img,(800,600))
    screen.blit(new_img,(1,1))
    screen.blit(fontObj.render(" Finalsy",False,(0,0,0)),(400,400))
    screen.blit(fontObj.render("New Game",False,(0,0,0)),(50,100))
    screen.blit(fontObj.render("Exit",False,(0,0,0)),(50,150))
    pygame.draw.circle(screen,(255,0,0),(start_x,start_y),10,0)


    if key[pygame.K_RETURN] and start_y==118:
        screen.fill((0,0,0))
        screen.blit(fontObj.render("Your New Adventure Awaits!",False,(255,255,255)),(300,300))
        pygame.display.flip()
        time.sleep(5)
        game=True
        startscreen=False
        pygame.mixer.music.stop()
    if key[pygame.K_RETURN] and start_y==168:
        break







    pygame.display.flip()


while game==True:
    screen.fill((0,0,0))
    pygame.event.pump()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        game=False




    if p1.pressing==True and key[pygame.K_w]==False and key[pygame.K_a]==False and key[pygame.K_s]==False and key[pygame.K_d]==False:
        p1.pressing=False
        fight1.encounter(p1.steps,p1.freq)








    p1.move(world.map,p1.pressing,shop,p1,p2,p3,p4)
    world.move(p1,town)
    world.render()
    town.render(p1,world)
    world.map.renderMap()
    town.map.renderMap()
    p1.render(screen)
    pygame.display.flip()
    if world.col==1 and world.row==3:
        location=2
    else:
        location=1
    if fight1.fighting==True and fight1.dead==False:
        pygame.mixer.music.load("battle.mp3")
        pygame.mixer.music.play()
        screen.fill((255,255,255))
        pygame.display.flip()
        fight1.initencounter(p1,p2,p3,p4,4,6,location)
        enemystr="ENEMY ENCOUNTER\n"+str(fight1.encountersize)+"\n"
        for i in range(len(fight1.enemylist)):
            i=fight1.enemylist[i]
            i.modify()
            enemystr+=i.enemyname+" "
        fontwrite(20,500,"Enemies encountered! Murder them! Kill kill kill!")
        fight1.update(True)
        fight1.update(True)
        p1.turn=True
        steps=0
        itemisused=False
    else:
        pygame.mixer.music.stop()




    while fight1.fighting==True and fight1.dead==False:
        pygame.event.pump()
        press=pygame.key.get_pressed()
        screen.fill((255,255,255))
        for i in fight1.playerlist:
             x=0
             y=0
             fight1.currentplayertarget="None"
             selecting=False
             itemisused=False
             while i.turn==True:
                increase=False
                decrease=False
                pygame.event.pump()
                press=pygame.key.get_pressed()
                screen.fill((255,255,255))
                if press[pygame.K_a]==False and press[pygame.K_d]==False and press[pygame.K_e]==False and press[pygame.K_q]==False:
                    pressing=False
                if press[pygame.K_a]==True and pressing==False:
                    pressing=True
                    if selecting==False:

                        x-=200
                    else:
                        y-=1
                        if y<0:
                            y=0
                        decrease=True
                        increase=False
                    if x<0:
                        x=0
                if press[pygame.K_d]==True and pressing==False:
                    if selecting==False:
                        x+=200
                    else:
                        y+=1
                        if y>len(fight1.enemylist)-1:
                            y=len(fight1.enemylist)-1
                        increase=True
                        decrease=False
                    pressing=True
                    if x>600:
                        x=600
                if press[pygame.K_e]==True and pressing==False:
                    pressing=True
                    if fight1.menuopen==True:
                        itemisused=True

                    if selecting==True:
                        i.attacking=True
                    if selecting==False and fight1.menuopen==False:
                        if x==0:
                            selecting=True
                        if x==200:
                            pass
                        if x==400:
                            fight1.menuopen=True

                if press[pygame.K_q]==True and pressing==False:
                    pressing=True
                    if selecting==True:
                        selecting=False
                    if fight1.menuopen==True:
                        fight1.menuopen=False
                while fight1.enemylist[y].alive==False:
                    if y==0:
                        increase=True
                    if y==len(fight1.enemylist)-1:
                        decrease=True
                    if decrease==True:
                        y-=1
                        if y<0:
                            y=0
                            decrease=False
                            increase=True
                    if increase==True:
                        y+=1
                        if y>len(fight1.enemylist)-1:
                            y=len(fight1.enemyist)-1
                            decrease=True
                            increase=False
                fight1.playerfight(i,x,y,selecting,bag1)
                fight1.itemuse(i,x,y,itemisused)
                pygame.display.flip()
        if fight1.fighting==True:
            fight1.enemyattack()
        fight1.update(False)



pygame.display.quit()
