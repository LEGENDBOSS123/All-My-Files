import pygame
import math
import time
pygame.init()

xval = 2500
yval = 1400
bg = (75,75,75)
wn = pygame.display.set_mode((xval,yval))
def refill():
    wn.fill(bg)


class VECTOR():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def add_vectors(a,b):
    return VECTOR(a.x+b.x,a.y+b.y)

def subtract_vectors(a,b):
    return VECTOR(a.x-b.x,a.y-b.y)

def multiply_vectors(a,b):
    return VECTOR(a.x*b,a.y*b)

def divide_vectors(a,b):
    return VECTOR(a.x/b,a.y/b)

def equal_vectors(a,b):
    if a.x==b.x and a.y==b.y:
        return True
    else:
        return False
    
def length(a):
    return math.sqrt(a.x**2+a.y**2)


def distance(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

def normalize(a):
    l = length(a)
    if l == 0:
        return VECTOR(0,1)
    return VECTOR(a.x/l,a.y/l)

def dot_product(a,b):
    return a.x*b.x+a.y*b.y

def cross_product(a,b):
    
    return a.x*b.y-a.y*b.x


def transform(a,angl,center):
    angle = -1*angl * math.pi / 180
    
    x = (a.x-center.x)*math.cos(angle)-(a.y-center.y)*math.sin(angle)
    y = (a.y-center.y)*math.cos(angle)+(a.x-center.x)*math.sin(angle)

    return VECTOR(x+center.x,y+center.y)



    
class POLYGON():
    def __init__(self,x,y, verticies,dense,color,bounciness,angle,r):
        self.x = x

        self.y = y

        self.density = dense

        self.bounciness = bounciness

        
        self.verticies = []
        for i in verticies:
            self.verticies.append(VECTOR(i[0],i[1]))
        self.overticies = self.verticies
        
        self.color = color
        
        self.angle = angle

        self.linearvel = VECTOR(0,0)

        self.force = VECTOR(0,0)

        self.angularvel = r


        self.static = False

        self.area = 0

        for i in range(len(self.verticies)-1):
            self.area+=self.verticies[i].x*self.verticies[i+1].y-self.verticies[i].y*self.verticies[i+1].x
        self.area+=self.verticies[-1].x*self.verticies[0].y-self.verticies[-1].y*self.verticies[0].x

        self.area = abs(self.area/2)

        self.mass = self.area*self.density

        if self.density == 0:
            self.static = True

        self.gravity = 0.5

        self.center = 0

        cx = 0
        cy = 0
        for i in self.verticies:
            cx+=i.x
            cy+=i.y
        
        
        self.center = [cx/len(self.verticies),cy/len(self.verticies)]

        

        
    def rotate(self,I):
        self.angle+=self.angularvel/I
        v = []
        for i in self.overticies:
            v.append(transform(i,self.angle,VECTOR(self.center[0],self.center[1])))
        self.verticies = v
        
        
    def apply_force(self,f):
        self.force = add_vectors(self.force,f)
    def update(self,I):
        self.linearvel = add_vectors(self.linearvel,divide_vectors(self.force,self.mass))
        self.linearvel.y+=self.gravity
        self.x+=self.linearvel.x/I
        self.y+=self.linearvel.y/I
        
        self.force = VECTOR(0,0)
        
        
    
        
    def draw(self,I):
        if not self.static:
            self.update(I)
        self.rotate(I)

        v = []
        
        for i in self.verticies:
            v.append((int(i.x+self.x),int(i.y+self.y)))
        pygame.draw.polygon(wn,self.color,v)

    
        
class CIRCLE():
    def __init__(self,x,y,radius,dense,color,bounciness):

        self.bounciness = bounciness
        
        self.x = x
        
        self.y = y
                
        self.radius = radius
        
        self.color = color
        
        self.area = radius**2 * math.pi
        
        self.density = dense

        self.static = False
        
        if dense==0:
            self.static = True

        self.mass = self.area * self.density


        self.gravity = 0.5

        self.linearvel = VECTOR(0,0)

        self.force = VECTOR(0,0)


        


    def apply_force(self,f):
        self.force = add_vectors(self.force,f)
    def update(self,I):
        self.linearvel = add_vectors(self.linearvel,divide_vectors(self.force,self.mass))
        self.linearvel.y+=self.gravity
        self.x += self.linearvel.x/I
        self.y += self.linearvel.y/I
        self.force = VECTOR(0,0)
    
            
    def draw(self,I):
        if not self.static:
            self.update(I)
        pygame.draw.circle(wn,self.color,(int(self.x),int(self.y)),int(self.radius))


        
class PLAYER():
    def __init__(self,x,y,radius,dense,color,bounciness):

        self.static = False

        self.bounciness = bounciness
        
        self.ox = x

        self.oy = y
        
        self.x = x
        
        self.y = y
                
        self.radius = radius
        
        self.color = color
        
        self.area = radius**2 * math.pi
        
        self.density = dense

        self.mass = self.area * self.density

        self.gravity = 0.5

        self.ogravity = self.gravity

        self.linearvel = VECTOR(0,0)

        self.speed = 0.5

        self.force = VECTOR(0,0)

        

    
    
    def apply_force(self,f):
        self.force = add_vectors(self.force,f)
    def update(self,I):
        self.linearvel = add_vectors(self.linearvel,divide_vectors(self.force,self.mass))
        self.linearvel.y+=self.gravity
        self.x += self.linearvel.x/I
        self.y += self.linearvel.y/I
        self.force = VECTOR(0,0)
        
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        
        dx = 0
        dy = 0
        
        if keys[pygame.K_RIGHT]:
            dx+=self.speed
        if keys[pygame.K_LEFT]:
            dx-=self.speed

        if keys[pygame.K_UP]:
            
            self.gravity = self.ogravity/4
        elif keys[pygame.K_DOWN]:
            self.gravity = self.ogravity*2
        else:
            self.gravity = self.ogravity

        if dx!=0 or dy!=0:
            force = multiply_vectors(normalize(VECTOR(dx,dy)),self.speed)
            self.linearvel = add_vectors(self.linearvel,force)
            
            

        
            
        
            
    
    
    def draw(self,I):
        self.update(I)
        self.move()
        pygame.draw.circle(wn,self.color,(int(self.x),int(self.y)),int(self.radius))
        
class WORLD():
    def __init__(self):
        self.polygons = []
        self.circles = []
    def resolve_collision(self,a,b,normal):
        bounciness = 0
        if a.bounciness<0 and b.bounciness<0:
            bounciness = 0
        elif a.bounciness<0 or b.bounciness<0:
            bounciness = a.bounciness+b.bounciness
        
        else:
            bounciness = max(a.bounciness,b.bounciness)
        bounciness = max(0,bounciness)
        relvel = subtract_vectors(b.linearvel,a.linearvel)
        j = 0
        if a.static:
            j = -(1+bounciness)*dot_product(relvel,normal)/(1/b.mass)
        elif b.static:
            j = -(1+bounciness)*dot_product(relvel,normal)/(1/a.mass)
        else:
            
            j = -(1+bounciness)*dot_product(relvel,normal) / (1/a.mass+1/b.mass)
        
        if not a.static:
            a.linearvel = subtract_vectors(a.linearvel,multiply_vectors(normal,j / a.mass))
        if not b.static:
            b.linearvel = add_vectors(b.linearvel,multiply_vectors(normal,j / b.mass))

    def circles_intersect(self,a,b):
        centerA = VECTOR(a.x,a.y)
        centerB = VECTOR(b.x,b.y)
        radiusA = a.radius
        radiusB = b.radius
        
        dis = distance(centerA,centerB)
        totalradius = radiusA + radiusB
        
        if dis>=totalradius:
            return False

        normal = normalize(subtract_vectors(centerB,centerA))
        depth = totalradius-dis
        return [normal,depth]
    
    def project_verticies(self,axis,v,a):
        mini = 99999999999999999999
        maxi = -99999999999999999999

        for i in range(len(v)):
            Vec = v[i]
            Vec = add_vectors(a,Vec)
            projection = dot_product(Vec,axis)
            if projection<mini:
                mini = projection
            if projection>maxi:
                maxi = projection
        
        return (mini,maxi)

        
    def polygons_intersect(self,a,b):
        depth = 99999999999999999999
        normal = 0
        for i in range(len(a.verticies)):
            va = a.verticies[i]
            vb = a.verticies[(i+1)%len(a.verticies)]
            
            edge = subtract_vectors(vb,va)

            axis = normalize(VECTOR(-edge.y,edge.x))
            
            first = self.project_verticies(axis, a.verticies,a)
            second = self.project_verticies(axis, b.verticies,b)
            
            if first[0] >= second[1] or first[1] <=second[0]:
                return False
            
            depthA = min(abs(second[1]-first[0]),abs(first[1]-second[0]))           
            if depthA<depth:
                depth = depthA
                normal = axis
            
            
        for i in range(len(b.verticies)):
            va = b.verticies[i]
            vb = b.verticies[(i+1)%len(b.verticies)]
            
            edge = subtract_vectors(vb,va)
            
            axis = normalize(VECTOR(-edge.y,edge.x))
            
            first = self.project_verticies(axis, a.verticies,a)
            second = self.project_verticies(axis, b.verticies,b)
            
            if first[0] >= second[1] or first[1] <=second[0]:
                return False
            
            depthA = min(abs(second[1]-first[0]),abs(first[1]-second[0]))           
            if depthA<depth:
                depth = depthA
                normal = axis
        
        direction = subtract_vectors(VECTOR(b.center[0]+b.x,b.center[1]+b.y),VECTOR(a.center[0]+a.x,a.center[1]+a.y))
        

        if dot_product(direction,normal)<0:
            normal = multiply_vectors(normal,-1)
        return [normal,depth]
    def project_circle_verticies(self,axis,b):
        direction = axis
        direction = multiply_vectors(direction,b.radius)
        p1 = add_vectors(VECTOR(b.x,b.y),direction)
        p2 = subtract_vectors(VECTOR(b.x,b.y),direction)
        mini = dot_product(p1,axis)
        maxi = dot_product(p2,axis)

        if mini>maxi:
            e = mini
            z = maxi
            mini = z
            maxi = e
        return (mini,maxi)
    def closest_point_on_polygon(self,a,b):
        result = 0
        mini = 99999999999999999999
        for i in range(len(a.verticies)):
            v = add_vectors(a.verticies[i],a)
            dis = distance(v,b)

            if dis<mini:
                mini = dis
                result = i
                
        return result


        
    def polygon_circle_intersect(self,a,b):
        depth = 99999999999999999999
        normal = 0
        axis = 0
        depthA = 0
        
        for i in range(len(a.verticies)):
            va = a.verticies[i]
            vb = a.verticies[(i+1)%len(a.verticies)]

            edge = subtract_vectors(vb,va)

            axis = normalize(VECTOR(-edge.y,edge.x))
            
            first = self.project_verticies(axis, a.verticies,a)
            second = self.project_circle_verticies(axis,b)
            
            if first[0] >= second[1] or first[1] <= second[0]:
                return False
            
            depthA = min(abs(second[1]-first[0]),abs(first[1]-second[0]))            
            if depthA<depth:
                depth = depthA
                normal = axis
        cpindex = self.closest_point_on_polygon(a,b)
        cp = add_vectors(a.verticies[cpindex],a)
        axis = normalize(subtract_vectors(cp,VECTOR(b.x,b.y)))
            
        first = self.project_verticies(axis, a.verticies,a)
        second = self.project_circle_verticies(axis,b)
        
        if first[0] >= second[1] or first[1] <= second[0]:
            return False
        
        depthA = min(abs(second[1]-first[0]),abs(first[1]-second[0]))          
        if depthA<depth:
            depth = depthA
            normal = axis
            
        
        direction = subtract_vectors(VECTOR(b.x,b.y),VECTOR(a.center[0]+a.x,a.center[1]+a.y))

        if dot_product(direction,normal)<0:
            normal = multiply_vectors(normal,-1)
        return (normal,depth)

        
    
WORLD = WORLD()

    
        
size = 30

for i in range(3):
    WORLD.circles.append(PLAYER(1000,400,size,1,(255,255,0),0.95))



'''WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,5,0))
WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,10,0))
WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,15,0))
WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,20,0))
WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,25,0))
WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,30,0))
WORLD.polygons.append(POLYGON(100,500,((100,100),(100,200),(200,200),(200,100)),0.1,(0,255,0),1,35,3))'''

WORLD.polygons.append(POLYGON(1000,1450,((-900,-500),(-900,500),(900,500),(900,-500)),0,(0,255,0),-1,0,0))
#WORLD.polygons.append(POLYGON(400,-150,((-3000,100),(-3000,200),(2000,200),(2000,100)),0,(0,255,0),-1,0,0))
WORLD.polygons.append(POLYGON(500,200,((-300,-10),(-300,10),(300,10),(300,-10)),0,(0,255,0),2,50,0))
WORLD.polygons.append(POLYGON(1500,200,((-300,-10),(-300,10),(300,10),(300,-10)),0,(0,255,0),2,-50,0))


WORLD.polygons.append(POLYGON(2050,750,((-100,10),(-100,-10),(100,-10),(100,10)),0,(0,255,0),1,-45,0))
WORLD.polygons.append(POLYGON(2120,1015,((-200,10),(-200,-10),(200,-10),(200,10)),0,(0,255,0),-100,90,0))
WORLD.polygons.append(POLYGON(2005,1200,((-100,10),(-100,-10),(100,-10),(100,10)),0,(0,255,0),4,0,0))
WORLD.polygons.append(POLYGON(-5,1200,((-100,10),(-100,-10),(100,-10),(100,10)),0,(0,255,0),4,0,0))
WORLD.polygons.append(POLYGON(-120,1015,((-200,10),(-200,-10),(200,-10),(200,10)),0,(0,255,0),-100,90,0))
WORLD.polygons.append(POLYGON(-50,750,((-100,10),(-100,-10),(100,-10),(100,10)),0,(0,255,0),1,45,0))
WORLD.circles.append(CIRCLE(50,800,105,500,(0,0,255),-1)) 
WORLD.polygons.append(POLYGON(500,500,((0,0),(100,20),(135,33),(150,66),(160,135),(100,200),(42,230),(-13,66)),1,(0,255,0),-3,45,0))




'''
WORLD.polygons.append(POLYGON(800,800,((-300,100),(-300,200),(1000,100)),0,(0,255,0),1,45,0))
WORLD.polygons.append(POLYGON(800,800,((-300,100),(-300,200),(-200,100)),0,(0,255,0),1,45,0))
'''

'''
WORLD.polygons.append(POLYGON(100,400,((0,0),(100,10),(210,0),(250,-30),(250,-100),(230,-120),(150,-200),(30,-160),(-30,-50)),1,(0,255,0),0,180,0))
WORLD.polygons.append(POLYGON(100,800,((0,0),(100,10),(210,0),(250,-30),(250,-100),(230,-120),(150,-200),(30,-160),(-30,-50)),1,(0,255,0),1,0,0))
'''
WORLD.polygons.append(POLYGON(1000,925,((-100,0),(0,50),(100,0)),0,(0,255,0),1,180,0))
'''
WORLD.polygons.append(POLYGON(-50,25,((0,0),(100,50),(200,0)),0,(0,255,0),1,90,0))
WORLD.polygons.append(POLYGON(100,130,((0,0),(1800,0),(1800,10),(0,10)),0,(0,255,0),1,0,0))
WORLD.polygons.append(POLYGON(1850,50,((0,0),(100,50),(200,0)),0,(0,255,0),1,0,0))
WORLD.polygons.append(POLYGON(1850,932,((0,0),(100,50),(200,0)),0,(0,255,0),1,-90,0))

'''
def draw():
    refill()
    
    for R in WORLD.polygons:
        for C in WORLD.circles:
            if C!=R:
                collide = WORLD.polygon_circle_intersect(R,C)
                if collide!=False and not( C.static==True and R.static == True):
                    
                    normal = collide[0]
                    depth = collide[1]+1
                    
                        
                    distanceC = multiply_vectors(normal,depth/2)
                    distanceR = multiply_vectors(normal,-depth/2)

                    if C.static:
                        distanceR = multiply_vectors(normal,-depth)
                        R.x+=distanceR.x
                        R.y+=distanceR.y
                        
                    elif R.static:
                        distanceC = multiply_vectors(normal,depth)
                        C.x+= distanceC.x
                        C.y+=distanceC.y
                    else:

                        C.x+=distanceC.x
                        C.y+=distanceC.y

                        R.x+=distanceR.x
                        R.y+=distanceR.y
                    WORLD.resolve_collision(R,C,normal)
                    
    for R in WORLD.polygons:
        for C in WORLD.polygons:
            if C!=R:
                collide = WORLD.polygons_intersect(R,C)
                
                if collide!=False and not( C.static==True and R.static == True):
                    
                    normal = collide[0]
                    depth = collide[1]+1
                    
                        
                    distanceC = multiply_vectors(normal,depth/2)
                    distanceR = multiply_vectors(normal,-depth/2)

                    if C.static:
                        distanceR = multiply_vectors(normal,-depth)
                        R.x+=distanceR.x
                        R.y+=distanceR.y
                        
                    elif R.static:
                        distanceC = multiply_vectors(normal,depth)
                        C.x+= distanceC.x
                        C.y+=distanceC.y
                    else:

                        C.x+= distanceC.x
                        C.y+=distanceC.y

                        R.x+=distanceR.x
                        R.y+=distanceR.y
                    WORLD.resolve_collision(R,C,normal)

    for R in WORLD.circles:
        for C in WORLD.circles:
            if C!=R:
                collide = WORLD.circles_intersect(R,C)
                if collide!=False and not( C.static==True and R.static == True):
                    normal = collide[0]
                    depth = collide[1]+1

                    
                        
                    distanceC = multiply_vectors(normal,depth/2)
                    distanceR = multiply_vectors(normal,-depth/2)

                    if C.static:
                        distanceR = multiply_vectors(normal,-depth)
                        R.x+=distanceR.x
                        R.y+=distanceR.y
                        
                    elif R.static:
                        distanceC = multiply_vectors(normal,depth)
                        C.x+= distanceC.x
                        C.y+=distanceC.y
                    else:

                        C.x+= distanceC.x
                        C.y+=distanceC.y

                        R.x+=distanceR.x
                        R.y+=distanceR.y

                    WORLD.resolve_collision(R,C,normal)

                

        
    I = 10
    
    for PLATFORM in WORLD.polygons:
        PLATFORM.draw(I)
    for PLATFORM in WORLD.circles:
        PLATFORM.draw(I)


print(str(len(WORLD.polygons)+len(WORLD.circles))+" SHAPES")
run = True
fps = 100
clock = pygame.time.Clock()
while run:
    timer = time.time()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    pygame.display.update()
    
    clock.tick(fps)

    
pygame.quit()
