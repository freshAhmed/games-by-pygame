import pygame
from linkedlist import LinkedList
import logging
from navbar import Navbar
log=logging


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
   tile.rotate(self.getcurrentspips(),side)
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
    if currentpips[0]!=newpips[1]:
     self.currentpips={'leftpip':newpips[1],'rightpip':currentpips[1]}
    else:
     self.currentpips={'leftpip':newpips[0],'rightpip':currentpips[1]}
   elif side == 'right':
    if currentpips[1]!=newpips[0]:
     self.currentpips={'leftpip':currentpips[0],'rightpip':newpips[0]}
    else:
     self.currentpips={'leftpip':currentpips[0],'rightpip':newpips[1]}
   else:
    self.currentpips={'leftpip':newpips[0],'rightpip':newpips[1]}
 

 def add_transparent_tiles(self,newtile,side):
  left_tile=self.linkedlist.get_lefttile_far_left().get_tile()
  right_tile=self.linkedlist.get_righttile_far_right().get_tile()
  new_tile_pips=newtile.getpips()
  transparentbackgroundcolor=(0,205,0)
  opacity=0
  angle=0 if new_tile_pips[0]==new_tile_pips[1] else 1
 
  size=tuple(reversed(newtile.size)) if angle>0 else newtile.size
  margen=2
  self.remove(*[self.transparentcentertile,self.transparentlefttile,self.transparentrighttile])
  if side is None:
   return None
  if side == "": # will add transparent tile to the center of the arena 
   self.transparentcentertile=Transparenttile((self.rect.centerx,self.rect.centery),size,transparentbackgroundcolor,opacity,newtile.scale)
   self.add(self.transparentcentertile) 
  
  elif side=="bothside" : # will add transparent tile on the left side and the right side 
    left_tile_pos=pygame.Vector2(left_tile.getpos())
    right_tile_pos=pygame.Vector2(right_tile.getpos())
    left_tile_pos[0]= left_tile.rect.left-size[0]//2-margen 
    right_tile_pos[0]=right_tile.rect.right+size[0]//2+margen 
    self.transparentlefttile=Transparenttile(left_tile_pos,size,transparentbackgroundcolor,opacity,newtile.scale)
    self.transparentrighttile=Transparenttile(right_tile_pos,size,transparentbackgroundcolor,opacity,newtile.scale)
    self.add(*[self.transparentlefttile,self.transparentrighttile])
  elif side=="leftside": # will add transparent tile on left side
    left_tile_pos=pygame.Vector2(left_tile.getpos())
    left_tile_pos[0]=left_tile.rect.left-size[0]//2-margen 
    self.transparentlefttile=Transparenttile(left_tile_pos,size,transparentbackgroundcolor,opacity,newtile.scale)
    self.add(self.transparentlefttile) 
  elif side=="rightside": # will add. transparent tile on right side
    right_tile_pos=pygame.Vector2(right_tile.getpos())
    right_tile_pos[0]=right_tile.rect.right+size[0]//2+margen 
    self.transparentrighttile=Transparenttile(right_tile_pos,size,transparentbackgroundcolor,opacity,newtile.scale)
    self.add(self.transparentrighttile)
 
  
 def checkside(self,tile):
  currentpips=self.getcurrentspips()
  tilepips=tile.getpips()
  if currentpips[0] is None:
   return ""
  if  ((currentpips[0]==tilepips[0] or currentpips[0]==tilepips[1]) and (currentpips[1]==tilepips[0] or currentpips[1]==tilepips[1])):
   return 'bothside'
  elif (currentpips[0]==tilepips[0] or currentpips[0]==tilepips[1]):
   return 'leftside'
  elif (currentpips[1]==tilepips[0] or currentpips[1]==tilepips[1]):
   return 'rightside'
 
 def getcurrentspips(self):

  return self.currentpips['leftpip'],self.currentpips['rightpip']
 
 def press(self,tile,pos):
  #  log.info(tile)
   if tile is not None :
    if self.transparentcentertile and self.transparentcentertile.press(pos):
     pos=self.transparentcentertile.getpos()
     self.remove(self.transparentcentertile)
     self.transparentcentertile=None
     tile.updateangle()
     side='center'
     self.addtile(tile,pos,side)
     player=self.players[self.playerindex]
     player.deck.removetile(tile)
     self.playerindex=0 if self.playerindex==1 else 1
     return True
    elif self.transparentlefttile and self.transparentlefttile.press(pos):     
     pos=self.transparentlefttile.getpos() 
     side='left'   
     self.remove(*[self.transparentlefttile,self.transparentrighttile])
     self.transparentlefttile=None
     tile.updateangle()
     self.addtile(tile,pos,side)
     player=self.players[self.playerindex]
     player.deck.removetile(tile)

     self.playerindex=0 if self.playerindex==1 else 1
     return True
    elif self.transparentrighttile and self.transparentrighttile.press(pos):
     pos=self.transparentrighttile.getpos()
     self.remove(*[self.transparentlefttile,self.transparentrighttile])
     side='right'
     self.transparentrighttile=None
     tile.updateangle()

     self.addtile(tile,pos,side)
     player=self.players[self.playerindex]
     player.deck.removetile(tile)
     self.playerindex=0 if self.playerindex==1 else 1
     return True
    
    return False
 

class Transparenttile(pygame.sprite.Sprite):
 def __init__(self, pos, size,backgroundcolor,opacity,scale):
  pygame.sprite.Sprite.__init__(self)
  self.size=size
  self.pos=pos
  self.scale=scale
  self.backgroundcolor=backgroundcolor+(opacity,)
  self.image=pygame.Surface(size)
  self.rect=self.image.get_rect(center=self.pos) 
  
 def update(self,*args,**kwargs):
  self.render()
 def render(self):
  pass
  surface=pygame.Surface(self.image.get_rect().size)
  # surface.convert_alpha()
  surface.fill(self.backgroundcolor)
  self.image.blit(surface,(0,0,*self.size))
 
  self.image.fill(self.backgroundcolor)

  # self.rect=self.image.get_rect(center=self.pos)

 def updatepos(self,pos):
  self.pos=pygame.Vector2(pos)
 def getpos(self):
  return self.pos 
 def getrect(self):
  return self.rect

 def press(self,pos):

  return  self.rect.collidepoint(pos) 