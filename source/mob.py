#usr/bin/env python
import os
import random
import dungeon

class mob:
  """
  giant enemy class.
  All the mob generation, IA and movement is implemented here.
  """
  #Position variables
  xpos=0
  ypos=0
  zpos=0

  #Primary attributes
  INT=0
  DEX=0
  PER=0
  WIL=0
  STR=0
  CON=0
  CHA=0

  #Secondary attributes
  HP=0
  MP=0
  END=0
  SPD=0
  defn=0
  lock=0
  
  def __init__(self,dungeon):
    """
    Mob generator. Receives a dungeon object and places the mob in a random spot that is not filled with rock.
    """

    #Initialize attributes
    self.str=3
    self.HP=20
    self.defn=3
    self.lock=0

    #Select starting coordinates
    self.xpos=random.randrange(dungeon.xsize)
    self.ypos=random.randrange(dungeon.ysize)
    while dungeon.dungarray[self.ypos][self.xpos]!=".":
      self.xpos=random.randrange(dungeon.xsize)
      self.ypos=random.randrange(dungeon.ysize)
    self.zpos=0
  
  def move(self,dungeon,direction,distance):
    """
    Move function. Needs a dungeon object.
    Accepts direction and distance
      1 north
      2 west
      3 south
      4 east

    If the mob is locked the function does nothing
    """
    if not self.lock:
      try:
        if direction==1:
          if dungeon.dungarray[self.ypos-1][self.xpos]==".":
            self.ypos -= distance
        if direction==2:
          if dungeon.dungarray[self.ypos][self.xpos-1]==".":
            self.xpos -= distance  
        if direction==3:
          if dungeon.dungarray[self.ypos+1][self.xpos]==".":     
            self.ypos += distance
        if direction==4:
          if dungeon.dungarray[self.ypos][self.xpos+1]==".":
            self.xpos += distance
      except indexError:
        pass
  
  def randmove(self,dungeon,dist):
    """
    Moves the mob in a random direction a given number of tiles
    """
    rand=0
    rand=random.randint(1,4)
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
    Moves 1 tile in a random direction
    """
    self.randmove(dungeon,1)

  def attack(self,player,dung):
    """
    Attacks the player object passed to the function
    """
    if (player.ypos<=self.ypos+1 and player.ypos>=self.ypos-1 and 
        player.xpos<=self.xpos+1 and player.xpos>=self.xpos-1):
      attackpow=(self.str*4)-player.totdefn
      # attackpow=0 # Temporary fix for random damage
      if attackpow<0:
        attackpow=0
      player.hp2-=attackpow