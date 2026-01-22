import pygame
import random

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

# CONSTANTS
WIDTH, HEIGHT = 460, 560
FPS = 60
BG_COLOR = 39, 36, 74           #even darker purple
BG_GRID_COLOR = 57, 52, 107     #darker purple
GRID_LINE_COLOR = 144, 134, 255 #light purple

grid_h, grid_w = 400, 400
title_h, title_w = 100, 460

# Create Snake Game Window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set caption of window
pygame.display.set_caption("Snake Game")

# draws grid on screen
def draw_grid(start_x, start_y, dist, len, grid_size):
    pygame.draw.line(window, GRID_LINE_COLOR, (45, 130), (45, 530), 1)

    for i in grid_size:

        # determine end_x, end_y:
        end_x, end_y = start_x+dist, start_y

        # draw vertical lines
        pygame.draw.line(window, GRID_LINE_COLOR, (start_x, start_y), (end_x, end_y), 1)

        # draw horizontal lines

        # shift start_x and start_y over by dist
        start_x

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

            # set window bg color
            window.fill(BG_COLOR)

            # background for game title
            pygame.draw.rect(window, BG_GRID_COLOR, pygame.Rect(0,0, title_w, title_h), 0)
            # outline for game title
            pygame.draw.rect(window, "black", pygame.Rect(0,0, title_w, title_h), 2)
            
            # background for game grid
            pygame.draw.rect(window, BG_GRID_COLOR,pygame.Rect(30, 130, grid_w, grid_h), 0)
            # outline for game grid
            pygame.draw.rect(window, "black", pygame.Rect(30, 130, grid_w, grid_h), 2)
            
            # first line of the grid
            pygame.draw.line(window, GRID_LINE_COLOR, (45, 130), (45, 530), 1)


            # update window
            pygame.display.flip()

    # Close the window right after the game loop
        # bc the main loop ONLY ends in the event 
        # that the window is closed
    pygame.quit()

if __name__ == "__main__":
    main(window)
