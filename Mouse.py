import pygame
import logging 
log=logging.getLogger('__main__')


class Mouse(pygame.sprite.Group):
 def __init__(self,sprites,pos,arena):
  super().__init__(*sprites)
  self.pos=pygame.Vector2(pos)
  self.tile=None
  self.arena=arena

 def click(self,gamestate,pos):

  gamestate=self.arena.navbar.click(self.pos) 
  playerindex=self.arena.playerindex
  player=self.arena.players[playerindex]
  if player.deck.rect.collidepoint(self.pos):
    self.tile=player.deck.chosetile(self.pos)
  if self.tile:
     side=self.arena.checkside(self.tile)
     self.arena.add_transparent_tiles(self.tile,side)
  if self.arena.press(self.tile,self.pos):
    self.tile=None
  
   
  return gamestate
 
 def Move(self,pos):
  self.pos=pygame.Vector2(pos)

