import pygame
import object 
'''
    # a snake object will be made up of multiple Objects, representing the snakes body parts. 
    # there will be a sorted list of objects (body parts) of the snake
    # every time 
'''
class Snake():

    # def __init__(self):
    #           #
    #     self.snake_obj = None
    #     self.velocity = None
    #     self.direction = None
    #     self.length = None

    #     # initial snake objects
    #     self.snake_coords = None

    def __init__(self, velocity, x, y, w, h, color):
        #
        self.snake_obj = object.Object(x, y, w, h, color)

        self.velocity = velocity
        self.direction = "right"
        self.length = 1

        # initial snake objects
        self.snake_coords = []

# GET_VALUE FUNCTIONS
    def get_x(self):
        self.snake_obj.get_x()

    def get_y(self):
        self.snake_obj.get_y()

    def get_width(self):
        self.snake_obj.get_w()

    def get_height(self):
        self.snake_obj.get_h()

    def get_color(self):
        self.snake_obj.get_color()
    
    def get_velocity(self):
        if self.velocity == None:
            print("This object's velocity is undefined")
        return self.velocity
        
    def get_direction(self):
        if self.direction == None:
            print("This object's direction is undefined")
        return self.direction
    
    def get_length(self):
        if self.length == None:
            print("This object's length is undefined")
        return self.length
    
    def get_snake_coords(self):
        if self.snake_coords == None:
            print("There are no recorded coordinates for this object")
        return self.snake_coords
    
    def get_snake_obj(self):
        if self.snake_obj == None:
            print("This object has no defined Object")
        return self.snake_obj
    
# PRINT_VALUE FUNCTIONS:    
    def print_velocity(self):
        print("\nVelocity: ", self.get_velocity())

    def print_direction(self):
        print("\nDirection: ", self.get_direction())
    
    def print_length(self):
        print("\nLength: ", self.get_length())

    def print_snake_coords(self):
        print("\nSnake Coordinates: ", self.get_snake_coords())

    def print(self):
        self.snake_obj.print()
        self.print_velocity()
        self.print_direction()
        self.print_length()
        self.print_snake_coords()

# MOVEMENT FUNCTIONS:

    # updates location of snake on the surface using the snake_coords
    def update(self, surface, color):
        pygame.draw.rect(surface, color, self.snake_obj)
        

