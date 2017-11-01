#Tyler Evans
#ETGG 1803
#Lab 7

import random
import pygame
import math


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
    def getData(self):
        return self.__mData
    def getDim(self):
        return self.__mDim


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
        elif isinstance(rhs,VectorN) or isinstance(rhs,MatrixN):
            return NotImplemented
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
        """This function returns the dot product of two vectors, returns a scalar"""
        if isinstance(rhs,VectorN) and len(self)==len(rhs):
            total=0
            for i in range(len(self.__mData)):
                result=self.__mData[i]*rhs[i]
                total+=result
            return total




    def cross(self,rhs):
        """this function returns the cross product of two vectors, returns a newly made VectorN"""
        if isinstance(rhs,VectorN) and len(rhs)==3 and len(self)==3:
            n=VectorN(*self.__mData)
            x=n[1]*rhs[2]-n[2]*rhs[1]
            y=n[2]*rhs[0]-n[0]*rhs[2]
            z=n[0]*rhs[1]-n[1]*rhs[0]
            result=VectorN(x,y,z)
            return result

    def pairwise_mult(self,rhs):
        """This function pairwise multiplies two vectors, works only when calculating color values"""
        if isinstance(rhs,VectorN) and len(rhs)==3 and len(self)==3:
            n=VectorN(*self.__mData)
            x=n[0]*rhs[0]
            y=n[1]*rhs[1]
            z=n[2]*rhs[2]
            result=VectorN(x,y,z)
            return result

def clamp(v,low=0,high=1.0):
    """This function clamps the final color value within this range"""
    if v[0]<low:
        v[0]=low
    if v[1]<low:
        v[1]=low
    if v[2]<low:
        v[2]=low
    if v[0]>high:
        v[0]=high
    if v[1]>high:
        v[1]=high
    if v[2]>high:
        v[2]=high
    return v



