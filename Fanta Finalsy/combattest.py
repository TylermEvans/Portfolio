import pygame
import enemy
import playerclass
import random
import time
#name1=input("Name of your Mounty:")
#name2=input("Name of your Ranger:")
#name3=input("Name of your Magician:")
#name4=input("Name of the useless bard:")
def fontwrite(screen,x,y,string,color=(0,0,0)):
    font_Pygame=pygame.font.SysFont("Arial",24)
    screen.blit(font_Pygame.render(string,True,color),(x,y))
class weapon(object):
    def __init__(self,damage):
        self.attack=damage
class armor(object):
    def __init__(self,resist):
        self.resist=resist
class potion(object):
    def __init__(self,effect,heal):
        self.effect=effect
        self.heal=heal
class bag(object):
    def __init__(self):
        self.gold=0
def addenemy(size,location,letter):
    if location==1:
        if size==1:
            return(enemy.fistsnake(letter))
        if size==2:
            return(enemy.snakefist(letter))
        if size==3:
            return(enemy.fistspider(letter))
    if location==2:
        if size==1:
            return(enemy.iratepigeon(letter))
        if size==2:
            return(enemy.wheelchair(letter))
        if size==3:
            return(enemy.ireland(letter))
    if location==3:
        if size==1:
            return(enemy.brick(letter))
        if size==2:
            return(enemy.trump(letter))
        if size==3:
            return(enemy.koolaid(letter))
        
