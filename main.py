# Import a library of functions called 'pygame'
import pygame
import copy
from cell import *
from music import *
from world import *

# Define the colors we will use in RGB format - only BLACK is used. 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

######################where the party gets started##########################
pygame.init() #initializes the game engine
pygame.display.set_caption("Cellular Autonoma")
clock = pygame.time.Clock()
multiplier = 15
theWorld = World(800/multiplier, 1600/multiplier)


# Set the height and width of the screen
size = [multiplier*theWorld.height, multiplier*theWorld.width]
screen = pygame.display.set_mode(size)
##################INSERT SONG######################
##musicPath = "song.wav" 

def main():
    global theWorld
    done = False
    theWorld.insertRandinWorld(theWorld.height*15)
    theWorld.copyWorld()
    
    #######If you added a song, uncomment these.
    ##mp = MusicPlayer()
    ##mp.initialize_music()
    ##mp.load_song(musicPath)
    ##mp.play_song()
    #######

    while not done:
        clock.tick(1000)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
        screen.fill(WHITE)
        currentCount = theWorld.printWorld(screen,pygame, multiplier)
        pygame.display.flip()

        ##if not mp.is_Playing():
            ##mp.load_song(musicPath)
            ##mp.play_song()
            ##theWorld.insertRandinWorld(theWorld.height*10)

        if currentCount <= 5:
            theWorld.insertRandinWorld(theWorld.height*5)
        theWorld.copyWorld()
# Be IDLE friendly
main()
pygame.quit()
