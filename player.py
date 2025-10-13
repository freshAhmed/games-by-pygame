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

 def render(self,screen):
  pygame.draw.rect(screen,self.background,self.rect)
  self.draw(screen)

 def addtile(self,tile):
  self.add(tile)
 
 def addtiles(self, tiles):
  offsetx=10
  offsety=self.rect.centery
  for tile in tiles:
   offsetx+=self.margen[0]*12
   tile.updatepos((offsetx,offsety))

  self.add(tiles)
 
 def removetile(self,tile):
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


