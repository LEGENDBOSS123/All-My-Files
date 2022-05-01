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

colors = ((1,0,0),
          (0,1,0),
          (0,0,1),
          (1,1,1),
          (0,0,0))

def Cube():
    glBegin(GL_QUADS)
    x=0
    for surface in surfaces:
        x+=1
        for vertex in surface:
            x+=1
            glColor3fv(colors[x%4])
            glVertex3fv(verticies[vertex])
            
    glEnd()



    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    
    glEnd()
    
gluPerspective(45,(xval/yval),0.1,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(0,0,0,0)
run  = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT]:
        glTranslatef(0.1,0,0)
    if keys[pygame.K_RIGHT]:
        glTranslatef(-0.1,0,0)
    if keys[pygame.K_UP]:
        glTranslatef(0,0,0.1)
    if keys[pygame.K_DOWN]:
        glTranslatef(0,0,-0.1)
    if keys[pygame.K_SPACE]:
        glTranslatef(0,-0.1,0)
    if keys[pygame.K_z]:
        glTranslatef(0,0.1,0)
    
    x = glGetDoublev(GL_MODELVIEW_MATRIX)
    
    camera_x = x[3][0]
    camera_y = x[3][1]
    camera_z = x[3][2]
    if camera_z<-1:
        run=False
    glTranslatef(0,0,0.05)
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()
    pygame.time.delay(10)
    


















    
pygame.quit()


    



