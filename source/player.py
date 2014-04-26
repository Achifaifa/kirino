#usr/bin/env python 
import copy, os, random, sys
import common, dungeon, item

#Player class definition
class player:
  "Player class. Creates and manages player objects"
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
  totalfl=0     #Total floors explored
  prestige=0
  prestigelv=1

  #Attribute and attribute booster variables
  INT=1
  intboost=0
  DEX=1
  dexboost=0
  PER=1
  perboost=0
  WIL=1
  wilboost=0
  STR=1
  strboost=0
  CON=1
  conboost=0
  CHA=1
  chaboost=0

  totatk=0
  totdefn=0

  #Status variables
  HP=0
  hp2=0
  MP=0
  mp2=0
  END=0
  SPD=0
  
  #Position
  xpos=0
  ypos=0
  zpos=0 #0: On the ground; 1: Flying
  
  def __init__(self,dungeon):
    """
    Initialization of the player objects. 

    Receives a dungeon object, then sets the coordinates of the player object in the entrance tile
    It also chooses a random race and class from the ./data/races and ./data/classes files
    """

    #Initialize atributes
    self.name="Test subject"
    self.pocket=0
    self.exp=1
    self.points=45
    self.race="_"
    self.charclass="_"
    self.totalfl=0
    self.prestigelv=0
    self.prestige=0

    #Initializing inventory arrays
    self.inventory=[]
    for i in range(11):
      new=item.item(0)
      self.equiparr.append(new)

    #Set attributes to 1, set secondary attributes
    self.STR=1
    self.INT=1
    self.CON=1
    self.WIL=1
    self.PER=1
    self.DEX=1
    self.CHA=1
    self.secondary()
    self.mp2=self.MP
    self.hp2=self.HP

    #Set attribute boosters to 0
    self.strboost=0
    self.intboost=0
    self.conboost=0
    self.wilboost=0
    self.perboost=0
    self.dexboost=0
    self.chaboost=0

    self.totatk=1
    self.totdefn=1
    
    #Initialize position at the entrance
    for i in range(len(dungeon.dungarray)):
      for j in range(len(dungeon.dungarray[i])):
        if dungeon.dungarray[i][j]=="A":
          self.ypos=i
          self.xpos=j
          self.zpos=0

    #Random race
    with open("../data/player/races","r") as file:
      racesarray=[]
      strarray=[]
      intarray=[]
      dexarray=[]
      perarray=[]
      conarray=[]
      chaarray=[]
      for line in file:
        if not line.startswith('#'):
          racesarray.append(line.rstrip('\n').partition(':')[0])
          strarray.append(line.rstrip('\n').partition(':')[2].partition(':')[0])
          intarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[0])
          dexarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          perarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          conarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          chaarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
    randrac=random.randrange(1,len(racesarray))
    self.race=racesarray[randrac]
    if not strarray[randrac]=="":
      self.STR+=int(strarray[randrac])
    if not strarray[randrac]=="":
      self.INT+=int(intarray[randrac])
    if not strarray[randrac]=="":
      self.DEX+=int(dexarray[randrac])
    if not strarray[randrac]=="":
      self.PER+=int(perarray[randrac])
    if not strarray[randrac]=="":
      self.CON+=int(conarray[randrac])
    if not strarray[randrac]=="":
      self.CHA+=int(chaarray[randrac])

    #Random class
    with open("../data/player/classes","r") as file:
      classesarray=[]
      for line in file:
          classesarray.append(line.rstrip('\n'))
    self.charclass=random.choice(classesarray) 

    #add two random items to the inventory
    for i in range(2):
      self.inventory.append(item.item(random.randint(1,11)))

  def pickobject(self,object):
    """
    Pick item from the floor. 

    This receives an item and adds it to the inventory if the inventory is not full.
    Returns 1 and adds the object to the inventory if the object was correctly picked, returns 0 if it wasn't.
    """
    #If the inventory is not full, it adds it. 
    #If the inventory is full, passes.
    if len(self.inventory)>=9:
      pass
      return 0,("Your inventory is full!\n")
    if len(self.inventory)<9:
      self.inventory.append(object)
      return 1,("You picked "+object.name+"\n")

    
  def getatr(self):
    """
    Prints the player attributes on screen.
    """
    print 'HP: '+str(self.hp2)+"/"+str(self.HP)+", MP: "+str(self.mp2)+"/"+str(self.MP)
    print 'INT: '+str(self.INT)+"+"+str(self.intboost)+'  DEX: '+str(self.DEX)+"+"+str(self.dexboost)
    print 'CON: '+str(self.CON)+"+"+str(self.conboost)+'  STR: '+str(self.STR)+"+"+str(self.strboost)
    print 'WIL: '+str(self.WIL)+"+"+str(self.wilboost)+'  PER: '+str(self.PER)+"+"+str(self.perboost)
    print 'CHA: '+str(self.CHA)+"+"+str(self.chaboost)
    print 'END: '+str(self.END)+'   SPD:', self.SPD    
    
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
    moves=1
    try:
      #Checks de direction and moves
      if direction==1:
        if dungeon.dungarray[self.ypos-1][self.xpos]=="#" or dungeon.dungarray[self.ypos-1][self.xpos]=="|":
          return 0
        if dungeon.filled[self.ypos-1][self.xpos]=="i":
          return 2
        else:
          self.ypos -= moves
          return 1
      elif direction==2:
        if dungeon.dungarray[self.ypos][self.xpos-1]=="#":
          return 0
        if dungeon.filled[self.ypos][self.xpos-1]=="i":
          return 2
        elif dungeon.dungarray[self.ypos][self.xpos-1]=="|":
          dungeon.vendorvar.commerce(self)
        else:
          self.xpos -= moves
          return 1  
      elif direction==3:
        if dungeon.dungarray[self.ypos+1][self.xpos]=="#" or dungeon.dungarray[self.ypos+1][self.xpos]=="|":
          return 0
        if dungeon.filled[self.ypos+1][self.xpos]=="i":
          return 2
        else:     
          self.ypos += moves
          return 1
      elif direction==4:
        if dungeon.dungarray[self.ypos][self.xpos+1]=="#":
          return 0
        if dungeon.filled[self.ypos][self.xpos+1]=="i":
          return 2
        elif dungeon.dungarray[self.ypos][self.xpos+1]=="|":
          dungeon.vendorvar.commerce(self)
        else:
          self.xpos += moves
          return 1
      elif direction==5:
        if dungeon.dungarray[self.ypos-1][self.xpos-1]=="#" or dungeon.dungarray[self.ypos-1][self.xpos-1]=="|":
          return 0
        if dungeon.filled[self.ypos-1][self.xpos-1]=="i":
          return 2
        else:
          self.ypos -= moves
          self.xpos -= moves
          return 1
      elif direction==6:
        if dungeon.dungarray[self.ypos-1][self.xpos+1]=="#" or dungeon.dungarray[self.ypos-1][self.xpos+1]=="|":
          return 0
        if dungeon.filled[self.ypos-1][self.xpos+1]=="i":
          return 2
        else:
          self.ypos -= moves
          self.xpos += moves
          return 1
      elif direction==7:
        if dungeon.dungarray[self.ypos+1][self.xpos-1]=="#" or dungeon.dungarray[self.ypos+1][self.xpos-1]=="|":
          return 0
        if dungeon.filled[self.ypos+1][self.xpos-1]=="i":
          return 2
        else:
          self.ypos += moves
          self.xpos -= moves
          return 1
      elif direction==8:
        if dungeon.dungarray[self.ypos+1][self.xpos+1]=="#" or dungeon.dungarray[self.ypos+1][self.xpos+1]=="|":
          return 0
        if dungeon.filled[self.ypos+1][self.xpos+1]=="i":
          return 2
        else:
          self.ypos += moves
          self.xpos += moves
          return 1
      else:
        return 0
    except IndexError:
      return 0

  def secondary(self):
    """
    Calculates and sets the secondary attributes from the primary ones.
 
    Receives a player object and recalculates HP, MP, END and SPD from the primary attributes. 
    It also adds the extra HP and MP gained.
    """

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
      os.system('clear')
      common.version()
      print self.name,"- Character sheet"
      print "_____________________"
      print "Level "+str(self.lv)+" "+self.race+" "+self.charclass
      if self.lv==1:
        print str(self.exp)+"/5 xp,",self.points,"points"
      if self.lv>1:
        print str(self.exp)+"/"+str(3*self.lv+(2*(self.lv-1))),"xp,",self.points,"points"
      print str(self.totalfl)+" floors explored"
      print ""
      self.getatr()
      print "_____________________"
      print ""
      print "1.- Spend points"
      print "2.- Inventory"
      print "3.- Character options"
      print "4.- Save"
      print "5.- Load"
      print ""
      print "0.- Exit"
      print "->",
      menu=common.getch()
      #Spend exp
      if menu=="1":
        self.spend()
      #Inventory menu
      elif menu=="2":
        self.invmenu()
      #Character options menu
      elif menu=="3":
        self.optmenu()
      #Save
      elif menu=="4":
        print "saving..."
        self.save()
        raw_input("Player saved")
      #Load
      elif menu=="5":
        print "loading..."
        self.load()
        raw_input("Player loaded")
      #Exit
      elif menu=="0":
        break
      pass

  def spend(self):
    """
    Point spending menu.
    """
    choice=-1
    while choice!="0": 
      os.system('clear')
      common.version()
      print self.name,"- Character sheet"
      print ""
      print "Spend points"
      if self.points==0:
        print "No points left!"
        print ""
      else:
        print self.points,"points left"
        print ""

      #Determining cost of improving attributes (Based on AFMBE rules, sort of)  
      if self.STR<5:
        coststr=5
      if self.STR>=5:
        coststr=((self.STR/5)+1)*5
      if self.INT<5:
        costint=5
      if self.INT>=5:
        costint=((self.INT/5)+1)*5
      if self.DEX<5:
        costdex=5
      if self.DEX>=5:
        costdex=((self.DEX/5)+1)*5
      if self.CON<5:
        costcon=5
      if self.CON>=5:
        costcon=((self.CON/5)+1)*5
      if self.PER<5:
        costper=5
      if self.PER>=5:
        costper=((self.PER/5)+1)*5
      if self.WIL<5:
        costwil=5
      if self.WIL>=5:
        costwil=((self.WIL/5)+1)*5
      if self.CHA<5:
        costcha=5
      if self.CHA>=5:
        costcha=((self.CHA/5)+1)*5

      #printing menu
      print "1.- ["+str(coststr)+"] STR "+str(self.STR)+" (+"+str(self.strboost)+")"
      print "2.- ["+str(costint)+"] INT "+str(self.INT)+" (+"+str(self.intboost)+")"
      print "3.- ["+str(costdex)+"] DEX "+str(self.DEX)+" (+"+str(self.dexboost)+")"
      print "4.- ["+str(costcon)+"] CON "+str(self.CON)+" (+"+str(self.conboost)+")"
      print "5.- ["+str(costper)+"] PER "+str(self.PER)+" (+"+str(self.perboost)+")"
      print "6.- ["+str(costwil)+"] WIL "+str(self.WIL)+" (+"+str(self.wilboost)+")"
      print "7.- ["+str(costcha)+"] CHA "+str(self.CHA)+" (+"+str(self.chaboost)+")"
      print ""
      print "Secondary attributes:"
      print 'END:', self.END, '     SPD:', self.SPD
      print 'Max. HP:',self.HP
      print 'Max. MP:',self.MP
      print "---"
      print "0.- Exit"
      print ""
      print "->",
      choice=common.getch()

      #Choice cases
      if self.points==0:
        pass
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
        elif choice=="0":
          pass
        else:
          pass

  def optmenu(self):
    """
    Player options menu
    """
    coptmen=-1
    while coptmen!="0": 
      os.system('clear')
      common.version()
      print self.name,"- Character sheet"
      print ""
      print "1.- Change name"
      print "---"
      print "0.- Back"
      print "->",
      coptmen=common.getch()
      if coptmen=="1":
        self.name=raw_input("New name? ")
      if coptmen=="0":
        break

  def calcbonus(self,item):
    """
    Generates the string with the attribute boosts for the inventory
    """
    calcarray=[]
    if item.strbonus>0:
      calcarray.append("+"+str(item.strbonus)+" STR")
    if item.intbonus>0:
      calcarray.append("+"+str(item.intbonus)+" INT")
    if item.dexbonus>0:
      calcarray.append("+"+str(item.dexbonus)+" DEX")
    if item.perbonus>0:
      calcarray.append("+"+str(item.perbonus)+" PER")
    if item.conbonus>0:
      calcarray.append("+"+str(item.conbonus)+" CON")
    if item.wilbonus>0:
      calcarray.append("+"+str(item.wilbonus)+" WIL")
    if item.chabonus>0:
      calcarray.append("+"+str(item.chabonus)+" CHA")
    if len(calcarray)>0:
      return "("+(', '.join(map(str,calcarray)))+")"
    if len(calcarray)==0:
      return ""


  def invmenu(self):
    """
    Inventory menu. 
    """

    while 1: 
      os.system('clear')
      common.version()
      print self.name,"- Character sheet"
      print ""
      print "Equipped"
      print ""
      bonusmsg=self.calcbonus(self.equiparr[0])
      print "01 [+"+str(self.equiparr[0].atk)+"/+"+str(self.equiparr[0].defn)+"] Head: "+self.equiparr[0].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[1])
      print "02 [+"+str(self.equiparr[1].atk)+"/+"+str(self.equiparr[1].defn)+"] Face: "+self.equiparr[1].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[2])
      print "03 [+"+str(self.equiparr[2].atk)+"/+"+str(self.equiparr[2].defn)+"] Neck: "+self.equiparr[2].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[3])
      print "04 [+"+str(self.equiparr[3].atk)+"/+"+str(self.equiparr[3].defn)+"] Shoulders: "+self.equiparr[3].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[4])
      print "05 [+"+str(self.equiparr[4].atk)+"/+"+str(self.equiparr[4].defn)+"] Chest: "+self.equiparr[4].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[5])
      print "06 [+"+str(self.equiparr[5].atk)+"/+"+str(self.equiparr[5].defn)+"] Left hand: "+self.equiparr[5].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[6])
      print "07 [+"+str(self.equiparr[6].atk)+"/+"+str(self.equiparr[6].defn)+"] Right hand: "+self.equiparr[6].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[7])
      print "08 [+"+str(self.equiparr[7].atk)+"/+"+str(self.equiparr[7].defn)+"] Ring: "+self.equiparr[7].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[8])
      print "09 [+"+str(self.equiparr[8].atk)+"/+"+str(self.equiparr[8].defn)+"] Belt: "+self.equiparr[8].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[9])
      print "10 [+"+str(self.equiparr[9].atk)+"/+"+str(self.equiparr[9].defn)+"] Legs: "+self.equiparr[9].name+bonusmsg
      bonusmsg=self.calcbonus(self.equiparr[10])
      print "11 [+"+str(self.equiparr[10].atk)+"/+"+str(self.equiparr[10].defn)+"] Feet: "+self.equiparr[10].name+bonusmsg
      print ""
      print "[+"+str(self.totatk)+"/+"+str(self.totdefn)+"]"
      print ""
      print "Inventory (+"+str(self.pocket)+" G)"
      print ""

      #Print everything in the inventory array
      for i in range(len(self.inventory)):
        print "0"+str(i+1)+" [+"+str(self.inventory[i].atk)+"/+"+str(self.inventory[i].defn)+"] "+self.inventory[i].name+" ("+str(self.inventory[i].price)+"G)" 

      print ""
      print "q - destroy item"
      print "w - enchant item"
      print "a - unequip item"
      print "0 - Back"
      print ""
      print "->",
      invmenu=common.getch()

      #Item flipping (Inventory <-> Equip)
      if "0"<invmenu<=str(len(self.inventory)):
        invmenu=int(invmenu)        
        if len(self.inventory)>=invmenu:
          if not self.equiparr[self.inventory[invmenu-1].type-1].name==" ":
            temp=self.equiparr[self.inventory[invmenu-1].type-1]
            self.strboost-=self.equiparr[self.inventory[invmenu-1].type-1].strbonus
            self.intboost-=self.equiparr[self.inventory[invmenu-1].type-1].intbonus
            self.conboost-=self.equiparr[self.inventory[invmenu-1].type-1].conbonus
            self.wilboost-=self.equiparr[self.inventory[invmenu-1].type-1].wilbonus
            self.perboost-=self.equiparr[self.inventory[invmenu-1].type-1].perbonus
            self.dexboost-=self.equiparr[self.inventory[invmenu-1].type-1].dexbonus
            self.chaboost-=self.equiparr[self.inventory[invmenu-1].type-1].chabonus
            self.totatk-=self.equiparr[self.inventory[invmenu-1].type-1].atk
            self.totdefn-=self.equiparr[self.inventory[invmenu-1].type-1].defn
          else:
            temp=item.item(0)
          self.inventory[invmenu-1].equip=1
          temp.equip=0
          self.strboost+=self.inventory[invmenu-1].strbonus
          self.intboost+=self.inventory[invmenu-1].intbonus
          self.conboost+=self.inventory[invmenu-1].conbonus
          self.wilboost+=self.inventory[invmenu-1].wilbonus
          self.perboost+=self.inventory[invmenu-1].perbonus
          self.dexboost+=self.inventory[invmenu-1].dexbonus
          self.chaboost+=self.inventory[invmenu-1].chabonus
          self.totatk+=self.inventory[invmenu-1].atk
          self.totdefn+=self.inventory[invmenu-1].defn
          self.equiparr[self.inventory[invmenu-1].type-1]=self.inventory[invmenu-1]
          del self.inventory[invmenu-1]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name==" ":
            del self.inventory[len(self.inventory)-1]

      #Destroy an item from inventory
      if invmenu=="q":
        print "Which item? "
        itdst=common.getch()
        if "0"<itdst<=str(len(self.inventory)):
          itemdestroyed=self.inventory[int(itdst)-1].name
          print "Destroy "+itemdestroyed+"? (y/n)"
          confirm=common.getch()
          if confirm=="y":
            del self.inventory[int(itdst)-1]
            raw_input(itemdestroyed+" destroyed")

      #Enchanting menu
      if invmenu=="w":
        try:
          print "Which item? "
          itech=int(common.getch())
          if 0<itech<=len(self.inventory):
            self.inventory[int(itech)-1].enchant(self)
            if self.inventory[int(itech)-1].name==" ":
              del self.inventory[int(itech)-1]
        except ValueError:
          pass

      #Unequip menu
      if invmenu=="a":
        try:
          unitem=int(raw_input("which item? "))
          if 0<int(unitem)<=len(self.equiparr) and self.equiparr[int(unitem)-1].name!=" ":
            temp=copy.copy(self.equiparr[int(unitem)-1])
            self.strboost-=self.equiparr[int(unitem)-1].strbonus
            self.intboost-=self.equiparr[int(unitem)-1].intbonus
            self.conboost-=self.equiparr[int(unitem)-1].conbonus
            self.wilboost-=self.equiparr[int(unitem)-1].wilbonus
            self.perboost-=self.equiparr[int(unitem)-1].perbonus
            self.dexboost-=self.equiparr[int(unitem)-1].dexbonus
            self.chaboost-=self.equiparr[int(unitem)-1].chabonus
            self.totatk-=self.equiparr[int(unitem)-1].atk
            self.totdefn-=self.equiparr[int(unitem)-1].defn
            self.inventory.append(temp)
            self.equiparr[int(unitem)-1].reset()
        except ValueError:
          print "Invalid choice"

      #Exit from inventory menu
      elif invmenu=="0":
        break

  def attack(self,mob):
    """
    attacks the mob object specified

    Returns a string to be displayed in the crawl screen
    """
    atkpow=(self.totatk*self.STR)-mob.defn
    if atkpow<=0:
      atkpow=1
    mob.HP-=atkpow
    mob.hit=1
    if mob.HP<=0:
      self.exp+=mob.exp
      return "You attack "+mob.name+" for "+str(atkpow)+" damage!\nYou killed "+mob.name+" for "+str(mob.exp)+" experience!"
    else:
      return "You attack "+mob.name+" for "+str(atkpow)+" damage!\n"

  def save(self):
    """
    Save function. Takes the player attributes and saves them into a text file in ../player/save
    If the path or the file do not exist they are created.
    """
    if not os.path.exists("../player/"):
      os.makedirs("../player/")
    with open("../player/save","w+") as savefile:
      savefile.write("# \n# Player \n# \n")
      savefile.write("Name:"+str(self.name)+"\n")
      savefile.write("Race:"+self.race+"\n")
      savefile.write("Class:"+self.charclass+"\n")
      savefile.write("Money:"+str(self.pocket)+"\n")
      savefile.write("Level:"+str(self.lv)+"\n")
      savefile.write("Exp:"+str(self.exp)+"\n")
      savefile.write("Points:"+str(self.points)+"\n")
      savefile.write("Floors:"+str(self.totalfl)+"\n")
      savefile.write("HP:"+str(self.hp2)+"\n")
      savefile.write("MP:"+str(self.mp2)+"\n")
      savefile.write("INT:"+str(self.INT)+"\n")
      savefile.write("DEX:"+str(self.DEX)+"\n")
      savefile.write("PER:"+str(self.PER)+"\n")
      savefile.write("WIL:"+str(self.WIL)+"\n")
      savefile.write("STR:"+str(self.STR)+"\n")
      savefile.write("CON:"+str(self.CON)+"\n")
      savefile.write("CHA:"+str(self.CHA)+"\n")
      savefile.write("# \n# Equipped items \n# \n")
      for a in self.equiparr:
        savefile.write("E:"+a.name+":"+str(a.enchantlv)+":"+str(a.type)+":"+str(a.atk)+":"+str(a.defn)+":"+str(a.strbonus)+":"+str(a.intbonus)+":"+str(a.dexbonus)+":"+str(a.perbonus)+":"+str(a.conbonus)+":"+str(a.wilbonus)+":"+str(a.chabonus)+":"+str(a.price)+"\n")
      savefile.write("# \n# Inventory items \n# \n")
      for a in self.inventory:
        savefile.write("I:"+a.name+":"+str(a.enchantlv)+":"+str(a.type)+":"+str(a.atk)+":"+str(a.defn)+":"+str(a.strbonus)+":"+str(a.intbonus)+":"+str(a.dexbonus)+":"+str(a.perbonus)+":"+str(a.conbonus)+":"+str(a.wilbonus)+":"+str(a.chabonus)+":"+str(a.price)+"\n")
    pass

  def bury(self):
    """
    Saves the character into a cemetery file 

    This file is ../player/cemetery and contains all the player's dead characters.
    Similar to save, except more verbose.

    Unlike save it does not record things like maximum HP, items or stats, so buried characters can NOT be recovered.
    """
    if not os.path.exists("../player/"):
      os.makedirs("../player/")
    with open("../player/cemetery","a+") as cemetery:
      cemetery.write("RIP "+self.name+", the "+self.race+" "+self.charclass+".\n")
      cemetery.write("Died at level "+str(self.lv)+" after exploring "+str(self.totalfl)+" floors.\n")
      cemetery.write("His body rots under "+str(self.pocket)+" gold.\n")
      cemetery.write('"'+raw_input("Your last words?")+'" \n \n')

  def reset(self):
    self.name="_"    
    self.pocket=0      
    self.exp=0
    self.lv=1
    self.points=0      
    self.race="_"
    self.charclass="_"
    self.inventory=[] 
    for i in range(11):
      new=item.item(0)
      self.equiparr.append(new)
    self.totalfl=0    
    self.prestige=0
    self.prestigelv=1

    self.INT=1
    self.intboost=0
    self.DEX=1
    self.dexboost=0
    self.PER=1
    self.perboost=0
    self.WIL=1
    self.wilboost=0
    self.STR=1
    self.strboost=0
    self.CON=1
    self.conboost=0
    self.CHA=1
    self.chaboost=0

    self.totatk=0
    self.totdefn=0

    self.HP=0
    self.hp2=0
    self.MP=0
    self.mp2=0
    self.END=0
    self.SPD=0
    
    self.xpos=0
    self.ypos=0
    self.zpos=0

  def load(self):
    """
    Takes the information from the save file stored in ../player/save and loads it into the player object.
    """

    #Save current position
    tempx=self.xpos
    tempy=self.ypos
    tempz=self.zpos

    #Reset all the variables
    self.reset()

    #Load values from file
    try:
      with open("../player/save","r") as savefile:
        for line in savefile:
          if not line.startswith("#"):
            #Load stats and player details
            if line.partition(':')[0]=="Name":
              self.name=(line.partition(':')[2]).strip()
            if line.partition(':')[0]=="Level":
              self.lv=int(line.partition(':')[2])
            if line.partition(':')[0]=="Exp":
              self.exp=int(line.partition(':')[2])
            if line.partition(':')[0]=="Money":
              self.pocket=int(line.partition(':')[2])
            if line.partition(':')[0]=="INT":
              self.INT=int(line.partition(':')[2])
            if line.partition(':')[0]=="DEX":
              self.DEX=int(line.partition(':')[2])
            if line.partition(':')[0]=="PER":
              self.PER=int(line.partition(':')[2])
            if line.partition(':')[0]=="WIL":
              self.WIL=int(line.partition(':')[2])
            if line.partition(':')[0]=="STR":
              self.STR=int(line.partition(':')[2])
            if line.partition(':')[0]=="CON":
              self.CON=int(line.partition(':')[2])
            if line.partition(':')[0]=="CHA":
              self.CHA=int(line.partition(':')[2])
            if line.partition(':')[0]=="Race":
              self.race=(line.partition(':')[2]).strip()
            if line.partition(':')[0]=="Class":
              self.charclass=(line.partition(':')[2]).strip()
            if line.partition(':')[0]=="HP":
              self.HP=int(line.partition(':')[2])
            if line.partition(':')[0]=="hp2":
              self.hp2=int(line.partition(':')[2])
            if line.partition(':')[0]=="MP":
              self.MP=int(line.partition(':')[2])
            if line.partition(':')[0]=="mp2":
              self.mp2=int(line.partition(':')[2])
            if line.partition(':')[0]=="Points":
              self.points=int(line.partition(':')[2])
            if line.partition(':')[0]=="Floors":
              self.totalfl=int(line.partition(':')[2])

            #Load equipped items
                                                                                                                                                            #E:name:enchantlv:type:atk:defn:strbonus:intbonus:dexbonus:perbonus:conbonus:wilbonus:chabonus:price
            if line.startswith("E:"):
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
            if line.startswith("I:"):
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
    except IOError:
      raw_input("Error loading character")

    #Update player bonuses
    for a in self.equiparr:
      self.strboost+=(a.strbonus)
      self.intboost+=(a.intbonus)
      self.dexboost+=(a.dexbonus)
      self.perboost+=(a.perbonus)
      self.conboost+=(a.conbonus)
      self.wilboost+=(a.wilbonus)
      self.chaboost+=(a.chabonus)
      self.totatk+=(a.atk)
      self.totdefn+=(a.defn)

    #Restore position values
    self.xpos=tempx
    self.ypos=tempy
    self.zpos=tempz