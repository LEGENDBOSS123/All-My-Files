import pygame
pygame.init()
import random
import math

x = 100
y = 100

wn = pygame.display.set_mode((x,y))


class PLAYER():
    def __init__(self):
        











bg = (0,0,0)

def refill():
    wn.fill(bg)
    
def draw():
    refill()

run = True

while run:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()

    pygame.display.update()
pygame.quit()
