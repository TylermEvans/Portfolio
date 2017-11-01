#Tyler Evans
#ETGG 1803
#Lab 2

import random
import pygame


"""This VectorN class creates a vector object that can store any number of variables."""

class VectorN(object):
    """"This is the VectorN object. This helps define the Vector Class"""
    def __init__(self,*other_Args):
        """The attributes of this class store data. .__mData stores the numbers passed in as parameters(converted to float values). .__mDim is the length or dimension of .__mData"""
        self.__mData=[]
        for arg in other_Args:
            arg=float(arg)
            self.__mData.append(arg)

        self.__mDim=len(self.__mData)




    def __str__(self):
        """ This function returns a string in the form shown below"""
        return"<Vector"+str(self.__mDim)+": "+str(self.__mData)[1:-1]+">"
    def __len__(self):
        """ This function returns the dimension of the Vector object"""

        return self.__mDim

    def __getitem__(self,index):
        """This function returns the position specified in self.__mData"""
        return self.__mData[index]










    def __setitem__(self,index,data):
        """This function sets a position specified to a specific value that is then converted to a float before being added to self.__mData"""
        self.__mData[index]=float(data)

    def copy(self):
        """This function creates a new Vector object that is a copy of the specified vector"""
        return VectorN(*self.__mData)


    def __eq__(self,Vector):
        """This Function compares two specified vectors to determine if they are equal. It compares if they are both the same object, if they have the same dimensions, and if they have the same data within them"""
        newVector=self.__mData
        if isinstance(Vector,VectorN) and newVector==Vector.__mData and len(newVector)==len(Vector):
            return True
        else:
            return False


    def int(self):
        """This function adds the data in self.__mData to a list. Then it converts the data in that list to integers. Then it returns the newly made integers as a tuple"""
        int_list=[]
        for integer in self.__mData:
            result=int(integer)
            int_list.append(result)
        t=tuple(int_list)
        return t


    def __neg__(self):
        """This Function takes the data in a VectorN object and negates the data"""
        n=VectorN(*self.__mData)
        for i in range(len(n)):
            n[i]=-1*n[i]
        return n




    def magnitudeSquared(self):
        """ This Function takes the Magnitude of the object and squares it"""
        total=0
        for i in range (len(self.__mData)):
            result=self.__mData[i]**2
            total+=result
        return total

    def magnitude(self):
        """ This Function calculates the magnitude of a Vector"""


        total=0
        for i in range (len(self.__mData)):
            result=self.__mData[i]**2
            total+=result
        return (total)**0.5


    def normalized(self):
        """ This function normalizes the Vector. Making the Magnitude Unit Length"""
        n=VectorN(*self.__mData)
        result=n.magnitude()
        n=n/result
        return n


















    def __mul__(self,rhs):
        """This Function allows for multiplication between a Vector and Scalar. Specifically when the scalar is on right hand side"""
        n=VectorN(*self.__mData)
        if isinstance(rhs,int) or isinstance(rhs,float):
            for i in range(len(n)):
                n[i]=n[i]*rhs
            return n
        else:
            raise ValueError("You can only multiply this Vector"+str(self.__mDim)+" and a scalar. You attempted to multiply by <Vector"+str(self.__mDim)+": " +str(rhs)[1:-1]+">")


    def __rmul__(self, lhs):
        """This Function allows for multiplication between a Vector and Scalar. Specifically when the scalar is on the left hand side"""
        n=VectorN(*self.__mData)
        for i in range(len(n)):
            n[i]=n[i]*lhs
        return n






    def __add__(self,rhs):
        """The function  allows for addition between two Vectors. Nothing else"""
        if isinstance(rhs,VectorN) and len(self)==len(rhs):
            n=VectorN(*self.__mData)
            for i in range(len(n)):
                n[i]+=rhs[i]
            return n
        else:
            raise ValueError("You can only add another Vector"+str(self.__mDim)+" to this Vector"+str(self.__mDim)+" (you passed '"+str(rhs)+"')")



    def __sub__(self,rhs):
        """This Function allows for subtraction between two Vectors. Nothing else"""
        if isinstance(rhs,VectorN) and len(self)==len(rhs):
            n=VectorN(*self.__mData)
            for i in range(len(n)):
                n[i]-=rhs[i]
            return n
        else:
            raise ValueError("You can only subtract another Vector"+str(self.__mDim)+" to this Vector"+str(self.__mDim)+" (you passed '"+str(rhs)+"')")

    def __truediv__(self,rhs):
        """This function allows for the division between a Vector and a Scalar. You can not divide between two Vectors"""
        if isinstance(rhs,int) or isinstance(rhs,float):
            n=VectorN(*self.__mData)
            for i in range(len(n)):
                n[i]=n[i]*(1/rhs)
            return n
        else:
         raise ValueError("You can only divide this Vector"+str(self.__mDim)+" by a scalar. You attempted to divide by <Vector"+str(self.__mDim)+": " +str(self.__mData)[1:-1]+">" )


    def __rtruediv__(self,lhs):
        """This function raises an error. Can not divide a scalar by a Vector"""
        raise TypeError(": unsupported operand type(s) for /: 'int' and 'VectorN'")

    def isZero(self,tolerance=0.0):
        """This function determines if the data in a Vector object is composed of all zeros"""
        for val in self.__mData:
            if abs(val) > tolerance:
                return False
        return True

    def dot(self,rhs):
        if isinstance(rhs,VectorN) and len(self)==len(rhs):
            total=0
            for i in range(len(self.__mData)):
                result=self.__mData[i]*rhs[i]
                total+=result
            return total




    def cross(self,rhs):
        if isinstance(rhs,VectorN) and len(rhs)==3 and len(self)==3:
            n=VectorN(*self.__mData)
            x=n[1]*rhs[2]-n[2]*rhs[1]
            y=n[2]*rhs[0]-n[0]*rhs[2]
            z=n[0]*rhs[1]-n[1]*rhs[0]
            result=VectorN(x,y,z)
            return result







class Ray(object):
    def __init__(self,origin,direction):
        self.origin=origin
        self.direction=direction.normalized()
        self.copy=origin.copy()
    def getPt(self,t):
        n=t*self.direction
        result=self.origin+n
        return result

    def drawPygame(self,screen):
        color=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pygame.draw.line(screen,color,(int(self.origin[0]),int(self.origin[1])),(int(n[0]),int(n[1])),5)


    def getDistanceToPoint(self,point):
        if isinstance(point,VectorN):
            distance=point-self.origin
            dispara=(distance.dot(self.direction)).dot(self.direction)
            disperp=distance-dispara
            if self.direction*distance<0:
                return None
            else:
                return disperp
















































