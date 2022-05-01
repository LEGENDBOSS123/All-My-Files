#CLIENT
import socket
import threading
import pygame
pygame.init()

xval = 750
yval = 750
IP = input("IP: ")
port = int(input("PORT: "))
wn = pygame.display.set_mode((xval,yval))

def ENCODE(lis):
    return str(lis[0])+","+str(lis[1])
def DECODE(string):
    return [int(string.split(",")[0]),int(string.split(",")[1])]


class PLAYER():
    def __init__(self,x,y,who):
        self.x = x
        self.y = y
        self.speed = 3
        self.color = 0
        self.size = 100
        self.who = who
        if self.who == True:
            self.color = (0,255,0)
        else:
            self.color = (255,0,0)
            
    def DRAW(self):
        self.MOVE()
        pygame.draw.rect(wn,self.color,(self.x,self.y,self.size,self.size))
        
    def MOVE(self):
        if self.who == True:
            key = pygame.key.get_pressed()
            
            if key[pygame.K_UP]:
                self.y-=self.speed
            if key[pygame.K_DOWN]:
                self.y+=self.speed
            if key[pygame.K_RIGHT]:
                self.x+=self.speed
            if key[pygame.K_LEFT]:
                self.x-=self.speed
            


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



client_sock.connect((IP, port))
connection = True

people = [PLAYER(200,200,True),PLAYER(200,200,False)]


        
        
        
        
        

while connection:
    client_sock.send(ENCODE((people[0].x,people[0].y)).encode())

    data = DECODE(client_sock.recv(1024).decode())
    #print(data)
    people[1].x = data[0]
    people[1].y = data[1]

    wn.fill((0,0,0))
    for i in people:
        i.DRAW()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            connection = False
    
    pygame.display.update()
    

client_sock.close()
pygame.quit()
