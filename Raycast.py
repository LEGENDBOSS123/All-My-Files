import pygame
import math
import random
pygame.init()

fps = 40
xval = 1200
yval = 700
wn = pygame.display.set_mode((xval,yval))
MAP = [[1,1,1,1,1,1],
       [1,9,0,0,0,1],
       [1,0,0,1,0,1],
       [1,0,1,0,0,1],
       [1,1,0,0,0,1],
       [1,0,1,1,0,1],
       [1,0,1,0,0,1],
       [1,0,0,0,1,1],
       [1,1,1,1,1,1]]


class PLAYER():
    def __init__(self):
        self.angle = 180
        self.rays = []
        self.ray = []
        self.speed = 5
        self.anglespeed = 3
        self.x = 60
        self.y = 60
        self.grid_size = 50
        self.radius = 10
        self.FOV = 75
        self.dis = 5000
        
        
    def MOVE(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            self.x-=self.speed*math.cos(self.angle*math.pi/180)
            self.y-=self.speed*math.sin(self.angle*math.pi/180)
        if key[pygame.K_s]:
            self.x+=self.speed*math.cos(self.angle*math.pi/180)
            self.y+=self.speed*math.sin(self.angle*math.pi/180)
        if key[pygame.K_d]:
            self.x-=self.speed*math.cos((self.angle+90)*math.pi/180)
            self.y-=self.speed*math.sin((self.angle+90)*math.pi/180)
        if key[pygame.K_a]:
            self.x-=self.speed*math.cos((self.angle-90)*math.pi/180)
            self.y-=self.speed*math.sin((self.angle-90)*math.pi/180)
        if key[pygame.K_RIGHT]:
            self.angle+=self.anglespeed
        if key[pygame.K_LEFT]:
            self.angle-=self.anglespeed
        if self.angle>360:
            self.angle-360
        if self.angle<0:
            self.angle+=360
    def WALL_COLLISION(self,x,y):
        if self.y>y and self.y<y+self.grid_size and self.x>x-self.radius and self.x<x+self.grid_size and self.x<x+self.grid_size/20:
            self.x=x-self.radius
        elif self.y>y and self.y<y+self.grid_size and self.x>x and self.x<x+self.grid_size+self.radius and self.x>x+19*self.grid_size/20:
            self.x=x+self.grid_size+self.radius
        if self.y>y and self.y<y+self.grid_size+self.radius and self.x>x and self.x<x+self.grid_size and self.y>y+self.grid_size/10:
            self.y=y+self.grid_size+self.radius
        elif self.y>y-self.radius and self.y<y+self.grid_size and self.x>x and self.x<x+self.grid_size+self.radius and self.y<y+19*self.grid_size/10:
            self.y=y-self.radius
            
    def LINE_SEGMENT_COLLISION(self,line1,line2):
        firstlineslope = (line1[1]-line1[3])/(line1[0]-line1[2]+0.000001)
        secondlineslope = (line2[1]-line2[3])/(line2[0]-line2[2]+0.000001)
        firstintercept = line1[1]-firstlineslope*line1[0]
        secondintercept = line2[1]-secondlineslope*line2[0]
        xvalue = (secondintercept-firstintercept)/(firstlineslope-secondlineslope+0.000001)
        yvalue = firstlineslope*xvalue+firstintercept
        if xvalue>=min(line1[0],line1[2]) and xvalue<=max(line1[0],line1[2]) and yvalue>=min(line1[1],line1[3]) and yvalue<=max(line1[1],line1[3]):
            if xvalue>=min(line2[0],line2[2]) and xvalue<=max(line2[0],line2[2]) and yvalue>=min(line2[1],line2[3]) and yvalue<=max(line2[1],line2[3]):
                self.ray.append(math.sqrt((self.x-xvalue)**2+(self.y-yvalue)**2))
            
    def DRAW_MAP(self,MAP):
        lines = 200
        angle = (self.angle-self.FOV/2+1)
        for i in range(len(self.rays)):
            if yval-self.rays[i]>0:
                if 255-self.rays[i]>=0:
                    
                    pygame.draw.rect(wn, (0,0,int(255-self.rays[i])),(i*xval/lines,yval/2-(yval-self.rays[i])/2,xval/(lines),(yval-self.rays[i])))
        self.rays = []
        for i in range(lines):
            

            for y in range(len(MAP)):
                for x in range(len(MAP[y])):
                    if MAP[y][x] == 1:
                        dis=self.dis
                        self.LINE_SEGMENT_COLLISION([self.x,self.y,self.x-dis*math.cos(angle*math.pi/180),self.y-dis*math.sin(angle*math.pi/180)],[x*self.grid_size-1,y*self.grid_size-1,(x)*self.grid_size+1,(y+1)*self.grid_size+1])
                        self.LINE_SEGMENT_COLLISION([self.x,self.y,self.x-dis*math.cos(angle*math.pi/180),self.y-dis*math.sin(angle*math.pi/180)],[(x+1)*self.grid_size-1,y*self.grid_size-1,(x+1)*self.grid_size+1,(y+1)*self.grid_size+1])
                        self.LINE_SEGMENT_COLLISION([self.x,self.y,self.x-dis*math.cos(angle*math.pi/180),self.y-dis*math.sin(angle*math.pi/180)],[x*self.grid_size-1,y*self.grid_size-1,(x+1)*self.grid_size+1,(y)*self.grid_size+1])
                        self.LINE_SEGMENT_COLLISION([self.x,self.y,self.x-dis*math.cos(angle*math.pi/180),self.y-dis*math.sin(angle*math.pi/180)],[x*self.grid_size-1,(y+1)*self.grid_size-1,(x+1)*self.grid_size+1,(y+1)*self.grid_size+1])
                        self.WALL_COLLISION(x*self.grid_size,y*self.grid_size)
            self.ray.append(dis)
            self.rays.append(min(self.ray)*(math.cos((self.angle-angle)*math.pi/180)))
            dis = min(self.ray)
            self.ray = []
                            
            pygame.draw.line(wn,(0,255,255),(int(self.x),int(self.y)),(int(self.x-dis*math.cos(angle*math.pi/180)),int(self.y-dis*math.sin(angle*math.pi/180))))
            angle+=self.FOV/lines
        
        
        for y in range(len(MAP)):
                for x in range(len(MAP[y])):
                    if MAP[y][x] == 1:
                        pygame.draw.rect(wn, (255,255,255),(self.grid_size*x,self.grid_size*y,self.grid_size,self.grid_size))
        
        
        
                        
    def DRAW(self,MAP):
        
        self.MOVE()
        self.DRAW_MAP(MAP)
        pygame.draw.circle(wn,(255,255,255),(int(self.x),int(self.y)),self.radius)


PLAYER = PLAYER()







def draw():
    wn.fill((0,0,0))
    PLAYER.DRAW(MAP)

run = True
clock = pygame.time.Clock()
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
