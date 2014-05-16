#usr/bin/env python
import os, random
import dungeon

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
  
  def __init__(self,dungeon):
    """
    Mob generator

    Receives a dungeon object and places the mob in a random spot that is not filled with rock.
    """

    #Initialize attributes
    self.lv=1
    self.str=3
    self.HP=20
    self.atk=4
    self.defn=3
    self.lock=0
    self.exp=1
    self.hit=0
    self.pres=1
    self.name="zombie"

    #Select starting coordinates
    self.xpos=random.randrange(dungeon.xsize)
    self.ypos=random.randrange(dungeon.ysize)
    while dungeon.dungarray[self.ypos][self.xpos]!=".":
      self.xpos=random.randrange(dungeon.xsize)
      self.ypos=random.randrange(dungeon.ysize)
    self.zpos=0

    #Load files
  
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
      except IndexError:
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
    
    #Check if the player is in range
    if (player.ypos<=self.ypos+1 and player.ypos>=self.ypos-1 and 
        player.xpos<=self.xpos+1 and player.xpos>=self.xpos-1):

      attackpow=((self.str*self.atk)-player.totdefn)
      if self.hit:
        attackpow=attackpow/2
      if attackpow<=0:
        attackpow=1
      player.hp2-=attackpow
      return ("Mob attacks "+player.name+" for "+str(attackpow)+" damage!\n")