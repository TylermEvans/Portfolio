 #gameItems.py

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
shop = False
Town = False


def fontwrite(x,y,string,color = (0,0,0)):
    """Allows us to write text with font"""
    
    font_pygame = pygame.font.SysFont("Arial", 24)
    screen.blit(font_pygame.render(string,True,color), (x,y))

class Item(object):
    """standard for all items"""
    
    def __init__(self,name, attack, armor, classReq):
        self.name = name
        self.attack = attack
        self.resist = armor
        self.classReq  = classReq

class Inventory(object):
    """Allow's the player to have item's in their inventory"""
    
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        del(self.items[item.name])

class Potion(object):
    def __init__(self,name,effect,value):
        self.name = name
        self.effect = effect
        self.value = value
        pass




class Shop(object):
    def __init__(self, gold, Ranger, Magician, UselessBard, Mounty):
        #self.item = self.ShopInventory
        #self.items[item.name] = item
        
        self.shopOpen=False
        self.buy = False
        self.sell = False
        self.buy_item = False
        self.sell_item = False
        self.P_inv = Inventory()
        self.gold = gold
        self.ranger=Ranger
        self.magician=Magician
        self.bard=UselessBard
        self.mounty=Mounty
        
            
    def openShop(self,p1,p2,p3,p4):
        
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        x = 5
        y = 20
        pressing = False
        if keys[pygame.K_e]:
            pressing = True
            self.shopOpen = True
        while self.shopOpen == True:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            screen.fill((130,130,130))

            ####kidney's######
            
            pygame.draw.rect(screen, (255,255,255), (600,0,100,70),0)
            pygame.draw.rect(screen, (0,0,0), (600,0,100,70),3)
            fontwrite(610,10,"Kidneys:")
            fontwrite(610,35,str(self.gold))
            
            #########BUY SCREEN################
            
            pygame.draw.rect(screen, (255,255,255), (0,0,100,70),0)
            pygame.draw.rect(screen, (0,0,0), (0,0,100,70),3)
            fontwrite(30,10,"Buy")
            fontwrite(30,35,"Exit")
            if self.buy == False:
                pygame.draw.polygon(screen,(0,0,0),((x,y),(x,y+10),(x+5,y+5)),0)
            
           
            if keys[pygame.K_s] == False and keys[pygame.K_w] == False and keys[pygame.K_e] == False:
                pressing = False

            if keys[pygame.K_w] and pressing == False and self.buy == False and self.buy_item == False:
                """Goes up in the menu as long as it is not in the self.buy and self.buy_item == False"""
                
                pressing = True
                y-=25
                if y <= 20:
                    y=20
                    
            if keys[pygame.K_s] and pressing == False and self.buy == False and self.buy_item == False:
                """Goes down in the menu as long as it is not in the self.buy and self.buy_item == False"""
                
                pressing = True
                y+=25
                if y >= 45:
                    y=45
            
            if keys[pygame.K_e] and y ==20 and pressing == False and self.buy_item == False and self.buy == False:
                """Opens self.buy"""
                
                pressing = True
                self.buy=True

            if keys[pygame.K_e] and y ==45 and pressing == False and self.buy_item == False and self.buy == False:
                """Exit the shop"""
                
                pressing = True
                pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                fontwrite(150,550,"Come back when you get more Kidneys.")
                pygame.display.flip()
                time.sleep(2)
                self.shopOpen=False

            if keys[pygame.K_q] and pressing == False:
                """act's as a back button"""
                
                pressing = True
                if self.buy_item == False:
                    self.buy=False
                else:
                    self.buy_item = False
                if y >= 20:
                    y = 20
                        
                
            #############@@@@@@@@@@@@@@@@@@@@@@@@@@####
            #########@@@@@@@@@@@@self.buy@@@@@@@@@@@@######
            ##########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##
                
            
            if self.buy == True and keys[pygame.K_q] == False:
                
                pygame.draw.rect(screen, (255,255,255), (150,0,250,265),0)
                pygame.draw.rect(screen, (0,0,0), (150,0,250,265),3)
                fontwrite(170, 10,"Lute")
                fontwrite(170, 35, "Horse")
                fontwrite(170, 60, "Stove")
                fontwrite(170, 85, "Facial hair")
                fontwrite(170, 110, "Pointy Hat")
                fontwrite(170, 135, "Tuxedo")
                fontwrite(170, 160, "Corndog Armor")
                fontwrite(170, 185, "Apron")
                fontwrite(170, 210, "Exit to Menu")
                fontwrite(350, 10,"$200")
                fontwrite(350, 35, "$200")
                fontwrite(350, 60, "$200")
                fontwrite(350, 85, "$200")
                fontwrite(350, 110, "$300")
                fontwrite(350, 135, "$300")
                fontwrite(350, 160, "$300")
                fontwrite(350, 185, "$300")
                
                if self.buy == True and self.buy_item == False:
                    pygame.draw.polygon(screen,(0,0,0),((x+155,y),(x+155,y+10),(x+160,y+5)),0)
                
                if keys[pygame.K_w] and pressing == False:
                    pressing = True
                    y-=25
                    if y <= 20:
                        y=20
                if keys[pygame.K_s] and pressing == False and self.buy_item == False:
                    pressing = True
                    y+=25
                    if y >= 220:
                         y=220 

                ########BUY LUTE################
                   
            if self.buy == True and keys[pygame.K_e] and y ==20 and pressing == False:
                if self.gold >= 200:                
                    pressing = True
                    self.P_inv.add_item(Item("Lute",1,0,"Useless Bard"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Congratulations, your useless Bard gets a useless Lute.")
                    self.gold -= 200
                    p4.damage+=1
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)
                
                    
                ##########BUY HORSE###############
            
            if self.buy == True and keys[pygame.K_e] and y ==45 and pressing == False:
                if self.gold >= 200:
                    pressing = True
                    self.P_inv.add_item(Item("Horse",5,0,"Mounty"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Look at your horse, your horse is amazing.")
                    self.gold -= 200
                    p1.damage+=5
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)
                    
                ###########BUY STOVE############
            
            if self.buy == True and keys[pygame.K_e] and y ==70 and pressing == False:
                if self.gold >=  200:
                    pressing = True
                    self.P_inv.add_item(Item("Stove",7,0,"Ranger"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Stoves are for throwing not cooking.")
                    self.gold -= 200
                    p2.damage+=7
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)

           #########BUY FACIAL HAIR###############
                    
            if self.buy == True and keys[pygame.K_e] and y ==95 and pressing == False:
                if self.gold >= 200:
                    pressing = True
                    self.P_inv.add_item(Item("Facial Hair",3,0,"Magician"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Why grow a beard when you can buy one.")
                    self.gold -= 200
                    p3.damage+=8
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)

                #####BUY POINTY HAT##################
            
            if self.buy == True and keys[pygame.K_e] and y ==120 and pressing == False:
                if self.gold >= 300:
                    pressing = True
                    self.P_inv.add_item(Item("Pointy Hat",0,2,"Mounty"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Pokey")
                    self.gold-=300
                    p1.armor.resist+=2
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)
                    
            #############BUY TUXEDO##################
                
            if self.buy == True and keys[pygame.K_e] and y ==145 and pressing == False:
                if self.gold >= 300:
                    pressing = True
                    self.P_inv.add_item(Item("Tuxedo",0,3,"Magician"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Gotta look good to do good")
                    self.gold -= 300
                    p3.armor.resist+=2
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)
                    
             ##########BUY CORNDOG ARMOR###############   
            
            if self.buy == True and keys[pygame.K_e] and y ==170 and pressing == False:
                if self.gold >= 300:
                    pressing = True
                    self.P_inv.add_item(Item("Corndog Armor",0,1,"Useless Bard"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You really are useless aren't you...")
                    self.gold -= 300
                    p4.armor.resist-=2
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)
                    
            ############BUY APRON#####################    
            
            if self.buy == True and keys[pygame.K_e] and y ==195 and pressing == False:
                if self.gold >= 300:
                    pressing = True
                    self.P_inv.add_item(Item("Apron",0,2,"Ranger"))
                    print(self.P_inv)
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"Good for not getting things on your clothes. Like blood.")
                    self.gold -= 300
                    p2.armor.resist+=2
                    pygame.display.flip()
                    time.sleep(3)
                else:
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"You don't have enough kidneys.")
                    pygame.display.flip()
                    time.sleep(3)

            ######################EXIT SELF.BUY###########################

            if self.buy == True and keys[pygame.K_e] and y ==220 and pressing == False:
                    pressing = True
                    pygame.draw.rect(screen, (255,255,255), (125,525,550,755),0)
                    pygame.draw.rect(screen, (0,0,0), (125,525,550,75),3)
                    fontwrite(150,550,"If you have no money then you can get out!")
                    pygame.display.flip()
                    time.sleep(2)
                    self.buy = False
                    if y >= 20:
                        y = 20
            pygame.display.flip()
            ############EXIT SHOP##########################
                
'''Shop1 = Shop()
PlayerInventory = Inventory()
                         
while not done:

    if keys[pygame.K_ESCAPE]:
        done = True

    screen.fill((255,255,255))
        
        
    Shop1.openShop()      
    pygame.display.flip()

##################@@@@@@@@END@@@@@@@@@@@@#############
    
pygame.display.quit()'''
