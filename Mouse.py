import pygame
import logging 
log=logging.getLogger('__main__')


class Mouse(pygame.sprite.Group):
 def __init__(self,sprites,pos,arena,boneyard):
  super().__init__(*sprites)          
  self.pos=pygame.Vector2(pos)
  self.tile=None
  self.arena=arena
  self.boneyard=boneyard
 def click(self,gamestate,pos):

  gamestate=self.arena.navbar.click(self.pos) 
  playerindex=self.arena.playerindex
  player=self.arena.players[playerindex]
  arena_previouspips=self.arena.getcurrentspips()
  if player.deck.rect.collidepoint(self.pos):
    if player.checkpips(arena_previouspips):
     self.tile=player.deck.chosetile(self.pos)
  if self.boneyard.display and self.boneyard.rect.collidepoint(self.pos):
      tile=self.boneyard.chosetile(self.pos)
      if tile is not None:
       self.boneyard.removetile(tile)
       player.deck.addtile(tile)
       tilepips=tile.getpips()
       if (tilepips[0]==arena_previouspips[0] or tilepips[0]==arena_previouspips[1]) or (tilepips[1]==arena_previouspips[0] or tilepips[1]==arena_previouspips[1]):
        #  self.boneyard.display=False
        pass

  if self.tile:
     side=self.arena.checkside(self.tile)
     self.arena.add_transparent_tiles(self.tile,side)
  if self.arena.press(self.tile,self.pos):
    self.tile=None
  
   
  return gamestate
 
 def Move(self,pos):
  player= self.arena.players[self.arena.playerindex]
  # self.boneyard.display=True if not player.checkpips(self.arena.getcurrentspips()) else False 
  self.pos=pygame.Vector2(pos)

