# Import a library of functions called 'pygame'
import pygame
import numpy
from math import pi
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [500, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Cellular Autonoma")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 

x = numpy.zeros((50,50))

x[1][4] = 1

x[2][3] = 1

while not done:
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    screen.fill(WHITE)

    for i in range (0, 50):
        for k in range (0, 50):
            if x[i][k] == 1:
                pygame.draw.rect(screen, BLACK, [i*10, k*10, 10, 10])
    
          
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()