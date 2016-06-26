import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second, the general speed of the program
fpsClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 480 # size of the window's width in pixels
WINDOWHEIGHT = 700 # size of the windows' height in pixels
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('CompSi-Fighters')

#Color      R   G   B
BLUE =  (  56, 134, 232)


fighterImg = pygame.image.load('new1.png')
planex = 100
planey = 100
direction = 'right'

while True: # The main game loop
    DISPLAYSURF.fill(BLUE)
    if direction == 'right':
        planex += 5
        if planex > 410:
            planex = 410
    elif direction == 'down':
        planey += 5
        if planey > 615:
            planey = 615
    elif direction == 'left':
        planex -= 5
        if planex < 0:
            planex = 0
    elif direction == 'up':
        planey -= 5
        if planey < 0:
            planey < 0


    DISPLAYSURF.blit(fighterImg, (planex,planey))
    
    for event in pygame.event.get(): # Event handling loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Event handling for moving the player's plane. Uses either WASD or arrow keys. 
        if event.type == KEYDOWN:
            if event.key in (K_LEFT, K_a):
                direction = 'left'
            if event.key in (K_RIGHT, K_d):
                direction = 'right'
            if event.key in (K_DOWN, K_s):
                direction = 'down'
            if event.key in (K_UP, K_w):
                direction = 'up'
        


    pygame.display.update()
    fpsClock.tick(FPS)
