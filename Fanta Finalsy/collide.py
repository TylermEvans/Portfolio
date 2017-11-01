

######### collision functions
def collideCircles(circle1_x,circle1_y,circle1_radius,circle2_x,circle2_y,circle2_radius):
    """CollideCircles(circle1_x,circle1_y,circle1_radius,circle2_x,circle2_y,circle2_radius) - Returns True if the two circles collide, False otherwise."""
    if ((circle2_x-circle1_x)**2 + (circle2_y-circle1_y)**2)**0.5  <= (circle1_radius+circle2_radius):
        return True
    else:
        return False
          
def collidePointCircle(point_x,point_y,circle_x,circle_y,circle_radius):
    """CollidePointCircle(point_x,point_y,circle_x,circle_y,circle_radius) - Returns True if the point collides with the circle, False otherwise."""
    if ((point_x-circle_x)**2 + (point_y-circle_y)**2)**0.5  <= circle_radius:
        return True
    else:
        return False
    
def collidePointRectangle(point_x,point_y,rect_x1,rect_y1,rect_x2,rect_y2):
    """CollidePointRectangle(point_x,point_y,rect_x1,rect_y1,rect_x2,rect_y2) - returns True if the point collides with the rectangle, False otherwise."""
    if (rect_x1<point_x<rect_x2  or rect_x2<point_x<rect_x1) and (rect_y1<point_y<rect_y2 or rect_y2<point_y<rect_y1):
        return True
    else:
        return False

def collideRectangles(rect1_x1,rect1_y1,rect1_x2,rect1_y2, rect2_x1,rect2_y1,rect2_x2,rect2_y2  ):
    """CollideRectangles(rect1_x1,rect1_y1,rect1_x2,rect1_y2, rect2_x1,rect2_y1,rect2_x2,rect2_y2  ) - Returns True if the two orthogonal rectangles collide, False otherwise. """
    r1 = pygame.Rect(rect1_x1,rect1_y1,rect1_x2-rect1_x1,rect1_y2-rect1_y1)
    r2 = pygame.Rect(rect2_x1,rect2_y1,rect2_x2-rect2_x1,rect2_y2-rect2_y1)
    return r1.colliderect(r2)    

def collideCircleRectangle(circle_x,circle_y,circle_radius,rect_x1,rect_y1,rect_x2,rect_y2):
    """CollideCircleRectangle(circle_x,circle_y,circle_radius,rect_x1,rect_y1,rect_x2,rect_y2) - Returns True if the circle collides with the rectangle, False otherwise """
    if((rect_x1-circle_radius<=circle_x<=rect_x2+circle_radius  or rect_x2-circle_radius<=circle_x<=rect_x1+circle_radius) and  (rect_y1<=circle_y<=rect_y2  or rect_y2<=circle_y<=rect_y1)) or ((rect_x1<=circle_x<=rect_x2  or rect_x2<=circle_x<=rect_x1) and  (rect_y1-circle_radius<=circle_y<=rect_y2+circle_radius  or rect_y2-circle_radius<=circle_y<=rect_y1+circle_radius)):
        return True
    else:
        if collidePointCircle(rect_x1,rect_y1,circle_x,circle_y,circle_radius):
            return True
        elif collidePointCircle(rect_x2,rect_y2,circle_x,circle_y,circle_radius):
            return True
        elif collidePointCircle(rect_x1,rect_y2,circle_x,circle_y,circle_radius):
            return True
        elif collidePointCircle(rect_x2,rect_y1,circle_x,circle_y,circle_radius):
            return True
        else:
            return False

def collideLineCircle(line_x1,line_y1,line_x2,line_y2,circle_x,circle_y,circle_radius):
   """CollideCircleLine(line_x1,line_y1,line_x2,line_y2,circle_x,circle_y,circlie_radius)"""
   # vector from end point 1 to circle center
   dx1 = circle_x-line_x1
   dy1 = circle_y-line_y1
   # vector from line end to end
   dx2 = line_x2 - line_x1
   dy2 = line_y2 - line_y1

   #dot product of two vectors
   dotprod = float(dx1*dx2 + dy1*dy2)

   dist = (dx2**2 + dy2**2)**0.5  # note, could optimize out the square root here

   param_point = dotprod / dist**2

   if(param_point < 0):
      closest_x = line_x1
      closest_y = line_y1
   elif(param_point > 1):
      closest_x = line_x2
      closest_y = line_y2
   else:
      closest_x = line_x1 + param_point * dx2
      closest_y = line_y1 + param_point * dy2

   dist = ((circle_x-closest_x)**2 + (circle_y-closest_y)**2) ** 0.5
   if dist<=circle_radius:
      return True
   return False
