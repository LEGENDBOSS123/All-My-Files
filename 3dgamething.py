size = 800
limit = 75

import pygame
pygame.init()
import math
import random

xval = size
yval = size
wn = pygame.display.set_mode((xval,yval))
verticies = [(-1,1,-1),(-1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1)]
edges = [(0,1),(0,3),(1,2),(2,3),(0,5),(5,4),(3,4),(1,6),(2,7),(7,4),(6,7),(5,6)]
faces = [(2,1,6,7),(0,1,2,3),(4,5,6,7),(0,3,4,5),(0,1,6,5),(3,4,7,2)]
colors = [(145,100,30),(145,100,20),(0,255,0),(140,100,0),(140,100,20),(150,90,20)]
class PLAYER():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.anglex = 0
        self.angley = 0
        self.FOV = 60
        self.speed = 0.5
        self.anglespeed = 5
    def MOVE(self):
        if self.anglex>360:
            self.anglex-=360
        if self.anglex<0:
            self.anglex+=360
        if self.angley>=90:
            self.angley=90
        if self.angley<=-90:
            self.angley=-90
            
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.z+=self.speed*math.cos(PLAYER.anglex*math.pi/180)
            self.x+=self.speed*math.sin(PLAYER.anglex*math.pi/180)
        if key[pygame.K_s]:
            self.z-=self.speed*math.cos(PLAYER.anglex*math.pi/180)
            self.x-=self.speed*math.sin(PLAYER.anglex*math.pi/180)
        if key[pygame.K_d]:
            self.z+=self.speed*math.cos((PLAYER.anglex+90)*math.pi/180)
            self.x+=self.speed*math.sin((PLAYER.anglex+90)*math.pi/180)
        if key[pygame.K_a]:
            self.z+=self.speed*math.cos((PLAYER.anglex-90)*math.pi/180)
            self.x+=self.speed*math.sin((PLAYER.anglex-90)*math.pi/180)
        if key[pygame.K_RIGHT]:
            self.anglex+=self.anglespeed
        if key[pygame.K_LEFT]:
            self.anglex-=self.anglespeed
        if key[pygame.K_UP]:
            self.angley-=self.anglespeed
        if key[pygame.K_DOWN]:
            self.angley+=self.anglespeed
        if key[pygame.K_SPACE]:
            self.y-=self.speed
        if key[pygame.K_LSHIFT]:
            self.y+=self.speed

