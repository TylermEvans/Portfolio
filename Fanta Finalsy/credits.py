#In game menu
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800,600))


class Credits(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pineapples = False

    def fontWrite(self,x,y,string,color=(255,255,255)):
        font_Pygame = pygame.font.SysFont("Arial",24)
        screen.blit(font_Pygame.render(string,True,color),(x,y))
    def creds(self,screen):
        screen.fill((0,0,0))
        self.y -=.5
        self.fontWrite(300,self.y-400,"YOU DIED")
        self.fontWrite(250,self.y-50,"FANTA-FINALSY!!!!!!!!!!!!")
        self.fontWrite(self.x,self.y,"Jordan Yahn: Shops and NPC")
        self.fontWrite(self.x,self.y+50,"Trenton Daugherty: General design, Art, Enemy's, Players and combat")
        self.fontWrite(self.x,self.y+100,"Tyler Evens: Map Cordinator and tieing game together")
        self.fontWrite(self.x,self.y+150,"Devin Kendall: Map Designer")
        self.fontWrite(self.x,self.y+200,"Hope You enjoyed")
        self.fontWrite(self.x,self.y+800,"NOW GET OUT!!!")
        if self.y<-850:
            self.pineapples=True


runC = Credits(100,750)
death = False
game = True
while runC.pineapples==False:
    screen.fill((255,255,255))
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]and death==False:
        death = True
    if death ==True:
        screen.fill((0,0,0))
        runC.creds(screen)
        pygame.display.flip()
        
pygame.display.quit()
