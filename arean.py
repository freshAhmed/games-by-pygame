import pygame
from linkedlist import LinkedList
import logging
from navbar import Navbar
log=logging.getLogger('__main__')


class Arena(pygame.sprite.Group):
 def __init__(self, sprites=[],pos=(0,0),size=(0,0),background=(0,0,0,1),players=[],margen=10):
  
  super().__init__(*sprites)
  self.size=size
  self.background=background
  self.pos=pygame.Vector2(pos)
  self.image=pygame.Surface(self.size,pygame.SRCALPHA)
  self.rect=self.image.get_rect(center=self.pos)
  self.playerindex=0
  self.margen=margen
  self.players=players
  self.navbar=Navbar([],(0,0),(size[0],25),(0,250,0))
  self.currentpips={'leftpip':None,'rightpip':None}
 
  self.transparentlefttile=None
  self.transparentrighttile=None
  self.transparentcentertile=None

  self.linkedlist=LinkedList(None) 

 def addtile(self,tile,pos,side):
  margen=self.margen
  headtile=self.linkedlist.head_tile.get_tile()
  if headtile is None:
   tile.rotate(self.getcurrentspips(),'')
   self.linkedlist.insert_head_tile(tile)
   self.updatepips(tile.getpips(),None)
  else:
   if side=='left':
    self.linkedlist.insert_left_tile(tile)
    tile.rotate(self.getcurrentspips(),side)
   elif side=='right': 
    self.linkedlist.insert_right_tile(tile)
    tile.rotate(self.getcurrentspips(),side)
  self.updatepips(tile.getpips(),side)  
  tile.updatepos(pos)
  self.add(tile)
 
 
 
 
 def render(self, screen):
  pygame.draw.rect(screen,self.background,self.rect)
  self.draw(screen)
  self.navbar.render(screen)
  self.update()


 def updatepips(self,newpips,side):
   currentpips=self.getcurrentspips()

   if side =='left':
    if newpips[1]!=currentpips[0]:
     newpips=tuple(reversed(newpips))
    self.currentpips={'leftpip':newpips[0],'rightpip':currentpips[1]}
   elif side == 'right':
    if  newpips[0]!=currentpips[1]:
      newpips=tuple(reversed(newpips))
    self.currentpips={'leftpip':currentpips[0],'rightpip':newpips[1]}

   else:
  
    self.currentpips={'leftpip':newpips[0],'rightpip':newpips[1]}

  


 def add_transparent_tiles(self, tile,side):

  margen=10
  tilepips=tile.getpips()
  lefttile=self.linkedlist.get_lefttile_far_left().get_tile()
  righttile=self.linkedlist.get_righttile_far_right().get_tile()
  transparentbackgroundcolor=(0,205,0)
  opacity=1
  angle=0 if tilepips[0]==tilepips[1] else 1
  size=tile.size

  if angle>0:
   margen=5
   size=tuple(reversed(size))
  #  log.info(size)

  if side is None:
   return None
  if side=='':

   self.transparentcentertile=Transparenttile(self.rect.center,size,transparentbackgroundcolor,opacity)
   self.add(self.transparentcentertile) 
  elif side=='leftright':
    leftpos=pygame.Vector2(lefttile.getpos())
    rightpos=pygame.Vector2(righttile.getpos())
    leftpos[0]=leftpos[0]-size[0]*1.45-margen if angle==0 else leftpos[0]-size[0]-margen
    rightpos[0]=rightpos[0]+size[0]*1.45+margen if angle==0 else rightpos[0]+size[0]+margen
    self.transparentlefttile=Transparenttile(leftpos,size,transparentbackgroundcolor,opacity)
    self.transparentrighttile=Transparenttile(rightpos,size,transparentbackgroundcolor,opacity)
    self.add(*[self.transparentlefttile,self.transparentrighttile])
  elif side=='left':
   
   leftpos=pygame.Vector2(lefttile.getpos())
   leftpos[0]=leftpos[0]-size[0]*1.45-margen if angle == 0 else leftpos[0]-size[0]-margen
   self.transparentlefttile=Transparenttile(leftpos,size,transparentbackgroundcolor,opacity)
   self.add(self.transparentlefttile) 

  elif side=='right':

   rightpos=pygame.Vector2(righttile.getpos())
   
   if righttile.angle==0:
    rightpos[0]=rightpos[0]+size[0]*0+margen 
  #  else:
  #   rightpos[0]=rightpos[0]+size[0]*1.5+margen if angle == 0 else rightpos[0]+size[0]+margen
   self.transparentrighttile=Transparenttile(rightpos,size,transparentbackgroundcolor,opacity)
   self.add(self.transparentrighttile)
  
 def checkside(self,tile):
  currentpips=self.getcurrentspips()
  tilepips=tile.getpips()

  if currentpips[0] is None:
   return ''
  else:
   if (currentpips[0]==tilepips[1] or currentpips[0]==tilepips[0])                                                                     and(currentpips[1]==tilepips[1] or currentpips[1]==tilepips[0]):
    return 'leftright'
   if currentpips[0]==tilepips[1] or currentpips[0]==tilepips[0] :
   #left
    return 'left'
 
   if currentpips[1]==tilepips[1] or currentpips[1]==tilepips[0]:
    #right
    return 'right'
  return None 

 def getcurrentspips(self):

  return self.currentpips['leftpip'],self.currentpips['rightpip']
 
class Transparenttile(pygame.sprite.Sprite):
 def __init__(self, pos, size,backgroundcolor,opacity):
  pygame.sprite.Sprite.__init__(self)
  self.size=size

  self.pos=pos
  self.backgroundcolor=backgroundcolor+(opacity,)

  self.image=pygame.Surface(size)

  self.rect=self.image.get_rect(center=self.pos) 
  
 def update(self,*args,**kwargs):
  self.render()

 def render(self):

  self.image.convert_alpha()
  self.image.fill(self.backgroundcolor)

  self.rect=self.image.get_rect(center=self.pos)

 def updatepos(self,pos):
  self.pos=pygame.Vector2(pos)
 def getpos(self):
  return self.pos 
 def getrect(self):
  return self.rect

  