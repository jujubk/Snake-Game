import pygame
import random
import Snake
from Dot import Dot

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

# CONSTANTS
WIDTH, HEIGHT = 460, 560
FPS = 60
BG_COLOR = 39, 36, 74           #even darker purple
BG_GRID_COLOR = 57, 52, 107     #darker purple
GRID_LINE_COLOR = 114, 84, 128 #light purple
GRID_BLOCK_SIZE = 16
SNAKE_VEL = GRID_BLOCK_SIZE

grid_h, grid_w = 400, 400
title_h, title_w = 100, 460
grid_size_x = 25 # 25 x 25 blocks
grid_size_y = 25
game_grid_start_x = 30
game_grid_start_y = 130
grid_block_x, grid_block_y = 16, 16
snake_start_x, snake_start_y = 222, 338

dot = Dot()

# Create Snake Game Window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set caption of window
pygame.display.set_caption("Snake Game")

# draws grid on screen
def draw_grid(start_x, start_y):
  
    # print vertical lines on the grid
    end_x, end_y = start_x, start_y+grid_h

    for i in range(grid_size_x+1):

        # print vertical line
        pygame.draw.line(window, GRID_LINE_COLOR, (start_x, start_y), (end_x, end_y), 1)

        # update start and end values
        start_x, start_y = start_x+GRID_BLOCK_SIZE, start_y
        end_x, end_y = start_x, start_y+grid_h

    # print horizontal lines on the grid
    start_x, start_y = 30, 130
    end_x, end_y = start_x+grid_h, start_y

    for i in range(grid_size_y+1):

        # print horizontal line
        pygame.draw.line(window, GRID_LINE_COLOR, (start_x, start_y), (end_x, end_y), 1)

        # update start and end values:
        start_x, start_y = start_x, start_y+GRID_BLOCK_SIZE
        end_x, end_y = start_x+grid_h, start_y   

# MAIN FUNCTION
    # pass 
def main(window):
    
    # flag for the main game loop
    run = True

    # init dot coords
    Dot.dot.randomize_coords(30,430, 130,530)

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
        # background for game grid
        pygame.draw.rect(window, BG_GRID_COLOR,pygame.Rect(30, 130, grid_w, grid_h), 0)
        
        # draw the grid on game block
        draw_grid(30, 130)

        # outline for game title
        pygame.draw.rect(window, "white", pygame.Rect(0,0, title_w, title_h), 2)
        # outline for game grid
        pygame.draw.rect(window, "white", pygame.Rect(30, 130, grid_w, grid_h), 2)
        
        # spawn random dot in the tick frame...
        
        dot.draw(window)

        # update window
        pygame.display.flip()

    # Close the window right after the game loop
        # bc the main loop ONLY ends in the event 
        # that the window is closed
    pygame.quit()

if __name__ == "__main__":
    main(window)
