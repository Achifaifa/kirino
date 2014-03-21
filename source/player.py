#usr/bin/env python 
import os
import copy
import random
import dungeon
import item
import common

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
    for i in range(7):
      self.inventory.append(item.item(random.randint(1,11)))

  def pickobject(self,object):
    """
    Pick item. This receives an item and adds it to the inventory if the inventory is not full/
    Returns 1 if the object was correctly picked, returns 0 if it wasn't
    """
    #If the inventory is not full, it adds it. 
    #If the inventory is full, passes.
    if len(self.inventory)>=9:
      pass
      return 0
    if len(self.inventory)<9:
      self.inventory.append(object)
      return 1
    
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
    Move function. Receives a dungeon object to check for obstacles and an integer [1,4] indicating the direction
      1 north
      2 west
      3 south
      4 east
      5 northwest
      6 northeast
      7 southwest
      8 southeast
    """
    #This gives 1 base move and 1 extra move for every 10 SPD
    moves=1
    # moves+=self.SPD/10 #disabled because of bugs
    try:
      #Checks de direction and moves
      if direction==1:
        if dungeon.dungarray[self.ypos-1][self.xpos]=="#":
          pass
        else:
          self.ypos -= moves
      elif direction==2:
        if dungeon.dungarray[self.ypos][self.xpos-1]=="#":
          pass
        else:
          self.xpos -= moves  
      elif direction==3:
        if dungeon.dungarray[self.ypos+1][self.xpos]=="#":
          pass
        else:     
          self.ypos += moves
      elif direction==4:
        if dungeon.dungarray[self.ypos][self.xpos+1]=="#":
          pass
        else:
          self.xpos += moves
      elif direction==5:
        if dungeon.dungarray[self.ypos-1][self.xpos-1]=="#":
          pass
        else:
          self.ypos -= moves
          self.xpos -= moves
      elif direction==6:
        if dungeon.dungarray[self.ypos-1][self.xpos+1]=="#":
          pass
        else:
          self.ypos -= moves
          self.xpos += moves
      elif direction==7:
        if dungeon.dungarray[self.ypos+1][self.xpos-1]=="#":
          pass
        else:
          self.ypos += moves
          self.xpos -= moves
      elif direction==8:
        if dungeon.dungarray[self.ypos+1][self.xpos+1]=="#":
          pass
        else:
          self.ypos += moves
          self.xpos += moves
      else:
        pass
    except indexError:
      pass

  def secondary(self):
    """
    Calculates and sets the secondary attributes from the primary ones.
    Receives a player object and recalculates HP, MP, END and SPD from the primary attributes
    """
    self.HP=((self.CON+self.conboost+self.STR+self.strboost)*4)+10
    self.MP=(self.STR+self.strboost+self.DEX+self.dexboost+self.INT+self.intboost+self.CON+self.conboost+self.WIL+self.wilboost+self.PER+self.perboost)
    self.END=((self.CON+self.conboost+self.STR+self.strboost+self.wilboost+self.WIL)*3)+5
    self.SPD=(self.CON+self.conboost+self.DEX+self.dexboost)*3

  def charsheet(self):
    """
    Character sheet. 
    Main menu to edit, view and configure characters and player options
    """
    menu=0
    while 1==1:
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
      print "01 [+"+str(self.equiparr[0].atk)+"/+"+str(self.equiparr[0].defn)+"] Head: "+self.equiparr[0].name
      print "02 [+"+str(self.equiparr[1].atk)+"/+"+str(self.equiparr[1].defn)+"] Face: "+self.equiparr[1].name
      print "03 [+"+str(self.equiparr[2].atk)+"/+"+str(self.equiparr[2].defn)+"] Neck: "+self.equiparr[2].name
      print "04 [+"+str(self.equiparr[3].atk)+"/+"+str(self.equiparr[3].defn)+"] Shoulders: "+self.equiparr[3].name
      print "05 [+"+str(self.equiparr[4].atk)+"/+"+str(self.equiparr[4].defn)+"] Chest: "+self.equiparr[4].name
      print "06 [+"+str(self.equiparr[5].atk)+"/+"+str(self.equiparr[5].defn)+"] Left hand: "+self.equiparr[5].name
      print "07 [+"+str(self.equiparr[6].atk)+"/+"+str(self.equiparr[6].defn)+"] Right hand: "+self.equiparr[6].name
      print "08 [+"+str(self.equiparr[7].atk)+"/+"+str(self.equiparr[7].defn)+"] Ring: "+self.equiparr[7].name
      print "09 [+"+str(self.equiparr[8].atk)+"/+"+str(self.equiparr[8].defn)+"] Belt: "+self.equiparr[8].name
      print "10 [+"+str(self.equiparr[9].atk)+"/+"+str(self.equiparr[9].defn)+"] Legs: "+self.equiparr[9].name
      print "11 [+"+str(self.equiparr[10].atk)+"/+"+str(self.equiparr[10].defn)+"] Feet: "+self.equiparr[10].name
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
          if not self.equiparr[self.inventory[invmenu-1].type-1].name=="":
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
          if self.inventory[len(self.inventory)-1].name=="":
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
        print "Which item? "
        itech=common.getch()
        if "0"<itech<=str(len(self.inventory)):
          self.inventory[int(itech)-1].enchant(self)
          if self.inventory[int(itech)-1].name=="":
            del self.inventory[int(itech)-1]

      #Unequip menu
      if invmenu=="a":
        try:
          unitem=int(raw_input("which item? "))
          if 0<int(unitem)<=len(self.equiparr) and self.equiparr[int(unitem)-1].name!="":
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

  def attack(self,dir):
    """
    attacks the mob object specified
    """
    atkpow=(self.totatk*self.str)-mob.defn
    if atkpow<0:
      atkpow=0
    mob.HP-=atkpow

  def save(self):
    """
    Save function. Takes the player attributes and saves them into a text file in ../player/save
    If the path or the file do not exists they are created.
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
      savefile.write("HP:"+str(self.hp2)+"\n")
      savefile.write("MP:"+str(self.mp2)+"\n")
      savefile.write("INT:"+str(self.INT)+"\n")
      savefile.write("DEX:"+str(self.DEX)+"\n")
      savefile.write("PER:"+str(self.PER)+"\n")
      savefile.write("WIL:"+str(self.WIL)+"\n")
      savefile.write("STR:"+str(self.STR)+"\n")
      savefile.write("CON:"+str(self.CON)+"\n")
      savefile.write("CHA:"+str(self.CHA)+"\n")
      savefile.write("# \n# Inventory \n# \n")

    pass

  def load(self):
    """
    Takes the information from the save file stored in ../player/save and loads it into the player object.
    If the path does not exist it is created. 
    """

    if not os.path.exists("../player/"):
      os.makedirs("../player/")
    with open("../player/save","r") as savefile:
      for line in savefile:
        if not line.startswith("#"):
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
            self.hp2=int(line.partition(':')[2])
          if line.partition(':')[0]=="MP":
            self.mp2=int(line.partition(':')[2])
          if line.partition(':')[0]=="Points":
            self.points=int(line.partition(':')[2])