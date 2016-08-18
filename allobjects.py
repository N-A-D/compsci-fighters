import pygame, sys

MAIN_BG = (56, 134, 232)
DELTA = 3

# ----- Classes----
class Ammo(pygame.sprite.Sprite):
    # This class represents the Ammunition.
    
    def __init__(self):
        # Call to parent class
        pygame.sprite.Sprite.__init__(self)
        # Load ammo image
        self.image = pygame.image.load("missile9.png")

        #set transparent color
        self.image.set_colorkey(MAIN_BG)
        
        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    def update(self):
        
        # Update the ammo position
        self.rect.y -= DELTA

class Plane(pygame.sprite.Sprite):
    
    screen_width  = 0
    screen_hieght = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def screenlimit(self,limit):
        self.screen_width  = limit[0]
        self.screen_hieght = limit[1]

            
class Enemy(Plane):
    # This class represents the Ammunition.
    small = "bomber1.png"
    big = "bomber2.png"
            
    def __init__(self,enemy):
        # Call parent(Sprite) constructor
        Plane.__init__(self)

        #load plane
        if enemy == "small":
            self.image = pygame.image.load("bomber1.png")
        elif enemy == "big":
            self.image = pygame.image.load("bomber2.png")

        #set transparent color
        self.image.set_colorkey(MAIN_BG)

        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        

  

class Player(Plane):
    # This class represents the Ammunition.

    fighter_direction = ''    # Sets the direction of plane
    

                
    def __init__(self):
        # Call parent(Sprite) constructor
        Plane.__init__(self)

        #load plane
        self.image = pygame.image.load("new1.png")

        #set transparent color
        self.image.set_colorkey(MAIN_BG)

        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    
    def update(self):
        
        # Update the plane direction and restrict within game surface. 
        if self.fighter_direction == 'left':
            if self.rect.x <=  0:
                self.rect.x = 0
            else:
                self.rect.x -= DELTA 
        if self.fighter_direction == 'right':
            if self.rect.x >= int (self.screen_width - self.rect.width):
                self.rect.x = int (self.screen_width - self.rect.width)
            else:
                self.rect.x += DELTA 
        if self.fighter_direction == 'up':
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= DELTA 
        if self.fighter_direction == 'down':
            if self.rect.y >= int (self.screen_hieght - self.rect.height):
                self.rect.y = int (self.screen_hieght - self.rect.height)
            else:
                self.rect.y += DELTA 