class fight(object):
    def __init__(self,screen):
        self.fighting=False
        self.wonfight=False
        self.losefight=False
        self.screen=screen
        self.dead=False
    def encounter(self,chance,frequency):
        if chance<1000:
            fightnum=random.randint(chance,2000)
        else:
            fightnum=2000
        if fightnum>frequency:
            self.fighting=True
    def initencounter(self,p1,p2,p3,p4,minsize,maxsize,location):
        
        self.enemylist=[]
        self.playerlist=[]
        enemyencounter=random.randint(minsize,maxsize)
        self.enemyencountersize=enemyencounter
        a=1
        b=1
        c=1
        while enemyencounter>0:
            enemysize=random.randint(1,3)
            if enemyencounter==1:
                enemysize=1
            if enemyencounter==2:
                enemysize=random.randint(1,2)
            if enemysize==1:
                self.enemylist.append(addenemy(1,location,a))
                a+=1
            if enemysize==2:
                self.enemylist.append(addenemy(2,location,b))
                b+=1
            if enemysize==3:
                self.enemylist.append(addenemy(3,location,c))
                c+=1
            enemyencounter-=enemysize
            enemysize=0
        
        self.encountersize=len(self.enemylist)
        self.playerturn=True
        self.enemyturn=False
        self.won=False
        self.playerlist.append(p1)
        self.playerlist.append(p2)
        self.playerlist.append(p3)
        self.playerlist.append(p4)
        self.party=len(self.playerlist)
        self.menuopen=False
        self.currentplayertarget="None"
    def skilluse(self,p,x,y):
        pass
    def itemuse(self,p,x,y,itemisused):
        pygame.event.pump()
            
        healing=0
        mana=0
        double=0
        revive=0
        if self.menuopen==True:
            for i in p.items:
                if i.effect=="HP":
                    healing+=1
                if i.effect=="MP":
                    mana+=1
                if i.effect=="HPMP":
                    double+=1
                if i.effect=="RES":
                    revive+=1
            self.screen.fill((255,255,255))
            fontwrite(self.screen,20,500,"Rootbeer X "+str(healing))
            fontwrite(self.screen,220,500,"Orange X "+str(mana))
            fontwrite(self.screen,420,500,"Grape X "+str(double))
            fontwrite(self.screen,620,500,"Santa Hat X "+str(revive))
            pygame.draw.polygon(self.screen,(0,0,0),((x+10,500),(x+15,512),(x+10,524)),0)
            self.update(False)
        if itemisused==True:
            itemisused=False
            p.turn=False
            self.screen.fill((255,255,255))
            self.menuopen=False
            if x==0 and healing>0:
                p.hp+=50
                healing-=1
                if p.hp>p.maxhp:
                    p.hp=p.maxhp
                fontwrite(self.screen,20,500,str(p.char)+" consumes the Rootbeer Faygo for 50 health!")
                self.update(True)
            elif x==200 and mana>0:
                p.mp+=20
                mana-=1
                if p.mp>p.maxmp:
                    p.mp=p.maxmp
                fontwrite(self.screen,20,500,str(p.char)+" consumes the Orange Faygo for 20 mana!")
                self.update(True)
            elif x==400 and double>0:
                double-=1
                p.mp+=15
                if p.mp>p.maxmp:
                    p.mp=p.maxmp
                p.hp+=40
                if p.hp>p.maxhp:
                    p.hp=p.maxhp
                fontwrite(self.screen,20,500,str(p.char)+" consumes the Grape Faygo for 40 health and 15 mana!")
                self.update(True)
            elif x==600 and revive>0:
                revive-=1
                j=0
                for q in self.playerlist:
                    if q.alive==False:
                        j+=1
                if j!=0:
                    d=random.randint(0,3)
                    while self.playerlist[d].alive==True:
                        d=random.randint(0,3)
                    self.playerlist[d].hp=self.playerlist[d].maxhp
                    self.playerlist[d].alive=True
                    fontwrite(self.screen,20,500,str(p.char)+" puts the Santa hat on "+str(self.playerlist[d].char)+"!")
                    self.update(True)
                    self.screen.fill((255,255,255))
                    fontwrite(self.screen,20,500,str(self.playerlist[d].char)+" has been revived by the demonic powers of Santa!")
                    self.update(True)
                else:
                    fontwrite(self.screen,20,500,str(p.char)+" contemplates placing the Santa hat on an ally!")
                    self.update(True)
                    self.screen.fill((255,255,255))
                    fontwrite(self.screen,20,500,"But nobody is dead, so they instead place it on a nearby rock!")
                    self.update(True)
                    self.screen.fill((255,255,255))
                    fontwrite(self.screen,20,500,"The rock suddenly comes to life and gains sentience!")
                    self.update(True)
                    self.screen.fill((255,255,255))
                    fontwrite(self.screen,20,500,"Unfortunately, the rock immediately succumbs to an existential crisis!")
                    self.update(True)
                    self.screen.fill((255,255,255))
                    fontwrite(self.screen,20,500,"The rock leaves to go contemplate existence!")
                    self.update(True)
            else:
                fontwrite(self.screen,20,500,str(p.char)+" consumes the lack of object for no health or mana!")
                self.update(True)
                
            if self.playerlist.index(p)!=3 and self.encountersize>0:
                self.playerlist[self.playerlist.index(p)+1].turn=True
                    
            
    def playerfight(self,p,x,y,selecting,bag):
        if p.alive==False:
            p.turn=False
            if self.playerlist.index(p)!=3:
                self.playerlist[self.playerlist.index(p)+1].turn=True
        elif self.menuopen==False:
            self.screen.fill((255,255,255))
            fontwrite(self.screen,20,500,"FIGHT")
            fontwrite(self.screen,220,500,"SKILL")
            fontwrite(self.screen,420,500,"ITEM")
            fontwrite(self.screen,620,500,"RUN AWAY")
            pygame.draw.polygon(self.screen,(0,0,0),((x+10,500),(x+15,512),(x+10,524)),0)
            self.update(False)
        if selecting==True:
            self.currentplayertarget=int(y)
        else:
            self.currentplayertarget="None"
        if p.attacking==True and self.enemylist[y].alive==True:
            p.attacking=False
            p.turn=False
            if p.weapon==None:
                bonus=0
            else:
                bonus=p.weapon.attack
            self.enemylist[y].hp-=(p.damage+bonus)
            self.screen.fill((255,255,255))
            fontwrite(self.screen,20,500,self.enemylist[y].enemyname+" has taken "+str(p.damage+bonus)+" damage!")
            self.update(True)
            if self.enemylist[y].hp<=0:
                self.enemylist[y].alive=False
            if self.enemylist[y].alive==False:
                self.screen.fill((255,255,255))
                fontwrite(self.screen,20,500,self.enemylist[y].enemyname+" has perished")
                self.update(True)
                self.encountersize-=1
            if self.encountersize==0:
                self.winfight(bag)
            if self.playerlist.index(p)!=3 and self.encountersize>0:
                self.playerlist[self.playerlist.index(p)+1].turn=True
    def enemyattack(self):
        for e in self.enemylist:
            pygame.event.pump()
            if e.alive==False:
                continue
            target2=random.randint(0,len(self.playerlist)-1)
            i=self.playerlist[target2]
            while i.alive==False:
                if self.party<=0:
                    continue
                target2=random.randint(0,len(self.playerlist)-1)
                i=self.playerlist[target2]
            if i.armor==None:
                block=0
            else:
                block=i.armor.resist
            i.hp-=e.damage-block
            self.screen.fill((255,255,255))
            fontwrite(self.screen,20,500,str(e.enemyname)+" attacks "+str(i.char)+" for "+str(e.damage-block)+" damage!")
            if i.hp<0:
                i.hp=0
            self.update(True)
            if i.hp<=0:
                i.alive=False
                self.screen.fill((255,255,255))
                fontwrite(self.screen,20,500,str(i.char)+" has become rip in peace-d!")
                self.update(True)
                self.party-=1
                
            if self.party<=0:
                break
        if self.party>0:
            self.enemyturn=False
            self.playerlist[0].turn=True
        else:
            self.losefight=True
    def update(self,w):
        pygame.draw.rect(self.screen,(0,0,0),(0,450,799,150),3)
        pygame.draw.rect(self.screen,(0,0,0),(0,0,799,125),2)
        fontwrite(self.screen,10,10,"Mounty")
        fontwrite(self.screen,10,40,"HP: "+str(self.playerlist[0].hp)+"/"+str(self.playerlist[0].maxhp))
        fontwrite(self.screen,10,70,"MP: "+str(self.playerlist[0].mp)+"/"+str(self.playerlist[0].maxmp))
        fontwrite(self.screen,210,10,"Ranger")
        fontwrite(self.screen,210,40,"HP: "+str(self.playerlist[1].hp)+"/"+str(self.playerlist[1].maxhp))
        fontwrite(self.screen,210,70,"MP: "+str(self.playerlist[1].mp)+"/"+str(self.playerlist[1].maxmp))
        fontwrite(self.screen,410,10,"Magician")
        fontwrite(self.screen,410,40,"HP: "+str(self.playerlist[2].hp)+"/"+str(self.playerlist[2].maxhp))
        fontwrite(self.screen,410,70,"MP: "+str(self.playerlist[2].mp)+"/"+str(self.playerlist[2].maxmp))
        fontwrite(self.screen,610,10,"Useless Bard")
        fontwrite(self.screen,610,40,"HP: "+str(self.playerlist[3].hp)+"/"+str(self.playerlist[3].maxhp))
        fontwrite(self.screen,610,70,"MP: "+str(self.playerlist[3].mp)+"/"+str(self.playerlist[3].maxmp))
        for i in self.playerlist:
            if i.turn==True and i.alive==True:
                pygame.draw.polygon(self.screen,(0,0,0),((20+self.playerlist.index(i)*200,140),(40+self.playerlist.index(i)*200,120),(60+self.playerlist.index(i)*200,140)),0)
            if i.alive==False:
                fontwrite(self.screen,20+self.playerlist.index(i)*200,100,"RIP'D IN PEACE")
        q=800/(self.enemyencountersize)
        p=q
        b=0
        a=64
        for i in self.enemylist:
            if i.alive==True:
                #i.render(screen,(q*(1+b),425-i.size*64))
                i.render(self.screen,(a,425-64*i.size))
                if self.currentplayertarget!="None":
                    if self.enemylist[self.currentplayertarget]==i:
                        pygame.draw.polygon(self.screen,(0,0,0),((a+32*(i.size/2),440),(a+10+32*(i.size/2),425),(a+20+32*(i.size/2),440)),0)
                a+=64*i.size
            
        #if w==False:
            #fontwrite(20,500,"PRESS E TO FIGHT!")
        pygame.display.flip()
        if w==True:
            time.sleep(2)
    def winfight(self,bag):
        pygame.event.pump()
        self.screen.fill((255,255,255))
        fontwrite(self.screen,20,500,"Hooray, you are better at murder than your opponents!")
        self.update(True)
        for i in self.playerlist:
            pygame.event.pump()
            if i.alive==True:
                for j in self.enemylist:
                    i.xp+=j.xp
            lv=i.level
            i.leveling()
            self.screen.fill((255,255,255))
            if i.level>lv:
                fontwrite(self.screen,20,500,str(i.char)+" leveled up! Now they suck less!")
                self.update(True)
            self.screen.fill((255,255,255))
            if i.alive==True:
                fontwrite(self.screen,20,500,str(i.char)+" has become level "+str(i.level))
                i.turn=False
                self.update(True)
        goldvalue=0
        for j in self.enemylist:
            goldvalue+=j.gold
        self.screen.fill((255,255,255))
        fontwrite(self.screen,20,500,"You gained "+str(goldvalue)+" kidneys!")
        self.update(True)
        bag.gold+=goldvalue
        self.fighting=False
                        
