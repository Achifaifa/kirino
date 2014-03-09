#usr/bin/env python
import os
import random
import dungeon

class mob:
  """
  giant enemy class.
  All the mob generation, IA and movement is implemented here.
  """
  xpos=0
  ypos=0
  
  def __init__(self,dungeon):
    """
    Mob generator. Receives a dungeon object and places the mob in a random spot that is not filled with rock.
    """
    self.xpos=random.randrange(dungeon.xsize)
    self.ypos=random.randrange(dungeon.ysize)
    while dungeon.dungarray[self.ypos][self.xpos]=="#":
      self.xpos=random.randrange(dungeon.xsize)
      self.ypos=random.randrange(dungeon.ysize)
  
  def move(self,dungeon,direction,distance):
    """
    Move function. Needs a dungeon object.
    Accepts direction and distance
      1 north
      2 west
      3 south
      4 east
    """
    if direction==1:
      if dungeon.dungarray[self.ypos-1][self.xpos]!="#":
        self.ypos -= distance
    if direction==2:
      if dungeon.dungarray[self.ypos][self.xpos-1]!="#":
        self.xpos -= distance  
    if direction==3:
      if dungeon.dungarray[self.ypos+1][self.xpos]!="#":     
        self.ypos += distance
    if direction==4:
      if dungeon.dungarray[self.ypos][self.xpos+1]!="#":
        self.xpos += distance
  
  def randmove(self,dungeon,dist):
    """
    Moves the mob in a random direction a given number of tiles
    """
    rand=0
    rand=random.randrange(4)
    if rand==1:
      self.move(dungeon,1,dist)
    elif rand==2:
      self.move(dungeon,2,dist)
    elif rand==3:
      self.move(dungeon,3,dist)
    elif rand==0:
      self.move(dungeon,4,dist)

  def trandmove(self,dungeon):
    """
    Moves a random number of tiles in a random direction
    """
    rand=0
    rand=random.randrange(2)+1#Will depend on the mob in the future
    self.randmove(dungeon,rand)

# Test stuff
# new=dungeon.dungeon(70,40)
# goblin=mob(new)
# while 1==1:
#   print "Current tile:",new.dungarray[goblin.ypos][goblin.xpos]
#   print "Current position:",(goblin.xpos,goblin.ypos)
#   goblin.move(new,(raw_input("Direction? ")),1)
# Moar test stuff
# step=0
# ite=0
# medi=0
# totstep=0
# #while 1==1:
#   print "Current steps:",step,"Iterations:",ite,"Median:",medi
#   os.system('clear')
#   goblin.trandmove()
#   print goblin.xpos,goblin.ypos
#   step+=1
#   if goblin.xpos==0 and goblin.ypos==0:
#     ite += 1
#     totstep += step
#     medi = totstep/ite
#     step=0
    
# print step