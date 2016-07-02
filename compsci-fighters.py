import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 24
FPSCLOCK = pygame.time.Clock()

#Game window dimensions
WINDOWWIDTH = 480
WINDOWHEIGHT = 680

#COLORS 
PAUSED_BG = (0,0,0,128)
PAUSED_FC = (255,255,255)
MAIN_BG = (56, 134, 232)


def main():
	player = pygame.image.load('new1.png')
	playerX = int(WINDOWWIDTH/2) - int(player.get_rect().width/2)
	playerY = WINDOWHEIGHT - player.get_rect().height
	player_direction = ''
	deltaX = 3
	deltaY = 3
	
	global MENU_FONT, DISPLAYSURF
	
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE)
	pygame.display.set_caption('Dog fighter')
	
	while True:
		DISPLAYSURF.fill(MAIN_BG)
		if player_direction == 'left':
			playerX -= deltaX
		if player_direction == 'right':
			playerX += deltaX
		if player_direction == 'up':
			playerY -= deltaY
		if player_direction == 'down':
			playerY += deltaY
		
		DISPLAYSURF.blit(player, (playerX, playerY))
		
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key in (K_LEFT, K_a):
					player_direction = 'left'
				if event.key in (K_RIGHT, K_d):
					player_direction = 'right'
				if event.key in (K_UP, K_w):
					player_direction = 'up'
				if event.key in (K_DOWN, K_s):
					player_direction = 'down'
				if event.key in (K_ESCAPE, K_p):
					if event.key == K_p:
						showPausedSreen()
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
			if event.type == VIDEORESIZE:
				DISPLAYSURF = pygame.display.set_mode(event.dict['size'], RESIZABLE)
			if event.type == KEYUP:
				player_direction =''
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
def showPausedSreen():
	pausedFont = pygame.font.Font('freesansbold.ttf',18)
	while True:
		DISPLAYSURF.fill(PAUSED_BG)

		pausedSurf = pausedFont.render('PAUSED', True, PAUSED_FC)
		pausedRect = pausedSurf.get_rect()
		pausedRect.center = (int(WINDOWWIDTH/2)), (int(WINDOWHEIGHT/2))
		DISPLAYSURF.blit(pausedSurf, pausedRect)
		
		unPauseButtonSurf = pausedFont.render('Press \'p\' to continue.', True, PAUSED_FC)
		unPauseButtonRect = unPauseButtonSurf.get_rect()
		unPauseButtonRect.center = (int(WINDOWWIDTH/2), int(WINDOWHEIGHT/2) + 25)
		DISPLAYSURF.blit(unPauseButtonSurf, unPauseButtonRect)
		
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
			if event.type == VIDEORESIZE:
				DISPLAYSURF = pygame.display.set_mode(event.dict['size'], RESIZABLE)
				continue
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	
	
		
if __name__ == '__main__':
	main()
