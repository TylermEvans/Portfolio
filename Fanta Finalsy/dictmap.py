
import pygame
import time
                         
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
    def __init__(self,mapWidth=25,mapHeight=19,tileWidth=32,tileHeight=32):
        self.mapWidth=mapWidth
        self.mapHeight=mapHeight
        self.tileWidth=tileWidth
        self.tileHeight=tileHeight
        self.tileMap=[]
        for row in range(0,mapHeight):
            self.tileMap.append([None]*mapWidth)
        self.tileTypes={}
    def addTileType(self,tileId,tileType):
        self.tileTypes[tileId]=tileType

    def renderTile(self,screenCol,screenRow,mapEntry):
        screenX=screenCol*self.tileWidth
        screenY=screenRow*self.tileHeight
        screen.blit(mapEntry.tileSurf,(screenX,screenY))

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
    
pygame.init()

screen=pygame.display.set_mode((800,600),pygame.SWSURFACE,24)

map1=TileMap()

map1.addTileType("MTN",TileType("Tiles2.png",(6,11)))

map1.addTileType("Water",TileType("Tiles2.png",(21,3)))
map1.addTileType("Water2",TileType("Tiles2.png",(22,3)))
map1.addTileType("Water3",TileType("Tiles2.png",(0,4)))


map1.addTileType("Tree",TileType("Tiles2.png",(0,1)))


map1.addTileType("Wall",TileType("Tiles2.png",(13,0)))
map1.addTileType("Wall2",TileType("Tiles2.png",(22,1)))


map1.addTileType("Dungeon",TileType("Tiles2.png",(15,0)))
map1.addTileType("Csl",TileType("Tiles2.png",(0,12)))
map1.addTileType("Csl2",TileType("Tiles2.png",(1,12)))
map1.addTileType("Csl3",TileType("Tiles2.png",(4,12)))
map1.addTileType("Csl4",TileType("Tiles2.png",(3,12)))


map1.addTileType("Gd",TileType("Tiles2.png",(0,0)))
map1.addTileType("Gd2",TileType("Tiles2.png",(22,0)))

map1.addTileType("Town",TileType("Tiles2.png",(6,12)))
map1.addTileType("Boss1",TileType("Tiles2.png",(10,0)))
map1.addTileType("Boss2",TileType("Tiles2.png",(13,4)))
map1.addTileType("Stat",TileType("Tiles2.png",(17,17)))
map1.addTileType("Penta",TileType("Tiles2.png",(12,4)))
map1.addTileType("LGd",TileType("Tiles2.png",(7,0)))
map1.addTileType("DBWall",TileType("Tiles2.png",(16,2)))
map1.addTileType("FTN",TileType("Tiles2.png",(7,12)))
map1.addTileType("Statue",TileType("Tiles2.png",(18,17)))
map1.addTileType("DdGd",TileType("Tiles2.png",(22,1)))
map1.addTileType("BMGd",TileType("Tiles2.png",(19,8)))
map1.addTileType("DLock",TileType("Tiles2.png",(9,5)))
map1.addTileType("BWall",TileType("Tiles2.png",(18,1)))
map1.addTileType("BMdoor",TileType("Tiles2.png",(0,15)))
map1.addTileType("WdGd",TileType("Tiles2.png",(17,2)))
map1.addTileType("DdDoor",TileType("Tiles2.png",(16,6)))
map1.addTileType("DUnlock",TileType("Tiles2.png",(10,5)))
map1.addTileType("Start",TileType("Tiles2.png",(12,15)))
map1.addTileType("Trash",TileType("trash.png",(0,0)))





clock = pygame.time.Clock()

curTileKey="Wall"

while True:
    pygame.event.pump()
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_ESCAPE]:
        break
    if keysPressed[pygame.K_s] and (keysPressed[pygame.K_RCTRL] or keysPressed[pygame.K_LCTRL]):
        map1.saveMap("map1.txt")
        map1.saveTileTypes("map1tiles.txt")
        print("Saved")
        while keysPressed[pygame.K_s] and (keysPressed[pygame.K_RCTRL] or keysPressed[pygame.K_LCTRL]):
            pygame.event.pump()
            keysPressed = pygame.key.get_pressed()

    if keysPressed[pygame.K_l] and (keysPressed[pygame.K_RCTRL] or keysPressed[pygame.K_LCTRL]):
        map1.loadMap("map1.txt")
        map1.saveTileTypes("map1tiles.txt")
        print("Loaded")
        while keysPressed[pygame.K_l] and (keysPressed[pygame.K_RCTRL] or keysPressed[pygame.K_LCTRL]):
            pygame.event.pump()
            keysPressed = pygame.key.get_pressed()

    if keysPressed[pygame.K_LEFT]:
        curTileKey=prevDictKey(map1.tileTypes,curTileKey)
        print("Current Tile:",curTileKey)
        while keysPressed[pygame.K_LEFT]:
            pygame.event.pump()
            keysPressed = pygame.key.get_pressed()

    if keysPressed[pygame.K_RIGHT]:
        curTileKey=nextDictKey(map1.tileTypes,curTileKey)
        print("Current Tile:",curTileKey)
        while keysPressed[pygame.K_RIGHT]:
            pygame.event.pump()
            keysPressed = pygame.key.get_pressed()

        
    (mx,my)=pygame.mouse.get_pos()
    (lb,mb,rb)=pygame.mouse.get_pressed()
    mouseCol=int(mx/map1.tileWidth)
    mouseRow=int(my/map1.tileHeight)
    if lb==True:
        map1.setTileMapEntry(mouseCol,mouseRow,curTileKey)
    if rb==True:
        map1.setTileMapEntry(mouseCol,mouseRow,None)

    screen.fill((0,0,0))  #clear screen

    map1.renderMap()


    newSurf = map1.tileTypes[curTileKey].tileSurf.copy()
    newSurf.set_alpha(150)    
    screen.blit(newSurf,(mouseCol*map1.tileWidth,mouseRow*map1.tileHeight))    
    pygame.draw.rect(screen,(0,0,255),(mouseCol*map1.tileWidth,mouseRow*map1.tileHeight,map1.tileWidth,map1.tileHeight),2)

    pygame.display.flip()

    clock.tick(60)
    
    #print(clock.get_fps())
print(map1.tileMap)


pygame.display.quit()
