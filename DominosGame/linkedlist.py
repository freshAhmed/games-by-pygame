class Node ():
 def __init__(self,currenttile,nexttile=None,previoustile=None):
  self.Next_tile=nexttile
  self.Previous_tile=previoustile
  self.current_tile=currenttile
 def get_tile(self):
  return self.current_tile
 def get_next_tile(self):
  return self.Next_tile
 def get_previous_tile(self):
  return self.Previous_tile
 def set_next_tile(self,tile):
  self.Next_tile=tile
 def set_previous_tile(self,tile):
  self.Previous_tile=tile


class LinkedList():
 def __init__(self,headtile=None):
  self.head_tile=Node(headtile)

 def insert_head_tile(self,newtile):
  newnode=Node(newtile)
  if self.head_tile.get_tile() is None:
   self.head_tile=newnode
  

 def insert_left_tile(self,newtile):
  newnode=Node(newtile)
  previous_tile=self.get_lefttile_far_left()
  newnode.set_next_tile(previous_tile)
  previous_tile.set_previous_tile(newnode)

 def insert_right_tile(self,newtile):
  newnode=Node(newtile)
  next_tile=self.get_righttile_far_right()
  newnode.set_previous_tile(next_tile)
  next_tile.set_next_tile(newnode)  


 def get_lefttile_far_left(self):
  previous_tile=self.head_tile.get_previous_tile()
  if previous_tile is None:
   return self.head_tile
  while previous_tile.get_previous_tile() is not None:
   previous_tile=previous_tile.get_previous_tile()
  return previous_tile  


 def get_righttile_far_right(self):
  next_tile=self.head_tile.get_next_tile()
  if next_tile is None:
   return self.head_tile
  while next_tile.get_next_tile() is not None:
   next_tile=next_tile.get_next_tile()
  return next_tile 
 