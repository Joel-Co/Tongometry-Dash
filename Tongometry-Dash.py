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
playerSpeed = 4

#Enemy
enemyImg = pygame.image.load("spaceship.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 6

#Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
#ready means you can't see the bullet 
#fired means you can 
bullet_state = "ready"

background = pygame.image.load("bg.jpg")


def player(x, y):
    screen.blit(playerImg, (x, y))
    
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletImg, (x + 16, y + 10))

keys = []

#Game Loop
running = True
while running:

    #RGB
    screen.fill((0, 12, 0))
    #background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(running)
            running = False
            print(running)
        #If keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left is pressed")
                playerX_change = -playerSpeed
            if event.key == pygame.K_RIGHT:
                print("right is pressed")
                playerX_change = playerSpeed
            if event.key == pygame.K_SPACE:
                print("space is pressed")
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("left is released")
            if event.key == pygame.K_RIGHT:
                print("right is released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("kestroke has been released")
                playerX_change = 0


    playerX += playerX_change
    player(playerX, playerY)
    
    #Avoid OOB
    if playerX <= 0:
        playerX = 0
    if playerX >= screenW - 64:
        playerX = screenW - 64


    enemyX += enemyX_change
    enemy(enemyX, enemyY)
    
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    if enemyX >= screenW - 64:
        enemyX_change = -1
        enemyY += enemyY_change

    #bullet movement
    if bullet_state is "fired":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = playerY + 10
        bullet_state = "ready"
        
    
    pygame.display.update()
