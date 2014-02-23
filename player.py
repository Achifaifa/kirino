#usr/bin/env python 
import os
import random

#Player class definition
class player:
  'Player instance'
  #Main characteristics
  Name="subject name here"; #Name
  pocket=0; #Money
  

  #Attribute variables 
  INT=1
  DEX=1
  PER=1
  WIL=1
  STR=1
  CON=1

  #Status variables
  HP=0
  MP=0
  END=0
  SPD=0
  
  #Position
  xPos=0
  yPos=0
  zPos=0
  
  #Temp status check 
  poison=0
  fire=0
  frozen=0
  

  #Initialization  
  def __init__(self):
    for i in range(8):
	rnd=random.randint(1,6)
	if rnd==1:
	  if self.STR<5:
	    self.STR=self.STR+1
	elif rnd==2:
	  if self.DEX<5:
	    self.DEX=self.DEX+1
	elif rnd==3:
	  if self.CON<5:
	    self.CON=self.CON+1
	elif rnd==4:
	  if self.INT<5:
	    self.INT=self.INT+1
	elif rnd==5:
	  if self.PER<5:
	    self.PER=self.PER+1
	elif rnd==6:
	  if self.WIL<5:
	    self.WIL=self.WIL+1
    self.HP=((self.CON+self.STR)*4)+10
    self.MP=(self.STR+self.DEX+self.INT+self.CON+self.WIL+self.PER)
    self.END=((self.CON+self.STR+self.WIL)*3)+5
    self.SPD=(self.CON+self.DEX)*3

  #Test function. Prints attributes.
  def getatr(self):
    print 'INT:', self.INT, 'DEX:', self.DEX, 'CON:', self.CON, 'WIL:', self.WIL, 'STR:', self.STR, 'PER:', self.PER;
    print 'HP:', self.HP, 'MP:', self.MP, 'END:', self.END, 'SPD:', self.SPD
    
  #Hit function. This damages the player.
  #For healing, just hit with negative damage
  def hit(self,damage):
    self.HP=(self.HP)-(damage);
    
  #Attack function. This damages other stuff. Returns the raw damage value
  def attack(self):
    return self.STR
    
 
pass
