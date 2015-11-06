#! /usr/bin/env pyton

import os, random, sys
import item
sys.path.append(os.path.abspath("../data/"))
from npcs import *
import vendor.vendormsg as msg

class npc:
  """
  NPC generator and manager

  #Characteristic strings
  name=""           #Name
  secondname=""     #Second name
  personality=""    #Personality
  appearance=""     #Appearance
  job=""            #Job
  likes1=""         #Things this NPC likes (1)
  likes2=""         #Things this NPC likes (2)
  dislikes1=""      #Things this NPC dislikes (1)
  dislikes2=""      #Things this NPC dislikes (2)
  
  #Primary attributes
  STR=1             #Strenght
  DEX=1             #Dexterity
  CON=1             #Constitution
  INT=1             #Intelligence
  PER=1             #Perception
  WIL=1             #Willpower
  CHA=1             #Charisma

  #Status variables

  rel=0             #Relation with player 
                    # <-10    - bad
                    # -10,10  - neutral
                    # >10     - good
  """
  
  def __init__(self,gender=0,stat=5,total=16):
    """
    Constructor. Generates an NPC, as in the standalone NPC generator:
    https://github.com/Achifaifa/GM-Tools/tree/master/npcgenerator

    Options:

    Gender
      1 female
      2 male
      Defaults at a random genre

    Maximum stat level
      A number smaller than 1 is corrected to 5
      defaults to 5

    Total attribute points
      A number smaller than 1 is corrected to 16
      defaults to 16

    The NPC will get 1 base point on every attribute even if the 'total' parameter passed is less than 6
    """

    if stat<1: stat=5
    if total<1: total=16
    if gender not in [1,2]: gender=random.choice([1,2])

    # Initialite attributes 
    self.attrs=["STR", "DEX", "CON", "INT", "PER", "WIL", "CHA"]
    for i in self.attrs: setattr(self,i,1)

    self.rel=0
    
    # Assign remaining points.
    for i in range(total-6):
      rnd=random.randint(0,6)
      current=getattr(self,self.attrs[rnd])
      if current<stat: setattr(self,self.attrs[rnd],current+1)

    # Assign other data
    namel=naming.firstnames_f if gender==1 else naming.firstnames_m
    self.name=random.choice(namel)
    self.secondname=random.choice(naming.secondnames)
    self.personality=random.choice(psych.personality)
    self.appearance=random.choice(physical.appearance)
    self.job=random.choice(jobs.jobs)
    t=things.things
    self.likes1=random.choice(t)
    self.likes2=random.choice(t)
    self.dislikes1=random.choice(t)
    self.dislikes2=random.choice(t)

class vendor:
  """
  Vendor class. Creates and manages vendors (shops) in a dungeon floor.
  """

  def __init__(self):
    """
    Vendor constructor. 

    Generates a random NPC (The shopkeeper) and generates items to be sold.
    """

    self.keeper=npc()
    self.forsale=[]
    self.potforsale=[]
    for i in range(random.randrange(4,7)): self.forsale.append(item.item(random.randrange(1,12)))
    for i in range(random.randrange(1,4)): self.potforsale.append(item.consumable(random.choice([0,0,3,1]),0))

  def pricecalc(self,cha):
    """
    Calculates the trading multiplier based on the total charisma and the player-NPC relationship

    Base multiplier: 2

    Additional multipliers: 

    Charisma: +- 0.1 for each point
    Relationship with vendor: +-0.5 for every 10 points
    """

    #Base modifier
    modifier=2

    #Charisma modifiers
    modifier-=(cha-2/10)

    #Relationship modifiers
    modifier-=(self.keeper.rel/15)
    if modifier<0.5: modifier=0.5
    return modifier

if __name__=="__main__": pass