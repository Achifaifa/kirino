#usr/bin/env python 
import os, random
import common

class consumable:
  """
  Potions, spells, items that can be eaten, drunk or consumed.
  """

  #Type
  type=4

  #General propieties
  name="--EMPTY--"
  price=0

  #Potion propieties
  hpr=0
  mpr=0
  statusr=0
  subtype=0

  #Tome propieties
  intbst=0
  dexbst=0
  perbst=0
  conbst=0
  wilbst=0
  chabst=0
  strbst=0

  #Attack propieties
  areatype=0
  areasize=0
  damage=0
  dps=0

  def __init__(self,newtype,subtype):
    """
    Class constructor. Creates a consumable item of the specified type.

    Consumable items can only be bought from vendors. They can't be found in the ground.
    Requires type and subtype:
    # 0 - Potion
    #   01 - HP potion
    #   02 - MP potion
    #   03 - Recovery potion (HP&MP)
    #   04 - Status potions
    #   00 - Random (except status potions)
    #
    # Potions regenerate a certain amout of HP or MP in a single turn.
    # The amout of points recovered depends on the type of potion. Each potion type has a fixed value that can vary in the -30% / +30% range with random modifiers.
    # Recovery potions recover both HP and MP, and status potions stop damage over time (Poison, fire, bleeding, etc)
    #
    # 1 - Tome of knowledge
    #
    # Tomes of knowledge add one point to an attribute and decrease one point to another attribute.
    #
    # 2 - Attack items
    #
    # Attack items inflict extra damage. They can be direct things like bombs or extra strenght, or they can inflict extra damage over time.
    #
    # 3.- Unidentified potions
    #
    # Unidentified consumables can have totally random and unexpected effects. 
    # Vendors can identify them. When this happens, they are converted to a random type 0, 1 or 2 item.
    #
    # 4.- Empty 
    #
    # Generates an object without propieties named "--EMPTY--" to be displayed in the crawl screen.
    # This objects can not be consumend and are for display purposes only.

    """

    #Variable initialization
    items=[]
    self.subtype=subtype
    self.type=newtype

    #Array loading
    try:
      with open ("../data/inventory/items_CI","r") as consumables:
        for line in consumables:

          #Only check the lines that contain items of the selected class.
          if line.startswith(str(newtype)):

            #If the item is a potion, save arrays with [name,HP,MP,price]
            if newtype==0:
              if subtype==0:
                subtype=random.randint(1,3)
              if int(line.strip().partition(':')[2].partition(':')[0])==subtype:
                tempitem=[]
                tempitem.append(line.strip().partition(':')[2].partition(':')[2].partition(':')[0])
                tempitem.append(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                tempitem.append(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                tempitem.append(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2])
                items.append(tempitem)

            if newtype==1:
              pass
            if newtype==2:
              pass
            if newtype==3:
              pass

    except IOError:
      raw_input("Could not load consumable data file")

    #Process item arrays:
    if newtype==0:
      data=random.choice(items)
      self.name=data[0]
      self.hpr=int(data[1])
      self.mpr=int(data[2])
      self.price=int(data[3])

    #Generate empty object
    if newtype==4:
      self.name="--EMPTY--"

  def reset(self):
    """
    resets an item so all the attributes are set to zero.
    """

    #Type
    self.type=4

    #General propieties
    self.name="--EMPTY--"
    self.price=0

    #Potion propieties
    self.hpr=0
    self.mpr=0

    #Tome propieties
    self.intbst=0
    self.dexbst=0
    self.perbst=0
    self.conbst=0
    self.wilbst=0
    self.chabst=0
    self.strbst=0

    #Attack propieties
    self.areatype=0
    self.areasize=0
    self.damage=0
    self.dps=0


#Item class. Creates and manages items.
class item:
  """
  Creates and manages items
  """

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
  enchantlv=0

  def __init__(self,type):
    """
    Item constructor. 

    Takes random data from the inventory data files and sets the attributes
    Needs an integer (type) to determine the item type

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
    #   00 - Empty (Item with all the attributes set to zero)
    """

    self.enchantlv=0
    self.equip=0
    self.type=type

    #Assign path depending on item type
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
          inventory.append(line.strip().partition(':')[0].strip())
          atkbarr.append(line.strip().partition(':')[2].partition(':')[0].strip())
          defbarr.append(line.strip().partition(':')[2].partition(':')[2].partition(':')[0].strip())
          pricearr.append(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].strip())

    #Assign the attributes from a random item in the chosen file
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
      self.price=(self.price+((self.price*int(atkmod[randint])/100)+(self.price*int(defmod[randint])/100)))

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
    self.price=(self.price*(1+self.strbonus+self.intbonus+self.dexbonus+self.perbonus+self.conbonus+self.wilbonus+self.chabonus))

    #Avoiding negative prices 
    if self.price<0:
      self.price=0

    #And, if the type selected was 0, set everything to 0 again
    if type==0:
      self.reset()

  def reset(self):
    """
    Sets all the attributes of the given item object to zero.
    """
    self.name=" "
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

  def enchant(self,player):
    """
    Enchants the item 

    Permanently adds attribute bonuses and increases either the attack or defense by 1.
    Requires the player enchanting the object to be passed to alter the money balance.
    Items can only be enchanted up to lv10.

    Chances of attribute boosts:
      79.0% chance of one attribute boost
      15.0% chance of two attribute boost
      04.5% chance of three attribute boost
      00.5% chance of four attribute boost
      01.0% chances of the item being destroyed

    Enchanting an item costs the current item price, and doubles its price.
    If the player has no money to pay for the enchant or the item is lv10, enchant() returns a message and passes.

    If the item is destroyed all its attributes are set to 0. 
    Deleting the resetted item from the inventory is done in the player module after calling the enchant() function.
    """

    enchantprice=self.price
    ex=0 #Exception variable
    if player.pocket<enchantprice:
      print "You don't have enough money"
      common.getch()
    if self.enchantlv>=10:
      print "Maximum enchant level reached"
      common.getch()
    if player.pocket>=enchantprice and self.enchantlv<10:
      player.pocket-=enchantprice

      # Calculate random number
      randint=random.randint(1,1000)
      attboost=0
      if randint<5:
        attboost=4
      if randint>51 and randint<=50:
        attboost=3
      if randint>50 and randint<=200:
        attboost=2
      if randint>200 and randint<=990:
        attboost=1
      if randint>990:
        print self.name+" broke during enchanting"
        common.getch()
        self.reset()
        ex=1

      if not ex:
        #Randomly assign the bonus points available
        for i in range(1,attboost+1):
          boosted=random.randint(1,7)
          if boosted==1:
            self.strbonus+=1
            print "+1 STR"
          if boosted==2:
            self.intbonus+=1
            print "+1 INT"
          if boosted==3:
            self.dexbonus+=1
            print "+1 DEX"
          if boosted==4:
            self.perbonus+=1
            print "+1 PER"
          if boosted==5:
            self.conbonus+=1
            print "+1 CON"
          if boosted==6:
            self.wilbonus+=1
            print "+1 WIL"
          if boosted==7:
            self.chabonus+=1
            print "+1 CHA"

        #double the price of the item
        #Adding 1 to avoid enchanted item prices to stay at zero
        self.price=((self.price+1)*2)

        #Increase attack or defense
        i=random.randint(0,1)
        if i==0:
          self.atk+=1
        if i==1:
          self.defn+=1

        #Increase enchant level
        self.enchantlv+=1

        #Display the enchanting level in the item name
        if "a"<=self.name[-1:]<="z":
          self.name=self.name+" +1"
        else:
          templv=int(self.name.partition('+')[2].strip())
          templv+=1
          tempname=self.name.partition('+')[0]
          self.name=tempname+"+"+str(templv)
          #Remove the numbers after the + in the name, add 1, attack the numbers to name.

        raw_input(self.name+" enchanted successfully")

    #If the player has no money, pass
    else:
      pass