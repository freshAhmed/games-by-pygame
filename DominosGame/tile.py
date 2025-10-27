
import pygame
import logging
log=logging.getLogger('__main__')


def joinimagetile(pos,size,angle,images,scale):
 width,height=size

 topimage,bottomimage=images
 if angle==0:
  surface=pygame.Surface((width,height))
  
  surface.blit(topimage,(0,0),(0,0,width,70))
  surface.blit(bottomimage,(0,75),(0,0,width,70))
 else:
  surface=pygame.Surface((height,width))
  surface.blit(topimage,(75,0),(0,0,width,70))
  surface.blit(bottomimage,(0,0),(0,0,width,70))
 
 return pygame.transform.scale_by(surface,scale)

class Tile(pygame.sprite.Sprite):
 def __init__(self,pos,imagestiles,size,pips):
  
  pygame.sprite.Sprite.__init__(self)
  self.pips=pips
  self.pos=pygame.Vector2(pos)
  self.imagestiles =imagestiles
  self.scale=1

  topimage=self.imagestiles[self.pips[0]]
  bottomimage=self.imagestiles[self.pips[1]]

  self.image=joinimagetile(pos,size,0,[topimage,bottomimage],self.scale)
  self.rect=self.image.get_rect(center=self.pos)
  self.angle=0
  self.flag=False #to control what tile allowed to play
  self.size=size
  self.dir=''

 def update(self,*args,**kwargs):
  # print(self.angle)
  self.render()
  self.updatesize()
  
 def render(self):
  width,height=self.size
  width=width*self.scale
  height=height*self.scale
  topimage=self.imagestiles[self.pips[1]]
  bottomimage=self.imagestiles[self.pips[0]]
  image=joinimagetile(self.pos,self.size,self.angle,[topimage,bottomimage],self.scale)
  if self.angle==0:
   surface=pygame.Surface((width,height))
   surface.blit(image,(0,0),(0,0,width,height))
  else:
   surface=pygame.Surface((height,width))
   surface.blit(image,(0,0),(0,0,height,width))
  self.image=surface
  self.rect=self.image.get_rect(center=self.pos)

 def checkpips_and_angle(self):
  leftpip,rightpip=self.getpips()
  if leftpip==rightpip:
   self.angle=0
  else:
   self.angle=1

 def walk(self,pos,speed):
  self.updatepos(pos)
  self.pos.move_towards_ip(self.pos,speed)  
 
 def updatepos(self,pos):
  self.pos=pygame.Vector2(pos)
  self.update()

 
 def getpips(self):
  return self.pips
 def updatesize(self):
   
  self.width,self.height=self.rect.size

 def getpos(self):
  return self.pos
 def updateangle(self):
  pips=self.getpips()
  if pips[0]!=pips[1]:
   self.angle=1
  else:
   self.angle=0
 def rotate(self,pips,side):

  tilepips=self.getpips()
  previousepips=tuple(self.getpips())
  if side=='right':
   if pips[1]!=tilepips[0]:
     self.pips=tuple(reversed(self.pips))
     
  elif side=='left':
    if pips[0]!=tilepips[1] :
     self.pips=tuple(reversed(self.pips))
  else:
   pass

 def updatescale(self,scale):
   self.scale=scale