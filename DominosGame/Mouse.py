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
  tile=player.get_tile(self.pos,arena_previouspips)
  player=self.boneyard.press(self.pos,player,arena_previouspips)

  if tile :
    self.tile=tile
  if len(self.boneyard.sprites())==0:

    self.arena.playerindex=0 if self.arena.playerindex==1 else 1


  if self.tile:
     side=self.arena.checkside(self.tile)
     self.arena.add_transparent_tiles(self.tile,side)
  if self.arena.press(self.tile,self.pos):
    self.tile=None
  
   
  return gamestate
 
 def Move(self,pos):
  player= self.arena.players[self.arena.playerindex]
  self.boneyard.display=True if (not player.checkpips(self.arena.getcurrentspips()) and not len(self.boneyard.sprites())==0 )else False 
  self.pos=pygame.Vector2(pos)

