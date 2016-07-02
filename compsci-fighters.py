import pygame, sys
from pygame.locals import *

FPS = 30
FPSCLOCK = pygame.time.Clock()

#Game window dimensions
WINDOWWIDTH = 480
WINDOWHEIGHT = 700

#COLORS 
PAUSED_BG = (0,0,0,128)
PAUSED_FC = (255,255,255)
MAIN_BG = (56, 134, 232)


def main():
	pygame.init()
	# Creates the player's plane and set its location
	player = pygame.image.load('new1.png')
	playerX = int(WINDOWWIDTH/2) - int(player.get_rect().width/2)
	playerY = WINDOWHEIGHT - player.get_rect().height
	player_direction = ''
	deltaX = 3
	deltaY = 3
	
	global DISPLAYSURF
	
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE)
	pygame.display.set_caption('Dog fighter')
	
	while True:
		DISPLAYSURF.fill(MAIN_BG)
		# The four if's allow the player to move. 
		if player_direction == 'left':
			playerX -= deltaX
		if player_direction == 'right':
			playerX += deltaX
		if player_direction == 'up':
			playerY -= deltaY
		if player_direction == 'down':
			playerY += deltaY
		# Draw the player to the screen
		DISPLAYSURF.blit(player, (playerX, playerY))
		# Event handling
		for event in pygame.event.get():
			# Event conditions and results for player movements
			if event.type == KEYDOWN:
				if event.key in (K_LEFT, K_a):
					player_direction = 'left'
				if event.key in (K_RIGHT, K_d):
					player_direction = 'right'
				if event.key in (K_UP, K_w):
					player_direction = 'up'
				if event.key in (K_DOWN, K_s):
					player_direction = 'down'
				# Game halting conditions
				if event.key in (K_ESCAPE, K_p):
					if event.key == K_p:
						showPausedSreen(DISPLAYSURF)
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
			#adjustable screen event handling
			if event.type == VIDEORESIZE:
				DISPLAYSURF = pygame.display.set_mode(event.dict['size'], RESIZABLE)
			if event.type == KEYUP:
				player_direction =''
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		pygame.display.update()
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
