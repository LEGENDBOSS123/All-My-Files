import pygame
pygame.init()
xval = 1200
yval = 700
wn = pygame.display.set_mode((xval,yval))


def draw(LIST):
    startpoint = LIST[0]
    LIST.remove(0)
        
    
run = True

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
pygame.quit()