pacman_points = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0),(25,0),(26,0),(27,0),(0,1),(13,1),(14,1),(27,1),(0,2),(2,2),(3,2),(4,2),(5,2),(7,2),(8,2),(9,2),(10,2),(11,2),(13,2),(14,2),(16,2),(17,2),(18,2),(19,2),(20,2),(22,2),(23,2),(24,2),(25,2),(27,2),(0,3),(2,3),(3,3),(4,3),(5,3),(7,3),(8,3),(9,3),(10,3),(11,3),(13,3),(14,3),(16,3),(17,3),(18,3),(19,3),(20,3),(22,3),(23,3),(24,3),(25,3),(27,3),(0,4),(2,4),(3,4),(4,4),(5,4),(7,4),(8,4),(9,4),(10,4),(11,4),(13,4),(14,4),(16,4),(17,4),(18,4),(19,4),(20,4),(22,4),(23,4),(24,4),(25,4),(27,4),(0,5),(27,5),(0,6),(2,6),(3,6),(4,6),(5,6),(7,6),(8,6),(10,6),(11,6),(12,6),(13,6),(14,6),(15,6),(16,6),(17,6),(19,6),(20,6),(22,6),(23,6),(24,6),(25,6),(27,6),(0,7),(2,7),(3,7),(4,7),(5,7),(7,7),(8,7),(10,7),(11,7),(12,7),(13,7),(14,7),(15,7),(16,7),(17,7),(19,7),(20,7),(22,7),(23,7),(24,7),(25,7),(27,7),(0,8),(7,8),(8,8),(13,8),(14,8),(19,8),(20,8),(27,8),(0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(7,9),(8,9),(9,9),(10,9),(11,9),(13,9),(14,9),(16,9),(17,9),(18,9),(19,9),(20,9),(22,9),(23,9),(24,9),(25,9),(26,9),(27,9),(5,10),(7,10),(8,10),(9,10),(10,10),(11,10),(13,10),(14,10),(16,10),(17,10),(18,10),(19,10),(20,10),(22,10),(5,11),(7,11),(8,11),(19,11),(20,11),(22,11),(5,12),(7,12),(8,12),(10,12),(11,12),(12,12),(15,12),(16,12),(17,12),(19,12),(20,12),(22,12),(0,13),(1,13),(2,13),(3,13),(4,13),(5,13),(7,13),(8,13),(10,13),(17,13),(19,13),(20,13),(22,13),(23,13),(24,13),(25,13),(26,13),(27,13),(10,14),(17,14),(0,15),(1,15),(2,15),(3,15),(4,15),(5,15),(7,15),(8,15),(10,15),(17,15),(19,15),(20,15),(22,15),(23,15),(24,15),(25,15),(26,15),(27,15),(5,16),(7,16),(8,16),(10,16),(11,16),(12,16),(13,16),(14,16),(15,16),(16,16),(17,16),(19,16),(20,16),(22,16),(5,17),(7,17),(8,17),(19,17),(20,17),(22,17),(5,18),(7,18),(8,18),(10,18),(11,18),(12,18),(13,18),(14,18),(15,18),(16,18),(17,18),(19,18),(20,18),(22,18),(0,19),(1,19),(2,19),(3,19),(4,19),(5,19),(7,19),(8,19),(10,19),(11,19),(12,19),(13,19),(14,19),(15,19),(16,19),(17,19),(19,19),(20,19),(22,19),(23,19),(24,19),(25,19),(26,19),(27,19),(0,20),(13,20),(14,20),(27,20),(0,21),(2,21),(3,21),(4,21),(5,21),(7,21),(8,21),(9,21),(10,21),(11,21),(13,21),(14,21),(16,21),(17,21),(18,21),(19,21),(20,21),(22,21),(23,21),(24,21),(25,21),(27,21),(0,22),(2,22),(3,22),(4,22),(5,22),(7,22),(8,22),(9,22),(10,22),(11,22),(13,22),(14,22),(16,22),(17,22),(18,22),(19,22),(20,22),(22,22),(23,22),(24,22),(25,22),(27,22),(0,23),(4,23),(5,23),(22,23),(23,23),(27,23),(0,24),(1,24),(2,24),(4,24),(5,24),(7,24),(8,24),(10,24),(11,24),(12,24),(13,24),(14,24),(15,24),(16,24),(17,24),(19,24),(20,24),(22,24),(23,24),(25,24),(26,24),(27,24),(0,25),(1,25),(2,25),(4,25),(5,25),(7,25),(8,25),(10,25),(11,25),(12,25),(13,25),(14,25),(15,25),(16,25),(17,25),(19,25),(20,25),(22,25),(23,25),(25,25),(26,25),(27,25),(0,26),(7,26),(8,26),(13,26),(14,26),(19,26),(20,26),(27,26),(0,27),(2,27),(3,27),(4,27),(5,27),(6,27),(7,27),(8,27),(9,27),(10,27),(11,27),(13,27),(14,27),(16,27),(17,27),(18,27),(19,27),(20,27),(21,27),(22,27),(23,27),(24,27),(25,27),(27,27),(0,28),(2,28),(3,28),(4,28),(5,28),(6,28),(7,28),(8,28),(9,28),(10,28),(11,28),(13,28),(14,28),(16,28),(17,28),(18,28),(19,28),(20,28),(21,28),(22,28),(23,28),(24,28),(25,28),(27,28),(0,29),(27,29),(0,30),(1,30),(2,30),(3,30),(4,30),(5,30),(6,30),(7,30),(8,30),(9,30),(10,30),(11,30),(12,30),(13,30),(14,30),(15,30),(16,30),(17,30),(18,30),(19,30),(20,30),(21,30),(22,30),(23,30),(24,30),(25,30),(26,30),(27,30)]
cubes = []
for i in pacman_points:
    cubes.append((i[0],0,i[1]))
