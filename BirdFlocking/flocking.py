import flock
import pygame
import math3d
import random

# Pygame startup
pygame.init()
win_width = 800
win_height = 600
screen = pygame.display.set_mode((win_width, win_height))
fontObj = pygame.font.SysFont("Courier New", 12)
clock = pygame.time.Clock()
done = False
paused = False

# This is a list of circular "obstacles" (pos_vector, rad)
obstacles = []
for i in range(3):
    x = random.randint(0, win_width)
    y = random.randint(0, win_height)
    obstacles.append([math3d.VectorN(x, y), random.randint(50, 150)])
print(obstacles)


# Create the flock.  Flock-members shouldn't spawn on obstacles (if doing the bonus)
F = flock.Flock(0,0,win_width,win_height, 20, obstacles)

# The mouse position (or None if the user isn't clicking)6
mpos = None
x=random.randint(1,799)
y=random.randint(1,599)

p=flock.Prey((math3d.VectorN(x,y)),5,(math3d.VectorN(1,1)))
P=flock.Predator((math3d.VectorN(x,y)),5,(math3d.VectorN(1,1)))


# Game Loop
while not done:
    # Update
    deltaTime = clock.tick() / 1000.0
    if paused:
        deltaTime = 0.0             # Everything remains functional, but we don't move anything...
    F.update(deltaTime, mpos)
    p.update(deltaTime)
    P.update(deltaTime)
    distance=p.circlePos-P.circlePos
    if distance.magnitude()<=10:#Random prey/pred behavior
        x=random.randint(1,20)
        y=random.randint(1,20)
        accel=(math3d.VectorN(x,y)-p.circlePos).normalized()*10*deltaTime
        p.applya(accel)




    # Input
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
        paused = not paused
    keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    if keys[pygame.K_ESCAPE]:
        done = True
    if pygame.mouse.get_pressed()[0]:
        mouseClicked = True
        mpos = math3d.VectorN(mx, my)
    else:
        mouseClicked = False
        mpos = None

    # Draw
    screen.fill((0,0,0))
    for o in obstacles:
        pygame.draw.circle(screen, (0,128,0), o[0].int(), o[1])
    F.render(screen)
    p.render(screen)
    P.render(screen)


    if mouseClicked:
        screen.blit(fontObj.render("--Mouse Button Down--", False, (255,255,255)), (0,0))
    pygame.display.flip()

# Shutdown
pygame.quit()