"""fight1=fight()

shield=armor(1)
dagger=weapon(1)
p1=playerclass.mounty()
p1.modify(dagger,shield,potion("HP",10),potion("RES",1))
p2=playerclass.ranger()
p2.modify(dagger,shield,potion("HPMP",20))
p3=playerclass.magician()
p3.modify(dagger,shield,potion("MP",10))
p4=playerclass.bard()
p4.modify(dagger,shield,potion("RES",1))
pygame.init()
screen=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)
game=True
p1pos=[100,100]
p2pos=[100,100]
p3pos=[100,100]
p4pos=[100,100]
pressing=False
freq=0
steps=0
bag1=bag()
while game==True:
    screen.fill((0,0,0))
    pygame.event.pump()
    press=pygame.key.get_pressed()
    
    if pressing==True and press[pygame.K_w]==False and press[pygame.K_a]==False and press[pygame.K_s]==False and press[pygame.K_d]==False:
        pressing=False
        fight1.encounter(steps,freq)
    if pressing==False:
        if press[pygame.K_w]:
            pressing=True
            p4pos[1]=p3pos[1]
            p3pos[1]=p2pos[1]
            p2pos[1]=p1pos[1]
            p4pos[0]=p3pos[0]
            p3pos[0]=p2pos[0]
            p2pos[0]=p1pos[0]
            p1pos[1]-=50
            steps+=2
        if press[pygame.K_s]:
            pressing=True
            p4pos[1]=p3pos[1]
            p3pos[1]=p2pos[1]
            p2pos[1]=p1pos[1]
            p4pos[0]=p3pos[0]
            p3pos[0]=p2pos[0]
            p2pos[0]=p1pos[0]
            p1pos[1]+=50
            steps+=2
        if press[pygame.K_a]:
            pressing=True
            p4pos[0]=p3pos[0]
            p3pos[0]=p2pos[0]
            p2pos[0]=p1pos[0]
            p4pos[1]=p3pos[1]
            p3pos[1]=p2pos[1]
            p2pos[1]=p1pos[1]
            p1pos[0]-=50
            steps+=2
        if press[pygame.K_d]:
            pressing=True
            p4pos[0]=p3pos[0]
            p3pos[0]=p2pos[0]
            p2pos[0]=p1pos[0]
            p4pos[1]=p3pos[1]
            p3pos[1]=p2pos[1]
            p2pos[1]=p1pos[1]
            p1pos[0]+=50
            steps+=2
    freq=970
    
    pygame.draw.circle(screen,(255,255,255),(p4pos[0],p4pos[1]),20)
    pygame.draw.circle(screen,(0,0,255),(p3pos[0],p3pos[1]),20)
    pygame.draw.circle(screen,(0,255,0),(p2pos[0],p2pos[1]),20)
    pygame.draw.circle(screen,(255,0,0),(p1pos[0],p1pos[1]),20)
    pygame.display.flip()
    x=0
    if fight1.fighting==True:
        screen.fill((255,255,255))
        pygame.display.flip()
        fight1.initencounter(p1,p2,p3,p4,4,6,1)
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
    while fight1.fighting==True:
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
pygame.display.quit()"""

    
    
