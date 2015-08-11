#Showing things in random position
#Lejay Chen

import pygame, sys
from pygame.locals import *
from random import *

pygame.init()
pygame.font.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Animation')
font = pygame.font.SysFont('Comic Sans MS',16)

WHITE = (255, 255, 255)
img = pygame.image.load('apple.jpg')
token = pygame.transform.scale(img,(50,50))
x = 400
y = 300
count = 0

while True:
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(token, (x,y))
	gametime=font.render('x='+str(int(x))+', y='+str(int(y)),False, (0,0,0) )
	DISPLAYSURF.blit(gametime,(x+50,y+15)) 

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	count += 1
	if count == FPS:
		count = 0
		x = 700*random()
		y = 500*random()

	pygame.display.update()
	fpsClock.tick(FPS)
