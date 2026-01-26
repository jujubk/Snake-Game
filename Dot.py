import pygame
import random
###

# 
class Dot:

    def __init__(self):

        self.width = 16
        self.height = 16    
        self.color = "white"
        self.x = 0
        self.y = 0

        self.dot = pygame.Rect(self.x,self.y, self.width, self.height)

# draw the dot on the specified surface
def draw(self, surface):
    pygame.draw.ellipse(surface, self.color, self.dot, self.width)

# get random value in certain given range
def random_val(low, high):
    return random.randrange(low, high)

# randomize the coordinates of the dot
def randomize_coords(self, x_low, x_high, y_low, y_high):
    self.x = random_val(x_low, x_high)
    self.y = random_val(y_low, y_high)