
import numpy

class Cell:
    red = 0
    green = 0
    blue = 0
    alive = False

class World:
    def __init__(self, h, w):
        self.height = h;
        self.width = w;
        self.currWorld = numpy.zeros((height,width))
        self.nextWorld = numpy.zeros((height,width))

    #this function checks the coordinate given and sets the NextWorld matrix for that spot
    def setNextWorld(self, x,y):
        neighbors = 0
        for i in range(-1,2):
            for k in range(-1,2):
                if self.currWorld[(x+i) % self.height][(y+k) % self.width] == 1 and not(i == 0 and k == 0):
                    neighbors += 1
        if self.currWorld[x][y] == 1 and neighbors == 2:
            self.nextWorld[x][y] = 1
        elif neighbors == 3:
            self.nextWorld[x][y] = 1
        else:
            self.nextWorld[x][y] = 0

    def insertRandinWorld(x):
        for i in range(0, x):
            self.currWorld[random.randrange(0,height)][random.randrange(0,width)] = 1
