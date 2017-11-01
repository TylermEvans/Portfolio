
import pygame
import time
import collide





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

def collidePointCircle(point_x,point_y,circle_x,circle_y,circle_radius):
    """CollidePointCircle(point_x,point_y,circle_x,circle_y,circle_radius) - Returns True if the point collides with the circle, False otherwise."""
    if ((point_x-circle_x)**2 + (point_y-circle_y)**2)**0.5  <= circle_radius:
        return True
    else:
        return False



class TileType(object):
    def __init__(self,tileSourceFilename=None,tileSourceColRow=(0,0),tileWidth=32,tileHeight=32,tileCollides=True):
        (tileSourceCol,tileSourceRow)=tileSourceColRow
        self.tileSourceFilename=tileSourceFilename
        self.tileSourceCol=tileSourceCol
        self.tileSourceRow=tileSourceRow
        self.tileWidth=tileWidth
        self.tileHeight=tileHeight
        self.tileCollides=tileCollides
        if tileSourceFilename!=None:
            tilesetSurf=pygame.image.load(tileSourceFilename)
            self.tileSurf=pygame.Surface((tileWidth,tileHeight)) #make a new surface
            self.tileSurf.blit(tilesetSurf,(0,0),(tileSourceCol*tileWidth,tileSourceRow*tileHeight,tileWidth,tileHeight))
    def dumpsTileType(self):
        outList=[]
        outList.append("tileSourceFilename="+self.tileSourceFilename)
        outList.append("tileSourceCol="+str(self.tileSourceCol))
        outList.append("tileSourceRow="+str(self.tileSourceRow))
        outList.append("tileWidth="+str(self.tileWidth))
        outList.append("tileHeight="+str(self.tileHeight))
        outList.append("tileCollides="+str(self.tileCollides))
        s=","
        return s.join(outList)
    def loadsTileType(self,inString):
        inList=inString.split(",")
        for item in inList:
            (key,value)=item.split("=")
            if key=="tileSourceCol":
                self.tileSourceCol=int(value)
            elif key=="tileSourceRow":
                self.tileSourceRow=int(value)
            elif key=="tileWidth":
                self.tileWidth=int(value)
            elif key=="tileHeight":
                self.tileHeight=int(value)
            elif key=="tileCollides":
                if value=="True":
                    self.tileCollides=True
                else:
                    self.tileCollides=False
            elif key=="tileSourceFilename":
                self.tileSourceFilename=value
        # reload the surface
        tilesetSurf=pygame.image.load(self.tileSourceFilename)
        self.tileSurf=pygame.Surface((self.tileWidth,self.tileHeight)) #make a new surface
        self.tileSurf.blit(tilesetSurf,(0,0),(self.tileSourceCol*self.tileWidth,self.tileSourceRow*self.tileHeight,self.tileWidth,self.tileHeight))



