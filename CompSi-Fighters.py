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
catx = 100
caty = 100
direction = 'right'

while True: # The main game loop
    DISPLAYSURF.fill(BLUE)
    if direction == 'right':
        catx += 5
        if catx == 410:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 615:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'


    DISPLAYSURF.blit(fighterImg, (catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    fpsClock.tick(FPS)