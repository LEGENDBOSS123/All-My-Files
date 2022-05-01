import random
import math
import pygame

pygame.init()

xval = 1200
yval = 700
wn = pygame.display.set_mode((xval, yval))

class QuadTree():
    def __init__(self,rect = (0, 0, xval, yval), maxp=4, depth=0):
        self.rect = rect
        self.points = []
        self.depth = depth
        self.maxp = maxp
        self.divided = False
        self.nw = 0
        self.ne = 0
        self.se = 0
        self.sw = 0
        
    def divide(self):
        cx, cy = self.rect[0], self.rect[1]
        w, h = self.rect[2]/2, self.rect[3]/2
        
        self.nw = QuadTree((cx, cy, w, h), self.maxp, self.depth + 1)
        self.ne = QuadTree((cx + w, cy, w, h),self.maxp, self.depth + 1)
        self.se = QuadTree((cx + w, cy + h, w, h),self.maxp, self.depth + 1)
        self.sw = QuadTree((cx, cy + h, w, h),self.maxp, self.depth + 1)

        

        self.divided = True
        
    def contains(self,point,rect):
        
        return (point[0] >= rect[0] and
                point[0] < rect[0]+rect[2] and
                point[1] >= rect[1] and
                point[1] < rect[1]+rect[3])
    
    def intersect(self,rectangle):
        return not(rectangle[0] > self.rect[0]+self.rect[2] or
                   rectangle[0]+rectangle[2] < self.rect[0] or
                   rectangle[1] > self.rect[1]+self.rect[3] or
                   rectangle[1]+rectangle[3] < self.rect[1])
    
    def PLACE(self,point):
        if not self.contains(point,self.rect):
            return False
        if len(self.points) < self.maxp:
            self.points.append(point)
            return True
        
        if not self.divided:
            self.divide()

        return (self.ne.PLACE(point) or
                self.nw.PLACE(point) or
                self.se.PLACE(point) or
                self.sw.PLACE(point))
    def REMOVE(self,point):
        if not self.contains(point,self.rect):
            return False
        
        if point in self.points:
            self.points.remove(point)
        
        
        
        if self.divided:
            return (self.ne.REMOVE(point) or
                    self.nw.REMOVE(point) or
                    self.se.REMOVE(point) or
                    self.sw.REMOVE(point))
        
    def RANGE(self,boundary,found_points=[]):
        
        if not(self.intersect(boundary)):
            
            return False
        
        for point in self.points:
            if self.contains(point,boundary):
                found_points.append(point)
                
        if self.divided:
            self.nw.RANGE(boundary,found_points)
            self.ne.RANGE(boundary,found_points)
            self.sw.RANGE(boundary,found_points)
            self.se.RANGE(boundary,found_points)
            
        return found_points
    def draw(self):
        pygame.draw.rect(wn,(255,255,255),self.rect,1)
        if self.divided:
            self.ne.draw()
            self.nw.draw()
            self.se.draw()
            self.sw.draw()
    

Tree = QuadTree()
squares = []
size = 20
view_margin = 2*size
width = 57
height = 32
how_many_squares = 300


for y in range(height):
    for x in range(width):
        x_coord = x * size + view_margin
        y_coord = y * size + view_margin
        squares.append((x_coord, y_coord))
        Tree.PLACE((x_coord, y_coord))
        
for i in range(width*height-how_many_squares):
    ran = random.choice(squares)
    Tree.REMOVE(ran)
    squares.remove(ran)
    

    
ask = (300,300,500,500)
points = Tree.RANGE(ask)

#print(found_points)
draw_color = (200, 200, 200)
border_width = 2

def draw_square(s):
    draw_rect = (s[0] - 0.5 * size, s[1] - 0.5 * size, size, size)
    #pygame.draw.rect(wn, draw_color, draw_rect, border_width)
    pygame.draw.circle(wn,draw_color,(s[0],s[1]),3)


def d(s):
    draw_rect = (s[0] - 0.5 * size, s[1] - 0.5 * size, size, size)
    #pygame.draw.rect(wn, draw_color, draw_rect, border_width)
    pygame.draw.circle(wn,(255,0,0),(s[0],s[1]),3)





def draw():
    
    wn.fill((100,100,100))
    
    pygame.draw.rect(wn,(255,0,0),ask,5)
    for s in squares:
        draw_square(s)
        
    for s in points:
        d(s)
    

        
    '''for i in range(width):
        pygame.draw.line(wn,(255,255,255),(i*size+view_margin,0),(i*size+view_margin,yval))
    for i in range(height):
        pygame.draw.line(wn,(255,255,255),(0,i*size+view_margin),(xval,i*size+view_margin))
'''
    Tree.draw()

run = True

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()

    
pygame.quit()
