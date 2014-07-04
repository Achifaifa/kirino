#usr/bin/env python 
import copy, os, random, sys
import common, dungeon, item

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

  def __init__(self,randomv):
    """
    Initialization of the player objects. 

    Receives a dungeon object, then sets the coordinates of the player object in the entrance tile
    It also chooses a random race and class from the ./data/races and ./data/classes files

    Needs a random parameter. if 1, the character is generated randomly.
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

    #Initialize stat variables
    self.totalfl =self.steps   =self.totalatks=self.totalgld=self.totalhits=self.totaldmg=self.totalrcv=self.kills   =0  
    self.totaltrp=self.itemspck=self.itemsdst =self.itemsenc=self.totalpot =self.totalsll=self.totalbuy=self.totalspn=0 
    self.maxdmg  =self.maxench =0

    #Initializing inventory arrays and items
    self.belt=[]
    self.equiparr=[]
    self.inventory=[]
    for i in range(3):  self.belt.append(item.consumable(4,0))
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
    
    #Initialize position
    self.ypos=0
    self.xpos=0
    self.zpos=0

    #Random race
    if randomv==1:
      namearray=[]
      with open("../data/player/names","r") as names:
        for line in names: namearray.append(line.strip())
      self.name=random.choice(namearray)

      with open("../data/player/races","r") as file:
        races={}
        for line in file:
          if not line.startswith('#'):
            temp=[]
            temp.append(int(line.strip().partition(':')[2].partition(':')[0]))
            temp.append(int(line.strip().partition(':')[2].partition(':')[2].partition(':')[0]))
            temp.append(int(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0]))
            temp.append(int(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0]))
            temp.append(int(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0]))
            temp.append(int(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0]))
            temp.append(int(line.strip().partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2]))
            races[line.strip().partition(':')[0]]=temp

        self.race=random.choice(races.keys())
        self.STR+=races[self.race][0]
        self.INT+=races[self.race][1]
        self.DEX+=races[self.race][2]
        self.PER+=races[self.race][3]
        self.CON+=races[self.race][4]
        self.WIL+=races[self.race][5]
        self.CHA+=races[self.race][6]

      #Random class
      with open("../data/player/classes","r") as file:
        classesarray=[]
        for line in file: classesarray.append(line.rstrip('\n'))
      self.charclass=random.choice(classesarray) 

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

  def enter(self,dungeon,fall):
    """
    Places the player object in a dungeon

    if fall==0, the player is placed in the entrance tile
    if fall==1, then a random tile is selected
    """

    if fall:
      while 1:
        randy=random.randint(len(dungeon.dungarray))
        randx=random.randint(len(dungeon.dungarray[randy]))
        if dungeon.dungarray[randy][randx]==".":
          self.xpos=randx
          self.ypos=randy
          self.zpos=0
          break
      
    else:
      for i in range(len(dungeon.dungarray)):
        for j in range(len(dungeon.dungarray[i])):
          if dungeon.dungarray[i][j]=="A":
            self.ypos=i
            self.xpos=j
            self.zpos=0


  def pickobject(self,object):
    """
    Pick item from the floor. 

    This receives an item and adds it to the inventory if the inventory is not full.
    Returns 1 and adds the object to the inventory if the object was correctly picked, returns 0 if it wasn't.
    """

    #If the inventory is not full, it adds it. 
    if len(self.inventory)>=9:
      pass
      return 0,("Your inventory is full!\n")
    #If the inventory is full, passes.
    if len(self.inventory)<9:
      self.inventory.append(object)
      self.itemspck+=1
      return 1,("You picked %s\n"%object.name)
    
  def getatr(self):
    """
    Prints the player attributes on screen.
    """

    print "HP: %i/%i, MP: %i/%i      "  %(self.hp2,self.HP,self.mp2,self.MP)
    print "STR: %i(+%i)  DEX: %i(+%i)"  %(self.STR,self.strboost,self.DEX,self.dexboost)
    print "INT: %i(+%i)  CON: %i(+%i)"  %(self.INT,self.intboost,self.CON,self.conboost)
    print "WIL: %i(+%i)  PER: %i(+%i)"  %(self.WIL,self.wilboost,self.PER,self.perboost)
    print "CHA: %i(+%i)              "  %(self.CHA,self.chaboost)
    print "END: %i SPD: %i           "  %(self.END,self.SPD)
    
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
      print "%i floors explored \n"               %(self.totalfl)
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

  def achievements(self):
    """
    Shows a list of completed achievements.
    """

    common.version()
    print "%s - Character sheet - Achievements\n" %(self.name)

    print "Exploration"
    if      self.totalfl>=500:    print "Elevator 4/4"
    elif    self.totalfl>=250:    print "Elevator 3/4"
    elif    self.totalfl>=100:    print "Elevator 2/4"
    elif    self.totalfl>=10:     print "Elevator 1/4"
    elif    self.totalfl<10:      print "????     0/4"

    if      self.steps>=10000:    print "Explorer 4/4"
    elif    self.steps>=5000:     print "Explorer 3/4"
    elif    self.steps>=1000:     print "Explorer 2/4"
    elif    self.steps>=500:      print "Explorer 1/4"
    elif    self.steps<500:       print "????     0/4"

    print "\nCombat"
    if      self.kills>=500:      print "Warrior  4/4"
    elif    self.kills>=250:      print "Warrior  3/4"
    elif    self.kills>=100:      print "Warrior  2/4"
    elif    self.kills>=10:       print "Warrior  1/4"
    elif    self.kills<10:        print "????     0/4"

    if      self.totaltrp>=100:   print "Bad luck 4/4"
    elif    self.totaltrp>=50:    print "Bad luck 3/4"
    elif    self.totaltrp>=20:    print "Bad luck 2/4"
    elif    self.totaltrp>=5:     print "Bad luck 1/4"
    elif    self.totaltrp<5:      print "????     0/4"

    print "\nItems"
    if      self.itemspck>=100:   print "Hoarder  4/4"
    elif    self.itemspck>=50:    print "Hoarder  3/4"
    elif    self.itemspck>=20:    print "Hoarder  2/4"
    elif    self.itemspck>=5:     print "Hoarder  1/4"
    elif    self.itemspck<5:      print "????     0/4"

    if      self.itemsdst>=100:   print "Cleaning 4/4"
    elif    self.itemsdst>=50:    print "Cleaning 3/4"
    elif    self.itemsdst>=20:    print "Cleaning 2/4"
    elif    self.itemsdst>=5:     print "Cleaning 1/4"
    elif    self.itemsdst<5:      print "????     0/4"

    if      self.itemsenc>=100:   print "Wizard   4/4"
    elif    self.itemsenc>=50:    print "Wizard   3/4"
    elif    self.itemsenc>=20:    print "Wizard   2/4"
    elif    self.itemsenc>=5:     print "Wizard   1/4"
    elif    self.itemsenc<5:      print "????     0/4"

    print "\nEconomy"
    if      self.totalgld>=10000: print "Gold!!   4/4"
    elif    self.totalgld>=5000:  print "Gold!!   3/4"
    elif    self.totalgld>=2500:  print "Gold!!   2/4"
    elif    self.totalgld>=1000:  print "Gold!!   1/4"
    elif    self.totalgld<1000:   print "????     0/4"

    common.getch()

  def statmenu(self):
    """
    Displays character stats on screen
    """

    common.version()
    print "%s - Character sheet - Stats\n"  %(self.name)

    print "Exploration"
    print "Floors explored:     %i"       %(self.totalfl)
    print "Steps:               %i"       %(self.steps)

    print "\nCombat"
    print "Attacks launched:    %i"       %(self.totalatks)
    try:     print "Hits:                %i (%i%%)"   %(self.totalhits,int(round((100*self.totalhits)/self.totalatks)))
    except : print "Hits:                %i (--%%)"   %(self.totalhits)
    print "Total damage:        %i"       %(self.totaldmg)
    try:     print "Average damage:      %i"          %(round(self.totaldmg/self.totalhits))
    except : print "Average damage:      0"
    print "Total damage taken:  %i"       %(self.totalrcv)
    print "Traps stepped on:    %i"       %(self.totaltrp)
    print "Mobs killed:         %i"       %(self.kills)
    print "Max hit damage:      %i"       %(self.maxdmg)

    print "\nItems"
    print "Items picked:        %i"       %(self.itemspck)
    print "Items destroyed:     %i"       %(self.itemsdst)
    print "Items enchanted:     %i"       %(self.itemsenc)
    print "Maximum enchant lv:  %i"       %(self.maxench)    
    print "Potions taken:       %i"       %(self.totalpot)

    print "\nEconomy"
    print "Gold earned:         %i"       %(self.totalgld)
    print "Gold spent:          %i"       %(self.totalspn)
    print "Items sold:          %i"       %(self.totalsll)
    print "Items bought:        %i"       %(self.totalbuy)
    common.getch()

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
      if self.STR<5:  coststr=5
      if self.STR>=5: coststr=((self.STR/5)+1)*5
      if self.INT<5:  costint=5
      if self.INT>=5: costint=((self.INT/5)+1)*5
      if self.DEX<5:  costdex=5
      if self.DEX>=5: costdex=((self.DEX/5)+1)*5
      if self.CON<5:  costcon=5
      if self.CON>=5: costcon=((self.CON/5)+1)*5
      if self.PER<5:  costper=5
      if self.PER>=5: costper=((self.PER/5)+1)*5
      if self.WIL<5:  costwil=5
      if self.WIL>=5: costwil=((self.WIL/5)+1)*5
      if self.CHA<5:  costcha=5
      if self.CHA>=5: costcha=((self.CHA/5)+1)*5

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
    if item.strbonus>0: calcarray.append("+"+str(item.strbonus)+" STR")
    if item.intbonus>0: calcarray.append("+"+str(item.intbonus)+" INT")
    if item.dexbonus>0: calcarray.append("+"+str(item.dexbonus)+" DEX")
    if item.perbonus>0: calcarray.append("+"+str(item.perbonus)+" PER")
    if item.conbonus>0: calcarray.append("+"+str(item.conbonus)+" CON")
    if item.wilbonus>0: calcarray.append("+"+str(item.wilbonus)+" WIL")
    if item.chabonus>0: calcarray.append("+"+str(item.chabonus)+" CHA")
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
      roll=random.randint(1,21)+self.WIL+self.wilboost
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
      nam=item.name

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

    if self.lv==1:
      if self.exp>=5:
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
      print "\nEquipped\n"
      parts=["Head","Face","Neck","Back","Chest","L hand","R hand","Ring","Belt","Legs","Feet"]
      for i,it in enumerate(parts): print "%02i [+%i/+%i] %s:  %s %s" %(i+1,self.equiparr[i].atk,self.equiparr[i].defn,it,self.equiparr[i].name,self.calcbonus(self.equiparr[i]))
      print "\n[+%i/+%i]"                 %(self.totatk,self.totdefn)

      #Print everything in the inventory array
      print "\nInventory (%i G)\n" %(self.pocket)
      for i in range(len(self.inventory)): print "0%i [+%i/+%i] %s (%iG)[%i]" %(i+1,self.inventory[i].atk,self.inventory[i].defn,self.inventory[i].name,self.inventory[i].price,self.inventory[i].type)

      #Print the belt items
      print "\nBelt\n"
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
      if atkpow<=0: atkpow=1
      #Change life and hit variables
      mob.HP-=atkpow
      mob.hit=1
      #Update total hits, total damage and max damage stats
      self.totalhits+=1
      self.totaldmg+=atkpow
      if atkpow>self.maxdmg: self.maxdmg=atkpow

      #Actions if themob has been killed
      if mob.HP<=0:
        #Increase kill stat
        self.kills+=1
        #Add experience to the player
        self.exp+=mob.exp
        #Add prestige only if the player is 3 levels or less over the mob
        if self.lv<=mob.lv+3: self.prestige+=mob.pres
        #Return attack string
        return "You attack %s for %i damage!\nYou killed %s for %i experience!\nYou earn %i prestige points.\n" %(mob.name,atkpow,mob.name,mob.exp,mob.pres)
      else: return "You attack %s for %i damage!\n"%(mob.name,atkpow)
    elif roll<=3:
      return "You try to hit %s, but miss" %(mob.name)

  def save(self):
    """
    Save function. Takes the player attributes and saves them into a text file in ../player/save
    If the path or the file do not exist they are created.
    """

    if not os.path.exists("../player/"): os.makedirs("../player/")
    with open("../player/save","w+") as savefile:
      savefile.write("# \n# Player \n# \n")
      savefile.write("Name:"+str(self.name)+"\n")
      savefile.write("Race:"+self.race+"\n")
      savefile.write("Class:"+self.charclass+"\n")
      savefile.write("Money:"+str(int(self.pocket))+"\n")
      savefile.write("Level:"+str(self.lv)+"\n")
      savefile.write("Exp:"+str(self.exp)+"\n")
      savefile.write("Points:"+str(self.points)+"\n")
      savefile.write("HP:"+str(self.hp2)+"\n")
      savefile.write("MP:"+str(self.mp2)+"\n")
      savefile.write("INT:"+str(self.INT)+"\n")
      savefile.write("DEX:"+str(self.DEX)+"\n")
      savefile.write("PER:"+str(self.PER)+"\n")
      savefile.write("WIL:"+str(self.WIL)+"\n")
      savefile.write("STR:"+str(self.STR)+"\n")
      savefile.write("CON:"+str(self.CON)+"\n")
      savefile.write("CHA:"+str(self.CHA)+"\n")

      savefile.write("#\n# Player stats \n#\n")
      savefile.write("Floors:"+str(self.totalfl)+"\n")
      savefile.write("Steps:"+str(self.steps)+"\n")
      savefile.write("Attacks:"+str(self.totalatks)+"\n")
      savefile.write("Hits:"+str(self.totalhits)+"\n")
      savefile.write("Damage given:"+str(self.totaldmg)+"\n")
      savefile.write("Damage taken:"+str(self.totalrcv)+"\n")
      savefile.write("Kills:"+str(self.kills)+"\n")
      savefile.write("Gold earned:"+str(int(self.totalgld))+"\n")
      savefile.write("Traps:"+str(self.totaltrp)+"\n")
      savefile.write("Items picked:"+str(self.itemspck)+"\n")
      savefile.write("Items erased:"+str(self.itemsdst)+"\n")
      savefile.write("Total enchants:"+str(self.itemsenc)+"\n")
      savefile.write("Potions taken:"+str(self.totalpot)+"\n")
      savefile.write("Items sold:"+str(self.totalsll)+"\n")
      savefile.write("Items bought:"+str(self.totalbuy)+"\n")
      savefile.write("Money spent:"+str(int(self.totalspn))+"\n")
      savefile.write("Max damage:"+str(self.maxdmg)+"\n")
      savefile.write("Max enchant:"+str(self.maxench)+"\n")

      savefile.write("#\n# Equipped items \n#\n")
      for a in self.equiparr: savefile.write("E:"+a.name+":"+str(a.enchantlv)+":"+str(a.type)+":"+str(a.atk)+":"+str(a.defn)+":"+str(a.strbonus)+":"+str(a.intbonus)+":"+str(a.dexbonus)+":"+str(a.perbonus)+":"+str(a.conbonus)+":"+str(a.wilbonus)+":"+str(a.chabonus)+":"+str(a.price)+"\n")
      
      savefile.write("#\n# Inventory items \n#\n")
      for a in self.inventory: savefile.write("I:"+a.name+":"+str(a.enchantlv)+":"+str(a.type)+":"+str(a.atk)+":"+str(a.defn)+":"+str(a.strbonus)+":"+str(a.intbonus)+":"+str(a.dexbonus)+":"+str(a.perbonus)+":"+str(a.conbonus)+":"+str(a.wilbonus)+":"+str(a.chabonus)+":"+str(a.price)+"\n")

      savefile.write("#\n# Belt items \n#\n")
      for a in self.belt:
        if a.type==4: savefile.write("B:"+str(a.type)+":"+a.name+"\n")
        if a.type==0: savefile.write("B:"+str(a.type)+":"+str(a.subtype)+":"+a.name+":"+str(a.hpr)+":"+str(a.mpr)+":"+str(a.price)+"\n")
    return "Player saved"

  def bury(self):
    """
    Saves the character into a cemetery file 

    This file is ../player/cemetery and contains all the player's dead characters.
    Similar to save, except more verbose.

    Unlike save it does not record things like maximum HP, items or stats, so buried characters can NOT be recovered.
    """

    if not os.path.exists("../player/"): os.makedirs("../player/")
    with open("../player/cemetery","a+") as cemetery:
      cemetery.write("RIP "+self.name+", the "+self.race+" "+self.charclass+" ("+str(self.prestige)+" prestige).\n")
      cemetery.write("Died at level "+str(self.lv)+" after exploring "+str(self.totalfl)+" floors.\n")
      cemetery.write("His body rots under "+str(self.pocket)+" gold.\n")
      cemetery.write('"'+raw_input("Your last words?")+'" \n \n')

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

    try:
      with open("../player/save","r") as savefile:
        if not savefile.readline().startswith("No character"):

          #Save current position
          tempx=self.xpos
          tempy=self.ypos
          tempz=self.zpos

          #Reset all the variables to the defaults
          self.reset()

          #Load values from file
          for line in savefile:
            if not line.startswith("#"):
              #Load stats and player details
              parA=line.partition(':')[0]
              parB=line.strip().partition(':')[2]
              if   parA=="Name":          self.name=      parB
              elif parA=="Level":         self.lv=        int(parB)
              elif parA=="Exp":           self.exp=       int(parB)
              elif parA=="Money":         self.pocket=    int(parB)
              elif parA=="INT":           self.INT=       int(parB)
              elif parA=="DEX":           self.DEX=       int(parB)
              elif parA=="PER":           self.PER=       int(parB)
              elif parA=="WIL":           self.WIL=       int(parB)
              elif parA=="STR":           self.STR=       int(parB)
              elif parA=="CON":           self.CON=       int(parB)
              elif parA=="CHA":           self.CHA=       int(parB)
              elif parA=="Race":          self.race=      parB
              elif parA=="Class":         self.charclass= parB
              elif parA=="HP":            self.HP=        int(parB)
              elif parA=="hp2":           self.hp2=       int(parB)
              elif parA=="MP":            self.MP=        int(parB)
              elif parA=="mp2":           self.mp2=       int(parB)
              elif parA=="Points":        self.points=    int(parB)
              elif parA=="Floors":        self.totalfl=   int(parB)
              elif parA=="Steps":         self.steps=     int(parB)
              elif parA=="Attacks":       self.totalatks= int(parB)
              elif parA=="Hits":          self.totalhits= int(parB)
              elif parA=="Damage given":  self.totaldmg=  int(parB)
              elif parA=="Damage taken":  self.totalrcv=  int(parB)
              elif parA=="Kills":         self.kills=     int(parB)
              elif parA=="Gold earned":   self.totalgld=  int(parB)
              elif parA=="Traps":         self.totaltrp=  int(parB)
              elif parA=="Items picked":  self.itemspck=  int(parB)
              elif parA=="Items erased":  self.itemsdst=  int(parB)
              elif parA=="Total enchants":self.itemsenc=  int(parB)
              elif parA=="Potions taken": self.totalpot=  int(parB)
              elif parA=="Items sold":    self.totalsll=  int(parB)
              elif parA=="Itembs bought": self.totalbuy=  int(parB)
              elif parA=="Money spent":   self.totalspn=  int(parB)
              elif parA=="Max damage":    self.maxdmg=    int(parB)
              elif parA=="Max enchant":   self.maxench=   int(parB)

              #Load equipped items
                                                                                                                                                              #E:name:enchantlv:type:atk:defn:strbonus:intbonus:dexbonus:perbonus:conbonus:wilbonus:chabonus:price
              elif line.startswith("E:"):
                if not line.rstrip("\n").partition(':')[2].partition(':')[0]==" ":
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].name=           line.rstrip('\n').partition(':')[2].partition(':')[0]
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].enchantlv=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].type=       int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].atk=        int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].defn=       int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].strbonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].intbonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].dexbonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].perbonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].conbonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].wilbonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].chabonus=   int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  self.equiparr[int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])-1].price=      int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2])

              #Load inventory
              elif line.startswith("I:"):
                temp=item.item(0)

                #E:name:enchantlv:type:atk:defn:strbonus:intbonus:dexbonus:perbonus:conbonus:wilbonus:chabonus:price
                temp.name=          line.rstrip('\n').partition(':')[2].partition(':')[0]
                temp.enchantlv= int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[0])
                temp.type=      int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.atk=       int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.defn=      int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.strbonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.intbonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.dexbonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.perbonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.conbonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.wilbonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.chabonus=  int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                temp.price=     int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2])
                self.inventory.append(copy.copy(temp))

              #Load belt items
              elif line.startswith("B:"):
                line=line.lstrip("B:")
                if line.partition(':')[0]=="4": self.belt.append(item.consumable(4,0))
                if line.partition(':')[0]=="0":
                  temp=item.consumable(0,0)
                  temp.subtype=int(line.partition(':')[2].partition(':')[0])
                  temp.name=line.partition(':')[2].partition(':')[2].partition(':')[0]
                  temp.hpr=int(line.partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  temp.mpr=int(line.partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
                  temp.price=int(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2])
                  self.belt.append(copy.copy(temp))

          #Add empty items to belt until it's full
          while len(self.belt)<3: self.belt.append(item.consumable(4,0))

          #Update player bonuses
          for a in self.equiparr:
            self.strboost+=(a.strbonus)
            self.intboost+=(a.intbonus)
            self.dexboost+=(a.dexbonus)
            self.perboost+=(a.perbonus)
            self.conboost+=(a.conbonus)
            self.wilboost+=(a.wilbonus)
            self.chaboost+=(a.chabonus)
            self.totatk  +=(a.atk)
            self.totdefn +=(a.defn)

          #Restore position values
          self.xpos=tempx
          self.ypos=tempy
          self.zpos=tempz

          return "Player loaded"
        else:return "Save file is empty"
    except IOError: return "Error loading character"