import pygame
import sys
from math import *

import os
import threading

SCREENWIDTH = 800
SCREENHEIGHT = 600
ASPECT = float(SCREENWIDTH)/float(SCREENHEIGHT)

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Raytracer")

pygame.mixer.init()

clock = pygame.time.Clock()
clock.tick()

time = 0

running = True

fps = 0

def normalize(i,j,k):
  norm = sqrt(float(i*i + j*j + k*k))
  if norm == 0:
      return (0,0,0)
  else:
      return (i/norm, j/norm, k/norm)
          
def dot(v1, v2):
  return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
  
def nSphere(pos, sphere):
  x,y,z,r = sphere
  
  return normalize(pos[0] - x, pos[1] - y, pos[2] - z)
  
def nPlane(pos):
  return (0.0, 1.0, 0.0)
          
def iSphere(ro, rd, sphere):

  x,y,z,r = sphere
  oc = (ro[0] - x, ro[1] - y, ro[2] - z)
  
  b = 2.0*dot(oc, rd)
  c = dot(oc,oc) - r*r;
  
  h = b*b - 4.0*c;
  
  if h < 0.0:
      return -1.0
          
  t = (-b - sqrt(h))/2.0
  
  return t
          
          
def iPlane(ro,rd):
  if rd[1] == 0:
      return -1.0
          
  return -ro[1]/rd[1]
  
sph1 = [0.0, 1.0, 0.0, 1.0]
def intersect(ro, rd):
  id = -1
  resT = 1000.0
  
  tsph = iSphere(ro, rd, sph1)
  tpla = iPlane(ro,rd)
  
  if tsph > 0.0:
      id = 1
      resT = tsph
  
  if tpla > 0.0 and tpla < resT:
      id = 2
      resT = tpla
  return id,resT

def mult(s,v):
  return (s*v[0], s*v[1], s*v[2])
def add(v1, v2):
  return (v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2])
def subtract(v1, v2):
  return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])
  
def smoothstep(low, high, x):
  if x > high:
      return 1.0
  if x < low:
      return 0.0
          
  x = (x - low)/(high - low)
  
  return x*x*(3-2*x)
  
def norm(v):
  return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])

light = normalize(0.57703,0.57703,0.57703)

def drawPixel(u,v):
  out = (0.7,0.7,0.7)
  
  ro = (0.0,0.5,3.0)
  rd = normalize( (-1.0 + 2.0*u )*ASPECT ,1.0 - 2.0*v, -1.0)

  
  id,t = intersect(ro, rd)
  
  if id == 1:
      pos =  add(ro, mult(t,rd))
      
      nor = nSphere(pos, sph1)
      
      dif = dot(nor, light)
      ao = 0.5 + 0.5*nor[1]

      out = (0.9, 0.8, 0.6)
      out = mult(dif*ao, out)
      out = add(out , mult(ao, (0.1, 0.2,0.4)))
  if id == 2:
          pos = add(ro, mult(t,rd))
          nor = nPlane(pos)
          dif = dot(nor, light)
          
          amb = smoothstep(0.0, 2.0*sph1[3], norm(subtract( (pos[0], 0.0, pos[2]), (sph1[0], 0.0, sph1[2]) )) )
          out = (amb*0.7, amb*0.7, amb*0.7)
          
          t2 = iSphere(pos, light, sph1)
          if  t2 > 0.0:
                  dist = norm(mult(t2, light))
                  factor = 0.5
                  if dist < 1:
                          factor = dist*0.5
                  out = mult(factor, out)
          
  out = (limit(out[0], 0.0, 1.0), limit(out[1], 0.0, 1.0), limit(out[2], 0.0, 1.0))
  out = (sqrt(out[0]),sqrt(out[1]),sqrt(out[2]))
  return out
  
def limit(value, lower, upper):
  if value < lower:
          return lower
  if value > upper:
          return upper
  return value
  
class Column( threading.Thread ):
  def __init__(self, low, high):
          self.low = low
          self.high = high
          self.draw = False
          threading.Thread.__init__(self)
  def run(self):
          while True:
                  if self.draw == True:
                          for x in range(self.low, self.high):
                                  for y in range(SCREENHEIGHT):
                                          color = drawPixel(float(x)/SCREENWIDTH,float(y)/SCREENHEIGHT)
                                          r = limit(color[0]*255, 0, 255)
                                          g = limit(color[1]*255, 0, 255)
                                          b = limit(color[2]*255, 0, 255)
                                          screen.set_at((x,y), (r,g,b) )
                          self.draw = False

threads = 1
columns = []

if threads > 1:
  for n in range(threads):
          columns.append( Column(n*(SCREENWIDTH/threads), (n+1)*(SCREENWIDTH/threads)) )
          columns[n].start()
          
frame = 0
frames = 250
fps = 25

def drawScene():
  screen.fill((0,0,0))
  
  if threads == 1:
          for x in range(SCREENWIDTH):
                  for y in range(SCREENHEIGHT):
                          color = drawPixel(float(x)/SCREENWIDTH,float(y)/SCREENHEIGHT)
                          r = limit(color[0]*255, 0, 255)
                          g = limit(color[1]*255, 0, 255)
                          b = limit(color[2]*255, 0, 255)
                          screen.set_at((x,y), (r,g,b) )
  else:
          for n in range(threads):
                  columns[n].draw = True
          while columns[4].draw == True:
                  pass
  
  #pygame.image.save(screen, "out\\" + str(frame) + ".png")
  
  pygame.display.flip()
  





while frame < frames:
  #Events
  for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  sys.exit()
          if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                          sys.exit()
                          
  time = float(frame)/fps
  sph1[0] = sin(time)
  sph1[1] = cos(time)
  sph1[2] = sin(time)*cos(time)
                          
  drawScene()
  
  print(time)
  
  frame += 1
  
#os.system('ffmpeg -framerate ' + str(fps) + ' -f image2 -i out//%d.png output.mp4')
