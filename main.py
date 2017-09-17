# Import a library of functions called 'pygame'
import pygame
import random
import numpy
from math import pi
import copy
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 

 
 #########################where the party gets started###################################
height = 160
width = 80
World = numpy.zeros((height,width))
NextWorld = numpy.zeros((height,width))

# Set the height and width of the screen
size = [10*height, 10*width]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Cellular Autonoma")
 
clock = pygame.time.Clock()

#this function checks the coordinate given and sets the NextWorld matrix for that spot
def setNextWorld(x,y):
    neighbors = 0
    global NextWorld
    for i in range(-1,2):
        for k in range(-1,2):
            if World[(x+i) % height][(y+k) %width] == 1 and not(i == 0 and k == 0):
                neighbors += 1
    if World[x][y] == 1 and neighbors == 2:
        NextWorld[x][y] = 1
    elif neighbors == 3:
        NextWorld[x][y] = 1
    else:
        NextWorld[x][y] = 0

def insertRandinWorld(x):
    global World
    for i in range(0, x):
        World[random.randrange(0,height)][random.randrange(0,width)] = 1
        
def main():
    done = False
    insertRandinWorld(height*16)
    global World
    global NextWorld
    while not done:
        clock.tick(100)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
        screen.fill(WHITE)
        currentCount = 0 #resets the count
        for i in range (0, height):
            for k in range (0, width):
                setNextWorld(i,k)
                if World[i][k] == 1:
                    currentCount += 1
                    pygame.draw.rect(screen, GREEN, [i*10, k*10, 10, 10])
        pygame.display.flip()
        World = numpy.copy(NextWorld)
        if currentCount <= 5:
            insertRandinWorld(height)
# Be IDLE friendly
main()
pygame.quit()