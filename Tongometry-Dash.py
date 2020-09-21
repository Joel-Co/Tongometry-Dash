'''Descripcion'''

import pygame

#Loading the images
images = {}
images["icon"] = pygame.image.load("space-invaders.png")
images["player"] = pygame.image.load("space-invaders.png")
images["bg"] = pygame.image.load("bg.png")
images["bg2"] = pygame.image.load("bg2.png")


class GameObject(object):
    '''Descripcion'''
    
    def __init__(self):
        '''Descripcion'''
        pass
    
    def display(self):
        '''Descripcion'''
        screen.blit(self.image, (self.x, self.y))


class Player(GameObject):
    '''Descripcion'''
    
    def __init__(self, image):
        '''Descripcion'''
        self.x = 500-32
        self.y = 250-32
        self.image = image
    
    def jump(self):
        '''Descripcion'''
        pass
    
    def dieAndRestart(self):
        '''Descripcion'''
        pass
    

class Plataforma(GameObject):
    '''Descripcion'''
    
    def __init__(self):
        '''Descripcion'''
        pass

    
class Danger(GameObject):
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


#Initialize Pygame
pygame.init()

#Create the screen
screenW, screenH = 1000, 500
screen = pygame.display.set_mode((screenW, screenH))

#Caption and icon
pygame.display.set_caption("Space-Invaders")
pygame.display.set_icon(images["icon"])


keys = []

player = Player(images["player"])

screen.blit(images["bg"], (0, 0))


#Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.blit(images["bg2"], (0, 0))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                screen.blit(images["bg"], (0, 0))


    player.display()
    
    pygame.display.update()