def draw_cube(cube,PLAYER):
    if math.sqrt((cube[0]-PLAYER.x)**2+(cube[1]-PLAYER.y)**2+(cube[2]-PLAYER.z)**2)<limit:
        
        '''for edge in edges:
            line = []
            for vertex in (verticies[edge[0]],verticies[edge[1]]):
                old_x = vertex[0]-PLAYER.x+cube[0]
                old_y = vertex[1]-PLAYER.y+cube[1]
                old_z = vertex[2]-PLAYER.z+cube[2]
                old_x,old_z = old_x*math.cos(PLAYER.anglex*math.pi/180)-old_z*math.sin(PLAYER.anglex*math.pi/180),old_z*math.cos(PLAYER.anglex*math.pi/180)+old_x*math.sin(PLAYER.anglex*math.pi/180)
                old_y,old_z = old_y*math.cos(PLAYER.angley*math.pi/180)-old_z*math.sin(PLAYER.angley*math.pi/180),old_z*math.cos(PLAYER.angley*math.pi/180)+old_y*math.sin(PLAYER.angley*math.pi/180)

                if old_z>1:
                    new_x = math.degrees(math.atan(old_x/(old_z+0.001)))/PLAYER.FOV*xval
                    new_y = math.degrees(math.atan(old_y/(old_z+0.001)))/PLAYER.FOV*yval
                    
                    new_x+=xval//2
                    new_y+=yval//2
                    
                    line.append([new_x,new_y])
            if len(line)>=2:
                pygame.draw.line(wn,(0,0,0),line[0],line[1],20)'''
                
        draw_sides = []
        for face in faces:
            sides = []
            for vertex in (verticies[face[0]],verticies[face[1]],verticies[face[2]],verticies[face[3]]):
                old_x = vertex[0]-PLAYER.x+cube[0]
                old_y = vertex[1]-PLAYER.y+cube[1]
                old_z = vertex[2]-PLAYER.z+cube[2]
                
                sides.append([old_x,old_y,old_z])
                    
            
            x = int(sides[0][0]+sides[1][0]+sides[2][0]+sides[3][0]/4)
            y = int(sides[0][1]+sides[1][1]+sides[2][1]+sides[3][1]/4)
            z = int(sides[0][2]+sides[1][2]+sides[2][2]+sides[3][2]/4)
            dis = math.sqrt(x**2+y**2+z**2)
            draw_sides.append(dis)
            
        draw_sides2 = draw_sides.copy() 
        draw_sides2.sort()
        faces1 = draw_sides.index(draw_sides2[0])
        faces2 = draw_sides.index(draw_sides2[1])
        faces3 = draw_sides.index(draw_sides2[2])
        faces4 = draw_sides.index(draw_sides2[3])
        faces5 = draw_sides.index(draw_sides2[4])
        faces6 = draw_sides.index(draw_sides2[5])
        for face in [faces[faces6],faces[faces5],faces[faces4],faces[faces3],faces[faces2],faces[faces1]]:
            sides = []
            for vertex in (verticies[face[0]],verticies[face[1]],verticies[face[2]],verticies[face[3]]):
                old_x = vertex[0]-PLAYER.x+cube[0]
                old_y = vertex[1]-PLAYER.y+cube[1]
                old_z = vertex[2]-PLAYER.z+cube[2]
                
                old_x,old_z = old_x*math.cos(PLAYER.anglex*math.pi/180)-old_z*math.sin(PLAYER.anglex*math.pi/180),old_z*math.cos(PLAYER.anglex*math.pi/180)+old_x*math.sin(PLAYER.anglex*math.pi/180)
                old_y,old_z = old_y*math.cos(PLAYER.angley*math.pi/180)-old_z*math.sin(PLAYER.angley*math.pi/180),old_z*math.cos(PLAYER.angley*math.pi/180)+old_y*math.sin(PLAYER.angley*math.pi/180)

                if old_z>0:
                    new_x = math.degrees(math.atan(old_x/(old_z+0.001)))/PLAYER.FOV*xval
                    new_y = math.degrees(math.atan(old_y/(old_z+0.001)))/PLAYER.FOV*yval
                    
                    new_x+=xval//2
                    new_y+=yval//2
                    variable = 300
                    if new_x<xval+variable and new_x>0-variable and new_y<yval+variable and new_y>0-variable:
                        sides.append([new_x,new_y,vertex[0],vertex[1],vertex[2]])
                    
            if len(sides)>=4:
                color = colors[verticies.index((sides[0][2],sides[0][3],sides[0][4]))]
                pygame.draw.polygon(wn,color,(sides[0][0:2],sides[1][0:2],sides[2][0:2],sides[3][0:2]))
                    
                


PLAYER = PLAYER()

def draw():
    wn.fill((255,255,255))
    cubes2 = []
    for cube in cubes:
        cubes2.append((math.sqrt((cube[0]-PLAYER.x)**2+(cube[1]-PLAYER.y)**2+(cube[2]-PLAYER.z)**2),cube[0],cube[1],cube[2]))
    cubes2.sort()
    cubes2.reverse()
    for cube in cubes2:
        draw_cube((cube[1],cube[2],cube[3]),PLAYER)
        
    PLAYER.MOVE()
        
run = True
while run:
    
    
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()

    
pygame.quit()
