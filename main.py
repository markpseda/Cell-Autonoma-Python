# Import a library of functions called 'pygame'
import pygame
import random
import copy
import class_decs

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

 #########################where the party gets started###################################

pygame.display.set_caption("Cellular Autonoma")
clock = pygame.time.Clock()
theWorld = World(80, 160)

# Set the height and width of the screen
size = [10*theWorld.height, 10*theWorld.width]
screen = pygame.display.set_mode(size)

def main():
    done = False
    insertRandinWorld(height*16)
    global theWorld
    while not done:
        clock.tick(100)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
        screen.fill(WHITE)
        currentCount = 0 #resets the count
        for i in range (0, theWorld.height):
            for k in range (0, theWorld.width):
                theWorld.setNextWorld(i,k)
                if theWorld.currWorld[i][k] == 1:
                    currentCount += 1
                    pygame.draw.rect(screen, GREEN, [i*10, k*10, 10, 10])
        pygame.display.flip()
        theWorld.currWorld = numpy.copy(NextWorld)
        if currentCount <= 5:
            theWorld.insertRandinWorld(theWorld.height)
# Be IDLE friendly
main()
pygame.quit()
