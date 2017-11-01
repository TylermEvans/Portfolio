import math3d
import math
import random
import time
import pygame




class Boid(object):
    """This class is the Boid object class"""
    def __init__(self,circlePos,circleRad,circleVel):
        """The constructor creates a boid with a position vector, velocity vector, and a radius of the center point."""
        self.circlePos=circlePos
        self.circleRad=circleRad
        self.circleVel=circleVel
    def update(self,time,mposition):
        """This function is the move method for a single boid. It includes a terminal velocity denoted by maz_vel. This function primarily updates the boids position bu adding multiple accelerations that influence the velocity."""
        max_speed=100
        self.circlePos += self.circleVel * time
        if mposition!=None:
            mouseDir = mposition - self.circlePos
            self.circleVel += mouseDir.normalized() * 80 * time #This is the terminal velocity being applied
            t=self.circleVel.magnitude()
            if t>=max_speed:
                self.circleVel=self.circleVel.normalized()*max_speed




    def applya(self,a):
        """This function allows for me to apply multiple different velocities easily"""
        self.circleVel += a

    def render(self,screen):
        """This function allows for the Boid to be drawn on screen. 4 points are created and a polygon function is called to draw the poid"""
        pygame.draw.circle(screen, (255,0,0), self.circlePos.int(),self.circleRad,0)
        tipPt = self.circlePos + 5 * self.circleVel.normalized()
        perpVector = math3d.VectorN(-self.circleVel[1], self.circleVel[0]).normalized()
        rsidePt = self.circlePos + 5 * perpVector
        lsidePt = self.circlePos + 5 *-perpVector

        pygame.draw.line(screen, (255,255,255), self.circlePos, tipPt)
        pygame.draw.line(screen, (255,255,255), self.circlePos, rsidePt)
        pygame.draw.line(screen,(255,255,255), self.circlePos, lsidePt)
        pygame.draw.polygon(screen,(255,255,255),(tipPt,rsidePt,lsidePt),3)





class Flock(object):
    """This class is the Flock class. The boids are appended to this class"""
    def __init__(self,x1,y1,x2,y2,numBoids,obstacles):
        """The constructor specifies a random interval for the boids to be spawned on, as well as the number of boids desired, as well as the ability to not  spawn on the obstacles"""
        self.circleVel=math3d.VectorN(1,1)
        self.boid_list=[] #This is the list the boids are appended to, creating a flock of boids
        self.numBoids=numBoids
        self.obstacle_list=obstacles

        for i in range(0,self.numBoids):
            x=random.randint(x1,x2)
            y=random.randint(y1,y2)
            self.circlePos=math3d.VectorN(x,y)
            self.boid_list.append(Boid(self.circlePos,2,self.circleVel))









    def update(self,time,position):
        """This method updates all the boids in the boid_list. It also cages the birds to the screen. Also applies the other acceleration vectors for direction and the center"""
        v=math3d.VectorN(0,0)
        n=math3d.VectorN(0,0)
        for boids in self.boid_list:
            boids.update(time,position)
            if boids.circlePos[0]>=800:
                boids.circlePos[0]=800
            if boids.circlePos[0]<=0:
                boids.circlePos[0]=0
            if boids.circlePos[1]>=600:
                boids.circlePos[1]=600
            if boids.circlePos[1]<=0:
                boids.circlePos[1]=0
            v+=boids.circlePos
        v/=self.numBoids

        for boids in self.boid_list:
            n+=boids.circleVel
        n/=self.numBoids

        for boids in self.boid_list:
            adirection=n.normalized()*30*time
            boids.applya(adirection)



        for boids in self.boid_list:
            centerpoint=(v-boids.circlePos).normalized()*30*time
            boids.applya(centerpoint)

        for boids in self.boid_list:#My attempt at avoiding obstacles
            for i in self.obstacle_list:
                if (i[0]-boids.circlePos).magnitude()<=i[1]+boids.circlePos.magnitude():
                    obstacle_accel=-(i[0]-boids.circlePos).normalized()*10*time
                    boids.applya(obstacle_accel)








    def render(self,screen):
        """The method renders all of the boids in the boid list"""
        for boids in self.boid_list:
            boids.render(screen)

class Prey(Boid):
    """prey class, interacts with predator"""
    def __init__(self,circlePos,circleRad,circleVel):
        self.circlePos=circlePos
        self.circleRad=circleRad
        self.circleVel=circleVel


    def update(self,time):
        self.circlePos += self.circleVel * time
        x=random.randint(1,799)
        y=random.randint(1,599)
        rand_vel=math3d.VectorN(x,y)
        random_dir=rand_vel-self.circlePos
        self.circleVel+=random_dir.normalized()*25*time

    def render(self,screen):
        pygame.draw.circle(screen, (255,0,0), self.circlePos.int(), self.circleRad,0)
        tipPt = self.circlePos + 5 * self.circleVel.normalized()
        perpVector = math3d.VectorN(-self.circleVel[1], self.circleVel[0]).normalized()
        rsidePt = self.circlePos + 5 * perpVector
        lsidePt = self.circlePos + 5 *-perpVector
        pygame.draw.line(screen, (255,255,255), self.circlePos, tipPt)
        pygame.draw.line(screen, (255,255,255), self.circlePos, rsidePt)
        pygame.draw.line(screen,(255,255,255), self.circlePos, lsidePt)
        pygame.draw.polygon(screen,(255,0,0),(tipPt,rsidePt,lsidePt),3)









class Predator(Boid):
    """predator class, interacts with prey"""

    def __init__(self,circlePos,circleRad,circleVel):
        self.circlePos=circlePos
        self.circleRad=circleRad
        self.circleVel=circleVel

    def update(self,time):
        self.circlePos += self.circleVel * time
        x=random.randint(1,799)
        y=random.randint(1,599)
        rand_vel=math3d.VectorN(x,y)
        random_dir=rand_vel-self.circlePos
        self.circleVel+=random_dir.normalized()*20*time








    def render(self,screen):
        pygame.draw.circle(screen, (255,0,0), self.circlePos.int(), self.circleRad,0)
        tipPt = self.circlePos + 5 * self.circleVel.normalized()
        perpVector = math3d.VectorN(-self.circleVel[1], self.circleVel[0]).normalized()
        rsidePt = self.circlePos + 5 * perpVector
        lsidePt = self.circlePos + 5 *-perpVector
        pygame.draw.line(screen, (255,255,255), self.circlePos, tipPt)
        pygame.draw.line(screen, (255,255,255), self.circlePos, rsidePt)
        pygame.draw.line(screen,(255,255,255), self.circlePos, lsidePt)
        pygame.draw.polygon(screen,(255,255,0),(tipPt,rsidePt,lsidePt),3)








