#! /usr/bin/env python
import os, random, sys
import common
sys.path.append(os.path.abspath("../data/"))
import mobs

class mob:
  """
  giant enemy class.

  All the mob generation, IA and movement is implemented here.

  #General attributes
  lv=1        #Mob level
  exp=0       #Experience given to the player
  pres=1      #Prestige given to the player
  name=""     #Name

  #Position variables
  xpos=0
  ypos=0
  zpos=0

  #Primary attributes
  INT=0       #Intelligence
  DEX=0       #Dexterity
  PER=0       #Perception
  WIL=0       #Willpower
  STR=0       #Strenght
  CON=0       #Constitution
  CHA=0       #Charisma

  #Secondary attributes
  HP=0        #Total life
  MP=0        #Total mana
  END=0       #Endurance
  SPD=0       #Speed

  atk=4       #Attack power
  defn=0      #Defense power

  #Status variables
  lock=0      #Locked onto a target for attack 
  hit=0       #Flags when the mob is hit (Does half damage)
  """
  
  def __init__(self,level=0):
    """
    Mob generator

    Receives the level of the mob as an optional argument
    If the level is equal or less than 0, a random level is returned
    The starting coordinates are set outside the construction, after calling.
    """

    # Initialize level and position
    self.level=random.randint(1,mobs.maxlevel) if level<1 or level>mobs.maxlevel else level
    self.xpos=self.ypos=self.zpos=0

    # Load all the mobs at the selected level
    moblist=eval("mobs.level%i.moblist"%self.level)

    # Pick a random mob
    tmob=eval("mobs.level%i.%s"%(self.level, random.choice(moblist)))

    # Iterate over the stored attributes and assign them to self
    for attr, value in tmob.iteritems():
      setattr(self,attr,value)
    self.zpos=tmob["flying"]

    #Secondary attributes
    self.HP=((self.CON+self.STR)*4)+10
    self.MP=(self.INT+self.WIL)
    if self.MP<0: self.MP=0
    self.END=((self.CON+self.STR+self.WIL)*3)+5
    self.SPD=(self.CON+self.DEX)*3
    if self.SPD<1: self.SPD=1

    #Status variables
    self.lock=self.hit=0
  
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
          if dungeon.dungarray[self.ypos-1][self.xpos]==".": self.ypos-=distance
        elif direction==2:
          if dungeon.dungarray[self.ypos][self.xpos-1]==".": self.xpos-=distance  
        elif direction==3:
          if dungeon.dungarray[self.ypos+1][self.xpos]==".": self.ypos+=distance
        elif direction==4:
          if dungeon.dungarray[self.ypos][self.xpos+1]==".": self.xpos+=distance
      except IndexError: pass
  
  def randmove(self,dungeon,dist):
    """
    Moves the mob in a random direction a given number of tiles
    """

    self.move(dungeon,random.randrange(1,5),dist)
   
  def trandmove(self,dungeon):
    """
    Moves 1 tile in a random direction
    """

    self.randmove(dungeon,1)

  def search(self,dungeon,player):
    """
    If the player is within the perception range of the mob, it chases. 
    If not, it moves randomly within the dungeon.
    """

    if abs(self.xpos-player.xpos)<=self.PER and abs(self.ypos-player.ypos)<=self.PER:

      #Choose vertical movement if there is more vertical than horizontal separation
      vert=abs(self.xpos-player.xpos)<abs(self.ypos-player.ypos)
      #Move vertically only if the mob is not in the vertical
      if vert:
        if self.ypos>player.ypos: self.move(dungeon,1,1)
        else: self.move(dungeon,3,1)
      else:
        if self.xpos>player.xpos: self.move(dungeon,2,1)
        else: self.move(dungeon,4,1)

    else: self.trandmove(dungeon)


  def attack(self,player,dung):
    """
    Attacks the player object passed to the function
    """
    
    roll=random.randint(1,10)+self.DEX
    #Check if the player is in range
    if (player.ypos<=self.ypos+1 and player.ypos>=self.ypos-1 and 
        player.xpos<=self.xpos+1 and player.xpos>=self.xpos-1 and 
        roll>3):

      attackpow=((self.STR*self.atk)-player.totdefn)
      if self.hit: attackpow=attackpow/2
      if attackpow<=0: attackpow=1
      player.hp2-=attackpow
      player.totalrcv+=attackpow
      return ("%s attacks %s for %i damage!\n"%(self.name,player.name,attackpow))
    elif roll<=3:
      return ("%s tries to hit you, but it misses\n"%self.name)

if __name__=="__main__": pass