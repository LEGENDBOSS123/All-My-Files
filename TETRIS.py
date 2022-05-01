import pygame
import random
X = 450
Y = 750
wn = pygame.display.set_mode((X,Y))
def refill():
    wn.fill((30,30,30))
    
L_BLOCK = [[" X",
            " X",
            "XX"],
           
           ["X  ",
            "XXX"],
           
           ["XX",
            "X ",
            "X "],
           
           ["XXX",
            "  X"]]

Z_BLOCK = [[" X",
            "XX",
            "X "],
           
           ["XX ",
            " XX"],
           
           [" X",
            "XX",
            "X "],
           
           ["XX ",
            " XX"]]

S_BLOCK = [["X",
            "XX",
            " X"],
           
           [" XX",
            "XX"],
           
           ["X",
            "XX",
            " X"],
           
           [" XX",
            "XX"]]

T_BLOCK = [["XXX",
            " X "],
           
           [" X",
            "XX",
            " X"],
           
           [" X ",
            "XXX"],
           
           ["X ",
            "XX",
            "X "]]
O_BLOCK = [["XX",
            "XX"],
           
           ["XX",
            "XX"],
           
           ["XX",
            "XX"],
           
           ["XX",
            "XX"]]

I_BLOCK = [["X",
            "X",
            "X",
            "X"],
           
           ["XXXX"],
           
           ["X",
            "X",
            "X",
            "X"],
           
           ["XXXX"]]




BLOCKS = [T_BLOCK,S_BLOCK,Z_BLOCK,L_BLOCK,O_BLOCK,I_BLOCK]


class SHAPE():
    def __init__(self,shapes,x,y):
        self.list_shape = shapes
        self.index = 0
        self.shape = self.list_shape[self.index]
        self.timer = 0
        self.max_timer = 4
        self.x = x
        self.y = y
        self.sx = X
        self.sy = Y
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.block_side = 25
        self.blocks = []
        self.landed = False
        self.gameover = False
        
        
    def restore(self):
        self.blocks = []
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x] == 'X':
                    self.blocks.append([self.x+x*self.block_side,self.y+y*self.block_side])
                    
        self.shape = self.list_shape[self.index]
        self.timer+=1
        if self.timer>=self.max_timer and self.landed==False:
            self.timer = 0
            self.y+=self.block_side
    def check(self,LIST):
        for i in self.blocks:
            if i[1]==self.sy-self.block_side:
                self.landed = True
                return 
            
        for i in self.blocks:
            for l in LIST:
                if l!=self:
                    for BLOCK in l.blocks:
                        if i[1]+self.block_side == BLOCK[1] and i[0] == BLOCK[0]:
                            self.landed = True
                            return
        
            
            
    def check_dir(self,LIST,d):
        for i in self.blocks:
            if i[0]<=0:
                self.x+=self.block_side
                return
            if i[0]>=self.sx-self.block_side:
                self.x-=self.block_side
                return
        for i in self.blocks:
            for l in LIST:
                if l!=self:
                    for BLOCK in l.blocks:
                        
                        if i[0]+self.block_side == BLOCK[0] and i[1] == BLOCK[1] and d == "r":
                            self.x-=self.block_side
                            return
                        if i[0]-self.block_side == BLOCK[0] and i[1] == BLOCK[1] and d=="l":
                            
                            self.x+=self.block_side
                            return
        
        
    def manage_keys(self,LIST):
          
        key = pygame.key.get_pressed()
        if self.timer==0:
            if key[pygame.K_UP]:
                self.index = (self.index+1)%4
            elif key[pygame.K_DOWN]:
                self.index = (self.index-1)%4
        if self.timer/2!=self.timer//2:
            if key[pygame.K_RIGHT]:
                self.x+=self.block_side
                self.check_dir(LIST,"r")
            elif key[pygame.K_LEFT]:
                self.x-=self.block_side
                self.check_dir(LIST,"l")
                    

            
            
    def draw(self):
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x] == 'X':
                    pygame.draw.rect(wn,self.color,(self.x+x*self.block_side,self.y+y*self.block_side,self.block_side,self.block_side))
    def GAMEOVERCHECK(self):
        for i in self.blocks:
            if i[1]<=0:
                self.gameover = True
                return
            
    def work(self,LIST):
        
        if self.landed == False:
            self.restore()
            self.check(LIST)
            self.manage_keys(LIST)
        else:
            self.GAMEOVERCHECK()
        self.draw()
    
s1 = [SHAPE(BLOCKS[2],X//2,-100)]
run = True
def draw():
    global run
    refill()
    variable = False
    for s in s1:
        s.work(s1)
        if s.landed==False:
            variable = True
        if s.gameover==True:
            run = False
            
            
    if variable==False:
        s1.append(SHAPE(random.choice(BLOCKS),X//2,-100))
    

while run:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()
pygame.quit()
