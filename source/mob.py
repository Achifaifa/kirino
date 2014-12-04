#! /usr/bin/env python
import os, random
import common, dungeon

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
  
  def __init__(self,dungeon,level):
    """
    Mob generator

    Receives a dungeon object and places the mob in a random spot that is not filled with rock.

    Needs the dungeon and the level. If the level is equal or less than 0 a random level is selected.
    """

    #Load list of mobs in the dictionary
    #Each dictionary contains the level as a key and an array of mobs at that level as value.
    mobs=[]
    with open("../data/mobs/_list","r") as moblist:
      if level>0:
        for line in moblist:
          if not line.startswith("#"):
            if line.partition(':')[0].strip()==str(level):
              mobs.append(line.partition(':')[2].strip())
      else:
        for line in moblist:
          if not line.startswith("#"):
            mobs.append(line.partition(':')[2].strip())

    path="../data/mobs/"+random.choice(mobs)
    self.zpos=0

    with open(path,"r") as mobfile:
      for line in mobfile:
        if not line.startswith('#'):
          parA=line.partition(':')[0]
          parB=line.partition(':')[2].strip()
          if   parA=="Name":      self.name=    parB
          elif parA=="marker":    self.marker=  parB
          elif parA=="level":     self.lv=      int(parB)
          elif parA=="exp":       self.exp=     int(parB)
          elif parA=="prestige":  self.pres=    int(parB)
          elif parA=="INT":       self.INT=     int(parB)
          elif parA=="DEX":       self.DEX=     int(parB)
          elif parA=="STR":       self.STR=     int(parB)
          elif parA=="PER":       self.PER=     int(parB)
          elif parA=="WIL":       self.WIL=     int(parB)
          elif parA=="CON":       self.CON=     int(parB)
          elif parA=="CHA":       self.CHA=     int(parB)
          elif parA=="atk":       self.atk=     int(parB)
          elif parA=="defn":      self.defn=    int(parB)
          elif parA=="flying" and parB=="1": self.zpos=1

    #Secondary attributes
    self.HP=((self.CON+self.STR)*4)+10
    self.MP=(self.INT+self.WIL)
    if self.MP<0: self.MP=0
    self.END=((self.CON+self.STR+self.WIL)*3)+5
    self.SPD=(self.CON+self.DEX)*3
    if self.SPD<1: self.SPD=1

    #Status variables
    self.lock=self.hit=0

    #Select starting coordinates
    self.xpos=random.randrange(dungeon.xsize)
    self.ypos=random.randrange(dungeon.ysize)
    while dungeon.dungarray[self.ypos][self.xpos]!=".":
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

if __name__=="__main__":
  try: os.chdir(os.path.dirname(__file__))
  except OSError: pass 
  dun=dungeon.dungeon(0,0,0)
  common.version()
  print "Mob module test"
  while 1:
    new=mob(dun,-1)
    print "%s lv%i (%ihp,%imp): %ixp, %ipr"%(new.name,new.lv,new.HP,new.MP,new.exp,new.pres)
    common.getch()
