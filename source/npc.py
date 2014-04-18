#!/usr/bin/env pyton

import os, random

data={}

class npc:
  """
  NPC generator and manager
  """
  #attribute variables
  statmax=0
  statotal=0

  name=""
  secondname=""
  personality=""
  appearance=""
  job=""
  likes1=""
  likes2=""
  dislikes1=""
  dislikes2=""
  
  STR=1 
  DEX=1 
  CON=1 
  INT=1 
  PER=1 
  WIL=1 
  CHA=1  

  def __init__(self,gender,stat,total):
    """
    Constructor. Generates an NPC, as in the standalone NPC generator:
    https://github.com/Achifaifa/GM-Tools/tree/master/npcgenerator

    Needs:

    Gender
      0 female
      1 male
      Anything else defaults at a random genre

    Maximum stat level
      A number smaller than 1 defaults to 5

    Total attribute points
      A number smaller than 1 defaults to 16
    """
    #Sanitize input
    if stat<1:
      stat=5
    if total<1:
      total=16
    if gender!=0 and gender!=1:
      gender=random.choice([0,1])

    self.STR=1 
    self.DEX=1 
    self.CON=1 
    self.INT=1 
    self.PER=1 
    self.WIL=1 
    self.CHA=1 
    
    for i in range(total-6):
      rnd=random.randint(1,7)
      if rnd==1:
        if self.STR<stat: 
          self.STR=self.STR+1
      elif rnd==2:
        if self.DEX<stat:
          self.DEX=self.DEX+1
      elif rnd==3:
        if self.CON<stat:
          self.CON=self.CON+1
      elif rnd==4:
        if self.INT<stat:
          self.INT=self.INT+1
      elif rnd==5:
        if self.PER<stat:
          self.PER=self.PER+1
      elif rnd==6:
        if self.WIL<stat:
          self.WIL=self.WIL+1
      elif rnd==7:
        if self.CHA<stat:
          self.CHA=self.CHA+1

    if gender==0:
      self.name=random.choice(data["namefemale"])
    if gender==1:
      self.name=random.choice(data["namemale"])
    self.secondname=random.choice(data["secondnames"])
    self.personality=random.choice(data["personality"])
    self.appearance=random.choice(data["appearance"])
    self.job=random.choice(data["jobs"])
    self.likes1=random.choice(data["things"])
    self.likes2=random.choice(data["things"])
    self.dislikes1=random.choice(data["things"])
    self.dislikes2=random.choice(data["things"])
      

def sanitize(): 
  """
  Rewrite the NPC data files to follow formatting standards.
  """

  try:
    with open("../data/npcs/firstnames_male","r+") as firstnamesmale:
      lines=firstnamesmale.readlines()
      firstnamesmale.seek(0,0)
      for line in lines:
        firstnamesmale.write(line.title())
       
    with open("../data/npcs/firstnames_female","r+") as firstnamesfemale:
      lines=firstnamesfemale.readlines()
      firstnamesfemale.seek(0,0)
      for line in lines:
        firstnamesfemale.write(line.title())

    with open("../data/npcs/secondnames","r+") as secondnames:
      lines=secondnames.readlines()
      secondnames.seek(0,0)
      for line in lines:
        secondnames.write(line.title())

    #First letter on the first selected thing will be capped later.
    with open("../data/npcs/things","r+") as things:
      lines=things.readlines()
      things.seek(0,0)
      for line in lines:
          things.write(line.lower())
  except IOError:
    raw_input("Error sanitizing NPC data files")

def load(): 
  """
  Load the data from the files into a dictionary. 
  The arrays with the data is stored in a dictionary.
  The dictionary is global in the module and is used by default in the NPC class.
  """
  global data

  try:
    with open("../data/npcs/firstnames_male","r") as file:
      namemale = []
      for line in file:
          namemale.append(line.rstrip('\n'))
    data["namemale"]=namemale
     
    with open("../data/npcs/firstnames_female","r") as file:
      namefemale = []
      for line in file:
          namefemale.append(line.rstrip('\n'))
    data["namefemale"]=namefemale

    with open("../data/npcs/secondnames","r") as file:
      secondnames = []
      for line in file:
          secondnames.append(line.rstrip('\n'))
    data["secondnames"]=secondnames

    with open("../data/npcs/appearance","r") as file:
      appearance = []
      for line in file:
          appearance.append(line.rstrip('\n'))
    data["appearance"]=appearance

    with open("../data/npcs/personality","r") as file:
      personality = []
      for line in file:
          personality.append(line.rstrip('\n'))
    data["personality"]=personality

    with open("../data/npcs/things","r") as file:
      things = []
      for line in file:
        things.append(line.rstrip('\n'))
    data["things"]=things

    with open("../data/npcs/jobs","r") as file:
      jobs = []
      for line in file:
          jobs.append(line.rstrip('\n'))
    data["jobs"]=jobs
  except IOError:
    raw_input("Error loading NPC data files")

sanitize()
load()