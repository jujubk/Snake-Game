# The Snake Game

This is my first lone attempt making a video game with python without any tutorials. I will be using the Python language and primarily using the Pygame module to develop this game. If I need assets, I will use premade ones for the sake of not losing my mind. This README file will be used as a file to keep track of all of my notes and documentation

## Game Description

In the Snake Game, you play as a snake, trying to collect each dot on the screen. One dot shows up on the screen at a time at random. You play on a grid in which the dot that shows on the screen takes up one grid space. the snake fills 2 grid spaces at the start. The snake essentially is made of dots or grid spaces, but it cannot overlap, each 'dot' or section of the snake must fill only one spot on the grid space at a time. The Snake begins with as the length of two dots, then as you collect a dot you grow in length by one dot. 

## Objective
You are playing as a snake, made up of dots, who is trying to collect as many dots as possible without crashing into itself or the wall. You win by collecting all dots without crashing into the wall or yourself, and filling the entire grid space with your body; leaving no space for more dots to spawn. This task becomes increasingly more difficult as the snake's velocity increases for each level. The game ends if the user/snake crashes into a wall or itself.

# Specifications For Game Development

## Movement
You play on a grid screen, where one dot of the snake fits into one grid block. 
- the snake can go in any direction except back into itself (3 directions)
- On the grid, your body follows through on past movement decicions.
- so that means, the game must remember your prev movements in some way

## Game Window

The title and game grid are on the same screen. 

### Title frame
The title frame is at the top of the window and it is where the player can start the game. This frame includes the game title, instructions, current score and high score. 

### Starting a game
To start a game the player can press any button on their keyboard. Once a button is pressed, the snake object will begin moving forward and the player can control the movements with the arrowkeys.

### Pausing or ending a game
There won't be a specific control for pausing the game in early editions of this game. It can be added later on, but if the player wans to end the game, they either crash, to lose the game, or press the 'X' at the top of the window.

### Game grid
The game 