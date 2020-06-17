#!/usr/bin/python3 


# Importing modules. 
import pygame 
import time 
import random 

pygame.init() # Initializing the screen 

# Adding RGB colors. 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
 
width = 800 # Width of the screen 
height = 600 # Height of the screen 
 
display = pygame.display.set_mode((width, height)) # Setting the display dimensions 
pygame.display.set_caption('Snake Game') # Setting a window caption 
clock = pygame.time.Clock() # FPS 
snakeBlock = 10 # Snake block 
fps = 15 # FPS count 

# Text font styles
font_style = pygame.font.SysFont("comicsansms", 50)
score_font = pygame.font.SysFont("comicsansms", 30)
 
# Function that displays the player score 
def playerScore(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])
# Initializing the snake. 
def snake(snakeBlock, snakeList): 
    for x in snakeList:
        pygame.draw.rect(display, green, [x[0], x[1], snakeBlock, snakeBlock])
# Displaying a message. 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width / 2, height / 2))
    display.blit(mesg, text_rect)
# Main game logic and loop. 
def gameLoop():
    gameOver = False
    gameClose = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0 # X axis change 
    y1_change = 0 # Y axis change 
    snakeList = [] 
    snakeLength = 1 # Snake length 
    # Food 
    foodx = round(random.randrange(0, width - snakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snakeBlock) / 10.0) * 10.0
    # While the game has not ended... 
    while not gameOver:
        while gameClose == True: 
            display.fill(black) # Filling the black color on the display 
            message("Game over!", white) # Message that player lost. 
            playerScore(snakeLength - 1) 
            pygame.display.update() # Updating the screen 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # Listening for the key strokes. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True 
            # Movement of the snake. 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        # If the snake hit the borders of the screen. 
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            gameClose = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(black) # Filling the screen with black color 
        pygame.draw.rect(display, red, [foodx, foody, snakeBlock, snakeBlock]) # Drawing the food. 
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for x in snakeList[:-1]:
            # If the snake hit itself the game ends. 
            if x == snakeHead:
                gameClose = True
 
        snake(snakeBlock, snakeList)
        playerScore(snakeLength - 1)
        pygame.display.update() # Updating the screen. 
        # If the snake eats the food it draws the food again on random places. 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snakeBlock) / 10.0) * 10.0
            snakeLength += 1
        clock.tick(15) # Setting the fps(15). 
    pygame.quit() # Quiting the game. 
    quit()# Quiting the program. 

# Function that calls the main game logic. 
def main(): 
    gameLoop()
main()