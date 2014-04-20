#!/usr/bin/env pyton

import copy, os, random
import item
import common, parser

npcdata={}
vendordata={}

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
      self.name=random.choice(npcdata["namefemale"])
    if gender==1:
      self.name=random.choice(npcdata["namemale"])
    self.secondname=random.choice(npcdata["secondnames"])
    self.personality=random.choice(npcdata["personality"])
    self.appearance=random.choice(npcdata["appearance"])
    self.job=random.choice(npcdata["jobs"])
    self.likes1=random.choice(npcdata["things"])
    self.likes2=random.choice(npcdata["things"])
    self.dislikes1=random.choice(npcdata["things"])
    self.dislikes2=random.choice(npcdata["things"])

class vendor:
  """
  Vendor class. Creates and manages vendors and peddlers. 
  """

  def __init__(self):
    """
    Vendor constructor. Generates a random NPC (The shopkeeper) and generates items to be sold.
    """
    self.keeper=npc(0,0,0)
    self.forsale=[]
    for i in range(random.randrange(4,7)):
      self.forsale.append(item.item(random.randrange(1,11)))

  def commerce(self,player):
    while 1:
      os.system('clear')
      common.version()
      print "Shop"
      print ""
      print random.choice(vendordata["welcomemsg"])
      print ""
      print "1.- Sell"
      print "2.- Buy"
      print "3.- Chat"
      print "--"
      print "0.- Back"
      print ""
      print "->",
      commenu=common.getch()

      if commenu=="1":
        self.sell(player)
      if commenu=="2":
        self.buy(player)
      if commenu=="3":
        parser.chat(self.keeper,player)
      if commenu=="0":
        print random.choice(vendordata["byemsg"])
        common.getch()
        break
      else:
        pass

  def buy(self,player):
    """
    Display the list of items available for buying from the vendor
    """
    while 1:
      os.system('clear')
      common.version()
      print "Shop - Buy items ("+str(player.pocket)+"G)"
      print ""
      for i in range(len(self.forsale)):
        print str(i+1)+".- "+self.forsale[i].name+" ("+str(2*self.forsale[i].price)+"G)"
      print "--"
      print "0.- Back"
      print ""
      print "->",

      try:
        try:
          buymenuc=common.getch()
          if buymenuc=="0":
            print "Nice doing business with you!"
            common.getch()
            break
          if player.pocket>=self.forsale[int(buymenuc)-1].price*2:
            player.pocket-=(2*self.forsale[int(buymenuc)-1].price)
            if player.pickobject(self.forsale[int(buymenuc)-1]):
              print random.choice(vendordata["okmsg"])
              del self.forsale[int(buymenuc)-1]
              common.getch()
            else:
              print random.choice(vendordata["failmsg"])
              common.getch()
          else:
            print random.choice(vendordata["failmsg"])
            common.getch()
        except ValueError:
          pass
      except IndexError:
        pass

  def sell(self,player):
    """
    Display the list of items in the inventory to sell
    """
    while 1:
      os.system('clear')
      common.version()
      print "Shop - Sell items ("+str(player.pocket)+"G)"
      print ""
      for i in range(len(player.inventory)):
        print str(i+1)+".- "+player.inventory[i].name+" ("+str(player.inventory[i].price/2)+"G)"
      print "--"
      print "0.- Back"
      print ""
      print "->",

      try:
        try:
          sellmenuc=common.getch()
          if sellmenuc=="0":
            print "Nothing else? I can pay you with roaches!"
            common.getch()
            break
          player.pocket+=player.inventory[int(sellmenuc)-1].price/2
          self.forsale.append(copy.copy(player.inventory[int(sellmenuc)-1]))
          del player.inventory[int(sellmenuc)-1]
        except ValueError:
          pass
      except IndexError:
        pass

      

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
  global npcdata
  global vendordata

  try:
    with open("../data/npcs/firstnames_male","r") as file:
      namemale = []
      for line in file:
          namemale.append(line.rstrip('\n'))
    npcdata["namemale"]=namemale
     
    with open("../data/npcs/firstnames_female","r") as file:
      namefemale = []
      for line in file:
          namefemale.append(line.rstrip('\n'))
    npcdata["namefemale"]=namefemale

    with open("../data/npcs/secondnames","r") as file:
      secondnames = []
      for line in file:
          secondnames.append(line.rstrip('\n'))
    npcdata["secondnames"]=secondnames

    with open("../data/npcs/appearance","r") as file:
      appearance = []
      for line in file:
          appearance.append(line.rstrip('\n'))
    npcdata["appearance"]=appearance

    with open("../data/npcs/personality","r") as file:
      personality = []
      for line in file:
          personality.append(line.rstrip('\n'))
    npcdata["personality"]=personality

    with open("../data/npcs/things","r") as file:
      things = []
      for line in file:
        things.append(line.rstrip('\n'))
    npcdata["things"]=things

    with open("../data/npcs/jobs","r") as file:
      jobs = []
      for line in file:
          jobs.append(line.rstrip('\n'))
    npcdata["jobs"]=jobs

  except IOError:
    raw_input("Error loading NPC data files")

  try:
    with open("../data/vendor/vendormsg","r") as file:
      welcomemsg=[]
      byemsg=[]
      okmsg=[]
      failmsg=[]
      for line in file:
        line=line.strip()
        if not line.startswith("#"):
          if line.partition(':')[0]=="W":
            welcomemsg.append(line.partition(':')[2])
            vendordata["welcomemsg"]=welcomemsg
          if line.partition(':')[0]=="G":
            byemsg.append(line.partition(':')[2])
            vendordata["byemsg"]=byemsg
          if line.partition(':')[0]=="S":
            okmsg.append(line.partition(':')[2])
            vendordata["okmsg"]=okmsg
          if line.partition(':')[0]=="F":
            failmsg.append(line.partition(':')[2])
            vendordata["failmsg"]=failmsg

  except IOError:
    raw_input("Error loading vendor data filer")

  

sanitize()
load()