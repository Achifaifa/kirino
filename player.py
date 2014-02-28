#usr/bin/env python 
import os
import random
import dungeon

#Player class definition
class player:
  'Player instance'
  #Main characteristics
  name="____" #Name
  pocket=0    #Money
  exp=0       #EXP
  lv=1        #Level

  #Attribute variables 
  INT=1
  DEX=1
  PER=1
  WIL=1
  STR=1
  CON=1

  #Status variables
  HP=0
  MP=0
  END=0
  SPD=0
  
  #Position
  xPos=0
  yPos=0
  zPos=0 #0: On the ground; 1: Flying
  

  #Initialization  
  def __init__(self,dungeon):
    #Initialize atributes
    self.name="Test subject"
    self.pocket=0
    self.exp=8

    #Set attributes to 1
    self.STR=1
    self.INT=1
    self.CON=1
    self.WIL=1
    self.PER=1
    self.DEX=1

    #Define secondary attributes
    self.HP=((self.CON+self.STR)*4)+10
    self.MP=(self.STR+self.DEX+self.INT+self.CON+self.WIL+self.PER)
    self.END=((self.CON+self.STR+self.WIL)*3)+5
    self.SPD=(self.CON+self.DEX)*3
    
    #Initialize position at the entrance
    for i in range(len(dungeon.dungarray)):
      for j in range(len(dungeon.dungarray[i])):
        if dungeon.dungarray[i][j]=="A":
          self.ypos=i
          self.xpos=j
          self.zpos=0
    
  #Test function. Prints attributes.
  def getatr(self):
    print 'INT:', self.INT, 'DEX:', self.DEX, 'CON:', self.CON
    print 'WIL:', self.WIL, 'STR:', self.STR, 'PER:', self.PER
    print ""
    print 'HP:', self.HP, '       MP:', self.MP
    print 'END:', self.END, '     SPD:', self.SPD
    
  #Move function. Accepts strings with direction and distance
  def move(self,dungeon,direction):
    #This gives 1 base move and 1 extra move for every 10 SPD
    moves=1
    moves+=self.SPD/10

    #Checks de direction and moves
    if direction=="n":
      if dungeon.dungarray[self.ypos-1][self.xpos]=="#":
        print "There is a wall there!"
      else:
        self.ypos -= moves
    elif direction=="w":
      if dungeon.dungarray[self.ypos][self.xpos-1]=="#":
         print "There is a wall there!"
      else:
        self.xpos -= moves  
    elif direction=="s":
      if dungeon.dungarray[self.ypos+1][self.xpos]=="#":
        print "There is a wall there!"
      else:     
        self.ypos += moves
    elif direction=="e":
      if dungeon.dungarray[self.ypos][self.xpos+1]=="#":
        print "There is a wall there!"
      else:
        self.xpos += moves
    else:
      print "That's not a direction!"
      print "Try n, s, e and w"

  #Attribute modifying 
  def charsheet(self):
    menu=0
    while 1==1:
      os.system('clear')
      print "Kirino test"
      print self.name,"- Character sheet"
      print "____________________"
      print "Gold: ",self.pocket
      print "Level",self.lv,"(",self.exp,"xp)"
      print ""
      self.getatr()
      print "____________________"
      print "1.- Spend experience"
      print "2.- Inventory"
      print "3.- Modify character"
      print ""
      print "0.- Exit"
      menu=raw_input("->")
      if menu=="1":
        choice=-1
        while choice!="0":
          os.system('clear')
          print "Kirino test"
          print self.name,"- Character sheet"
          print ""
          print "Spend experience"
          if self.exp==0:
            print "No XP left!"
          else:
            print self.exp,"points left"
            print ""

          #Recalculating secondary attributes
          self.HP=((self.CON+self.STR)*4)+10
          self.MP=(self.STR+self.DEX+self.INT+self.CON+self.WIL+self.PER)
          self.END=((self.CON+self.STR+self.WIL)*3)+5
          self.SPD=(self.CON+self.DEX)*3

          #Determining cost of improving attributes (Based on AFMBE rules)  
          if self.STR<5:
            coststr=1
          else:
            coststr=(((self.STR/5)+1)*5)-5
          if self.INT<5:
            costint=1
          else:
            costint=(((self.INT/5)+1)*5)-5
          if self.DEX<5:
            costdex=1
          else:
            costdex=(((self.DEX/5)+1)*5)-5
          if self.CON<5:
            costcon=1
          else:
            costcon=(((self.CON/5)+1)*5)-5
          if self.PER<5:
            costper=1
          else:
            costper=(((self.PER/5)+1)*5)-5
          if self.WIL<5:
            costwil =1
          else:
            costwil=(((self.WIL/5)+1)*5)-5

          #printing menu
          print "1.-",[coststr],"STR",(self.STR)
          print "2.-",[costint],"INT",(self.INT)
          print "3.-",[costdex],"DEX",(self.DEX)
          print "4.-",[costcon],"CON",(self.CON)
          print "5.-",[costper],"PER",(self.PER)
          print "6.-",[costwil],"WIL",(self.WIL)
          print ""
          print "Secondary attributes:"
          print 'HP:', self.HP, '       MP:', self.MP
          print 'END:', self.END, '     SPD:', self.SPD
          print "---"
          print "0.- Exit"
          print ""
          choice=raw_input("->")

          #Choice cases
          if self.exp==0:
            pass
          else:
            if choice=="1":
              if self.exp>=coststr:
                self.STR+=1
                self.exp-=coststr
            elif choice=="2":
              if self.exp>=costint:
                self.INT+=1
                self.exp-=costint
            elif choice=="3":
              if self.exp>=costdex:
                self.DEX+=1
                self.exp-=costdex
            elif choice=="4":
              if self.exp>=costcon:
                self.CON+=1
                self.exp-=costcon
            elif choice=="5":
              if self.exp>=costper:
                self.PER+=1
                self.exp-=costper
            elif choice=="6":
              if self.exp>=costwil:
                self.WIL+=1
                self.exp-=costwil
            elif choice=="0":
              pass
            else:
              pass

      #Inventory menu        
      elif menu=="2":
        os.system('clear')
        print "Kirino test"
        print self.name,"- Character sheet"
        print ""
        print "Inventory"
        print "You are not carrying anything"
        raw_input("go back")
      
      #Character options menu
      elif menu=="3":
        os.system('clear')
        print "Kirino test"
        print self.name,"- Character sheet"
        print ""
        print "X.- Change name"
        print "---"
        print "0.- Back"
        raw_input("go back")
      elif menu=="0":
        break
      pass
pass