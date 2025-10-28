import pygame
import logging
import os
from button import Button
log=logging.getLogger("__main__")


class Navbar(pygame.sprite.Group):
    def __init__(self, sprites=[],pos=(0,0),size=(0,0),color=(0,0,0),
                 dirname='games-by-pygame/DominosGame/navbar_icons',
                 type_buttons=["settings","restart","exit"]):
        super().__init__(*sprites)

        self._rect_navbar=pygame.Rect(*pos,*size)
        self._icons_navbar=os.listdir(dirname)
        self._icons_navbar=list(filter(lambda x:x!='.DS_Store',self._icons_navbar))
        self.pos=pos
        self._type_buttons=type_buttons
        self._icons_navbar.sort()
        self._dirname=dirname
        self.backgroundcolor=color
        self.add_sprites()

    def render (self,screen):
     pygame.draw.rect(screen,self.backgroundcolor,self._rect_navbar)
     self.draw(screen)
     self.update()

    def add_sprites(self):
     x,y=self._rect_navbar.topleft
     x=50
     y+=15
     type_buttons=self._type_buttons
     for i,icons_path_image in enumerate(self._icons_navbar):
        icon_image=pygame.image.load(os.path.join(self._dirname,icons_path_image))
        button=Button((x,y),icon_image,(25,25),type_buttons[i])
        x+=70
        self.add(button)


    def click(self,mousepos):
       for button in self.sprites():
         if button.rect.collidepoint(mousepos):
            return button.type