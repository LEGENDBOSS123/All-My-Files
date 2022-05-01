import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()
xval = 500
yval = 500
wn = pygame.display.set_mode((xval,yval),DOUBLEBUF|OPENGL)

verticies = ((1,-1,-1),
             (1,1,-1),
             (-1,1,-1),
             (-1,-1,-1),
             (1,-1,1),
             (1,1,1),
             (-1,-1,1),
             (-1,1,1))

edges = ((0,1),
         (0,3),
         (0,4),
         (2,1),
         (2,3),
         (2,7),
         (6,3),
         (6,4),
         (6,7),
         (5,1),
         (5,4),
         (5,7))

surfaces = ((0,1,2,3),
            (3,2,7,6),
            (6,7,5,4),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6))
class PLAYER():
    def __init__(self,x,y,z):
        glTranslatef(x,y,z)
        self.x = 0
        self.y = 0
        self.z = 0
    def MOVE(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            glRotatef(1,0,1,0)
        if keys[pygame.K_LEFT]:
            glRotatef(-1,0,1,0)
        if keys[pygame.K_UP]:
            glRotatef(-1,1,0,0)
        if keys[pygame.K_DOWN]:
            glRotatef(1,1,0,0)
        if keys[pygame.K_w]:
            self.z-=0.1
        if keys[pygame.K_s]:
            self.z+=0.1
        if keys[pygame.K_a]:
            self.x-=0.1
        if keys[pygame.K_d]:
            self.x+=0.1


        
class CUBE():
    def __init__(self,x,y,z,PLAYER):
        self.P = PLAYER
        self.x = x
        self.y = y
        self.z = z
        self.Vert = []
    def MAKE_CUBE(self):
        self.Vert = []
        for vert in verticies:
            self.Vert.append((vert[0]-self.x-self.P.x,vert[1]-self.y-self.P.y,vert[2]-self.z-self.P.z))

    def DRAW(self):
        self.MAKE_CUBE()
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(self.Vert[vertex])
        
        glEnd()
    
gluPerspective(90,(xval/yval),0.1,50.0)
glTranslatef(0,0,0)
glRotatef(1,0,0,0)
PLAYER = PLAYER(0,0,0)
CUBES = [CUBE(0,0,10,PLAYER),CUBE(0,2,10,PLAYER)]

run = True
while run:

    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    for C in CUBES:
        C.DRAW()
    PLAYER.MOVE()
    pygame.display.flip()

pygame.quit()



