import pygame, sys
from pygame.locals import *
from math import *

pygame.init()
pygame.font.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')
font = pygame.font.SysFont('Comic Sans MS',16)

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
theta=0
speed=5
time=0
count=0



while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    gametime=font.render('Your Game Time: '+str(time),False, (0,0,0) )
    DISPLAYSURF.blit(gametime,(10,10))  #display game time
    catx = catx + speed*sin(theta)
    caty = caty + speed*cos(theta)
    if catx<5:
        theta = -theta
    if catx>680:
        theta = -theta
    if caty<5:
        theta = pi - theta
    if caty > 520:
        theta = pi - theta

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_LEFT]:
                theta = theta + 3./speed
            if pygame.key.get_pressed()[K_RIGHT]:
                theta = theta - 3./speed
            if pygame.key.get_pressed()[K_UP]:
                speed = speed  * 1.05 
            if pygame.key.get_pressed()[K_DOWN]:
                speed = speed * 0.95

    #get game time            
    count = count +1
    if count == FPS:
        time = time +1
        count = 0

    pygame.display.update()
    fpsClock.tick(FPS)
