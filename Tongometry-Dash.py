'''Descripcion'''

import pygame

#Initialize Pygame
pygame.init()
pygame.font.init()


#Loading the images
images = {}
images["icon"] = pygame.image.load("images/space-invaders.png")
images["player"] = pygame.image.load("images/space-invaders.png")
images["bg"] = pygame.image.load("images/bg.png")
images["bg2"] = pygame.image.load("images/bg2.png")

#Creates the fonts
bigFont = pygame.font.SysFont('Times New Roman', 60)
smlFont = pygame.font.SysFont('Times New Roman', 30)



#Definition of the classes:

class Button():
    '''
    This class creates a button that is displayed on the screen
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
        '''Displays the button (rect and text) on the screen'''
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        screen.blit(self.buttonTextSurface, (self.x, self.y))
        
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



#Create the screen
screenW, screenH = 1000, 500
screen = pygame.display.set_mode((screenW, screenH))

#Caption and icon
pygame.display.set_caption("Space-Invaders")
pygame.display.set_icon(images["icon"])


keys = []
frame = 0

player = Player(images["player"])
background = GameObject(0, 0, images["bg"])


startButton = Button(screenW / 2 - 200 / 2, 200, 200, 100, (100, 100, 200), "START")
#In variable names, TS stands for Text Surface
titleTS = bigFont.render("Tongometry Dash", False, (50, 50, 150))
creditsTS = smlFont.render("Creado por I. BORTHA, J. COLASO, T. ONGA. 2020", False, (50, 50, 150))


#Game loop
running = True
while running:

    #Code for the first frame
    if frame == 0:
        screen.fill((200, 255, 255))
        
        startButton.display()
        screen.blit(titleTS, (300, 25))
        screen.blit(creditsTS, (180, 460))

        #Events of the first frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONUP:
                #Button that goes to the next frame
                if startButton.press():
                    screen.blit(images["bg"], (0, 0))
                    frame = 1


    #Code for the second frame
    elif frame == 1:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.y = 100

            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.y = 200

        background.display()
        player.display()

    pygame.display.update()