class TileMap(object):
    def __init__(self,screen,mapWidth=25,mapHeight=19,tileWidth=32,tileHeight=32):
        self.mapWidth=mapWidth
        self.mapHeight=mapHeight
        self.tileWidth=tileWidth
        self.tileHeight=tileHeight
        self.tileMap=[]
        self.screen=screen
        for row in range(0,mapHeight):
            self.tileMap.append([None]*mapWidth)
        self.tileTypes={}
    def addTileType(self,tileId,tileType):
        self.tileTypes[tileId]=tileType
    def renderTile(self,screenCol,screenRow,mapEntry):
        screenX=screenCol*self.tileWidth
        screenY=screenRow*self.tileHeight
        self.screen.blit(mapEntry.tileSurf,(screenX,screenY))
    def setTileMapEntry(self,mapCol,mapRow,tileTypeKey):
        if tileTypeKey==None:
            self.tileMap[mapRow][mapCol]=None
        else:
            self.tileMap[mapRow][mapCol]=tileTypeKey
    def renderMap(self):
        for row in range(0,self.mapHeight):
            for col in range(0,self.mapWidth):
                mapEntryKey=self.tileMap[row][col]
                if mapEntryKey != None:
                    self.renderTile(col,row,self.tileTypes[mapEntryKey])
    def saveTileTypes(self,filename):
        fp = open(filename,"w")
        for tileType in sorted(self.tileTypes.keys()):
            fp.write(tileType+":"+self.tileTypes[tileType].dumpsTileType()+"\n")
        fp.close()
    def loadTileTypes(self,filename):
        fp = open(filename,"r")
        for tileType in self.tileTypes:
            fp.write(tileType+":"+self.tileTypes[tileType].dumpsTileType()+"\n")

        for line in fp:
            line=line.strip()
            if len(line)==0 or line[0]=='#': # skip blank lines and comment lines
                continue
            (tileType,tileTypeDumpedString)=line.split(":") # divide the line into the two sides of the :
            self.tileTypes[tileType]=TileType()
            self.tileTypes[tileType].loadsTileType(tileTypeDumpedString)
        fp.close()
    def saveMap(self,filename):
        fp = open(filename,"w")
        fp.write("mapWidth="+str(self.mapWidth)+"\n")
        fp.write("mapHeight="+str(self.mapHeight)+"\n")
        fp.write("tileWidth="+str(self.tileWidth)+"\n")
        fp.write("tileHeight="+str(self.tileHeight)+"\n")
        fp.write("tileMap=\n")
        for row in range(0,self.mapHeight):
            for col in range(0,self.mapWidth):
                if self.tileMap[row][col]==None:
                    fp.write("None")
                else:
                    mapEntry=self.tileMap[row][col]
                    fp.write(mapEntry)
                if col<self.mapWidth-1: #suppress comma on last item in row
                    fp.write(",") # comma is our column field delimiter
            fp.write("\n")
        fp.close()
    def loadMap(self,filename):
        fp = open(filename,"r")
        for line in fp:
            line=line.strip()
            if len(line)==0 or line[0]=='#': # skip blank lines and comment lines
                continue
            (attribute,value)=line.split("=") # divide the line into the two sides of the equal
            if attribute=="mapWidth":
                self.mapWidth=int(value)
            if attribute=="mapHeight":
                self.mapHeight=int(value)
            if attribute=="tileWidth":
                self.tileWidth=int(value)
            if attribute=="tileHeight":
                self.tileHeight=int(value)
            if attribute=="tileMap":
                for row in range(0,self.mapHeight):
                    mapline=fp.readline().strip() #read in row
                    entry_list=mapline.split(",") #split row on comma
                    for col in range(0,len(entry_list)):
                        if entry_list[col]=="None":
                            self.tileMap[row][col]=None
                        else:
                            self.tileMap[row][col]=entry_list[col]
        fp.close()
    def getCollisionSetCircle(self,testCircleX,testCircleY,testCircleR):
        collisionSet=[]
        for mapRow in range(0,self.mapHeight):
            for mapCol in range(0,self.mapWidth):
                mapEntryKey=self.tileMap[mapRow][mapCol]
                if mapEntryKey!=None:
                    rectY1 = mapRow*self.tileTypes[mapEntryKey].tileHeight
                    rectX1 = mapCol*self.tileTypes[mapEntryKey].tileWidth
                    rectY2 = rectY1 + self.tileTypes[mapEntryKey].tileHeight
                    rectX2 = rectX1 + self.tileTypes[mapEntryKey].tileWidth

                    if collideCircleRectangle(testCircleX,testCircleY,testCircleR,rectX1,rectY1,rectX2,rectY2):
                        tileCenterX=(rectX1+rectX2)/2
                        tileCenterY=(rectY1+rectY2)/2
                        tileDistance=distance(testCircleX,testCircleY,tileCenterX,tileCenterY)
                        collisionSet.append(CollisionTile(mapEntryKey,mapCol,mapRow,tileCenterX,tileCenterY,tileDistance))
        return collisionSet

    def collision(self,cx,cy,cr):
        collide_list=[]
        for row in range(0,self.mapHeight):
            for col in range(0,self.mapWidth):
                if self.tileMap[row][col]==None:
                    pass
                else:
                    if collide.collideCircleRectangle(cx,cy,cr,col*self.tileWidth,row*self.tileHeight,(col+1)*self.tileWidth,(row+1)*self.tileHeight):
                       collide_list.append(self.tileMap[row][col])
        return collide_list


class CollisionTile(object):
    def __init__(self,mapEntryKey,mapCol,mapRow,mapTileCenterX,mapTileCenterY,collideDistance):
        self.mapEntryKey=mapEntryKey
        self.mapCol=mapCol
        self.mapRow=mapRow
        self.mapTileCenterX=mapTileCenterX
        self.mapTileCenterY=mapTileCenterY
        self.collideDistance=collideDistance

def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def nextDictKey(dictionary,key):
    keyList = sorted(dictionary.keys())
    currentIndex=keyList.index(key)
    newIndex=currentIndex+1
    if newIndex>len(keyList)-1:
        newIndex=0

    return keyList[newIndex]
def prevDictKey(dictionary,key):
    keyList = sorted(dictionary.keys())
    currentIndex=keyList.index(key)
    newIndex=currentIndex-1
    if newIndex<0:
        newIndex=len(keyList)-1
    return keyList[newIndex]