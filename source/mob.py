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

    #Add secondary attributes
    self.secondary()

    #Status variables
    self.lock=self.hit=0

  def secondary(self):
    """
    Calculates secondary attributes
    """

    self.HP=((self.CON+self.STR)*4)+10
    self.MP=(self.INT+self.WIL)
    if self.MP<0: self.MP=0
    self.END=((self.CON+self.STR+self.WIL)*3)+5
    self.SPD=(self.CON+self.DEX)*3
    if self.SPD<1: self.SPD=1
  
  def move(self,dungeon,direction=0,distance=1):
    """
    Move function. Needs a dungeon object.

    Accepts direction (OPtional, defaults to random) and distance (Optional, defaults to 1)
      1 north
      2 west
      3 south
      4 east

    If the mob is locked the function does nothing

    #TO-DO: it only checks the initial position. Pending: Check if the path is clear to avoid noclipping
    """

    direction=random.randint(1,4) if not direction else direction
    
    if self.lock: return 1

    try:
      if direction==1:
        if dungeon.dungarray[self.ypos-1][self.xpos]==".":
          self.ypos-=distance
        else: return 1
      elif direction==2:
        if dungeon.dungarray[self.ypos][self.xpos-1]==".":
          self.xpos-=distance  
        else: return 1
      elif direction==3:
        if dungeon.dungarray[self.ypos+1][self.xpos]==".":
          self.ypos+=distance
        else: return 1
      elif direction==4:
        if dungeon.dungarray[self.ypos][self.xpos+1]==".":
          self.xpos+=distance
        else: return 1
      else: return 1
    except IndexError: return -1
    return 0

  def search(self,player):
    """
    Search for the player

    Returns the direction the mob has to move in.

    If the mob can't detect the player, returns 0 (Random direction)
    """

    # The mob detects a player if the total horizontal and vertical difference 
    # is less than 2*perception
    if abs((self.xpos-player.xpos)+(self.ypos-player.ypos))<=2*self.PER:

      # Choose vertical movement if there is more vertical than horizontal separation
      vert=abs(self.xpos-player.xpos)<abs(self.ypos-player.ypos)

      # Choose left/right or up/down depending on the coord difference
      if vert: return 1 if self.ypos>player.ypos else 3 
      else:    return 2 if self.xpos>player.xpos else 4
    else: return 0


  def attack(self,player):
    """
    Attacks the player object passed to the function
    """
    
    if not self.lock: return ""
    roll=random.randint(1,10)+self.DEX
    #Check if the player is in range
    if (player.ypos<=self.ypos+1 and player.ypos>=self.ypos-1 and 
        player.xpos<=self.xpos+1 and player.xpos>=self.xpos-1 and 
        roll>3):

      attackpow=(self.STR*self.atk)-player.totdefn
      attackpow=attackpow/2 if self.hit else attackpow
      if attackpow<=0: attackpow=0
      player.hp2-=attackpow
      player.totalrcv+=attackpow
      return ("%s attacks %s for %i damage!\n"%(self.name,player.name,attackpow))
    elif roll<=3:
      return ("%s tries to hit %s, but it misses\n"%(self.name, player.name))

  def flock(self,player):
    """
    If the player is within range, lock the mob so it attacks in the next turn
    """

    if (self.ypos-1<=player.ypos<=self.ypos+1 and self.xpos-1<=player.xpos<=self.xpos+1):
      self.lock=1

if __name__=="__main__": pass