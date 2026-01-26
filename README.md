# The Snake Game

This is my first lone attempt making a video game with python without any tutorials. I will be using the Python language and primarily using the Pygame module to develop this game. If I need assets, I will use premade ones for the sake of not losing my mind. This README file will be used as a file to keep track of all of my notes and documentation

## Game Description

In the Snake Game, you play as a snake, tyring to collect each dot on the screen. One dot shows up on the screen at a time. The Snake is made of dots, so once it collects a dot, it increases in length by a single dot.

### Objective
You are playing as a snake, made up of dots, who is trying to collect as many dots as possible without crashing into itself or the wall.

### Movement
You play on a grid screen, where one dot of the snake fits into one grid block. 
- the snake can go in any direction except back into itself (3 directions)
- On the grid, your body follows through on past movement decitions.
- so that means, the game must remember your prev movements in some way


_where_to_start_
- build the screen
    - background image
    - draw the sprites, or get asset for sprite
    - build a walkable grid for the snake

- build 'loading screen'
    - separate screen to press start or exit
    - be able to see highest score?
    
- Snake movement around the grid
    - snake to follow grid path
    - get snake to go in all 4 possible directions
    - tail end of snake follows past movements of head

- Have dots show up on the grid at random locations
    - dot cannot spawn on location that the snake is on
    - dot cannot spawn at least a few blocks away from the snake head