class MatrixN(object):
    """This class defines a MatrixN object"""
    def __init__(self,n1,n2,num_list=None):
        """The contructor has a row and column number as well as a list of integers. These values are organized into their respective rows and columns"""
        self.row=n1
        self.col=n2
        nums=self.row*self.col
        self.matrix=[]

        if num_list==None:
        #If the list has no integers, a zero matrix is created
            num_list=[]
            for i in range(0,nums):
                num_list.append(0)
            for i in range(0,self.row):
                t=num_list[i*self.col:(i+1)*self.col]
                v=VectorN(*t)
                self.matrix.append(v)

        else:
            if nums!=len(num_list):
                raise ValueError("You must pass exactly "+str(nums)+" values")


            for i in range(0,self.row):
                t=num_list[i*self.col:(i+1)*self.col]
                v=VectorN(*t)
                self.matrix.append(v)



    def __str__(self):
        """This method returns the matrix into its readable format"""
        result=""
        for i in range(len(self.matrix)):
            if i==0:
                result+="/"
            elif i==len(self.matrix)-1:
                result+="\\"
            else:
                result+="|"
            for num in self.matrix[i]:
                result+=str(num)+" "

            if i==0:
                result+="\\"
                result+="\n"
            elif i==len(self.matrix)-1:
                result+="/"
            else:
                result+="|"
                result+="\n"
        return result



    def copy(self):
        """This method creates a copy of the Matrix specified"""
        L = []
        for i in range(self.row):
            for j in range(self.col):
                L.append(self.matrix[i][j])
        newM = MatrixN(self.row, self.col, L)
        return newM



    def __setitem__(self,pos,data):
        """This method sets an item in the matrix to a single number"""
        self.matrix[pos[0]][pos[1]]=float(data)



    def __getitem__(self,data):
        """This item gets the position of an item"""
        return self.matrix[data[0]][data[1]]

    def getRow(self,row):
        """This method returns the elements in a row of matrices"""
        v=(self.matrix[row]).getData()
        t=VectorN(*v)
        return t

    def getCol(self,col):
        """This method gets the elements in a column of matrices"""
        n=[]
        for i in range(len(self.matrix)):
            v=self.matrix[i]
            t=v[col]
            n.append(t)
        return VectorN(*n)




    def setRow(self,row,vector):
        """This method sets a specific row to a new row with new values"""
        if self.col==vector.getDim():
           self.matrix[row]=vector
        else:
            raise ValueError("Invalid row argumnent(must be a VectorN with size= "+str(self.col)+")")



    def setColumn(self,col,vector):
        """This method sets a column to a column of the same size with new values"""
        for i in range(len(self.matrix)):
            v=self.matrix[i]
            v[col]=vector[i]








    def transpose(self):
        """This method transposes a matrix"""
        t = MatrixN(self.col, self.row)
        for i in range(self.row):
            for j in range(self.col):
                t[j, i] = self[i, j]
        return t

    def __mul__(self,rhs):
        """This method allows for matrix to matrix/vector/scalar multiplication from the right side"""
        if isinstance(rhs,int) or isinstance(rhs,float):
            m=self.copy()
            for i in range(len(m.matrix)):
                m.matrix[i]=m.matrix[i]*rhs
            return m

        elif isinstance(rhs,VectorN):
            mData=rhs.getData()
            mDim=rhs.getDim()
            result_list=[]
            m=MatrixN(mDim,1,(mData))
            if self.col==m.row:
                for row in range(len(self.matrix)):
                    for col in range(0,m.col):
                        num=self.matrix[row].dot(m.getCol(col))
                        result_list.append(num)
            result=VectorN(*result_list)
            return result
        else:
            if isinstance(rhs,MatrixN):
                result_list=[]
                if self.col==rhs.row:
                    for row in range(len(self.matrix)):
                        for col in range(0,rhs.col):
                            num=self.matrix[row].dot(rhs.getCol(col))
                            result_list.append(num)
                result=MatrixN(self.row,rhs.col,result_list)
                return result





    def __rmul__(self,lhs):
        """This method allows for matrix/vector/scalar multiplication from the left side"""
        if isinstance(lhs, float) or isinstance(lhs,int):
            m=self.copy()
            for i in range(len(m.matrix)):
                m.matrix[i]=m.matrix[i]*lhs
            return m
        elif isinstance(lhs,VectorN):
            mData=lhs.getData()
            mDim=lhs.getDim()
            result_list=[]
            m=MatrixN(1,mDim,(mData))
            if m.col==self.row:
                for row in range(len(m.matrix)):
                    for col in range(0,self.col):
                        num=m.matrix[row].dot(self.getCol(col))
                        result_list.append(num)
            result=VectorN(*result_list)
            return result
        else:
            if isinstance(lhs,MatrixN):
                result_list=[]
                if self.col==lhs.row:
                    for row in range(len(self.matrix)):
                        for col in range(0,lhs.col):
                            num=self.matrix[row].dot(lhs.getCol(col))
                            result_list.append(num)
                result=MatrixN(self.row,lhs.col,result_list)
                return result

#These tranform functions create 4x4 transformation matrices

def rotate(boolean,theta):
    """rotate in the z-axis"""
    theta=math.radians(theta)
    m=MatrixN(4,4,(math.cos(theta),math.sin(theta),0,0,-math.sin(theta),math.cos(theta),0,0,0,0,1,0,0,0,0,1))
    if boolean==True:
        return m
    else:
        rightm=m.transpose()
        return rightm

def rotateX(boolean,theta):
    """rotate around the x-Axis"""
    m=MatrixN(4,4,(1,0,0,0,0,math.cos(math.radians(theta)),math.sin(math.radians(theta)),0,0,-math.sin(math.radians(theta)),math.cos(math.radians(theta)),0,0,0,0,1))
    if boolean==True:
        return m
    else:
        rightm=m.transpose()
        return rightm
