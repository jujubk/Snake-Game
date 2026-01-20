import pygame
import random

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

# CONSTANTS
WIDTH = 600
HEIGHT = 600
FPS = 60
BG_COLOR = 89, 82, 173          #darker purple
GRID_LINE_COLOR = 144, 134, 255 #light purple

# Create Snake Game Window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set caption of window
pygame.display.set_caption("Snake Game")

# My draw function
def draw():
    pass

# MAIN FUNCTION
    # pass 
def main(window):
    
    # flag for the main game loop
    run = True

    # Main game loop
    while(run):

        # tick the clock so that the program maintains
        # a frame rate of FPS (60)
        clock.tick(FPS)

        # check for events in the game loop
        for event in pygame.event.get():

        # First event to check for:

            # event that user closes the window
            if event.type == pygame.QUIT:
                # change the loop flag
                run = False
                # break out of main loop
                break

    # Close the window right after the game loop
        # bc the main loop ONLY ends in the event 
        # that the window is closed
    pygame.quit()

if __name__ == "__main__":
    main(window)
