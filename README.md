# The Snake Game

This is my first lone attempt making a video game with python without any tutorials. I will be using the Python language and primarily using the Pygame module to develop this game. If I need assets, I will use premade ones for the sake of not losing my mind. This README file will be used as a file to keep track of all of my notes and documentation

## Game Description

In the Snake Game, you play as a snake, tyring to collect each dot on the screen. One dot shows up on the screen at a time at random. You play on a grid in which the dot that shows on the screen takes up one grid space. the snake fills 2 grid spaces at the start. The snake essentially is made of dots or grid spaces, but it cannot overlap, each 'dot' or section of the snake must fill only one spot on the grid space at a time. 

## Objective
You are playing as a snake, made up of dots, who is trying to collect as many dots as possible without crashing into itself or the wall.

### Movement
You play on a grid screen, where one dot of the snake fits into one grid block. 
- the snake can go in any direction except back into itself (3 directions)
- On the grid, your body follows through on past movement decitions.
- so that means, the game must remember your prev movements in some way


_where_to_start_

- build the screen
    - background image
       - download background image
       - import 
    - draw the sprites, or get asset for sprite
    - build a walkable grid for the snake
    - 

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

# Specifications
Listed here are the specifications of how everything will work and brainstorm of how it will be built.

## Game Snake 
- 
1. 
## Game Grid
1. make window

2. draw grid lines on the window

3. outline the title rectangle and game grid rectangle

## Dots on the grid

1. dot will spawn in random locations around the game grid
- random x and y values will be selected
- then a dot will be drawn at that location

2. dot cannot spawn on a space the snake is occupying
- make function that checks location(s) of the snake

## Building sprites/assets
- build snake
    > 