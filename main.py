# Import a library of functions called 'pygame'
import pygame
import copy
from class_decs import *
from music import *

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
musicPath = "electronic.wav"


def main():
    global theWorld
    done = False
    theWorld.insertRandinWorld(theWorld.height*15)
    theWorld.copyWorld()
    MusicPlayer.initialize_music()
    MusicPlayer.load_song(musicPath)
    MusicPlayer.play_song()

    while not done:
        clock.tick(1000)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
        screen.fill(WHITE)
        currentCount = theWorld.printWorld(screen,pygame) #resets the count
        pygame.display.flip()

        if not MusicPlayer.is_Playing():
            MusicPlayer.load_song(musicPath)
            MusicPlayer.play_song()
            theWorld.insertRandinWorld(theWorld.height*10)

        if currentCount <= 5:
            theWorld.insertRandinWorld(theWorld.height*5)
        theWorld.copyWorld()
# Be IDLE friendly
main()
pygame.quit()
