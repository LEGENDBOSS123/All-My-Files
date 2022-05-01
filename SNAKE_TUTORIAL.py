import pygame
import random
x = 700
y = 700
wn = pygame.display.set_mode((x,y))

def refill():
    wn.fill((255,255,255))


class SNAKE():
    def __init__(self,x1, y1, k1, k2, k3, k4):
        self.x = x
        self.y = y
        self.snake_size = 25
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.apple_color = (255,0,0)
        self.blocks = [[x1,y1]]
        self.direction = [0,0]
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
    def add_block(self):
        b = self.blocks[-1].copy()
        self.blocks.append([b[0],b[1]])
        
    def check(self):
        
        for i in self.blocks:
            if self.blocks.count(i)>1:
                self.blocks = [self.blocks[0]]
                break
    def move(self):
        block = self.blocks[-1].copy()
        oneb = self.blocks[0].copy()
        self.blocks.pop(-1)
        block[0]=oneb[0] + self.direction[0]
        block[1]=oneb[1] + self.direction[1]
        if block[0]<0:
            block[0] = self.x-self.snake_size
        if block[0]>self.x-self.snake_size:
            block[0] = 0
        if block[1]<0:
            block[1] = self.y-self.snake_size
        if block[1]>self.y-self.snake_size:
            block[1] = 0
        self.blocks.insert(0,block)
    def control(self):
        
        self.move()
        
        keys = pygame.key.get_pressed()
        if keys[self.k1] and self.direction[1]!=self.snake_size:
            self.direction = [0,-self.snake_size]
        if keys[self.k2] and self.direction[1]!=-self.snake_size:
            self.direction = [0,self.snake_size]
        if keys[self.k3] and self.direction[0]!=self.snake_size:
            self.direction = [-self.snake_size,0]
        if keys[self.k4] and self.direction[0]!=-self.snake_size:
            self.direction = [self.snake_size,0]
    def draw_snake(self):
        self.control()
        self.check()
        for i in self.blocks:
            pygame.draw.rect(wn, self.color,(i[0],i[1],self.snake_size,self.snake_size))
        
def collisioncheck(s1,s2):
    for i in s1.blocks:
        if i in s2.blocks:
            return True
    return False
def collision1(s1, s2):


    
    if collisioncheck(s1,s2):
        if s1.direction[0] != 0 and s2.direction[0] != 0:
            if s1.direction[0]/s2.direction[0]==-1:
                s2.blocks = [s2.blocks[0]]
                s1.blocks = [s1.blocks[0]]
                return
        if s1.direction[1] != 0 and s2.direction[1] != 0:
            if s1.direction[1]/s2.direction[1]==-1:
                s2.blocks = [s2.blocks[0]]
                s1.blocks = [s1.blocks[0]]
                return
        
    for i in s2.blocks:
        if i == s1.blocks[0]:
            add = len(s1.blocks)-1
            for i in range(add):
                s2.add_block()
            s1.blocks = [s1.blocks[0]]
            return
    for i in s1.blocks:
        if i == s2.blocks[0]:
            add = len(s2.blocks)-1
            for i in range(add):
                s1.add_block()
            s2.blocks = [s2.blocks[0]]
            return
def collision(snakes):
    s = snakes
    for x in range(len(s)-1):
        for y in range(x,len(s)):             
             collision1(s[x],s[y])
            


        
    
snakes = [SNAKE(100,100,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT),
          SNAKE(600,600,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d),SNAKE(600,100,pygame.K_KP8,pygame.K_KP5,pygame.K_KP4,pygame.K_KP6)]
APPLE_NUMBER = 10



APPLES = []
for i in range(APPLE_NUMBER):
    APPLES.append([random.randint(0,x//25-1)*25,random.randint(0,y//25-1)*25])
def appleget(s,APPLES):

    for apple in APPLES:
        pygame.draw.rect(wn, (255,0,0),(apple[0],apple[1],snakes[0].snake_size,snakes[0].snake_size))
        
    for snake in s:
        for apple in APPLES:
            if apple in snake.blocks:
                snake.add_block()
                while apple in snake.blocks:
                    a = random.randint(0,snake.x//25-1)*25
                    b = random.randint(0,snake.y//25-1)*25
                    APPLES[APPLES.index(apple)] = [a,b]
                    apple = [a,b]
                



            
def draw():
    refill()
    for p in snakes:
        p.draw_snake()
    appleget(snakes,APPLES)
    collision(snakes)
    
run = True
while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()
            
pygame.quit()
