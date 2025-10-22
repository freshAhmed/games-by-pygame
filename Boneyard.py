import pygame
import logging 
log =logging.getLogger('__main__')


class Boneyard(pygame.sprite.Group):
    def __init__(self, sprites=[],pos=(220,220),size=(0,0),scale=1,background=(0,0,0,1),display=False,margen=(16,16)):
        super().__init__(*sprites)

        self.pos=pos
        self.size=size
        self.scale=scale
        self.background=background
        self.image=pygame.Surface(self.size)
    
        self.margen=margen
        self.display=True
        self.rect=self.image.get_rect(center=self.pos) 
        self.addtiles(sprites)
    def addtiles(self,tiles):
      xoffset=self.rect.left
      yoffset=self.rect.top+55
      for tile in tiles:
        xoffset+=(tile.size[0])
        if xoffset >self.rect.right-tile.size[0]:
          xoffset=self.rect.left+(tile.size[0])
          yoffset+=tile.size[1]
        tile. updatescale(self.scale)
        tile.updatepos((xoffset,yoffset))
        self.add(tile)

    def render(self,screen,*args,**kwargs):
    #  if self.display:
      self.image=pygame.Surface(self.size,pygame.SRCALPHA)
      self.image.fill(self.background)
      screen.blit(self.image,(self.rect.left,self.rect.top,*self.size))
      self.update(*args,**kwargs)
      self.draw(screen)
    
    def updatepos(self,pos):
        self.pos=pygame.Vector2(pos)
   
    def updatesize(self,size):
        self.size=size
   
    def walk_by(self,pos,speed):
      self.updatepos(pos)
      self.pos.move_towards_ip(speed)
   
    def chosetile(self,pos):
     tiles=self.sprites()
     for tile in tiles:
        if tile.rect.collidepoint(pos):
           return tile
     return None
    
    def removetile(self,tile):
       self.remove(tile)
   
