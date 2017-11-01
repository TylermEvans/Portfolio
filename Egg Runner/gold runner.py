
import pygame
import math
import random
import player
import time
import dicttool
import AI


screen=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)
map1=dicttool.TileMap(screen)


pygame.init()

#initialization
startscreen=True
level1=False
level2=False
level3=False
level4=False
level5=False
level6=False
level7=False
level8=False
level9=False
level10=False
victory=False
game_over=False
start_x=280
start_y=318
clock=pygame.time.Clock()


#start screen
pygame.mixer.music.load("sunny.mp3")
pygame.mixer.music.play()
while startscreen==True:
    screen.fill((0,0,0))
    pygame.event.pump()
    key=pygame.key.get_pressed()
    if key[pygame.K_s]:
        start_y=318+50
    if key[pygame.K_w]:
        start_y=318

    fontObj = pygame.font.SysFont("Courier New", 12)
    screen.blit(fontObj.render("Egg Runner",False,(255,255,255)),(100,200))
    screen.blit(fontObj.render("New Game",False,(255,255,255)),(300,300))
    screen.blit(fontObj.render("Exit",False,(255,255,255)),(300,350))
    pygame.draw.circle(screen,(255,0,0),(start_x,start_y),10,0)


    if key[pygame.K_RETURN] and start_y==318:
        screen.fill((0,0,0))
        screen.blit(fontObj.render("Collect all of the treasures to traverse the next level",False,(255,255,255)),(300,300))
        screen.blit(fontObj.render("Also, don't die",False,(255,255,255)),(300,350))
        pygame.display.flip()
        time.sleep(5)
        level1=True
        startscreen=False
        pygame.mixer.music.stop()
    if key[pygame.K_RETURN] and start_y==318+50:
        break







    pygame.display.flip()




#levels 1-10
map1.loadTileTypes("map1tiles.txt")
map1.loadMap("level 1.txt")
player=player.Player(600,450)
enemy1=AI.Enemy(200,100,player.time_out)
player.treasure=3
pygame.mixer.music.load("smash.mp3")
pygame.mixer.music.play()

while level1==True:
    clock.tick(60)
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break


    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy1.x,enemy1.y)
    enemy1.move(player.x,player.y,map1)
    if player.next_level==True:
        level2=True
        level1=False
        player.level+=1
        player.score+=1000



    #drawing of the map and hud and movement
    map1.renderMap()
    player.render(screen)
    enemy1.render(screen)
    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))


    pygame.display.flip()





player.x=20
player.y=470
enemy2=AI.Enemy(200,100,player.time_out)
map1.loadMap("level 2.txt")
player.treasure=3
while level2==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break


    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy2.x,enemy2.y)
    enemy2.move(player.x,player.y,map1)
    if player.next_level==True:
        level3=True
        level2=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy2.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()


player.x=100
player.y=500
map1.loadMap("level 3.txt")
enemy3=AI.Enemy(400,100,player.time_out)
player.treasure=3
while level3==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy3.x,enemy3.y)
    enemy3.move(player.x,player.y,map1)
    if player.next_level==True:
        level4=True
        level3=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy3.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()

player.x=300
player.y=500
map1.loadMap("level 4.txt")
enemy4=AI.Enemy(230,100,player.time_out)
player.treasure=4
while level4==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy4.x,enemy4.y)
    enemy4.move(player.x,player.y,map1)
    if player.next_level==True:
        level5=True
        level4=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy4.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()

player.x=200
player.y=500
map1.loadMap("level 5.txt")
enemy5=AI.Enemy(200,100,player.time_out)
player.treasure=3
while level5==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy5.x,enemy5.y)
    enemy5.move(player.x,player.y,map1)
    if player.next_level==True:
        level6=True
        level5=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy5.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()
player.x=200
player.y=500
map1.loadMap("level 6.txt")
enemy6=AI.Enemy(600,100,player.time_out)
player.treasure=4
while level6==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy6.x,enemy6.y)
    enemy6.move(player.x,player.y,map1)
    if player.next_level==True:
        level7=True
        level6=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy6.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()
player.x=200
player.y=500
map1.loadMap("level 7.txt")
enemy7=AI.Enemy(200,100,player.time_out)
player.treasure=5
while level7==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy7.x,enemy7.y)
    enemy7.move(player.x,player.y,map1)
    if player.next_level==True:
        level8=True
        level7=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy7.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()
player.x=100
player.y=500
map1.loadMap("level 8.txt")
enemy8=AI.Enemy(200,100,player.time_out)
player.treasure=3
while level8==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy8.x,enemy8.y)
    enemy8.move(player.x,player.y,map1)
    if player.next_level==True:
        level9=True
        level8=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy8.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()
player.x=100
player.y=500
map1.loadMap("level 9.txt")
enemy9=AI.Enemy(200,100,player.time_out)
player.treasure=4
while level9==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy9.x,enemy9.y)
    enemy9.move(player.x,player.y,map1)
    if player.next_level==True:
        level10=True
        level9=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy9.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()
player.x=100
player.y=500
map1.loadMap("level 10.txt")
enemy10=AI.Enemy(200,140,player.time_out)
player.treasure=4
while level10==True:
    if player.game_over==True: #game over
        screen.fill((0,0,0))
        fontObj = pygame.font.SysFont("Courier New", 20)
        screen.blit(fontObj.render("Game Over :(",False,(255,255,255)),(150,200))
        screen.blit(fontObj.render("You have failed to get gud",False,(255,255,255)),(150,300))
        screen.blit(fontObj.render("Come back when you get gud",False,(255,255,255)),(150,400))
        pygame.display.flip()
        time.sleep(5)
        break

    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    player.move(map1,enemy10.x,enemy10.y)
    enemy10.move(player.x,player.y,map1)
    if player.next_level==True:
        victory=True
        level10=False
        player.level+=1
        player.score+=1000
    map1.renderMap()
    player.render(screen)
    enemy10.render(screen)

    font=pygame.font.SysFont("Arial",12)
    screen.blit(font.render("Lives: "+str(player.lives),False,(255,255,255)),(20,20))
    screen.blit(font.render("Treasures left: "+str(player.treasure),False,(255,255,255)),(70,20))
    screen.blit(font.render("Score: "+str(player.score),False,(255,255,255)),(150,20))
    screen.blit(font.render("Level: "+str(player.level),False,(255,255,255)),(240,20))

    pygame.display.flip()

pygame.mixer.music.load("funky.mp3")
pygame.mixer.music.play()
while victory==True:
    screen.fill((0,0,0))
    pygame.event.pump()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break

    fontObj = pygame.font.SysFont("Courier New", 15)
    screen.blit(fontObj.render("Victory!",False,(255,255,255)),(150,200))
    screen.blit(fontObj.render("You have successfully collected all of the eggs...",False,(255,255,255)),(150,300))
    screen.blit(fontObj.render("...while avoiding your death at the hands of alien children",False,(255,255,255)),(150,400))
    screen.blit(fontObj.render("press escape to stop your adventure permenantly",False,(255,255,255)),(150,500))


    pygame.display.flip()








pygame.quit()