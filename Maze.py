import turtle
import math
import random
import time
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(700,700)
wn.tracer(0)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.ht()
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
    def up(self):
        if (self.xcor(),self.ycor()+24) not in walls:
            self.goto(self.xcor(),self.ycor()+24)
    def down(self):
        if (self.xcor(),self.ycor()-24) not in walls:
            self.goto(self.xcor(),self.ycor()-24)
    def left(self):
        if (self.xcor()-24,self.ycor()) not in walls:
            self.goto(self.xcor()-24,self.ycor())
    def right(self):
        if (self.xcor()+24,self.ycor()) not in walls:
            self.goto(self.xcor()+24,self.ycor())
    def collision(self,t2,a):
        distance = math.sqrt(math.pow(self.xcor()-t2.xcor(),2)+math.pow(self.ycor()-t2.ycor(),2))
        if distance == a:
            return True
    def destroy(self):
        self.ht()
class Portal(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)
        self.goto(x,y)
         
class Money(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        
class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.ways = ["up","down","left","right"]
        self.direction = random.choice(self.ways)
    def move(self):
        
        
        if self.direction == "up":
            dx = 0
            dy = 24
        if self.direction == "down":
            dx = 0
            dy = -24
        if self.direction == "right":
            dx = 24
            dy = 0
        if self.direction == "left":
            dx = -24
            dy  = 0
      
        futurex = self.xcor() + dx
        futurey = self.ycor() + dy

        if (futurex , futurey) not in walls:
            self.goto(futurex , futurey)
        else:
            self.direction = random.choice(self.ways)
            
        turtle.ontimer(self.move, t = 200)
    def destroy(self):
        self.goto(2000,2000)
        self.ht()
 
        




walls = []

levels = []


          
   

penwrite = Pen()

pen = Pen()
enemies = []
moneys = []
portals = []
p1 = Player()
b=0
lives = 5
def setmaze(pen,level):
    global b
    if b==len(level):
        b=False
    else:
        a = level[b]
    
        b+=1
   
    
        for y in range(len(a)):
            for x in range(len(a[y])):
                char = a[y][x]
                scrnx = -288 + (x*24)
                scrny = 288-(y*24)
                if char == "X":
                    pen.goto(scrnx,scrny)
                    pen.stamp()
                    walls.append((scrnx,scrny))
                if char == "P":
                    p1.goto(scrnx,scrny)
                if char == "E":
                    enemies.append(Enemy(scrnx,scrny))
                if char == "M":
                    moneys.append(Money(scrnx,scrny))
                if char =="p":
                    
                    portals.append(Portal(scrnx,scrny))
                    
                
                
def game(pen,moneys,p1,portals,enemies,walls,levels,penwrite):
    global b
    global lives
    
    message = "LIVES: %s"%(lives)
    messagelevel = "LEVEL %s"%(b+1)
    penwrite.goto(-288,300)
    penwrite.write(message, font = ("Arial",16,"normal"))
    messagelevel = "LEVEL %s"%(b+1)
    penwrite.goto(200,300)
    penwrite.write(messagelevel, font = ("Arial",16,"normal"))
    if lives==0:
        
        print("GAMEOVER")
        p1.destroy()
        wn.bye()
        
        
    
    totalmoney=0
    
    
    accessportal = False
    nextlevel=True
    setmaze(pen,levels)
    
    turtle.listen()
    turtle.onkey(p1.down,"Down")
    turtle.onkey(p1.up,"Up")
    turtle.onkey(p1.left,"Left")
    turtle.onkey(p1.right,"Right")

    for enemy in enemies:
            enemy.move()
    if b==False:
        print("YOU WON")
        wn.bye()
    while nextlevel:
            
        for enemy in enemies:
            if p1.collision(enemy,0):
                b-=1
                lives-=1
                nextlevel=False
                
                break
            
        for money in moneys:
            if p1.collision(money,0):
                totalmoney+=1
                money.ht()
                money.goto(200000,20000000)
        for portal in portals:
            if p1.collision(portal,0):
                if totalmoney==len(moneys):
                    accessportal = True
                    nextlevel = False
                    
                        
                else:
                    print("YOU NEED TO COLLECT ALL THE COINS")
                    p1.undo()
        wn.update()

        
    for enemy in enemies:
        enemy.ht()
        
    for portal in portals:
        portal.ht()
        
    for money in moneys:
        money.ht()
        
    walls.clear()
    enemies.clear()
    portals.clear()
    moneys.clear()
    
    
    
    penwrite.clear()
    pen.clear()
    game(pen,moneys,p1,portals,enemies,walls,levels,penwrite)



level1 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XP M      M     M      pX",
          "XXXXXXXXXXXXXXXXXXXXXXXXX"]
