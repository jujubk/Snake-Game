import pygame
import random
import Snake
from Dot import Dot

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

        ## CONSTANTS ##

WIDTH, HEIGHT = 460, 560

# COLORS:
BG_COLOR = 39, 36, 74           # dark purple
BG_GRID_COLOR = 57, 52, 107     # lighter purple
GRID_LINE_COLOR = 114, 84, 128  # even lighter purple
DOT_COLOR = "white"
SNAKE_COLOR = None              # TBD

# OTHER SIZES & VELOCITIES
GRID_BLOCK_SIZE = 16
GRID_H, GRID_W = 400, 400
TITLE_H, TITLE_W = 100, 460

FPS = 1

SNAKE_VEL = GRID_BLOCK_SIZE

# OTHER 
GRID_BLOCK_PXL_SIZE = 25 # 25 x 25 blocks
grid_size_y = 25
game_grid_start_x = 30
game_grid_start_y = 130
snake_start_x, snake_start_y = 222, 338

# initialize the dot pygame rect
global dot
dot = pygame.Rect(0,0, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE)

# Create Snake Game Window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set caption of window
pygame.display.set_caption("Snake Game")

        ## FUNCTIONS ##

# draws grid on window
    # no return value
    # code moved out of main function for readability
def draw_grid(start_x, start_y):
  
    # print vertical lines on the grid
    end_x, end_y = start_x, start_y+GRID_H

    for i in range(GRID_BLOCK_PXL_SIZE+1):

        # print vertical line
        pygame.draw.line(window, GRID_LINE_COLOR, (start_x, start_y), (end_x, end_y), 1)

        # update start and end values
        start_x, start_y = start_x+GRID_BLOCK_SIZE, start_y
        end_x, end_y = start_x, start_y+GRID_H

    # print horizontal lines on the grid
    start_x, start_y = 30, 130
    end_x, end_y = start_x+GRID_H, start_y

    for i in range(GRID_BLOCK_PXL_SIZE+1):

        # print horizontal line
        pygame.draw.line(window, GRID_LINE_COLOR, (start_x, start_y), (end_x, end_y), 1)

        # update start and end values:
        start_x, start_y = start_x, start_y+GRID_BLOCK_SIZE
        end_x, end_y = start_x+GRID_H, start_y 

# returns two lists (x_list, y_list) 
    # these lists contain possible x and y combinations for the 
    # dot to spawn in accordance to this grid space
def dot_coord_lists(x_low, x_high, y_low, y_high):

    # init x & y lists
    x_list,y_list = [],[]

    # init variables
    done = False
    x = x_low
    y = y_low

    while(not done):

    # if x value is in range append it to the x list
    # else end loop
        if x >= x_low and x <= x_high:
            x_list.append(x)
            x+= GRID_BLOCK_SIZE
        else:
            done = True

        if y >= y_low and y <= y_high:
            y_list.append(y)
            y+= GRID_BLOCK_SIZE
        else:
            done = True
    
    return x_list, y_list

# randomize the coords from given coordinate lists
    # returns x, y values
def randomize_coords(x_list, y_list):

    x = random.choice(x_list)
    y = random.choice(y_list)
    return x,y
    
# updates dot coords and draws the dot on the game grid
def update_dot(x_list, y_list):
    # randomize coordinates using randomize_coords function 
    x,y = randomize_coords(x_list, y_list)

    # update the dot pygame.Rect
    dot = pygame.Rect(x,y,GRID_BLOCK_SIZE,GRID_BLOCK_SIZE)

    # draw the dot on the window
    pygame.draw.ellipse(window, DOT_COLOR, dot, GRID_BLOCK_SIZE)

# MAIN FUNCTION
    # pass 
def main(window):
    
    # flag for the main game loop
    run = True

    # possible x and y values for the dot
    x_list, y_list = dot_coord_lists(30,414,130,514)

    # init dot coords
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
        pygame.draw.rect(window, BG_GRID_COLOR, pygame.Rect(0,0, TITLE_W, TITLE_H), 0)
        # background for game grid
        pygame.draw.rect(window, BG_GRID_COLOR,pygame.Rect(30, 130, GRID_W, GRID_H), 0)
        
        # draw the grid on game block
        draw_grid(30, 130)

        # outline for game title
        pygame.draw.rect(window, "white", pygame.Rect(0,0, TITLE_W, TITLE_H), 2)
        # outline for game grid
        pygame.draw.rect(window, "white", pygame.Rect(30, 130, GRID_W, GRID_H), 2)
        
        # update dot position on game grid
        update_dot(x_list, y_list)

        # update window
        pygame.display.flip()

    # Close the window right after the game loop
        # bc the main loop ONLY ends in the event 
        # that the window is closed
    pygame.quit()

if __name__ == "__main__":
    main(window)
