import pygame
pygame.init()
import random
import math

xval = 1200
yval = 700
wn = pygame.display.set_mode((xval,yval))


class PLAYER():
    def __init__(self):
        self.x = 2730
        self.y = 400
        self.speed = 10

class CONTROLS():
    def __init__(self,player):
        self.player = player
        self.map = pygame.transform.smoothscale(pygame.image.load("theskeld.png"),(6000,3600))
        self.Vent = pygame.transform.smoothscale(pygame.image.load("Vent.png"),(100,100))
        self.Kill = pygame.transform.smoothscale(pygame.image.load("Kill.png"),(100,100))
        #self.Sab = pygame.image.load()
        self.Use = pygame.image.load("Use.png")
        self.player_image = pygame.image.load("Cyan.png")
    def DRAW(self):
        wn.blit(self.map,(-self.player.x,-self.player.y))
        wn.blit(self.player_image,(xval//2,yval//2))
        wn.blit(self.Kill,(xval-200,yval-100))
        wn.blit(self.Vent,(xval-100,yval-100))
    def MOVE(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_UP]:
            self.player.y-=self.player.speed
        if key[pygame.K_DOWN]:
            self.player.y+=self.player.speed
        if key[pygame.K_RIGHT]:
            self.player.x+=self.player.speed
        if key[pygame.K_LEFT]:
            self.player.x-=self.player.speed
            
        
        



Player = PLAYER()
CONTROLS = CONTROLS(Player)


def draw():
    wn.fill((0,0,0))
    CONTROLS.MOVE()
    CONTROLS.DRAW()

run = True

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()

    
pygame.quit()