levels.append(level1)

level2 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XXXXXXXXXXXEXXXXXXXXXXXXX",
          "XP MMM M         M     pX",
          "XXXXXXXXXXX XXXXXXXXXXXXX",
          "XXXXXXXXXXXXXXXXXXXXXXXXX"]
levels.append(level2)

level3 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XPXM MXM MXM MXM MXMX   X",
          "X X X X X X X X X X X p X",
          "X X X X X X X X X X XE  X",
          "X X X X X X X X X X XX XX",
          "X X X X X X X X X X X   X",
          "X X X X X X X X X X XXX X",
          "X X X X X X X X X X   X X",
          "X X X X X X X X X X X X X",
          "X   X   X   X   X   X   X",
          "XXXXXXXXXXXXXXXXXXXXXXXXX"]
levels.append(level3)

level4 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XPX     XM      E       X",
          "X X M X XXXXXX XXXXX XXXX",
          "X XE  X XX  EX X   X XXpX",
          "X  X XX    M X X X X XX X",
          "XX X  X XX   X X X X XX X",
          "XX XX XXXXXX X X X   XX X",
          "XX XE  X     X X XXXXXX X",
          "XX X M X XXX X X      X X",
          "XX X   X XXXXX XXXX XXX X",
          "XE  X XX X M   XM    X  X",
          "X M   XEM X XX XXXX XXX X",
          "X   XXX      XMX        X",
          "XXXXXXXXXXXXXXXXXXXXXXXXX",]
levels.append(level4)
level5 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XXPXXXXXXE           MXXX",
          "XX XXXXXXXXXXXXXX XX XXXX",
          "X  M  EXE     M    X XXXX",
          "XX XXXXXXXXX XXXXXXX XXXX",
          "XX XE    M    X   M   EXX",
          "XX XXXXXXXXX XXXXXXXXX XX",
          "X   M     EX XX       MXX",
          "XXXX XXXXXXX XXXXXX XXXXX",
          "XE       M    Xp      EXX",
          "XXXXXXXXXXXXXXXXXXXXXXXXX"]
levels.append(level5)
YouWon = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "X                       X",
          "X p   p ppppppp p     p X",
          "X p   p p     p p     p X",
          "X p   p p     p p     p X",
          "X p   p p     p p     p X",
          "X p   p p     p p     p X",
          "X ppppp p     p p     p X",
          "X   p   p     p p     p X",
          "X   p   p     p p     p X",
          "X   p   p     p p     p X",
          "X   p   ppppppp ppppppp X",
          "X                       X",
          "X                       X",
          "X p     p pppppp pppppp X",
          "X p     p p    p p    p X",
          "X p     p p    p p    p X",
          "X p  p  p p    p p    p X",
          "X p  p  p p    p p    p X",
          "X p  p  p p    p p    p X",
          "X p  p  p p    p p    p X",
          "X p  p  p p    p p    p X",
          "X ppppppp pppppp p    p X",
          "X                       X",
          "XXXXXXXXXXXXXXXXXXXXXXXXX"]
levels.append(YouWon)
game(pen,moneys,p1,portals,enemies,walls,levels,penwrite)
