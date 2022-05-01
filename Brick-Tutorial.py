import pygame
pygame.init()
import random
import math

x = 1000
y = 750

wn = pygame.display.set_mode((x,y))
class BRICK():
    def __init__(self,x,y,width,height):
        self.color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def DRAW(self):
        pygame.draw.rect(wn, self.color, (self.x,self.y,self.width,self.height))



        
class BALL():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.radius = 0
        self.color = color
        self.lives = 0
        
    def STARTUP(self,xvel,yvel,radius,lives):
        self.xvel = xvel
        self.yvel = yvel
        self.radius = radius
        self.lives = lives
        
    def DEATH(self):
        self.lives-=1
        self.x = x//2
        self.y = (3*y)//4
        
    def WALLS_DETECTION(self):
        if self.x>x-self.radius or self.x<self.radius:
            self.xvel*=-1
        if self.y>y-self.radius or self.y<self.radius:
            self.yvel*=-1
        if self.y>y-self.radius:
            self.DEATH()
        
    def DRAW(self):
        self.x+=self.xvel
        self.y+=self.yvel
        self.WALLS_DETECTION()
        pygame.draw.circle(wn,self.color,(self.x,self.y),self.radius)





class PLAYER():
    def __init__(self,width,height,color,speed):
        
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.x = x//2-self.width//2
        self.y = (8*y)//9-self.height//2
        
    def WALLS_DETECTION(self):
        if self.x+self.width>=x:
            self.x = x-self.width
        if self.x<=0:
            self.x = 0
        
    def MOVE(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x+=self.speed
        if keys[pygame.K_LEFT]:
            self.x-=self.speed
    def DRAW(self):
        self.MOVE()
        self.WALLS_DETECTION()
        pygame.draw.rect(wn,self.color,(self.x,self.y,self.width,self.height))






BALL = BALL(x//2,(3*y)//4,(255,255,255))

BALL.STARTUP(1,5,15,5)

PLAYER = PLAYER(200,10,(255,255,255),5)

BRICKS = []

for i in range (10):
    BRICKS.append(BRICK(150*i,100,100,50))

bg = (0,0,0)

def refill():
    wn.fill(bg)
    
def draw():
    refill()
    PLAYER.DRAW()
    BALL.DRAW()
    for i in BRICKS:
        i.DRAW()

run = True

while run:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()

    pygame.display.update()
pygame.quit()
