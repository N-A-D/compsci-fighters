import pygame, sys
from pygame.locals import *

FPS = 30
FPSCLOCK = pygame.time.Clock()

# Game window dimensions
WINDOWWIDTH = 480
WINDOWHEIGHT = 700
DELTA = 3

#COLORS 
PAUSED_BG = (0,0,0,128)
PAUSED_FC = (255,255,255)
MAIN_BG = (56, 134, 232)

# ----- Classes----

class Ammo(pygame.sprite.Sprite):
    # This class represents the Ammunition.
    
    def __init__(self):
        # Call to parent class
        pygame.sprite.Sprite.__init__(self)
        # Load ammo image
        self.image = pygame.image.load("missile8.png")

        #set transparent color
        self.image.set_colorkey(MAIN_BG)
        
        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    def update(self):
        
        # Update the ammo position
        self.rect.y -= DELTA
        

class Plane(pygame.sprite.Sprite):
    # This class represents the Ammunition.

    plane_direction = ''    # Sets the direction of plane
            
    def __init__(self):
        # Call parent(Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #load plane
        self.image = pygame.image.load("new1.png")

        #set transparent color
        self.image.set_colorkey(MAIN_BG)

        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    def update(self):
        
        # Update the plane direction and restrict within game surface. 
        if self.plane_direction == 'left':
            if self.rect.x <=  0:
                self.rect.x = 0
            else:
                self.rect.x -= DELTA 
        if self.plane_direction == 'right':
            if self.rect.x >= int (SCREENLIMIT[0] - self.rect.width):
                self.rect.x = int (SCREENLIMIT[0] - self.rect.width)
            else:
                self.rect.x += DELTA 
        if self.plane_direction == 'up':
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= DELTA 
        if self.plane_direction == 'down':
            if self.rect.y >=int (SCREENLIMIT[1] - self.rect.height):
                self.rect.y = int (SCREENLIMIT[1] - self.rect.height)
            else:
                self.rect.y += DELTA 

#---- Main ----
def main():
    
    pygame.init()

    # Create game Sprite list
    all_sprite_list = pygame.sprite.Group()
    ammo_list = pygame.sprite.Group()
    
    # Creates the player's plane and set its location
    player = Plane()
    player.rect.x = int(WINDOWWIDTH/2) - int(player.rect.width/2)
    player.rect.y = int (3*(WINDOWHEIGHT/4 )) - (player.rect.height) 

    # Add player to sprite list
    all_sprite_list.add(player)
    
    # Create game surface
    global DISPLAYSURF,SCREENLIMIT
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE)
    pygame.display.set_caption('Dog fighter')
    SCREENLIMIT = [DISPLAYSURF.get_width(),DISPLAYSURF.get_height()]

    # Game loop
    while True:
        DISPLAYSURF.fill(MAIN_BG)
        
        # Event handling
        for event in pygame.event.get():
            # Event conditions and results for player movements
            if event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    player.plane_direction = 'left'
                if event.key in (K_RIGHT, K_d):
                    player.plane_direction = 'right'
                if event.key in (K_UP, K_w):
                    player.plane_direction = 'up'
                if event.key in (K_DOWN, K_s):
                    player.plane_direction = 'down'
                # Game halting conditions
                if event.key in (K_ESCAPE, K_p):
                    if event.key == K_p:
                        showPausedSreen(DISPLAYSURF)
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                # Release ammunition
                if event.key in (K_BACKSPACE,K_x):
                    # Create 2 ammo objects
                    ammo1 = Ammo()
                    ammo2 = Ammo()
                    # Assign ammo objects x and y coordinates
                    ammo1.rect.x = player.rect.x + int(player.rect.width -10)
                    ammo1.rect.y = player.rect.y
                    ammo2.rect.x = player.rect.x 
                    ammo2.rect.y = player.rect.y
                    all_sprite_list.add(ammo1,ammo2)
                    ammo_list.add(ammo1,ammo2)
                                    
            #adjustable screen event handling
            if event.type == VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode(event.dict['size'], RESIZABLE)
                SCREENLIMIT = [DISPLAYSURF.get_width(),DISPLAYSURF.get_height()]
            if event.type == KEYUP:
                player.plane_direction =''
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update screen graphics
        all_sprite_list.update()
        all_sprite_list.draw(DISPLAYSURF)
        pygame.display.flip()
        
        FPSCLOCK.tick(FPS)

#Pauses the game
def showPausedSreen(surf):
    pausedFont = pygame.font.Font('freesansbold.ttf',18)
    while True:
        surf.fill(PAUSED_BG)
        # Surace obj that displays 'Paused'
        pausedSurf = pausedFont.render('PAUSED', True, PAUSED_FC)
        pausedRect = pausedSurf.get_rect()
        pausedRect.center = (int(surf.get_width()/2)), (int(surf.get_height()/2))
        surf.blit(pausedSurf, pausedRect)
        # Surface obj that displays how to unpause
        unPauseButtonSurf = pausedFont.render('Press \'p\' to continue.', True, PAUSED_FC)
        unPauseButtonRect = unPauseButtonSurf.get_rect()
        unPauseButtonRect.center = (int(surf.get_width()/2), int(surf.get_height()/2) + 25)
        surf.blit(unPauseButtonSurf, unPauseButtonRect)
        
        # Event handling loop. Similar to the one in the main loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    return
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # Uses the parameter's (surf) width and height to allow dynamic adjusting of window size 
            if event.type == VIDEORESIZE:
                surf = pygame.display.set_mode(event.dict['size'], RESIZABLE)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
    
        
if __name__ == '__main__':
    main()
