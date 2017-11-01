#Tyler Evans
#ETGG 1803
#Lab 6




import objects3d
import math3d
import pygame


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
#camera setup
#uses your test image
camPos = math3d.VectorN(-15, 19, -30)
camCOI = math3d.VectorN(2, 5, 3)
camUp = math3d.VectorN(0,1,0)
camFOV = 60
camNear = 1.5
cam = objects3d.Camera(camPos, camCOI, camUp,
                       camFOV, camNear, screen)

SphereCol=objects3d.Material(math3d.VectorN(1,0,0),math3d.VectorN(0.3,0,0),math3d.VectorN(1,1,1),10)
plane1Col=objects3d.Material(math3d.VectorN(0,1,0),math3d.VectorN(0,0.5,0),math3d.VectorN(1,0,0),2)
plane2Col=objects3d.Material(math3d.VectorN(0,0,1),math3d.VectorN(0,0,0.1),math3d.VectorN(1,0,1),6)
aabbCol=objects3d.Material(math3d.VectorN(1,1,0),math3d.VectorN(0.5,0.3,0.1),math3d.VectorN(0.5,1,0.5),30)

#Creates an object list and appends the objects into the list
objects = []
objects.append(objects3d.Sphere(math3d.VectorN(2,5,3), 7, SphereCol))
objects.append(objects3d.Plane(math3d.VectorN(0, 1, 0), 5, plane1Col))
objects.append(objects3d.Plane(math3d.VectorN(0.1, 1, 0), 4, plane2Col))
objects.append(objects3d.AABB(math3d.VectorN(2,9,-6),math3d.VectorN(8,15,0),aabbCol))

light_list=[]
light_list.append(objects3d.Light(math3d.VectorN(0,50,0),math3d.VectorN(1,1,1),math3d.VectorN(1,1,1)))
light_list.append(objects3d.Light(math3d.VectorN(50,50,-50),math3d.VectorN(0.4,0,0),math3d.VectorN(0,0.6,0)))


y = 0
ambient_light=math3d.VectorN(1,1,1)

# Game Loop
while not done:
    # Update
    # Render ONE line (if we have more to render)
    if y < screen.get_height():
        for x in range(screen.get_width()):
            # Create a ray that starts at the current
            # pixels' 3d virtual position




            origin = cam.getPixelPos(x, y)

            direction = origin - cam.mPos
            R = objects3d.Ray(origin, direction)

            # Loop through all objects in the scene.
            # Find the color of the CLOSEST object we
            # hit.  Set color to that object's color.
            color=(128,128,128)
            closet_dist=5000
            #goes through the objects and intersects rays to them
            #sets the closest hits to their color
            for o in objects:
                result=o.rayIntersection(R)
                if result==None:
                    continue
                if result.hitDis<closet_dist:
                    #Defines the overall lit_c
                    lit_c=math3d.VectorN(0,0,0)
                    closet_dist=result.hitDis
                    #Gets the ambient color and adds it to the lit_c
                    obj=result.object
                    matAmbCol=obj.mColor.mAmbient
                    amb_c=ambient_light.pairwise_mult(matAmbCol)
                    lit_c+=amb_c
                    for l in light_list:
                        inShadow=False
                        for ob in objects:
                            #checks to see if objects are in shadows
                            sray_org=result.hitPt
                            sray_dir=l.lPos-sray_org
                            new_org=sray_org+sray_dir*0.01
                            sray_dis=sray_dir.magnitude()
                            shadow_ray=objects3d.Ray(new_org,sray_dir)
                            sresult=ob.rayIntersection(shadow_ray)
                            #if so it skips their color calculations

                            if sresult!=None and sresult.hitDis<sray_dis:
                                inShadow=True

                        if not inShadow:
                            #if not in a shadow, it calculates the diffuse and specular color and adds them to lit_c
                            d=l.lPos-result.hitPt
                            light_dir=d.normalized()
                            dStr=light_dir.dot(result.normal)
                            if dStr<=0:
                                diff_c=math3d.VectorN(0,0,0)
                            else:
                                diff_c=dStr*(l.lDiffuse.pairwise_mult(obj.mColor.mDiffuse))
                                lit_c+=diff_c


                            r1=2*(light_dir.dot(result.normal))
                            r2=r1*result.normal-light_dir
                            V=(cam.mPos-result.hitPt).normalized()
                            sStr=V.dot(r2)
                            if sStr<=0:
                                spec_c=math3d.VectorN(0,0,0)
                            else:
                                s=sStr**obj.mColor.mHardness
                                spec_c=s*(l.lSpecular.pairwise_mult(obj.mColor.mSpecular))
                                lit_c+=spec_c












                    #clamps the color values

                    math3d.clamp(lit_c)






                    #converts and applies the color calculations
                    color=(lit_c*255).int()






            #sets the screen to that color
            screen.set_at((x,y),color)


        y += 1

    # Input
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        #saves an image of the rendered picture
        pygame.image.save(screen,"raytracer.png")
        done = True

    # Drawing
    pygame.display.flip()

pygame.display.quit()