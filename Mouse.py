import pygame
import logging 
log=logging.getLogger('__main__')


class Mouse(pygame.sprite.Group):
 def __init__(self,sprites,pos,arena):
  super().__init__(*sprites)

  self.pos=pygame.Vector2(pos)
  self.tile=None
  
  self.arena=arena

  
 def click(self,gamestate):
  gamestate=self.arena.navbar.click(self.pos) 
   
  playerindex=self.arena.playerindex
  player=self.arena.players[playerindex]
  if player.deck.rect.collidepoint(self.pos):
    self.tile=player.deck.chosetile(self.pos)
    if self.tile:
     side=self.arena.checkside(self.tile)
     self.arena.remove(*[self.arena.transparentcentertile,
                         self.arena.transparentlefttile,
                         self.arena.transparentrighttile])
     self.arena.add_transparent_tiles(self.tile,side)
  elif self.tile is not None and self.arena.rect.collidepoint(self.pos):
   if self.arena.transparentcentertile and self.arena.transparentcentertile.rect.collidepoint(self.pos):
    self.tile.updateangle()
    self.arena.addtile(self.tile,self.arena.transparentcentertile.getpos(),'')
    self.arena.remove(*[self.arena.transparentcentertile,
                        self.arena.transparentlefttile,
                        self.arena.transparentrighttile])
    self.arena.playerindex=1 if playerindex==0 else 0
    self.tile=None
   elif self.arena.transparentlefttile and self.arena.transparentlefttile.rect.collidepoint(self.pos):
    self.tile.updateangle()
    self.arena.addtile(self.tile,self.arena.transparentlefttile.getpos(),'left')
    self.arena.remove(*[self.arena.transparentcentertile,
                        self.arena.transparentlefttile,
                        self.arena.transparentrighttile])
    self.arena.playerindex=1 if playerindex==0 else 0
    self.tile=None
   elif self.arena.transparentrighttile and  self.arena.transparentrighttile.rect.collidepoint(self.pos):
    self.tile.updateangle()
    self.arena.addtile(self.tile,self.arena.transparentrighttile.getpos(),'right')
    self.arena.remove(*[self.arena.transparentcentertile,
                        self.arena.transparentlefttile,
                        self.arena.transparentrighttile])
    self.arena.playerindex=1 if playerindex==0 else 0
    self.tile=None

  return gamestate
 
 def Move(self,pos):
  self.pos=pygame.Vector2(pos)



"""
problem with alianment of position of the tiles need to fix 



"""
