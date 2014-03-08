#usr/bin/env python 
import os
import random

#Item class. Creates and manages items.
class item:
  "Item class creates and manages items"

  #Item attributes
  ID=0      #Identifier
  name="_"  #Item name
  type=00   #Item table. See any item_XX file or the table below
  equip=0   #Equipped. 1=yes, 2=no

  #Item bonuses
  strbonus=0
  intbonus=0
  dexbonus=0
  perbonus=0 
  conbonus=0
  wilbonus=0 
  chabonus=0
  atk=0
  defn=0

  #Item constructor. Takes random data and sets the attributes
  #Needs an integer (type) to determine the item type (See any item_XX file or the table below)
  def __init__(self,type):

    self.equip=0
    self.type=type

    #Assign path depending on item type
    # Place/Type:
    #   01 - Head
    #   02 - Face
    #   03 - Neck
    #   04 - Shoulders
    #   05 - Chest
    #   06 - One hand
    #   07 - Two hands
    #   08 - Ring
    #   09 - Belt
    #   10 - Legs
    #   11 - Feet
    #   00 - Empty
    path="_"
    if type==1:
      path="../data/inventory/items_01"
    if type==2:
      path="../data/inventory/items_02"
    if type==3:
      path="../data/inventory/items_03"
    if type==4:
      path="../data/inventory/items_04"
    if type==5:
      path="../data/inventory/items_05"
    if type==6:
      path="../data/inventory/items_06"
    if type==7:
      path="../data/inventory/items_07"
    if type==8:
      path="../data/inventory/items_08"
    if type==9:
      path="../data/inventory/items_09"
    if type==10:
      path="../data/inventory/items_10"
    if type==11:
      path="../data/inventory/items_11"
    if type==0:
      path="../data/inventory/items_01" #Pick any of the files, it doesn't matter.
    else:
      pass

    #Open file containing the defined type weapons
    with open (path,"r") as invfile:
      inventory=[]
      atkbarr=[]
      defbarr=[]
      pricearr=[]
      for line in invfile:
        if not line.startswith("#"):
          inventory.append(line.rstrip("\n").partition(':')[0].strip())
          atkbarr.append(line.rstrip("\n").partition(':')[2].partition(':')[0].strip())
          defbarr.append(line.rstrip("\n").partition(':')[2].partition(':')[2].partition(':')[0].strip())
          pricearr.append(line.rstrip("\n").partition(':')[2].partition(':')[2].partition(':')[2].strip())

    #Assign the attributes to an item.
    randitem=random.randrange(len(inventory))
    self.name=inventory[randitem].rstrip()
    self.atk=int(atkbarr[randitem])
    self.defn=int(defbarr[randitem])
    self.price=int(pricearr[randitem])

    #Add attack and defense modifiers and modifier naming.
    #Modifiers are loaded 1-9 to the array. 
    #01 useless:-100:-100  -> 03.00%
    #02 rusty:-50:-50      -> 04.00%
    #03 cracked:-25:-25    -> 06.00%
    #04 bent:-10:-10       -> 07.00%
    #05 refined:10:10      -> 05.00%
    #06 masterful:25:25    -> 04.00%
    #07 perfect:50:50      -> 00.89%
    #08 celestial:100:100  -> 00.10%
    #09 universal:200:200  -> 00.01%
    #10 no modifiers       -> 70.00%
    randint=0
    randint=random.randint(1,10000)
    if randint<=7000: #no modifiers
      randint=9
    if randint>7000 and randint<=7001: #universal
      randint= 8
    if randint>7001 and randint<=7011: #celestial
      randint= 7
    if randint>7011 and randint<=7100: #perfect
      randint= 6
    if randint>7100 and randint<=7500: #masterful
      randint= 5
    if randint>7500 and randint<=8000: #refined
      randint= 4
    if randint>8000 and randint<=8700: #bent
      randint= 3
    if randint>8700 and randint<=9300: #cracked
      randint= 2
    if randint>9300 and randint<=9700: #rusty
      randint= 1
    if randint>9700 and randint<=10000: #useless
      randint= 0

    #Open the file and load the data
    with open ("../data/inventory/atk_def_modifiers","r") as modifile:
      modifiers=[]
      atkmod=[]
      defmod=[]
      for line in modifile:
        if not line.startswith("#"):
          modifiers.append(line.rstrip("\n").partition(':')[0].strip())
          atkmod.append(line.rstrip("\n").partition(':')[2].partition(':')[0].strip())
          defmod.append(line.rstrip("\n").partition(':')[2].partition(':')[2].strip())

    #Assign the data with the random values
    if randint!=9:
      self.name=modifiers[randint]+" "+self.name
    self.atk=self.atk+(self.atk*int(atkmod[randint])/100)
    self.defn=self.defn+(self.defn*int(defmod[randint])/100)
    self.price=self.price+(self.price*int(atkmod[randint])/100)+(self.price*int(defmod[randint])/100)

    # Modifying attribute boosts
    # 20.0% chance of one attribute boost
    # 05.0% chance of two attribute boost
    # 01.0% chance of three attribute boost
    # 00.1% chance of four attribute boost
    randint=random.randint(1,1000)
    attboost=0
    if randint==1:
      attboost=4
    if randint>1 and randint<=10:
      attboost=3
    if randint>10 and randint<=60:
      attboost=2
    if randint>60 and randint<=200:
      attboost=1
    else:
      pass

    #Initialize bonuses
    self.strbonus=0
    self.intbonus=0
    self.dexbonus=0
    self.perbonus=0 
    self.conbonus=0
    self.wilbonus=0 
    self.chabonus=0

    #Randomly assign the bonus points available
    for i in range(1,attboost+1):
      boosted=random.randint(1,7)
      if boosted==1:
        self.strbonus+=1
      if boosted==2:
        self.intbonus+=1
      if boosted==3:
        self.dexbonus+=1
      if boosted==4:
        self.perbonus+=1
      if boosted==5:
        self.conbonus+=1
      if boosted==6:
        self.wilbonus+=1
      if boosted==7:
        self.chabonus+=1

    #assigning prefix depending on attributes boosted
    #This will be done from file in the future. Probably.
    strarray=["tough","warrior's","knight's","berserker's"]       #line 1
    intarray=["obscure","bookworm's","academic","grandmaster's"]  #line 2
    dexarray=["swift","rogue's","ninja","shadow"]                 #line 3
    perarray=["detecting","tracing","radar","omniscient"]         #line 4 
    conarray=["healing","invigorating","armoured","terminator"]   #line 5 
    wilarray=["determined","leader's","commanding","napoleonic"]  #line 6 
    chaarray=["friendly","posh","diplomatic","respectable"]       #line 7 

    #Choose one name depending on what attribute boost is higher.
    if not self.intbonus+self.dexbonus+self.perbonus+self.conbonus+self.wilbonus+self.chabonus+self.strbonus==0:
      if self.strbonus>=self.intbonus+self.dexbonus+self.perbonus+self.conbonus+self.wilbonus+self.chabonus:
        self.name=strarray[self.strbonus]+" "+self.name
      if self.intbonus>=self.strbonus+self.dexbonus+self.perbonus+self.conbonus+self.wilbonus+self.chabonus:
        self.name=intarray[self.intbonus]+" "+self.name
      if self.dexbonus>=self.intbonus+self.strbonus+self.perbonus+self.conbonus+self.wilbonus+self.chabonus:
        self.name=dexarray[self.dexbonus]+" "+self.name
      if self.perbonus>=self.intbonus+self.dexbonus+self.strbonus+self.conbonus+self.wilbonus+self.chabonus:
        self.name=perarray[self.perbonus]+" "+self.name
      if self.conbonus>=self.intbonus+self.dexbonus+self.perbonus+self.strbonus+self.wilbonus+self.chabonus:
        self.name=conarray[self.conbonus]+" "+self.name
      if self.wilbonus>=self.intbonus+self.dexbonus+self.perbonus+self.conbonus+self.strbonus+self.chabonus:
        self.name=wilarray[self.wilbonus]+" "+self.name
      if self.chabonus>=self.intbonus+self.dexbonus+self.perbonus+self.conbonus+self.wilbonus+self.strbonus:
        self.name=chaarray[self.chabonus]+" "+self.name

    #Adjust price after attr boost
    self.price=self.price*(self.strbonus+self.intbonus+self.dexbonus+self.perbonus+self.conbonus+self.wilbonus+self.chabonus)

    #Avoiding negative prices 
    if self.price<0:
      self.price=0

    #And, if the type selected was 0, set everything to 0 again
    if type==0:
      self.reset()

  def reset(self):
    self.name=""
    self.price=0
    self.atk=0
    self.defn=0
    self.strbonus=0
    self.intbonus=0
    self.dexbonus=0
    self.perbonus=0 
    self.conbonus=0
    self.wilbonus=0 
    self.chabonus=0

  #Enchants the item (Permanently adds attribute, attack or defense bonuses)
  def enchant(self):
    pass

#test stuff
# while 1:
#   new=item(2)
#   print "name:",new.name
#   print "atk:",new.atk
#   print "def:",new.defn
#   print "price:",new.price
#   print "str boost",new.strbonus
#   print "int boost",new.intbonus
#   print "dex boost",new.dexbonus
#   print "per boost",new.perbonus 
#   print "con boost",new.conbonus
#   print "wil boost",new.wilbonus 
#   print "cha boost",new.chabonus
#   print ""
#   print "_________"
#   print ""

# while 1:
#   new=item(random.randint(1,11))
#   print new.name