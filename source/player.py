#usr/bin/env python 
import os
import random
import dungeon
import item

#Player class definition
class player:
  "Player class. Creates and manages player objects"
  #Main characteristics
  name="_" #Name
  pocket=0    #Money
  exp=0       #EXP
  lv=1        #Level
  points=0    #Expendable points
  race="_"
  charclass="_"
  inventory=[]  #10 slot inventory
  equiparr=[]   #Equipped item inventory

  #Attribute variables
  INT=1
  DEX=1
  PER=1
  WIL=1
  STR=1
  CON=1
  CHA=1

  #Status variables
  HP=0
  hp2=0
  MP=0
  mp2=0
  END=0
  SPD=0
  
  #Position
  xPos=0
  yPos=0
  zPos=0 #0: On the ground; 1: Flying
  

  #Initialization of the player objects. 
  #Receives a dungeon object, then sets the coordinates of the player object in the entrance tile
  #It also chooses a random race and class from the ./data/races and ./data/classes files
  def __init__(self,dungeon):
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

    #add a one hand weapon to the inventory
    for i in range(2):
      self.inventory.append(item.item(random.randint(1,11)))

  #Pick item. This receives an item and adds it to the inventory if the inventory is not full
  def pickobject(self,object):

    #Counts item in inventory
    invcounter=0
    for i in range(len(self.inventory)):
      invcounter+=1

    #If the inventory is not full, it adds it. 
    #If the inventory is full, passes.
    if invcounter>10:
      pass
    if invcounter<10:
      self.inventory.append(item)
    
  #Test function. Prints attributes.
  def getatr(self):
    print 'HP:',self.hp2,"/",self.HP
    print 'MP:',self.mp2,"/",self.MP
    print 'INT:',self.INT,'DEX:',self.DEX,'CON:',self.CON
    print 'WIL:',self.WIL,'STR:',self.STR,'PER:',self.PER
    print 'CHA:',self.CHA
    print 'END:',self.END,'SPD:', self.SPD    
    
  #Move function. Accepts strings with direction(n, w, s, e) and an integer with the distance
  def move(self,dungeon,direction):
    #This gives 1 base move and 1 extra move for every 10 SPD
    moves=1
    # moves+=self.SPD/10 #disabled because of bugs

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
    else:
      pass

  #Define secondary attributes from the primary ones.
  #Receiver a player object and recalculates HP, MP, END and SPD from the primary attributes
  def secondary(self):
    self.HP=((self.CON+self.STR)*4)+10
    self.MP=(self.STR+self.DEX+self.INT+self.CON+self.WIL+self.PER)
    self.END=((self.CON+self.STR+self.WIL)*3)+5
    self.SPD=(self.CON+self.DEX)*3

  #Character sheet. Character managing and modifying menu. 
  def charsheet(self):
    menu=0
    while 1==1:
      self.secondary()
      os.system('clear')
      print "Kirino test"
      print self.name,"- Character sheet"
      print "_____________________"
      print "Level "+str(self.lv)+" "+self.race+" "+self.charclass
      if self.lv==1:
        print self.exp,"/ 5 xp",self.points,"points"
      if self.lv>1:
        print self.exp,"/",3*self.lv+(2*(self.lv-1)),"xp,",self.points,"points"
      print int(self.pocket),"gold"
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
      menu=raw_input("->")
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
        self.save()
      #Load
      elif menu=="5":
        self.load()
      elif menu=="0":
        break
      pass

  #Experience spending menu
  def spend(self):
    choice=-1
    while choice!="0":
      os.system('clear')
      print "Kirino test"
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
      print "1.-",[coststr],"STR",(self.STR)
      print "2.-",[costint],"INT",(self.INT)
      print "3.-",[costdex],"DEX",(self.DEX)
      print "4.-",[costcon],"CON",(self.CON)
      print "5.-",[costper],"PER",(self.PER)
      print "6.-",[costwil],"WIL",(self.WIL)
      print "7.-",[costcha],"CHA",(self.CHA)
      print ""
      print "Secondary attributes:"
      print 'END:', self.END, '     SPD:', self.SPD
      print 'Max. HP:',self.HP
      print 'Max. MP:',self.MP
      print "---"
      print "0.- Exit"
      print ""
      choice=raw_input("->")

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

  #Player options menu
  def optmenu(self):
    coptmen=-1
    while coptmen!="0":
      os.system('clear')
      print "Kirino test"
      print self.name,"- Character sheet"
      print ""
      print "1.- Change name"
      print "---"
      print "0.- Back"
      coptmen=raw_input("->")
      if coptmen=="1":
        self.name=raw_input("New name? ")
      if coptmen=="0":
        break

  #Inventory menu
  def invmenu(self):
    while 1:
      os.system('clear')
      print "Kirino test"
      print self.name,"- Character sheet"
      print ""
      print "Equipped"
      print ""
      print "[+"+str(self.equiparr[0].atk)+"/+"+str(self.equiparr[0].defn)+"]Head: "+self.equiparr[0].name
      print "[+"+str(self.equiparr[1].atk)+"/+"+str(self.equiparr[1].defn)+"]Face: "+self.equiparr[1].name
      print "[+"+str(self.equiparr[2].atk)+"/+"+str(self.equiparr[2].defn)+"]Neck: "+self.equiparr[2].name
      print "[+"+str(self.equiparr[3].atk)+"/+"+str(self.equiparr[3].defn)+"]Shoulders: "+self.equiparr[3].name
      print "[+"+str(self.equiparr[4].atk)+"/+"+str(self.equiparr[4].defn)+"]Chest: "+self.equiparr[4].name
      print "[+"+str(self.equiparr[5].atk)+"/+"+str(self.equiparr[5].defn)+"]Left hand: "+self.equiparr[5].name
      print "[+"+str(self.equiparr[6].atk)+"/+"+str(self.equiparr[6].defn)+"]Right hand: "+self.equiparr[6].name
      print "[+"+str(self.equiparr[7].atk)+"/+"+str(self.equiparr[7].defn)+"]Ring: "+self.equiparr[7].name
      print "[+"+str(self.equiparr[8].atk)+"/+"+str(self.equiparr[8].defn)+"]Belt: "+self.equiparr[8].name
      print "[+"+str(self.equiparr[9].atk)+"/+"+str(self.equiparr[9].defn)+"]Legs: "+self.equiparr[9].name
      print "[+"+str(self.equiparr[10].atk)+"/+"+str(self.equiparr[10].defn)+"]Feet: "+self.equiparr[10].name
      print ""
      totatk=0
      totdefn=0
      for i in range(len(self.equiparr)):
        totatk+=self.equiparr[i].atk
        totdefn+=self.equiparr[i].defn
      print "[+"+str(totatk)+"/+"+str(totdefn)+"]"
      print ""
      print "Inventory"
      print ""

      #Print everything in the inventory array
      for i in range(len(self.inventory)):
        if self.inventory[i].equip==0:
          print i+1,"-",self.inventory[i].name

      print ""
      print "0.- Back"
      print ""
      invmenu=raw_input("-> ")

      temp=0
      #Item flipping (Inventory <-> Equip)
      if invmenu=="1":
        if len(self.inventory)>0:
          if not self.equiparr[self.inventory[0].type-1].name=="":
            temp=self.equiparr[self.inventory[0].type-1]
          else:
            temp=item.item(0)
          self.inventory[0].equip=1
          temp.equip=0
          self.equiparr[self.inventory[0].type-1]=self.inventory[0]
          del self.inventory[0]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="2":
        if len(self.inventory)>1:
          if not self.equiparr[self.inventory[1].type-1].name=="":
            temp=self.equiparr[self.inventory[1].type-1]
          else:
            temp=item.item(0)
          self.inventory[1].equip=1
          temp.equip=0
          self.equiparr[self.inventory[1].type-1]=self.inventory[1]
          del self.inventory[1]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="3":
        if len(self.inventory)>2:
          if not self.equiparr[self.inventory[2].type-1].name=="":
            temp=self.equiparr[self.inventory[2].type-1]
          else:
            temp=item.item(0)
          self.inventory[2].equip=1
          temp.equip=0
          self.equiparr[self.inventory[2].type-1]=self.inventory[2]
          del self.inventory[2]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="4":
        if len(self.inventory)>3:
          if not self.equiparr[self.inventory[3].type-1].name=="":
            temp=self.equiparr[self.inventory[3].type-1]
          else:
            temp=item.item(0)
          self.inventory[3].equip=1
          temp.equip=0
          self.equiparr[self.inventory[3].type-1]=self.inventory[3]
          del self.inventory[3]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="5":
        if len(self.inventory)>4:
          if not self.equiparr[self.inventory[4].type-1].name=="":
            temp=self.equiparr[self.inventory[4].type-1]
          else:
            temp=item.item(0)
          self.inventory[4].equip=1
          temp.equip=0
          self.equiparr[self.inventory[4].type-1]=self.inventory[4]
          del self.inventory[4]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="6":
        if len(self.inventory)>5:
          if not self.equiparr[self.inventory[5].type-1].name=="":
            temp=self.equiparr[self.inventory[5].type-1]
          else:
            temp=item.item(0)
          self.inventory[5].equip=1
          temp.equip=0
          self.equiparr[self.inventory[5].type-1]=self.inventory[5]
          del self.inventory[5]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="7":
        if len(self.inventory)>6:
          if not self.equiparr[self.inventory[6].type-1].name=="":
            temp=self.equiparr[self.inventory[6].type-1]
          else:
            temp=item.item(0)
          self.inventory[6].equip=1
          temp.equip=0
          self.equiparr[self.inventory[6].type-1]=self.inventory[6]
          del self.inventory[6]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="8":
        if len(self.inventory)>7:
          if not self.equiparr[self.inventory[7].type-1].name=="":
            temp=self.equiparr[self.inventory[7].type-1]
          else:
            temp=item.item(0)
          self.inventory[7].equip=1
          temp.equip=0
          self.equiparr[self.inventory[7].type-1]=self.inventory[7]
          del self.inventory[7]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="9":
        if len(self.inventory)>8:
          if not self.equiparr[self.inventory[8].type-1].name=="":
            temp=self.equiparr[self.inventory[8].type-1]
          else:
            temp=item.item(0)
          self.inventory[8].equip=1
          temp.equip=0
          self.equiparr[self.inventory[8].type-1]=self.inventory[8]
          del self.inventory[8]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      if invmenu=="10":
        if len(self.inventory)>9:
          if not self.equiparr[self.inventory[9].type-1].name=="":
            temp=self.equiparr[self.inventory[9].type-1]
          else:
            temp=item.item(0)
          self.inventory[9].equip=1
          temp.equip=0
          self.equiparr[self.inventory[9].type-1]=self.inventory[9]
          del self.inventory[9]
          self.inventory.append(temp)
          if self.inventory[len(self.inventory)-1].name=="":
            del self.inventory[len(self.inventory)-1]
      elif invmenu=="0":
        break

  #Save function.
  #Takes a player object and saves the stats into a text file
  def save(self):
    with open("../player/save","w") as savefile:
      savefile.write("Name:"+str(self.name)+"\n")
      savefile.write("Level:"+str(self.lv)+"\n")
      savefile.write("HP:"+str(self.hp2)+"\n")
      savefile.write("MP:"+str(self.mp2)+"\n")
      savefile.write("Race:"+self.race+"\n")
      savefile.write("Class:"+self.charclass+"\n")
      savefile.write("Exp:"+str(self.exp)+"\n")
      savefile.write("Points:"+str(self.points)+"\n")
      savefile.write("Money:"+str(self.pocket)+"\n")
      savefile.write("INT:"+str(self.INT)+"\n")
      savefile.write("DEX:"+str(self.DEX)+"\n")
      savefile.write("PER:"+str(self.PER)+"\n")
      savefile.write("WIL:"+str(self.WIL)+"\n")
      savefile.write("STR:"+str(self.STR)+"\n")
      savefile.write("CON:"+str(self.CON)+"\n")
      savefile.write("CHA:"+str(self.CHA))

    pass

  #Load player stats from a text file into a player object
  def load(self):
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
pass