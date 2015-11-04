#! /usr/bin/env python 
import os, copy, random, sys
data="../data/"
sys.path.append(os.path.abspath(data))
from inventory import *

class consumable:
  """
  Potions, spells, items that can be eaten, drunk or consumed.

  Default attributes

  #Type
  type=4
  
  # 0 - Potion
  #   01 - HP potion
  #   02 - MP potion
  #   03 - Recovery potion (HP&MP)
  #   04 - Status potions #TO-DO
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
  # 3.- Unidentified potions/food
  #
  # Unidentified consumables can have totally random and unexpected effects. 
  # Vendors can identify them. When this happens, they are converted to a random type 0, 1 or 2 item. (#TO-DO)
  #
  # 4.- Empty 
  #
  # Generates an object without propieties named "--EMPTY--" to be displayed in the crawl screen.
  # This objects can not be consumend and are for display purposes only.

  #General propieties
  name="--EMPTY--"  #Name
  price=0           #Price

  #Potion propieties
  hpr=0             #Maximum HP recovered
  mpr=0             #Maximum MP recovered
  statusr=0         #If 1, recovers status
  subtype=0         #Potion subtype

  #Tome propieties
  intbst=0          #Intelligence modifier
  dexbst=0          #Dexterity modifier
  perbst=0          #Perception modifier
  conbst=0          #Constitution modifier
  wilbst=0          #Willpower modifier 
  chabst=0          #Charisma modifier
  strbst=0          #Strenght modifier

  #Food propieties
  hungrec=0         #Hunger recovery
  chance=0          #Type of food (Good,risky,bad)

  #Attack propieties #TO-DO
  areatype=0        #Type of area affected
  areasize=0        #Size of the area
  damage=0          #Damage caused
  dps=0             #Damage over time
  """

  def __init__(self,newtype,subtype=0):
    """
    Class constructor. Creates a consumable item of the specified type. Needs a subtype parameter for the potions, which is ignored in the rest of the items.

    Consumable items can only be bought from vendors. They can't be found in the ground.
    Requires a type integer. It also accepts a subtype keyword argument for potions (Defaults to 0 - Random)
    """

    self.reset()
    self.subtype=subtype
    self.type=newtype
    self.statusr=0

    #Process item arrays:
    if newtype==0:
      if subtype!=4: # Status potions are not implemented yet
        typelist=["hp_potions","mp_potions","rec_potions"]
        subtype=random.randrange(1,4) if not subtype else subtype
        data=random.choice(eval("consumables."+typelist[subtype-1]))
        self.name=   data[0]
        self.hpr=    data[1]
        self.mpr=    data[2]
        self.price=  data[3]

    if newtype==1:
      data=random.choice(consumables.tomes)
      self.name=      data[0]
      self.strbst=    data[1]
      self.intbst=    data[2]
      self.dexbst=    data[3]
      self.perbst=    data[4]
      self.conbst=    data[5]
      self.wilbst=    data[6]
      self.chabst=    data[7]
      self.price=     data[8]

    if newtype==3:
      data=random.choice(consumables.food)
      self.name=    data[0]
      self.hungrec= int(data[1])
      self.chance=  int(data[2])
      self.price=   int(data[3])

    #Generate empty object
    if newtype==4: self.name="--EMPTY--"

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
    self.hpr=self.mpr=self.hungrec=self.chance=0

    #Tome propieties
    self.intbst=self.dexbst=self.perbst=self.conbst=self.wilbst=self.chabst=self.strbst=0

    #Attack propieties
    self.areatype=self.areasize=self.damage=self.dps=0

