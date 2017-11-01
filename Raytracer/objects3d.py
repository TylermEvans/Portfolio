#Tyler Evans
#Lab 5

import math3d
import random
import math
import pygame


class Camera(object):
    """This class sets up the camera"""
    def __init__(self,pos,coi,up,fov,near,surf):
        self.up = up.normalized() #the up of the camera
        self.mPos=pos #the position of the camera

        self.surf=surf # sureface dimensions
        self.surfW=surf.get_width()
        self.surfH=surf.get_height()

        self.fov=fov  # the feild of view
        self.near=near #the near in world units
        self.zAxis = (coi-pos).normalized() #the z axis of the camera
        self.xAxis = (self.up.cross(self.zAxis)).normalized() #the x axis of the camera
        self.yAxis = self.zAxis.cross(self.xAxis) #the y axis of the camera


        self.aspectRatio = self.surfW/self.surfH #setting up the viewpoint
        self.viewpointH = 2*self.near*math.tan(math.radians(self.fov/2))
        self.viewpointW = self.viewpointH*self.aspectRatio

        a = self.near*self.zAxis
        b = (self.viewpointH/2)*self.yAxis
        c = -(self.viewpointW/2)*self.xAxis


        self.VPO = pos+a+b+c # the viewpoint origin




    def getPixelPos(self,ix,iy):
        """Gets the pixel position of a point on the viewplane"""
        s=ix/(self.surfW-1)*self.viewpointW
        t=iy/(self.surfH-1)*self.viewpointH
        d=s*self.xAxis
        e=-t*self.yAxis
        p=self.VPO+d+e
        return p




class Ray(object):
    """Creates a ray object"""
    def __init__(self,origin,direction):
        """Sets up the ray"""
        self.mOrigin=origin
        self.mDirection=direction.normalized()
        self.copy=origin.copy()
    def getPoint(self,t):
        """Gets a point along the length of the ray"""
        n=t*self.mDirection
        result=self.mOrigin+n
        return result



    def drawPygame(self,screen):
        """draws a projection of the ray"""
        color=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pygame.draw.line(screen,color,(int(self.mOrigin[0]),int(self.mOrigin[1])),(int(n[0]),int(n[1])),5)


    def getDistanceToPoint(self,point):
        """"Does collision"""
        if isinstance(point,VectorN):
            distance=point-self.mOrigin
            dispara=(distance.dot(self.mDirection)).dot(self.mDirection)
            disperp=distance-dispara
            if self.mDirection*distance<0:
                return None
            else:
                return disperp

class rayHit(object):
    """returns a rayhit object that stores the objects,the ray,the objects normals, hit distance, and hit points"""
    def __init__(self,t,normal,ray,o):
        self.hitDis=t
        self.hitPt=ray.getPoint(self.hitDis)
        self.normal=normal.normalized()
        self.ray=ray
        self.object=o

class Plane(object):
    """Creates a plane object"""
    def __init__(self,normal,dvalue,color):
        """creates the plane"""
        self.mNormal=normal.normalized()
        self.mDistance=dvalue
        self.mColor=color

    def rayIntersection(self,ray):
        """Returns the distance from the intersection of the ray and the object"""
        if self.mNormal.dot(ray.mDirection)==0:
            return None

        t=(self.mDistance-(ray.mOrigin.dot(self.mNormal)))/self.mNormal.dot(ray.mDirection)
        if t<0:
            return None
        else:
            return rayHit(t,self.mNormal,ray,self)

class Sphere(object):
    """creates the sphere object"""
    def __init__(self,origin,radius,color):
        self.mCenter=origin
        self.mRadius=radius
        self.mColor=color

    def rayIntersection(self,ray):
        """Returns the distance from the intersecion of the ray and the sphere. Returns the closest distance"""

        origin_vect=self.mCenter-ray.mOrigin
        if ray.mDirection.dot(origin_vect)<0:
            return None
        para_dist=origin_vect.dot(ray.mDirection)
        perp_dist_sq=origin_vect.dot(origin_vect)-para_dist**2

        if perp_dist_sq>self.mRadius**2:
            return None
        else:
            offset=(self.mRadius**2-perp_dist_sq)**0.5
            t1=para_dist-offset
            t2=para_dist+offset
            hitPt=ray.getPoint(t1)
            sphere_norm=hitPt-self.mCenter
            return rayHit(t1,sphere_norm,ray,self)

class AABB(object):
    """Creates a Axis Alighned Bounding Box"""
    def __init__(self,point1,point2,color):
        """takes two points and organizes the minimum and maximum values. Creates 6 planes and appends them to a list based on the norms and min amd max points"""
        self.mColor=color
        self.plane_list=[]
        point_1=point1
        point_2=point2
        if point_1[0]>point_2[0]:
            min_x=point_2[0]
            max_x=point_1[0]
        else:
            min_x=point_1[0]
            max_x=point_2[0]
        if point_1[1]>point_2[1]:
            min_y=point_2[1]
            max_y=point_1[1]
        else:
            min_y=point_1[1]
            max_y=point_2[1]
        if point_1[2]>point_2[2]:
            min_z=point_2[2]
            max_z=point_1[2]
        else:
            min_z=point_1[2]
            max_z=point_2[2]

        self.mMinPoint=math3d.VectorN(min_x,min_y,min_z)
        self.mMaxPoint=math3d.VectorN(max_x,max_y,max_z)

        left_norm=math3d.VectorN(1,0,0)
        self.plane_list.append(Plane(left_norm,self.mMaxPoint[0],self.mColor))

        right_norm=math3d.VectorN(-1,0,0)
        self.plane_list.append(Plane(right_norm,-self.mMinPoint[0],self.mColor))

        top_norm=math3d.VectorN(0,1,0)
        self.plane_list.append(Plane(top_norm,self.mMaxPoint[1],self.mColor))

        bot_norm=math3d.VectorN(0,-1,0)
        self.plane_list.append(Plane(bot_norm,-self.mMinPoint[1],self.mColor))

        back_norm=math3d.VectorN(0,0,-1)
        self.plane_list.append(Plane(back_norm,-self.mMinPoint[2],self.mColor))

        front_norm=math3d.VectorN(0,0,1)
        self.plane_list.append(Plane(front_norm,self.mMaxPoint[2],self.mColor))



    def rayIntersection(self,ray):
        """Test the intersecion of all 6 planes, sees if the hit point is within the boxes bounds. If it is then it returns the closest intersection distance"""
        closest_dist=5000
        v=0.001
        closest_result=None
        for plane in self.plane_list:
            result=plane.rayIntersection(ray)
            if result!=None:
                hitPt=result.hitPt
                if self.mMinPoint[0]-v<=hitPt[0] and hitPt[0]<=self.mMaxPoint[0]+v and self.mMinPoint[1]-v<=hitPt[1] and hitPt[1]<=self.mMaxPoint[1]+v and self.mMinPoint[2]-v<=hitPt[2] and hitPt[2]<=self.mMaxPoint[2]+v:
                    if result.hitDis<closest_dist:
                        closest_dist=result.hitDis
                        closest_result=result
        if closest_dist==5000:
            return None
        return closest_result






class Material(object):
    """Defines the material colors of objects"""
    def __init__(self,diffuse,ambient,specular,hardness):
        self.mDiffuse=diffuse
        self.mAmbient=ambient
        self.mSpecular=specular
        self.mHardness=hardness

class Light(object):
    """Defines light objects and their colors they emit"""
    def __init__(self,position,diffuse,specular):
        self.lPos=position
        self.lDiffuse=diffuse
        self.lSpecular=specular





































