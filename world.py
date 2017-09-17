import numpy
import random
from cell import *



class World:
    def __init__(self, w, h):
        self.height = h
        self.width = w
        self.currWorld = [[]]
        self.nextWorld = [[]]
        for i in range(0,h):
            self.currWorld.append([])
            self.nextWorld.append([])
            for j in range(0,w):
                self.currWorld[i].append(Cell(0,0,0,False))
                self.nextWorld[i].append(Cell(0,0,0,False))

    #this function checks the coordinate given and sets the NextWorld matrix for that spot
    def setNextWorld(self, x ,y):
        neighbors = []
        for i in range(-1,2):
            for k in range(-1,2):
                if self.currWorld[(x+i) % self.height][(y+k) % self.width].alive == True and not(i == 0 and k == 0):
                    neighbors.append(self.currWorld[(x+i) % self.height][(y+k) % self.width])
        if self.currWorld[x][y].alive == True and len(neighbors) == 2:
            self.nextWorld[x][y].updateHealth(True)
        elif len(neighbors) == 3:
            self.nextWorld[x][y].updateHealth(True)
            self.nextWorld[x][y].updateColor((neighbors[0].red+neighbors[1].red+neighbors[2].red)/3,(neighbors[0].green+neighbors[1].green+neighbors[2].green)/3,(neighbors[0].blue+neighbors[1].blue+neighbors[2].blue)/3)
        else:
            self.nextWorld[x][y].updateHealth(False)
            self.nextWorld[x][y].updateColor(0,0,0)

    def insertRandinWorld(self, x):
        for i in range(0, x):
            a = random.randrange(0,self.height)
            b = random.randrange(0,self.width)
            self.nextWorld[a][b].updateHealth(True)
            self.nextWorld[a][b].updateColor(random.randrange(0,256),random.randrange(0,256),random.randrange(0,256))

    def copyWorld(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.currWorld[i][j].copyCell(self.nextWorld[i][j])

    def printWorld(self,s,p):
        currentCount = 0
        for i in range (0, self.height):
            for k in range (0, self.width):
                self.setNextWorld(i,k)
                if self.currWorld[i][k].alive == True:
                    currentCount += 1
                    p.draw.rect(s, (self.currWorld[i][k].red, self.currWorld[i][k].green, self.currWorld[i][k].blue), [i*10, k*10, 10, 10])
        return currentCount