#Item class. Creates and manages items.
class item:
  """
  Creates and manages items

  #Item attributes
  ID=0          #Identifier
  name="_"      #Item name
  type=00       #Item table. See any item_XX file or the table below
  equip=0       #Equipped. 1=yes, 2=no

  #Item bonuses
  strbonus=0    #Intelligence boost
  intbonus=0    #Dexterity boost
  dexbonus=0    #Perception boost
  perbonus=0    #Constitution boost
  conbonus=0    #Willpower boost
  wilbonus=0    #Charisma boost
  chabonus=0    #Strenght boost

  #Other
  atk=0         #Attack power
  defn=0        #Defense power
  enchantlv=0   #Enchant level
  """

  def __init__(self,typev):
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

    self.enchantlv=self.equip=0
    self.type=typev

    #Assign path depending on item type
    types=["items_%02i" for i in range(1,12)]
    typev=random.randint(1,12) if not typev else typev
    randitem=random.choice(eval("items."+types[typev]))

    #Assign the attributes from a random item in the chosen section
    self.name=  randitem[0]
    self.atk=   randitem[1]
    self.defn=  randitem[2]
    self.price= randitem[3]

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

    randint=random.randint(1,10000)
    if   randint<=7000: randint=9 #no modifiers
    elif randint>7000 and randint<=7001:  randint= 8  #universal
    elif randint>7001 and randint<=7011:  randint= 7  #celestial
    elif randint>7011 and randint<=7100:  randint= 6  #perfect
    elif randint>7100 and randint<=7500:  randint= 5  #masterful
    elif randint>7500 and randint<=8000:  randint= 4  #refined
    elif randint>8000 and randint<=8700:  randint= 3  #bent
    elif randint>8700 and randint<=9300:  randint= 2  #cracked
    elif randint>9300 and randint<=9700:  randint= 1  #rusty
    elif randint>9700 and randint<=10000: randint= 0  #useless

    #Assign the data with the random values
    if randint!=9:
      modifier=atk_def_modifiers.mods[randint]
      self.name=modifier[0]+" "+self.name
      self.atk+=  (self.atk*modifier[1]/100)
      self.defn+= (self.defn*modifier[2]/100)
      self.price+=(self.price*(modifier[0]+modifier[1])/100)

    # Modifying attribute boosts
    # 20.0% chance of one attribute boost
    # 05.0% chance of two attribute boost
    # 01.0% chance of three attribute boost
    # 00.1% chance of four attribute boost

    randint=random.randint(1,1000)
    attboost=0
    if   randint==1: attboost=4
    elif randint>1  and randint<=10:  attboost=3
    elif randint>10 and randint<=60:  attboost=2
    elif randint>60 and randint<=200: attboost=1
    else: pass

    # generate array with bonus names and array with bonus values
    bonuses=["strbonus","intbonus","dexbonus","perbonus","conbonus","wilbonus","chabonus"]
    bonusvals=[getattr(self,i) for i in bonuses]

    #Initialize bonuses
    for i in bonuses: setattr(self,i,0)

    #Randomly assign the bonus points available
    for i in range(attboost):
      randbonus=bonuses[random.randint(1,7)]
      temp=getattr(self,randbonus)
      setattr(self,randbonus,temp+1)

    # Choose one name depending on what attribute boost is higher.
    # Only if the total sum of the values is over zero
    # It gets the names from the attr_modifiers module
    if sum(bonusvals):
      for i,v in enumerate(bonusvals):
        temp=bonusvals.pop(i)
        if temp>sum(bonusvals): self.name=attr_modifiers.mods[bonuses[i]]
        bonusvals.insert(i,temp)

    #Adjust price after attr boost
    self.price*=(1+sum(bonusvals))

    #Avoid negative prices 
    self.price=0 if self.price<0 else self.price

    #And, if the type selected was 0, set everything to 0 again
    if not typev: self.reset()

  def reset(self):
    """
    Sets all the attributes of the given item object to zero.
    """

    self.defn=self.strbonus=self.intbonus=self.dexbonus=self.perbonus=self.conbonus=self.wilbonus=self.chabonus=0
    self.name=" "
    self.price=0
    self.atk=0

  def enchant(self):
    """
    Enchants the item 

    Permanently adds attribute bonuses and increases either the attack or defense by 1.
    Requires an item 
    Returns 0 if the enchant failed and 1 if it succeeded.
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

    # Calculate random number
    randint=random.randint(1,1000)
    attboost=0
    if randint<5: attboost=4
    elif randint>51 and randint<=50: attboost=3
    elif randint>50 and randint<=200: attboost=2
    elif randint>200 and randint<=990: attboost=1
    elif randint>990:        
      self.reset()
      return 0

    # If the item has not broken, enchant it
    # Randomly assign the bonus points available
    for i in range(1,attboost+1):
      boosted=random.choice(["STR","INT","DEX","PER","CON","WIL","CHA"])
      if boosted=="STR": self.strbonus+=1
      if boosted=="INT": self.intbonus+=1
      if boosted=="DEX": self.dexbonus+=1
      if boosted=="PER": self.perbonus+=1
      if boosted=="CON": self.conbonus+=1
      if boosted=="WIL": self.wilbonus+=1
      if boosted=="CHA": self.chabonus+=1

    # Double the price of the item
    # Set price first to avoid enchanted item prices to stay at zero
    if self.price<1: self.price=1
    self.price*=2

    # Increase attack or defense
    if random.choice([0,1]): self.atk+=1
    else: self.defn+=1

    # Increase enchant level
    self.enchantlv+=1

    # Increase maximum enchanted level in the stats
    if self.enchantlv>player.maxench: player.maxench=self.enchantlv

    #Display the enchanting level in the item name
    if self.name[-1].isalpha(): self.name=self.name+" +1"
    else: elf.name=self.name.split('+')[0]+str(int(self.name.split('+')[1])+1)

    return 1

if __name__=="__main__": pass