class RectangularRoom(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.cleaned_tiles=[]
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        l=(int(pos.getX()), int(pos.getY()))
        if l not in self.cleaned_tiles:
            self.cleaned_tiles.append(l)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        self.m=m
        self.n=n
        tile=(self.m,self.n)
        if tile in self.cleaned_tiles:
            return True
        else:
            return False
            
        
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        rx=random.uniform(0,self.width)
        ry=random.uniform(0,self.height)
        return Position(rx,ry)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.x >=0 and pos.x < self.width and pos.y >=0 and pos.y <self.height:
            return True
        else:
            return False
