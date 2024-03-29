import pygame, sys, random, allobjects
from pygame.locals import *

FPS = 30
FPSCLOCK = pygame.time.Clock()

# Game window dimensions
WINDOWWIDTH = 480
WINDOWHEIGHT = 700

#COLORS 
START_FC = (0,0,255)
START_BG = (255,255,255,128)
PAUSED_BG = (0,0,0,128)
PAUSED_FC = (255,255,255)
MAIN_BG = (56, 134, 232)

#---- Main ----
def main():
    
    pygame.init()

    # Create game surface
    global DISPLAYSURF,SCREENLIMIT
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE)
    pygame.display.set_caption('Dog fighter')
    SCREENLIMIT = [DISPLAYSURF.get_width(),DISPLAYSURF.get_height()]
    
    start_screen(DISPLAYSURF)

    # Create game Sprite list
    all_sprite_list = pygame.sprite.Group()
    ammo_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    
    # Creates the player's plane and set its location
    player = allobjects.Player()
    player.screenlimit(SCREENLIMIT)
    player.rect.x = int(WINDOWWIDTH/2) - int(player.rect.width/2)
    player.rect.y = int (3*(WINDOWHEIGHT/4 )) - (player.rect.height) 

    # Add player to sprite list
    all_sprite_list.add(player)

    #Create 6 enemy planes
    for i in range(4):
        enemy = allobjects.Enemy("big")
        enemy.screenlimit(SCREENLIMIT)
        enemy.rect.x = random.randrange(enemy.screen_width - enemy.rect.width)
        enemy.rect.y = 3
        enemy_list.add(enemy)
        all_sprite_list.add(enemy)
        
  
    # Game loop
    while True:
        DISPLAYSURF.fill(MAIN_BG)
        
        # Event handling
        for event in pygame.event.get():
            # Event conditions and results for player movements
            if event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    player.fighter_direction = 'left'
                if event.key in (K_RIGHT, K_d):
                    player.fighter_direction = 'right'
                if event.key in (K_UP, K_w):
                    player.fighter_direction = 'up'
                if event.key in (K_DOWN, K_s):
                    player.fighter_direction = 'down'
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
                    ammo1 = allobjects.Ammo()
                    ammo2 = allobjects.Ammo()
                    # Assign ammo objects x and y coordinates
                    ammo1.rect.x = player.rect.x + int(player.rect.width -10)
                    ammo1.rect.y = player.rect.y
                    ammo2.rect.x = player.rect.x 
                    ammo2.rect.y = player.rect.y
                    all_sprite_list.add(ammo1,ammo2)
                    ammo_list.add(ammo1,ammo2)

            #Update graphics
            all_sprite_list.update()
            # Check for collison of ammo and enemy 
            for ammo in ammo_list:
                enemy_hit_list = pygame.sprite.spritecollide(ammo,enemy_list,True)
                for enemy in enemy_hit_list:
                    enemy_list.remove(enemy)
                    ammo_list.remove(ammo)
                    all_sprite_list.remove(enemy,ammo)
                # Remove ammo once they leaves the screen
                if ammo.rect.y < -10:
                    ammo_list.remove(ammo)
                    all_sprite_list.remove(ammo)
                # Remove enemy once they leave the screen
                if enemy.rect.y > SCREENLIMIT[1]:
                    enemy_list.remove(enemy)
                    all_sprite_list.remove(enemy)                
                                    
            #adjustable screen event handling
            if event.type == VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode(event.dict['size'], RESIZABLE)
                SCREENLIMIT = [DISPLAYSURF.get_width(),DISPLAYSURF.get_height()]
                player.screenlimit(SCREENLIMIT)
            if event.type == KEYUP:
                player.fighter_direction =''
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
    
def start_screen(surf):
    start_font = pygame.font.Font(None,50)
    enter_font = pygame.font.Font('freesansbold.ttf',30)
    lock_var = True
    while lock_var:
        surf.fill(START_BG)
        display_message("Welcome to Dog Fighters",START_FC, surf,start_font,-100)
        display_message("Press enter to play:",(234,23,154), surf,enter_font)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    lock_var = False
            if event.type == VIDEORESIZE:
                surf = pygame.display.set_mode(event.dict['size'], RESIZABLE)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

#display message to a surface object        
def display_message(msg,color,surf,font,displacement = 0):
    temp_surf = font.render(msg, True, color)
    temp_rect = temp_surf.get_rect()
    temp_rect.center = (surf.get_width()/2, surf.get_height()/2 + displacement)
    surf.blit(temp_surf, temp_rect)

if __name__ == '__main__':
    main()