def rotateY(boolean,theta):
    """rotate around the y-axis"""
    theta=math.radians(theta)
    m=MatrixN(4,4,(math.cos(theta),0,-math.sin(theta),0,0,1,0,0,math.sin(theta),0,math.cos(theta),0,0,0,0,1))
    if boolean==True:
        return m
    else:
        rightm=m.transpose()
        return rightm

def scale(boolean,xscalar,yscalar,zscalar):
    """scales an object"""
    m=MatrixN(4,4,(xscalar,0,0,0,0,yscalar,0,0,0,0,zscalar,0,0,0,0,1))
    if boolean==True:
        return m
    else:
        rightm=m.transpose()
        return rightm
def translate(boolean,xscalar,yscalar,zscalar):
    """translates the object"""
    m=MatrixN(4,4,(1,0,0,0,0,1,0,0,0,0,1,0,xscalar,yscalar,zscalar,1))
    if boolean==True:
        return m
    else:
        rightm=m.transpose()
        return rightm


class Face(object):
    """"creates a face object"""
    def __init__(self,face_vert,color,Fnormal,normal=None):
        self.vind=face_vert
        self.mind=normal
        self.mColor=(VectorN(*color)*255).int()
        self.Fnormal=Fnormal



class Polymesh(object):
    """creates a polymesh object using an obj file and a mathcing mtl file(for color)"""
    def __init__(self,file,MTL,matrix=None):
        self.Vlist=[]
        self.Flist=[]
        self.Mtransform=matrix
        self.mats={}
        self.children=[]

        name=""
        mtl=open(MTL,"r")
        for line in mtl:
            line=line.strip()
            if line=="" or line[0]=="#":
                continue
            elem=line.split(" ")
            if elem[0]=="newmtl":
                name=elem[1]
            if elem[0]=="Kd":
                self.mats[name]=(elem[1],elem[2],elem[3])
        mtl.close()

        curMat=(0,0,0)
        fp=open(file,"r")
        for line in fp:
            line=line.strip()
            if line=="" or line[0]=="#":
                continue
            elem=line.split(" ")
            if elem[0]=="v":
                n=VectorN(elem[1],elem[2],elem[3],1)
                self.Vlist.append(n)
            elif elem[0]=="usemtl":
                    curMat=self.mats[elem[1]]


            elif elem[0]=="f" and len(elem)>2:
                temp_vind=[]
                temp_mind=[]
                temp_uv=[]
                for i in range(1,len(elem)):
                    if elem[1].count("/")==0:
                        temp_vind.append(elem[i])
                    if elem[1].count("/")==1:
                        Nline=elem[i].split("/")
                        temp_vind.append(Nline[0])
                        temp_mind.append(Nline[1])
                    if elem[1].count("//")==1:
                        Nline=elem[i].split("//")
                        temp_vind.append(Nline[0])
                        temp_mind.append(Nline[1])

                point1=self.Vlist[int(temp_vind[0])-1]
                point2=self.Vlist[int(temp_vind[1])-1]
                point3=self.Vlist[int(temp_vind[2])-1]
                vector1=point2-point1
                vector2=point3-point1
                NewVector1=VectorN(vector1[0],vector1[1],vector1[2])
                NewVector2=VectorN(vector2[0],vector2[1],vector2[2])
                result=(NewVector1.cross(NewVector2)).normalized()
                finalVector=VectorN(result[0],result[1],result[2],0)
                f=Face(temp_vind,curMat,finalVector,temp_mind)
                self.Flist.append(f)

        fp.close()

    def render(self,screen,matrix):
        """renders the loaded polymesh"""
        c=self.Mtransform*matrix
        for face in self.Flist:
            normal=face.Fnormal
            t=normal*c
            if t[2]>=0:
                resultL=[]
                for i in face.vind:
                    v=self.Vlist[int(i)-1]
                    t=v*c
                    pair=(t[0],t[1])
                    resultL.append(pair)
                pygame.draw.polygon(screen,face.mColor,resultL,1)
        for child in self.children:
            child.render(screen,c)

