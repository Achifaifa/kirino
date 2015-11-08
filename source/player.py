#! usr/bin/env python 
import copy, json, os, random, sys
import common, copy, dungeon, item
sys.path.append(os.path.abspath("../data/"))
import playerd

class player:
  """
  Player class. Creates and manages player objects

  #Main characteristics

  name="_"      #Name
  pocket=0      #Money
  exp=0         #EXP
  lv=1          #Level
  points=0      #Expendable points
  race="_"      #Race
  charclass="_" #Class
  inventory=[]  #10 slot inventory
  equiparr=[]   #Equipped item inventory
  belt=[]       #Quick access consumable items
  status=0      #Paralyzed, burned, bleeding, etc
  prestige=0    #Prestige points
  prestigelv=1  #Prestige level (unused)

  #Attribute and attribute booster variables

  INT=1         #Intelligence
  DEX=1         #Dexterity
  PER=1         #Perception
  WIL=1         #Willpower
  STR=1         #Strenght
  CON=1         #Constitution
  CHA=1         #Charisma
  intboost=0    #
  dexboost=0    #
  perboost=0    #
  wilboost=0    # Extra attributes given by equipped items
  strboost=0    #
  conboost=0    #
  chaboost=0    #

  totatk=1      #Total attack power
  totdefn=1     #Total defense power

  #Secondary and status variables

  HP=0          #Maximum hit points
  hp2=0         #Current hit points
  MP=0          #Maximum mana points
  mp2=0         #Current mana points
  END=0         #Endurance
  SPD=0         #Speed
  stomach=10     #Hunger level

  #Stats and achievements

  totalfl=0     #Floors explored
  steps=0       #Steps
  totalatks=0   #Total attacks
  totalhits=0   #Total hits
  totaldmg=0    #Damage given
  totalrcv=0    #Damage taken
  kills=0       #Enemies killed
  totalgld=0    #Total gold gained
  totaltrp=0    #Times stepped on traps
  itemspck=0    #Total items picked
  itemsdst=0    #Total items destroyed
  itemsenc=0    #Total enchants
  totalpot=0    #Potions taken
  totalsll=0    #Items sold
  totalbuy=0    #Items bought
  totalspn=0    #Money spent
  maxdmg=0      #Maximum damage
  maxench=0     #Maximum enchant lv

  #Position
  xpos=0
  ypos=0
  zpos=0
  """

  def __init__(self):
    """
    Initialization of the player objects. 

    Generates a random player. Coordinate setting must be done through enter()

    Attribute setting for manual player creation must be done externally
    """

    #Main characteristics
    self.name="_"      #Name
    self.pocket=0      #Money
    self.exp=0         #EXP
    self.lv=1          #Level
    self.points=40     #Expendable points
    if randomv: self.points=0
    self.race="_"      #Race
    self.charclass="_" #Class
    self.status=0      #Paralyzed, burned, bleeding, etc
    self.prestige=0    #Prestige points
    self.prestigelv=1  #Prestige level (unused)
    self.stomach=100
    self.hungsteps=0

    #Initialize stat variables
    self.totalfl =self.steps   =self.totalatks=self.totalgld=self.totalhits=self.totaldmg=self.totalrcv=self.kills   =0  
    self.totaltrp=self.itemspck=self.itemsdst =self.itemsenc=self.totalpot =self.totalsll=self.totalbuy=self.totalspn=0 
    self.maxdmg  =self.maxench =0

    #Initializing inventory arrays and items
    self.belt=[]
    self.equiparr=[]
    self.inventory=[]
    for i in range(6):  self.belt.append(item.consumable(4))
    for i in range(11): self.equiparr.append(item.item(0))
    for i in range(2):  self.inventory.append(item.item(random.randint(1,11)))

    #Set attributes to 1, set secondary attributes
    self.STR=self.INT=self.CON=self.WIL=self.PER=self.DEX=self.CHA=1

    #Set attribute boosters to 0
    self.strboost=self.intboost=self.conboost=self.wilboost=self.perboost=self.dexboost=self.chaboost=0

    #Secondary attributes
    self.HP=self.hp2=0
    self.MP=self.mp2=0
    self.END=self.SPD=0
    self.totatk=self.totdefn=1
    self.secondary()
    self.mp2=self.MP
    self.hp2=self.HP
    
    # Initialize position
    self.ypos=0
    self.xpos=0
    self.zpos=0

    # Name
    self.name=random.choice(playerd.names.names)
    # Race
    self.race=random.choice(playerd.races.stats)
    self.STR+=stats[self.race]["STR"]
    self.INT+=stats[self.race]["INT"]
    self.DEX+=stats[self.race]["DEX"]
    self.PER+=stats[self.race]["PER"]
    self.CON+=stats[self.race]["CON"]
    self.WIL+=stats[self.race]["WIL"]
    self.CHA+=stats[self.race]["CHA"]

    #Random class
    self.charclass=random.choice(playerd.classes.classes) 

    #Random initial attributes
    for i in range(9):
      randstat=random.randrange(7)
      if   randstat==0: self.STR+=1
      elif randstat==1: self.INT+=1
      elif randstat==2: self.DEX+=1
      elif randstat==3: self.PER+=1
      elif randstat==4: self.CON+=1
      elif randstat==5: self.WIL+=1
      elif randstat==6: self.CHA+=1
      else: pass

  def enter(self,dungeon,fall=0):
    """
    Places the player object in a dungeon

    if fall==0, the player is placed in the entrance tile
    if fall==1, then a random tile is selected

    fall is optional and defaults to 0
    """

    self.totalfl+=1
    self.exp+=1
    self.levelup()

    if fall:
      while 1:
        randy=random.randrange(len(dungeon.dungarray))
        randx=random.randrange(len(dungeon.dungarray[randy]))
        if dungeon.dungarray[randy][randx]==".":
          self.xpos, self.ypos=randx, randy
          return 0
      
    else:
      for i in range(len(dungeon.dungarray)):
        for j in range(len(dungeon.dungarray[i])):
          if dungeon.dungarray[i][j]=="A":
            self.ypos, self.xpos=i, j
            return 0

    return 1

  def pickobject(self,picked):
    """
    Pick item from the floor. 

    This receives an item and adds it to the inventory if the inventory is not full.

    Returns 0 and adds the item to the inventory if the item was correctly picked
    Returns 0 if it wasn't
    """

    
    #If the inventory is full, passes.
    if len(self.inventory)>=9:
      pass
      return 1, "Your inventory is full!\n"
    
    #If the inventory is not full, it adds it. 
    if len(self.inventory)<9:
      self.inventory.append(picked)
      self.itemspck+=1
      return 0, "You picked %s\n"%picked.name

  def hunger(self):
    """
    Processes the current hunger state 
    """

    #Update hunger stats
    self.hungsteps+=1
    if self.hungsteps==10:
      self.hungsteps=0
      self.stomach-=1
      if self.stomach<10:
        return "Your stomach growls...\n"

    #Act if hungry
    if not self.stomach:
      self.hp2-=1
      return "You feel hungry and weak\n"

  def pickconsumable(self,item):
    """
    Picks a consumable item from the floor.

    It adds it to the consumable inventory, potions to slots 1-3 and food to slots 4-6.

    Returns an interger if it has been picked (0:no, 1:yes) and a message.
    """
    
    if object.type in [0,3]:
      for i in self.belt:
        if i.type==4:
          i=copy.copy(item)
          return 1,"You picked %s."%item.name
      return 0,"Your belt is full"
    
  def move(self,dungeon,direction):
    """
    Move function. 

    Receives a dungeon object to check for obstacles and an integer [1,4] indicating the direction
      1 north
      2 west
      3 south
      4 east
      5 northwest
      6 northeast
      7 southwest
      8 southeast

    Returns an integer:
      0 Can't move (Wall or other obstacle)
      1 Moved successfully
      2 Mob present (Not moved, signaled for attack)
    """

    #This gives 1 base move 
    #It used to add 1 extra move for every 10 SPD but this caused bugs
    mobmarkers=[]
    for i in dungeon.mobarray: mobmarkers.append (i.marker)
    moves=1
    try:
      #Checks the direction and moves
      if direction==1:
        if dungeon.dungarray[self.ypos-1][self.xpos] in ["#","|"]: return 0
        if dungeon.filled[self.ypos-1][self.xpos] in mobmarkers: return 2
        else:
          self.steps+=moves
          self.ypos-=moves
          return 1
      elif direction==2:
        if dungeon.dungarray[self.ypos][self.xpos-1]=="#": return 0
        if dungeon.filled[self.ypos][self.xpos-1] in mobmarkers: return 2
        elif dungeon.dungarray[self.ypos][self.xpos-1]=="|": dungeon.vendorvar.commerce(self)
        else:
          self.steps+=moves
          self.xpos-=moves
          return 1  
      elif direction==3:
        if dungeon.dungarray[self.ypos+1][self.xpos] in ["#","|"]: return 0
        if dungeon.filled[self.ypos+1][self.xpos] in mobmarkers: return 2
        else:   
          self.steps+=moves  
          self.ypos+=moves
          return 1
      elif direction==4:
        if dungeon.dungarray[self.ypos][self.xpos+1]=="#": return 0
        if dungeon.filled[self.ypos][self.xpos+1] in mobmarkers: return 2
        elif dungeon.dungarray[self.ypos][self.xpos+1]=="|": dungeon.vendorvar.commerce(self)
        else:
          self.steps+=moves
          self.xpos+=moves
          return 1
      elif direction==5:
        if dungeon.dungarray[self.ypos-1][self.xpos-1] in ["#","|"]: return 0
        if dungeon.filled[self.ypos-1][self.xpos-1] in mobmarkers: return 2
        else:
          self.steps+=moves
          self.ypos-=moves
          self.xpos-=moves
          return 1
      elif direction==6:
        if dungeon.dungarray[self.ypos-1][self.xpos+1] in ["#","|"]: return 0
        if dungeon.filled[self.ypos-1][self.xpos+1] in mobmarkers: return 2
        else:
          self.steps+=moves
          self.ypos-=moves
          self.xpos+=moves
          return 1
      elif direction==7:
        if dungeon.dungarray[self.ypos+1][self.xpos-1] in ["#","|"]: return 0
        if dungeon.filled[self.ypos+1][self.xpos-1] in mobmarkers: return 2
        else:
          self.steps+=moves
          self.ypos+=moves
          self.xpos-=moves
          return 1
      elif direction==8:
        if dungeon.dungarray[self.ypos+1][self.xpos+1] in ["#","|"]: return 0
        if dungeon.filled[self.ypos+1][self.xpos+1] in mobmarkers: return 2
        else:
          self.steps+=moves
          self.ypos+=moves
          self.xpos+=moves
          return 1
      else: return 0
    except IndexError: return 0

  def secondary(self):
    """
    Calculates and sets the secondary attributes from the primary ones.
 
    Receives a player object and recalculates HP, MP, END and SPD from the primary attributes. 
    It also adds the extra HP and MP gained after adding an attribute point or leveling up.
    """

    #This fails when saving and loading a character
    temp=self.HP-self.hp2
    self.HP=((self.CON+self.conboost+self.STR+self.strboost)*4)+10
    self.hp2=(self.HP-temp)

    temp2=self.MP-self.mp2
    self.MP=(self.INT+self.intboost+self.WIL+self.wilboost)
    self.mp2=(self.MP-temp2)

    self.END=((self.CON+self.conboost+self.STR+self.strboost+self.wilboost+self.WIL)*3)+5
    self.SPD=(self.CON+self.conboost+self.DEX+self.dexboost)*3

  def charsheet(self):
    """
    Character sheet. 

    Main menu to edit, view and configure characters and player options
    """

    menu=0
    while 1:
      self.secondary()
      common.version()
      print "%s - Character sheet\n"              %(self.name)
      print "Level %i %s %s"                      %(self.lv,self.race,self.charclass)
      if self.lv==1: print "%i/5 xp, %i points"   %(self.exp,self.points)
      if self.lv>1:  print "%i/%i xp, %i points"  %(self.exp,3*self.lv+(2*(self.lv-1)),self.points)
      print "%i floors explored"                  %(self.totalfl)
      print "Stomach is %i%% full\n"              %(self.stomach)
      self.getatr()
      print "\n1.- Spend points"
      print "2.- Inventory"
      print "3.- Character options"
      print "4.- Stats"
      print "5.- Achievements"
      print "\n8.- Save"
      print "9.- Load"
      print "\n0.- Exit"
      print "->",
      menu=common.getch()
      if   menu=="1": self.spend()
      elif menu=="2": self.invmenu()
      elif menu=="3": self.optmenu()
      elif menu=="4": self.statmenu()
      elif menu=="5": self.achievements()
      elif menu=="8":
        print "saving... "+self.save()
        common.getch()
      elif menu=="9":
        print "loading... "+self.load()
        common.getch()
      elif menu=="0": break
      pass

  def spend(self):
    """
    Point spending menu.
    """

    choice=-1
    while choice!="0": 
      self.secondary()
      common.version()
      print "%s - Character sheet \n"%(self.name)
      print "Spend points"
      if self.points==0:  print "No points left! \n"
      else:               print "%i points left \n"%(self.points)

      #Determining cost of improving attributes (Based on AFMBE rules, sort of)  
      coststr=5 if self.STR<5 else ((self.STR/5)+1)*5
      costint=5 if self.INT<5 else ((self.INT/5)+1)*5
      costdex=5 if self.DEX<5 else ((self.DEX/5)+1)*5
      costper=5 if self.PER<5 else ((self.PER/5)+1)*5
      costcon=5 if self.CON<5 else ((self.CON/5)+1)*5
      costwil=5 if self.WIL<5 else ((self.WIL/5)+1)*5
      costcha=5 if self.CHA<5 else ((self.CHA/5)+1)*5

      #printing menu
      print "1.- [%i] STR %i (+%i)"%(coststr,self.STR,self.strboost)
      print "2.- [%i] INT %i (+%i)"%(costint,self.INT,self.intboost)
      print "3.- [%i] DEX %i (+%i)"%(costdex,self.DEX,self.dexboost)
      print "4.- [%i] CON %i (+%i)"%(costcon,self.CON,self.conboost)
      print "5.- [%i] PER %i (+%i)"%(costper,self.PER,self.perboost)
      print "6.- [%i] WIL %i (+%i)"%(costwil,self.WIL,self.wilboost)
      print "7.- [%i] CHA %i (+%i)"%(costcha,self.CHA,self.chaboost)
      print "\nSecondary attributes:"
      print 'END:', self.END, '     SPD:', self.SPD
      print "Max. HP: %i"%(self.HP)
      print "Max. MP: %i"%(self.MP)
      print "---"
      print "0.- Exit"
      print "\n->",
      choice=common.getch()

      #Choice cases
      if self.points==0: pass
      else:
        if choice=="1":
          if self.points>=coststr:
            self.STR+=1
            self.points-=coststr
        elif choice=="2":
          if self.points>=costint:
            self.INT+=1
            self.points-=costint
        elif choice=="3":
          if self.points>=costdex:
            self.DEX+=1
            self.points-=costdex
        elif choice=="4":
          if self.points>=costcon:
            self.CON+=1
            self.points-=costcon
        elif choice=="5":
          if self.points>=costper:
            self.PER+=1
            self.points-=costper
        elif choice=="6":
          if self.points>=costwil:
            self.WIL+=1
            self.points-=costwil
        elif choice=="7":
          if self.points>=costcha:
            self.CHA+=1
            self.points-=costcha
        elif choice=="0": pass
        else: pass

  def optmenu(self):
    """
    Player options menu
    """

    coptmen=-1
    while coptmen!="0": 
      common.version()
      print "%s - Character sheet \n"%(self.name)
      print "1.- Change name"
      print "---"
      print "0.- Back"
      print "->",
      coptmen=common.getch()
      if coptmen=="1": self.name=raw_input("New name? ")
      if coptmen=="0": break

  def calcbonus(self,item):
    """
    Generates the string with the attribute boosts for the inventory
    """

    calcarray=[]
    if item.strbonus>0: calcarray.append("+%s STR"%item.strbonus)
    if item.intbonus>0: calcarray.append("+%s INT"%item.intbonus)
    if item.dexbonus>0: calcarray.append("+%s DEX"%item.dexbonus)
    if item.perbonus>0: calcarray.append("+%s PER"%item.perbonus)
    if item.conbonus>0: calcarray.append("+%s CON"%item.conbonus)
    if item.wilbonus>0: calcarray.append("+%s WIL"%item.wilbonus)
    if item.chabonus>0: calcarray.append("+%s CHA"%item.chabonus)
    if len(calcarray)>0: return "("+(', '.join(map(str,calcarray)))+")"
    if len(calcarray)==0: return ""

  def willtest(self):
    """
    Tests if the player has enough willpower to move.

    Roll a die [1,20] and add the total willpower
    If the roll is less than 20/remaining HP, the test fails 

    If the player's health is bigger than 5, the player automatically passes the test.
    """

    if self.hp2<=5:
      roll=random.randint(1,20)+self.WIL+self.wilboost
      if self.hp2>0:
        if roll<20/self.hp2: return 0,"Your body refuses to move"
    return 1,""

  def use(self,item):
    """
    Takes an item object from the player belt and uses it.

    Returns a message to be displayed.
    """

    if item.type==0:
      hppool=int(item.hpr)
      mppool=int(item.mpr)
      mpres=hpres=0
      name=item.name
      self.stomach+=10

      #restore HP
      while hppool>0 and self.hp2<self.HP:
        hppool-=1
        self.hp2+=1
        hpres+=1

      #restore MP
      while mppool>0 and self.mp2<self.MP:
        mppool-=1
        self.mp2+=1
        mpres+=1

      #restore status
      if item.statusr: self.status=0

      #Message generation
      msg="You drank "+item.name+". "
      if hpres>0 or mpres>0: msg=msg+"You recovered "
      if hpres>0: msg=msg+str(hpres)+" HP"
      if hpres>0 and mpres>0: msg=msg+" and "
      if mpres>0: msg=msg+str(mpres)+" MP"
      if hpres>0 or mpres>0: msg=msg+"."
      self.totalpot+=1
      item.reset()
      return msg

    if item.type==1:
      self.INT+=item.intbst
      self.DEX+=item.dexbst
      self.PER+=item.perbst
      self.CON+=item.conbst
      self.WIL+=item.wilbst
      self.CHA+=item.chabst
      self.STR+=item.strbst
      item.reset()

      #Message generation
      msg="You used "+item.name+". "
      if item.intbst>0: msg=msg+"INT +"+str(item.intbst)+" "
      if item.dexbst>0: msg=msg+"DEX +"+str(item.dexbst)+" "
      if item.perbst>0: msg=msg+"PER +"+str(item.perbst)+" "
      if item.conbst>0: msg=msg+"CON +"+str(item.conbst)+" "
      if item.wilbst>0: msg=msg+"WIL +"+str(item.wilbst)+" "
      if item.chabst>0: msg=msg+"CHA +"+str(item.chabst)+" "
      if item.strbst>0: msg=msg+"STR +"+str(item.strbst)+" "
      msg=msg+"\n"
      item.reset()
      return msg

    if item.type==3:
      if self.stomach+item.hungrec>=100:
        self.stomach-=10
        item.reset()
        return "Your can't eat anymore. \nYou throw everything up."
      else:
        self.stomach+=item.hungrec
        if item.chance==1:
          if random.choice([0,0,0,1]): self.hp2-=5
          item.reset()
          return "You filled your stomach with food in bad condition. \nLost 5HP"
        if item.chance==2:
          self.hp2-=5
          item.reset()
          return "That was clearly not edible. \nLost 5HP"
        else: return "Om nom nom nom"

    if item.type==4:
      return ""

  def addbonuses(self,item):
    """
    Adds bonuses from an item to the player
    """

    self.strboost+=item.strbonus
    self.intboost+=item.intbonus
    self.conboost+=item.conbonus
    self.wilboost+=item.wilbonus
    self.perboost+=item.perbonus
    self.dexboost+=item.dexbonus
    self.chaboost+=item.chabonus
    self.totatk  +=item.atk
    self.totdefn +=item.defn

  def rembonuses(self,item):
    """
    Removes bonuses from an item
    """

    self.strboost-=item.strbonus
    self.intboost-=item.intbonus
    self.conboost-=item.conbonus
    self.wilboost-=item.wilbonus
    self.perboost-=item.perbonus
    self.dexboost-=item.dexbonus
    self.chaboost-=item.chabonus
    self.totatk  -=item.atk
    self.totdefn -=item.defn

  def levelup(self):
    """
    Levels the player up
    """

    if self.lv==1 and self.exp>=5:
      self.lv+=1
      self.exp-=5
      self.points+=2
    if self.lv>1:
      lvlimit=3*self.lv+(2*(self.lv-1))
      while self.exp>=lvlimit:
        self.lv+=1
        self.exp-=lvlimit
        self.points+=2

  def invmenu(self):
    """
    Inventory menu and managing. 
    """

    while 1: 
      common.version()
      print "%s - Character sheet"%(self.name)

      #Print equipped items
      print "\nEquipped"
      parts=["Head","Face","Neck","Back","Chest","L hand","R hand","Ring","Belt","Legs","Feet"]
      for i,it in enumerate(parts): print "%02i [+%i/+%i] %s:  %s %s" %(i+1,self.equiparr[i].atk,self.equiparr[i].defn,it,self.equiparr[i].name,self.calcbonus(self.equiparr[i]))
      print "   [+%i/+%i] Total"                 %(self.totatk,self.totdefn)

      #Print everything in the inventory array
      print "\nInventory (%i G)" %(self.pocket)
      for i in range(len(self.inventory)): print "0%i [+%i/+%i] %s (%iG)[%i]" %(i+1,self.inventory[i].atk,self.inventory[i].defn,self.inventory[i].name,self.inventory[i].price,self.inventory[i].type)

      #Print the belt items
      print "\nBelt"
      parts=["B1","B2","B3"]
      for i in range(3): print "%s - %s"%(parts[i],self.belt[i].name)

      #Print the inventory action menu
      print "\nq - destroy item"
      print "w - enchant item"
      print "a - unequip item"
      print "b - use belt item"
      print "0 - Back"
      print "\n->",
      invmenu=common.getch()

      #Belt using menu
      if invmenu=="b":
        try:
          print "Which item? ",
          beltmen=common.getch
          self.use(self.belt[int(beltmen)-1])
        except IndexError: pass

      #Destroy an item from inventory
      elif invmenu=="q":
        print "Which item? "
        itdst=common.getch()
        if "0"<itdst<=str(len(self.inventory)):
          itemdestroyed=self.inventory[int(itdst)-1].name
          print "Destroy "+itemdestroyed+"? (y/n)"
          confirm=common.getch()
          if confirm=="y":
            self.itemsdst+=1
            del self.inventory[int(itdst)-1]
            raw_input(itemdestroyed+" destroyed")

      #Enchanting menu
      elif invmenu=="w":
        try:
          print "Which item? "
          itech=int(common.getch())
          if 0<itech<=len(self.inventory):
            self.inventory[int(itech)-1].enchant(self)
            if self.inventory[int(itech)-1].name==" ": del self.inventory[int(itech)-1]
        except ValueError: pass

      #Unequip menu
      elif invmenu=="a":
        try:
          unitem=int(raw_input("which item? "))
          if 0<int(unitem)<=len(self.equiparr) and self.equiparr[int(unitem)-1].name!=" ":
            temp=copy.copy(self.equiparr[int(unitem)-1])
            self.rembonuses(self.equiparr[int(unitem)-1])
            self.inventory.append(temp)
            self.equiparr[int(unitem)-1].reset()
            for i in self.equiparr: 
              if i.name=="--": i.reset()
        except ValueError: print "Invalid choice"

      #Exit from inventory menu
      elif invmenu=="0": break

      #Item flipping
      else:
        try:
          if 0<int(invmenu)<=len(self.inventory):
            #Flip only if the item is not a weapon
            if self.inventory[int(invmenu)-1].type not in [6,7]:

              #Transform the menu choice in an actual index
              invmenu=int(invmenu)-1

              #If swapping to a non-empty slot     
              if not self.equiparr[self.inventory[invmenu].type-1].name==" ":
                #Store the item in the equipped array in temp
                temp=self.equiparr[self.inventory[invmenu].type-1]
                #Remove bonuses
                self.rembonuses(temp)

              #If swapping to an empty space, just assign an empty object to temp
              else: temp=item.item(0)

              #Flip equip variables
              self.inventory[invmenu].equip=1
              temp.equip=0
              #Add bonuses
              self.addbonuses(self.inventory[invmenu])
              #Move the item to the equip and delete the inventory reference
              self.equiparr[self.inventory[invmenu].type-1]=self.inventory[invmenu]
              del self.inventory[invmenu]
              #Return the temp item to the inventory if it's not empty
              if temp.name!=" ": self.inventory.append(temp)

            #If it's a weapon, evaluate cases. 
            #1H goes to either left or right hand (Unequips left first if both full)
            elif self.inventory[int(invmenu)-1].type==6:
              
              #Case 1: Slot 6 empty
              if self.equiparr[5].name in [" ","--"]:

                #Flip equip variables
                self.inventory[int(invmenu)-1].equip=1
                #Add bonuses
                self.addbonuses(self.inventory[int(invmenu)-1])
                #Move the item to the equip and delete the inventory reference
                self.equiparr[5] = self.inventory[int(invmenu)-1]
                del self.inventory[int(invmenu)-1]

                #Remove any equipped 2H weapon
                if self.equiparr[6].name not in [" ","--"]:
                  self.rembonuses(self.equiparr[6])
                  self.equiparr[6].equip=0
                  self.inventory.append(copy.copy(self.equiparr[6]))
                  self.equiparr[6].reset()

              #Case 2: Slot 7 empty
              elif self.equiparr[6].name in [" ","--"]:

                #Flip equip variables
                self.inventory[int(invmenu)-1].equip=1
                #Add bonuses
                self.addbonuses(self.inventory[int(invmenu)-1])
                #Move the item to the equip and delete the inventory reference
                self.equiparr[6] = self.inventory[int(invmenu)-1]
                del self.inventory[int(invmenu)-1]

              #Case 3: Both slots used (Input slot)
              else: 
                while 1:
                  print "Where? (6-L hand; 7-R hand; 0-cancel)"
                  place=common.getch()
                  if place in ["6","7","0"]: break

                if place=="6":
                  #Remove equipment in slot 5
                  self.rembonuses(self.equiparr[5])
                  self.equiparr[5].equip=0
                  self.inventory.append(copy.copy(self.equiparr[5]))
                  self.equiparr[5].reset()
                  #Flip equip variables
                  self.inventory[int(invmenu)-1].equip=1
                  #Add bonuses
                  self.addbonuses(self.inventory[int(invmenu)-1])
                  #Move the item to the equip and delete the inventory reference
                  self.equiparr[5] = self.inventory[int(invmenu)-1]
                  del self.inventory[int(invmenu)-1]

                elif place=="7":
                  #Remove equipment in slot 6
                  self.rembonuses(self.equiparr[6])
                  self.equiparr[6].equip=0
                  self.inventory.append(copy.copy(self.equiparr[6]))
                  self.equiparr[6].reset()
                  #Flip equip variables
                  self.inventory[int(invmenu)-1].equip=1
                  #Add bonuses
                  self.addbonuses(self.inventory[int(invmenu)-1])
                  #Move the item to the equip and delete the inventory reference
                  self.equiparr[6] = self.inventory[int(invmenu)-1]
                  del self.inventory[int(invmenu)-1]

                elif place=="0": pass
              
            #2H unequips both hands first
            elif self.inventory[int(invmenu)-1].type==7:

              #Return elements 5 and 6 to inventory
              for i in [5,6]:

                #If swapping to a non-empty slot     
                if not self.equiparr[i].name in [" ","--"]:
                  #Store the item in the equipped array in temp
                  temp=self.equiparr[i]
                  #Remove bonuses
                  self.rembonuses(temp)

                #If swapping to an empty space, just assign an empty object to temp
                else: temp=item.item(0)
                #Flip equip variables
                temp.equip=0                
                #Return the temp item to the inventory if it's not empty
                if temp.name!=" ": self.inventory.append(copy.copy(temp))

              invmenu=int(invmenu)-1
              #Flip equip
              self.inventory[invmenu].equip=1
              #Add bonuses
              self.addbonuses(self.inventory[invmenu])
              #Move the item to the equip and delete the inventory reference
              self.equiparr[6]=copy.copy(self.inventory[invmenu])
              del self.inventory[invmenu]
              #Remove weapon bonus indicators in slot 5
              self.equiparr[5].reset()
              #Show that the weapon is 2H
              self.equiparr[5].name="--"

        except: pass


  def attack(self,mob):
    """
    attacks the mob object specified

    Returns a string to be displayed in the crawl screen
    """

    #Increase total attack stat
    self.totalatks+=1

    #Roll for damage. -3 penalty if the enemy is flying
    roll=random.randint(1,10)+self.DEX+self.dexboost
    if mob.zpos==1: roll-=3

    #Once passed, attack
    if self.willtest() and roll>3:
      #Calculate damage
      atkpow=(self.totatk*self.STR)-mob.defn
      if atkpow<0: atkpow=0
      #Change life and hit variables
      mob.HP-=atkpow
      mob.hit=1
      #Update total hits, total damage and max damage stats
      self.totalhits+=1
      self.totaldmg+=atkpow
      if atkpow>self.maxdmg: self.maxdmg=atkpow

      #Actions if the mob has been killed
      if mob.HP<=0:
        #Increase kill stat
        self.kills+=1
        #Add experience to the player
        self.exp+=mob.exp
        #Add prestige only if the player is 3 levels or less over the mob
        if self.lv<=mob.lv+3: self.prestige+=mob.pres
        #Return attack string
        return "You attack %s for %i damage\nYou killed %s for %i experience\nYou earn %i prestige points\n" %(mob.name,atkpow,mob.name,mob.exp,mob.pres)
      else: return "You attack %s for %i damage\n"%(mob.name,atkpow)
    elif roll<=3:
      return "You try to hit %s, but miss" %(mob.name)

  def save(self):
    """
    Save function. Takes the player attributes and saves them into a text file in ../player/save
    If the path or the file do not exist they are created.
    """

    # Generate dictionary with all player attributes 
    attrs=[i for i in dir(self) if not a.startswith('__') and not callable(getattr(self,i))]
    datadict={i:getattr(self,i) for i in attrs}

    # Create/open save file
    if not os.path.exists("../player/"): os.makedirs("../player/")
    with open("../player/save.json","w+") as savefile:
      json.dump(datadict,savefile,indent=2)

  def bury(self):
    """
    Saves the character into a cemetery file 

    This file is ../player/cemetery and contains all the player's dead characters.
    Similar to save, except more verbose.

    Unlike save it does not record things like maximum HP, items or stats, so buried characters can NOT be recovered.
    """

    if not os.path.exists("../player/"): os.makedirs("../player/")
    with open("../player/cemetery","a+") as cemetery:
      cemetery.write("RIP %s, the %s %s (%i prestige).\n"             %(self.name,self.race,self.charclass,self.prestige))
      cemetery.write("Died at level %i after exploring %i floors.\n"  %(self.lv,self.totalfl))
      cemetery.write("His body rots under %i gold.\n"                 %(self.pocket))
      cemetery.write('"%s" \n \n'                                     %(raw_input("Your last words?")))

  def reset(self):
    """
    Changes all player variables to the default values
    """

    self.name="_"    
    self.pocket=0      
    self.exp=0
    self.lv=1
    self.points=0      
    self.race="_"
    self.charclass="_"
    self.stomach=100

    self.inventory=[] 
    self.belt=[]
    self.equiparr=[]
    for i in range(11):
      new=item.item(0)
      self.equiparr.append(new)

    self.totalfl=0    
    self.prestige=0
    self.prestigelv=1

    self.totalfl =self.steps   =self.totalatks=self.totalhits=self.totaldmg=self.totalhit=self.kills   =0 
    self.totalgld=self.totaltrp=self.itemspck =self.itemsenc =self.itemsdst=self.totalpot=self.totalsll=0  
    self.totalbuy=self.totalspn=self.maxdmg   =self.maxench  =0
    self.INT     =self.DEX     =self.PER      =self.WIL      =self.STR     =self.CON     =self.CHA     =1
    self.intboost=self.dexboost=self.perboost =self.wilboost =self.strboost=self.conboost=self.chaboost=0
    self.totatk=self.totdefn=0
    self.HP=self.hp2=0
    self.MP=self.mp2=0
    self.END=self.SPD=0
    
    self.xpos=self.ypos=self.zpos=0

  def load(self):
    """
    Takes the information from the save file stored in ../player/save and loads it into the player object.
    """

    #Save current position
    tempx, tempy, tempz=self.xpos, self.ypos, self.zpos
    #Reset all the variables to the defaults
    self.reset()
    
    #Load file
    try:
      with open("../player/save","r") as savefile:
        attrdict=json.load(savefile)
    except IOError: 
        pass

    #Restore player attributes
    for key,value in attrdict.iteritems(): setattr(self,key,value)

    #Restore position values
    self.xpos, self.ypos, self.zpos=tempx, tempy, tempz
