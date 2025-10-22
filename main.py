import pygame
from Mouse import Mouse
import os
from tile import Tile
from arean import Arena
import random
from player import Player
import logging
import json
from Boneyard import Boneyard
def gettiles(dirname='./tiles_images',numbertiles=7,width=70,hieght=145):
 pathimagetiles=os.listdir(dirname)
 log=logging.getLogger('__main__')

 pathimagetiles=sorted(pathimagetiles)
 ntiles=0
 l=[]
 imagestiles={}
 for path in pathimagetiles:
  topimage=pygame.image.load(os.path.join(dirname,path))
  for i in range(ntiles,numbertiles):
   imagestiles[i]=topimage  
   l.append(Tile((0,0),imagestiles,(width,hieght),[ntiles,i]))
  ntiles+=1
 random.shuffle(l)
 return l
def loadData(filename):
 try: 
  with open(filename) as file:
   data= json.load(file)
   return data
 except FileNotFoundError:
  print(f"Error: the file '{filename}' was not found")
 except json.JSONDecodeError:
  pass
def render(screen,itemsGame):
  for i in itemsGame:
   i.render(screen)

def checkStateGame(itemsgame=[],gameData={}):
#  log=logging.getLogger('')
#  log.info(gameData.get('gameState'))
 if gameData.get('gameState')=='restart':
    
  tiles=gettiles(gameData.get('dir_tiles_images'),
                gameData.get('number_tiles'),
                gameData.get('imageWidth'),
                gameData.get('imageHieght'))
  itemsgame['Player0']=Player(tuple(gameData.get('Player0')['pos']),
                tuple(gameData.get('Player0')['size']),
                tuple(gameData.get('Player0')['margen']),
                tuple(gameData.get('Player0')['Background']),
                tiles[:7])
  itemsgame['Player1']=Player(tuple(gameData.get('Player1')['pos']),
                tuple(gameData.get('Player1')['size']),
                tuple(gameData.get('Player0')['margen']),
                tuple(gameData.get('Player0')['Background']),
                tiles[7:14])
  itemsgame['arena']=Arena([],tuple(gameData.get('Arena')['pos']),
                tuple(gameData.get('Arena')['size']),
                tuple(gameData.get('Arena')['Background']),
                [itemsgame['Player0'],itemsgame['Player1']])
  itemsgame['boneyard']=Boneyard(tiles[14:],
                   gameData.get('boneyard')['pos'],
                   gameData.get('boneyard')['size'],
                   gameData.get('boneyard')['scale'],
                   gameData.get('boneyard')['Background'],
                   gameData.get('boneyard')['display'])
  itemsgame['mouse']=Mouse([],(0,0),itemsgame['arena'],itemsgame['boneyard'])
  
  gameData['gameState']=''
 elif gameData.get('gameState')=='exit':
     pygame.quit()
     gameData['Game_Loop_state']=False
 elif gameData.get('gameState')=='settings':
  pass 
   
 return itemsgame



def main():
 #settings
 data=dict(loadData('settings.json'))['Main'] 
 
 logging.basicConfig(format=data.get("loggingFormat"), level=logging.DEBUG)
 log=logging.getLogger('__main__')
 width=data.get('Width')
 height=data.get('height')
 background=data.get('Background')
 running=data.get('Game_Loop_state')
 pygame.init()
 gamestate=data.get('gameState')
 screen=pygame.display.set_mode((width,height))
 clock=pygame.time.Clock()
 tiles=gettiles(data.get('dir_tiles_images'),
                data.get('number_tiles'),
                data.get('imageWidth'),
                data.get('imageHieght'))
 Player0=Player(tuple(data.get('Player0')['pos']),
                tuple(data.get('Player0')['size']),
                tuple(data.get('Player0')['margen']),
                tuple(data.get('Player0')['Background']),
                tiles[:7])
 Player1=Player(tuple(data.get('Player1')['pos']),
                tuple(data.get('Player1')['size']),
                tuple(data.get('Player0')['margen']),
                tuple(data.get('Player0')['Background']),
                tiles[7:14])

 boneyard=Boneyard(tiles[14:],
                   data.get('boneyard')['pos'],
                   data.get('boneyard')['size'],
                   data.get('boneyard')['scale'],
                   data.get('boneyard')['Background'],
                   data.get('boneyard')['display'])
 
 arena=Arena([],tuple(data.get('Arena')['pos']),
                tuple(data.get('Arena')['size']),
                tuple(data.get('Arena')['Background']),
                [Player0,Player1])
 mouse=Mouse([],(0,0),arena,boneyard)


 while running:
  running=data['Game_Loop_state']
  for event in  pygame.event.get():
   if event.type==pygame.QUIT:
     pygame.quit()
     data['Game_Loop_state']=False
   if event.type==pygame.MOUSEBUTTONDOWN:
    data['gameState']= mouse.click(gamestate,event.pos)
   if event.type==pygame.MOUSEMOTION:
     
     mouse.Move(event.pos)
   elif event.type==pygame.MOUSEBUTTONUP:
    mouse.flagDragDrop=False
   list_item=checkStateGame({
   'Player0':Player0,
   'Player1':Player1,
   'arena':arena,
   'mouse':mouse,
   "boneyard":boneyard
  },data) 
   Player0=list_item["Player0"]
   Player1=list_item["Player1"]
   arena=list_item["arena"]
   mouse=list_item['mouse']
   boneyard=list_item["boneyard"]
  render(screen,[arena,boneyard,Player0,
                 Player1,
                 ])

  pygame.display.flip()
  clock.tick(60)
if __name__=='__main__':
  
  main()





