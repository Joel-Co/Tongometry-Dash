'''Descripcion'''

import pygame
import time
import random

#Initialize Pygame
pygame.init()
pygame.font.init()

#Colors in RGB format
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#Loading the images
images = {}
images["icon"] = pygame.image.load("images/space-invaders.png")
images["player"] = pygame.image.load("images/space-invaders.png")
images["bg"] = pygame.image.load("images/bg.png")
images["tonga"] = pygame.image.load("images/tonga.png")

#Creates the fonts
bigFont = pygame.font.SysFont('Times New Roman', 60)
smlFont = pygame.font.SysFont('Times New Roman', 30)
largeText = pygame.font.Font('freesansbold.ttf', 70)

#Create the screen
gameDisplayW, gameDisplayH = 1000, 500
gameDisplay = pygame.display.set_mode((gameDisplayW, gameDisplayH))

#Caption and icon
pygame.display.set_caption("Tongometry Dash")
pygame.display.set_icon(images["icon"])

#Function to display text made by Isidro
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((gameDisplayW/2),(gameDisplayH/2))
    gameDisplay.blit(TextSurf, TextRect)

#Definition of the classes:
class Button():
    '''
    This class creates a button that is displayed on the gameDisplay
    and that has a color and a text. It's useful for the GUI.
    '''
    def __init__(self, x, y, w, h, color, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        
        self.state = False
        
        self.buttonTextSurface = bigFont.render(self.text, False, (0, 0, 0))

    def display(self):
        '''Displays the button (rect and text) on the gameDisplay'''
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.w, self.h))
        gameDisplay.blit(self.buttonTextSurface, (self.x, self.y))
        
    def press(self):
        '''Checks is the mouse is inside the button or not'''
        pos = pygame.mouse.get_pos()
        if self.x < pos[0] < self.x + self.w and \
           self.y < pos[1] < self.y + self.h:
            return True
        else:
            return False

class GameObject(object):
    '''Descripcion'''
    
    def __init__(self, x, y, image):
        '''Descripcion'''
        self.x = x
        self.y = y
        self.image = image
    
    def display(self):
        '''Descripcion'''
        gameDisplay.blit(self.image, (self.x, self.y))

class Player(GameObject):
    '''Descripcion'''
    
    def __init__(self, image):
        '''Descripcion'''
        self.x = (gameDisplayW * 0.1)
        self.y = (gameDisplayH * 0.35)
        self.w = 64
        self.h = 64
        self.image = image
    
    def jump(self):
        '''Descripcion'''
        pass
    
    def dieAndRestart(self):
        '''Descripcion'''
        pass
    
player = Player(images["player"])
frame = 0

class Danger(GameObject):
    '''Descripcion'''
    
    def __init__(self):
        '''Descripcion'''
        self.x = 1500
        self.y = random.randrange(300, gameDisplayH)
        self.w = 40
        self.h = 40
        
        self.speed = -10

    def display(self, color):
        '''Descripcion'''
        pygame.draw.rect(gameDisplay, color, [self.x, self.y, self.w, self.h])

    def checkOOBAndRestart(self):
        '''Descripcion'''
        if self.x <= 0:
            self.x = 1000
            self.y = random.randrange(200,gameDisplayH)

    def collide(self):
        '''Descripción'''
        if self.x < player.x + player.w and \
           self.x + self.w > player.x and \
           self.y < player.y + player.h and \
           self.y + self.h > player.y:
            restartGame()

class Plataforma(GameObject):
    '''Descripcion'''
    
    def __init__(self):
        '''Descripcion'''
        pass

class Level():
    def __init__(self):
        '''Descripcion'''
        pass

    def printLevel(self):
        '''Descripcion'''
        pass
    
    def displayLevel(self):
        '''Descripcion'''
        pass


startButton = Button(gameDisplayW / 2 - 200 / 2, 200, 200, 100, (100, 100, 200), "START")

#In variable names, TS stands for Text Surface
titleTS = bigFont.render("Tongometry Dash", False, (50, 50, 150))
creditsTS = smlFont.render("Creado por I. BORTHA, J. COLASO, T. ONGA. 2020", False, (50, 50, 150))
    
def titleScreen():
    '''Descripción'''

    global frame
    gameDisplay.fill((200, 255, 255))
        
    startButton.display()
    gameDisplay.blit(titleTS, (300, 25))
    gameDisplay.blit(creditsTS, (180, 460))

    #Events of the first frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
        if event.type == pygame.MOUSEBUTTONUP:
            #Button that goes to the next frame
            if startButton.press():
                gameDisplay.blit(images["bg"], (0, 0))
                frame = 1

def gameplay():
    '''Descripción'''
    
    y_change = 0
    speed = 2
    
    danger = Danger()
    
    keys = {}
    keys["up"]= False
    keys["down"] = False

    background = GameObject(0, 0, images["bg"])

    clock = pygame.time.Clock()
    
    gameExit  = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit  = True
                pygame.quit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    keys["down"] = True
                elif event.key == pygame.K_UP:
                    keys["up"] = True
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    keys["down"] = False
                elif event.key == pygame.K_UP:
                    keys["up"] = False

        if keys["up"] and keys["down"] == False:
            y_change = -10
        elif keys["down"] and keys["up"] == False:
            y_change = 10
        elif keys["down"] and keys["up"]:
            y_change = 0
        elif keys["down"] == False and keys["up"] == False:
            y_change = 0
            
        background.x = background.x - speed  
        if background.x == -1000:
            background.x = 0
        gameDisplay.blit(images["bg"], (background.x + 1000, 0))
        gameDisplay.blit(images["bg"], (background.x, 0))

        player.y += y_change
        player.display()

        if player.y < 0:
            restartGame() 
        if player.y + player.h > gameDisplayH:
            player.y = gameDisplayH - player.h

        danger.x += danger.speed
        danger.display(red)
        danger.checkOOBAndRestart()
        danger.collide()
        
        pygame.display.update()
        clock.tick(120)

def restartGame():
    '''Descripción'''

    message_display('Ouch ouch')
    pygame.display.update()
    player.y = (gameDisplayH * 0.35)
    time.sleep(1)
    gameplay()


#Game loop
running = True
while running:

    #Code for the first frame
    if frame == 0:
        titleScreen()

    #Code for the second frame
    elif frame == 1:
        gameplay()
        pygame.quit()
        quit()

    pygame.display.update()

