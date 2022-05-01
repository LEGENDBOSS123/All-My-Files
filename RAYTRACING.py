import pygame
pygame.init()
import math
import random
import numpy


xval = 1000
yval = 1000
wn = pygame.display.set_mode((xval,yval))
fps = 30


class VECTOR():
    def __init__(self,x,y):
        self.x = x
        self.y = y
class VECTORMATH():
    
    def add_vectors(self,a,b):
        return VECTOR(a.x+b.x,a.y+b.y)

    def subtract_vectors(self,a,b):
        return VECTOR(a.x-b.x,a.y-b.y)

    def multiply_vectors(self,a,b):
        return VECTOR(a.x*b,a.y*b)

    def divide_vectors(self,a,b):
        return VECTOR(a.x/b,a.y/b)

    def equal_vectors(self,a,b):
        if a.x==b.x and a.y==b.y:
            return True
        else:
            return False
        
    def length(self,a):
        return math.sqrt(a.x**2+a.y**2)


    def distance(self,a,b):
        return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

    def normalize(self,a):
        l = length(a)
        if l == 0:
            return VECTOR(0,1)
        return VECTOR(a.x/l,a.y/l)

    def dot_product(self,a,b):
        return a.x*b.x+a.y*b.y

    def cross_product(self,a,b):
        
        return a.x*b.y-a.y*b.x


VECTORMATH = VECTORMATH()

class LIGHT_SOURCE():
    def __init__(self,x,y,color,numofrays):
        self.x = x
        self.y = y
        self.color = color
        
        
        
class RAY():
    def __init__(self,origin,direction,color):
        self.direction = direction
        self.origin = origin
        self.color = color
        
   
        
class SPHERE():
    def __init__(self,center,radius,color,reflect):
        self.center = center
        self.radius = radius
        self.color = color
        self.reflect = reflect
        
    
        
class POLYGON():
    def __init__(self,verticies,color,reflect):
        self.verticies = verticies
        self.color = color
        self.reflect = reflect

class CAMERA():
    def __init__(self,x,y,angle,fov):
        self.x = x
        self.y = y
        self.angle = angle
        self.fov = fov
        
    def draw(self):
        for i in range(self.fov):
            pass
        
        
class WORLD():
    def __init__(self):
        self.spheres = []
        self.polygons = []
        self.light_sources = []
        
    
        





CAMERA = CAMERA(0,0,0,90)

WORLD = WORLD()

WORLD.polygons.append(POLYGON(((200,0),(100,100),(-100,100)),(100,200,0),0))
WORLD.light_sources.append(LIGHT_SOURCE(50,200,(255,255,255),1000))

def draw():
    wn.fill((0,0,0))
    CAMERA.draw()
    

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

