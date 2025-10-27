import pygame
import logging
"""
add button sprites class
so we can add it navbar of game 
 
"""
class Button(pygame.sprite.Sprite):
    def __init__(self, pos,image,size,type):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(size,pygame.SRCALPHA)
        self.image.blit(image,(0,0),(0,0,*size))
        self.pos=pos
        self.image_data=image
        self.size=size
        self.type=type
        self.rect=self.image.get_rect(center=self.pos)
    def update(self):
        self.render()
    
    def render(self):
      self.image=pygame.Surface(self.size,pygame.SRCALPHA)
      self.image.blit(self.image_data,(0,0),(0,0,*self.size))
    
    # def click(self,mousepos):
    #     if self.rect.collidepoint(*mousepos):
    #      return self.type
