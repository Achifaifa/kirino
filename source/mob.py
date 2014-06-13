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
  
  def __init__(self,dungeon ):
    """
    Mob generator

    Receives a dungeon object and places the mob in a random spot that is not filled with rock.
    """

    with open("../data/mobs/zombie","r") as mobfile:
      for line in mobfile:
        if not line.startswith('#'):
          parA=line.partition(':')[0]
          parB=line.partition('#')[2]
            if parA==Name:      self.name=    parB
          elif parA==marker:    self.marker=  parB
          elif parA==level:     self.lv=      parB
          elif parA==exp:       self.exp=     parB
          elif parA==prestige:  self.pres=    parB
          elif parA==INT:       self.INT=     parB
          elif parA==DEX:       self.DEX=     parB
          elif parA==STR:       self.STR=     parB
          elif parA==PER:       self.PER=     parB
          elif parA==WIL:       self.WIL=     parB
          elif parA==CON:       self.CON=     parB
          elif parA==CHA:       self.CHA=     parB
          elif parA==atk:       self.atk=     parB
          elif parA==def:       self.def=     parB

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

  def attack(self,player,dung):
    """
    Attacks the player object passed to the function
    """
    
    #Check if the player is in range
    if (player.ypos<=self.ypos+1 and player.ypos>=self.ypos-1 and 
        player.xpos<=self.xpos+1 and player.xpos>=self.xpos-1):

      attackpow=((self.str*self.atk)-player.totdefn)
      if self.hit: attackpow=attackpow/2
      if attackpow<=0: attackpow=1
      player.hp2-=attackpow
      return ("Mob attacks "+player.name+" for "+str(attackpow)+" damage!\n")

if __name__=="__main__":
  try: os.chdir(os.path.dirname(__file__))
  except OSError: pass 
  dun=dungeon.dungeon(0,0,0)
  common.version()
  print "Mob module test"
  while 1:
    new=mob(dun)
    print "%s lv%i (%ihp,%imp): %ixp, %ipr"%(new.name,new.lv,new.HP,new.MP,new.exp,new.pres)
