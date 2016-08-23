import pygame, sys, math, random

DELTA = 3
MAIN_BG = (56, 134, 232)
START_BG = (186,241,246,128)

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
    # This is the plane class
    screen_width  = 0
    screen_hieght = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def screenlimit(self,limit):
        self.screen_width  = limit[0]
        self.screen_hieght = limit[1]

            
class Enemy(Plane):
    # This enemy class inherit from the plane class.
    small = "bomber1.png"
    big   = "bomber2.png"
    __speed = 0
            
    def __init__(self,Type):
        # Call parent(Sprite) constructor
        Plane.__init__(self)
        self.__speed = 1
        #load plane
        if Type == "small":
            self.image = pygame.image.load("bomber1.png")
        elif Type == "big":
            self.image = pygame.image.load("bomber2.png")

        #set transparent color
        self.image.set_colorkey(MAIN_BG)

        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.__speed
        shift = random.randint(1,10)
        if shift == 3:
            self.flightManeuvering()
    def set_speed(self, speed):    
        self.__speed = speed

    def flightManeuvering(self):
        #Sine movement   : 0
        #Cosine movement : 1
        #zigzag          : 2
        #diagonal        : 3
        r_maneuver = random.randint(1,3)
        dx = self.rect.x
        if r_maneuver == 0:
            self.rect.x = math.sin(dx)
        if r_maneuver == 1:
            self.rect.x = math.cos(dx)

class Player(Plane):
    # The player class inherit from the plane class.
    
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
                
class Cloud(Plane):
    #This class inherits from the plane class

    def __init__(self,size):
        Plane.__init__(self)
        #load cloud
        if size == 1:
            self.image = pygame.image.load("smallcloud.png")
        elif size == 2:
            self.image = pygame.image.load("cloud.png")
        elif size == 3:
            self.image = pygame.image.load("big_cloud.png")
        #set transparent color
        self.image.set_colorkey(START_BG)
        # Set image rectangle x and y coordinates
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y +=2
            
#class function to retrieve the width of enemy planes
def getEnemyWidth(Type):
    if Type == "big":
        dummy = pygame.image.load("bomber1.png")
        return dummy.get_rect().width
    else:
        dummy = pygame.image.load("bomber2.png")
        return dummy.get_rect().width

def getEnemyHeight(Type):
    if Type == "big":
        dummy = pygame.image.load("bomber1.png")
        return dummy.get_rect().height
    else:
        dummy = pygame.image.load("bomber2.png")
        return dummy.get_rect().height
