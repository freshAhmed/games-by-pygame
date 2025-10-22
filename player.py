import pygame
import logging 
log=logging.getLogger('__main__')
class Deck(pygame.sprite.Group):
 def __init__(self, sprites=[],pos=(0,0),size=(0,0),margen=(16,16),background=(0,0,0,1)):
  super().__init__(*sprites)
  self.pos=pygame.Vector2(pos)
  self.size=size
  self.margen=margen
  self.background=background
  self.image=pygame.Surface(size,pygame.SRCALPHA)
  self.rect=self.image.get_rect(center=self.pos)
  self.scale=0.8
  self.dectpips=[]
 def render(self,screen):
  # pygame.draw.rect(screen,self.background,self.rect)
  self.draw(screen)

 def addtile(self,tile):
  # self.add(tile)
  tiles=self.sprites()
  xoffset,yoffset=tiles[-1:][0].pos
  tile.updatepos((xoffset+tile.size[0],yoffset))


  tile.updatescale(self.scale) 
  self.add(tile)
 
 def addtiles(self, tiles):
  offsetx=self.rect.centerx//1.8
  offsety=self.rect.centery
  for tile in tiles:
   offsetx+=self.margen[0]*5
   self.dectpips.append(tile.getpips())
   tile.updatepos((offsetx,offsety))
   tile.updatescale(self.scale) 

  self.add(tiles)
 
 def removetile(self,tile):
  tilepips=tile.getpips() if tile.getpips() in self.dectpips else tuple(reversed(tile.getpips()))
  for pip in self.dectpips:
   if (pip[0]==tilepips[0] and pip[1]==tilepips[1] ) or (pip[0]==tilepips[1] and pip[1]==tilepips[0]):
    self.dectpips.remove(pip)
  self.remove(tile)
 
 def chosetile(self,pos):
  tiles=self.sprites()
  for tile in tiles :
   if tile.rect.collidepoint(pos):
    return tile
  return None




class Player():

 def __init__(self,pos=(0,0),size=(0,0),margen=(16,16),background=(0,0,0,1),tiles=[]):
  self.pos=pygame.Vector2(pos)
  self.size=size
  self.background=background
  self.margen=margen
  self.deck=Deck(tiles,self.pos,self.size,self.margen,self.background)
  self.deck.addtiles(tiles)

 def render(self,screen,*args,**kwargs):
  self.deck.update(*args,**kwargs)
  self.deck.render(screen)

 def checkpips(self,currentpips):
  if currentpips[0]==None:
   return True 
  for pip in self.deck.dectpips:
    if (pip[0]==currentpips[0] or pip[1]==currentpips[0] )or (pip[0]==currentpips[1] or pip[1]==currentpips[1] ):
     return True
  return False 

