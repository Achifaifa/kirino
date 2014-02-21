#usr/bin/env python
import os
import random
import dungeon

class mob:
  "Mob class"
  xpos=0
  ypos=0
  
  #Mob generator. It just sets the coordinates to (0,0)
  def __init__(self):
    self.xpos=0
    self.ypos=0
    pass
  
  #Move function. Accepts strings with direction and distance
  def move(self,direction,distance):
    if direction=="north" or direction=="n":
      self.ypos -= distance
    if direction=="west" or direction=="w":
      self.xpos -= distance
    if direction=="south" or direction=="s":
      self.ypos += distance
    if direction=="east" or direction=="e":
      self.xpos += distance
  
  #Moves a given distance in a random direction
  def randmove(self,dist):
    rand=0
    rand=random.randrange(4)
    if rand==1:
      self.move("n",dist)
    elif rand==2:
      self.move("s",dist)
    elif rand==3:
      self.move("e",dist)
    elif rand==0:
      self.move("w",dist)

  #Twitch plays kirino
  def trandmove(self):
    rand=0
    rand=random.randrange(5)#Will depend on the mob in the future
    self.randmove(rand)
  
  #Store the copypastes here
  def copypaste(self):
    pass
    ###
  
    ###
    


#Test stuff
goblin=mob()
print goblin.xpos,goblin.ypos
step=0
while 1==1:
  goblin.trandmove()
  print goblin.xpos,goblin.ypos,step
  step+=1
  if goblin.xpos==0 and goblin.ypos==0:
    break
print step

