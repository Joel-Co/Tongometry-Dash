import pygame
import random

#Initialize Pygame
pygame.init()

#Create the screen
screenW = 800
screenH = 600
screen = pygame.display.set_mode((screenW, screenH))

#Caption and icon
pygame.display.set_caption("Space-Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 500
playerY = 500
playerX_change = 0
playerY_change = 0
playerSpeed = 5


#background = pygame.image.load("bg.jpg")


def player(x, y):
    screen.blit(playerImg, (x, y))
 
keys = []

#Game Loop
running = True
while running:

    #RGB
    #screen.fill((0, 0, 0))
    #background

#screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(running)
            running = False
            print(running)
        #If keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("space is pressed")
                screen.fill((0, 0, 255))


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("kestroke has been released")
                screen.fill((0, 0, 0))

    playerX += playerX_change
    player(playerX, playerY)
    
    #Avoid OOB
    if playerX <= 0:
        playerX = 0
    if playerX >= screenW - 64:
        playerX = screenW - 64


    
    pygame.display.update()
