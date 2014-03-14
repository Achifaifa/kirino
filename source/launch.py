#!/usr/bin/env pyton
"""
Main procedure file.
All the crawl and configuration implementation are in this module.
"""
import os
import sys
import random
import player
import dungeon
import mob
import item
import parser
import common
import help

#load/save global variables
dex=0
intv=0
con=0
per=0
wil=0
strv=0
cha=0
xp=0
points=0
pocket=0
lv=1
hp2=0
mp2=0
name="empty"
flcounter=1 #Floor counter
fl=1#Actual floor (Displayed)
tempinventory=[]
tempequiparr=[]

#Environment variables
autosave=0
fog=1

#Key mapping variables
north="n"
south="s"
east="e"
west="w"
charsh="c"
opt="o"
quit="q"
report="z"
nextf="m"

#Main menu
def menu():
  """
  Main menu function. Loads the configuration file and enters the menu loop.
  """
  global north
  global south
  global east
  global west
  global charsh
  global opt
  global quit
  global report
  global autosave
  global fog
  global nextf

  #Checks if there is a config file. If it exists, loads the key mapping variables from it
  if not os.path.exists("../player/"):
    os.makedirs("../player/")
  if os.path.isfile("../player/config"):
    with open("../player/config","r") as configfile:
      for line in configfile:
        if not line.startswith('#'):
          if line.partition(':')[0]=="North":
            north=(line.partition(':')[2]).strip()          
          if line.partition(':')[0]=="South":
            south=(line.partition(':')[2]).strip()          
          if line.partition(':')[0]=="East":
            east=(line.partition(':')[2]).strip()         
          if line.partition(':')[0]=="West":
            west=(line.partition(':')[2]).strip()          
          if line.partition(':')[0]=="Sheet":
            charsh=(line.partition(':')[2]).strip()         
          if line.partition(':')[0]=="Options":
            opt=(line.partition(':')[2]).strip()          
          if line.partition(':')[0]=="Quit":
            quit=(line.partition(':')[2]).strip()   
          if line.partition(':')[0]=="Report":
            report=(line.partition(':')[2]).strip()          
          if line.partition(':')[0]=="Autosave":
            if line.partition(':')[2].strip()=="on":
              autosave=1
          if line.partition(':')[0]=="Fog":
            if line.partition(':')[2].strip()=="off":
              fog=0
          if line.partition(':')[0]=="Next floor":
            nextf=(line.partition(':')[2]).strip()


  #Main menu
  while 1:
    os.system('clear')
    common.version()
    print ""
    print ""
    print "1.- Play"
    print "2.- Options"
    print "3.- "
    print "--"
    print "9.- Help"
    print "0.- Exit"
    print "->"
    menu=common.getch()
    if menu=="1":
      crawl()
    if menu=="2":
      options(0)
    if menu=="3":
      pass
    if menu=="9":
      help.help()
    if menu=="0":
      print "Close kirino (y/n)?"
      ec=common.getch()
      if ec=="y": 
        exit()


def options(restricted):
  """
  Game options menu. This allows modification of the general options, such as key mappings, autosave, etc.
  If the restricted parameter is 1, it hides the options that should not be changed during the game (fog, etc)

  """
  global autosave
  global fog
  while 1:
    os.system('clear')
    common.version()
    print "Options"
    print ""
    if autosave==0:
      print "1.- Autosave [off]"
    if autosave==1:
      print "1.- Autosave [on]"
    print "  Saves the character to file between floors"
    if fog==0 and not restricted:
      print "2.- Fog [off]"
    if fog==1 and not restricted:
      print "2.- Fog [on]"
    print "3.- Key mapping"
    print ""
    print "--"
    print "9.- Help"
    print "0.- Go back"
    print "-> "
    opmen=common.getch()
    if opmen=="1":
      autosave=not autosave
    if opmen=="3":
      keymap()
    if opmen=="2" and not restricted:
      fog=not fog
    if opmen=="9":
      help.help()
    if opmen=="0":
      saveoptions()
      break

#Keyboard mapping options menu. Saves the configuration to file at exit
def keymap():
  """
  Key mapping configuration menu.
  """
  global north
  global south
  global east
  global west
  global charsh
  global opt
  global quit
  global report
  while 1:
    os.system('clear')
    common.version()
    print "Options - Keyboard mapping"
    print ""
    print "1.- Go north: "+north
    print "2.- Go south: "+south
    print "3.- Go east: "+east
    print "4.- Go west: "+west
    print "5.- Character sheet : "+charsh
    print "6.- Option menu: "+opt
    print "7.- Report dungeon: "+report
    print "8.- Quit dungeon: "+quit
    print "---"
    print "9.- More keys"
    print "0.- Go back"
    print ""
    print "-> "
    keymenu=common.getch()
    if keymenu=="0":
      saveoptions()
      break
    if keymenu=="9":
      pass
    if keymenu=="1":
      print "New key for 'go north' "
      north=common.getch()
    if keymenu=="2":
      print "New key for 'go south' "
      south=common.getch()
    if keymenu=="3":
      print "New key for 'go east' "
      east=common.getch()
    if keymenu=="4":
      print "New key for 'go west' "
      west=common.getch()
    if keymenu=="5":
      print "New key for 'Character sheet' "
      charsh=common.getch()
    if keymenu=="6":
      print "New key for 'Option menu' "
      opt=common.getch()
    if keymenu=="7":
      print "New key for 'Report dungeon' "
      report=common.getch()
    if keymenu=="8":
      print "New key for 'Quit dungeon' "
      quit=common.getch()

def saveoptions():
  """
  Option saving function. Takes all the configuration variables and writes them into a file.
  The file is located in ../player/, if the directory does not exist this creates the directory and the file.
  """
  if not os.path.exists("../player/"):
    os.makedirs("../player/")
  with open("../player/config","w+") as configfile:
    configfile.write("# \n")
    configfile.write("# Keyboard options \n")
    configfile.write("# \n")
    configfile.write("North:"+north+"\n")
    configfile.write("South:"+south+"\n")
    configfile.write("East:"+east+"\n")
    configfile.write("West:"+west+"\n")
    configfile.write("Sheet:"+charsh+"\n")
    configfile.write("Options:"+opt+"\n")
    configfile.write("Quit:"+quit+"\n")
    configfile.write("Report:"+report+"\n")
    configfile.write("Next floor:"+nextf+"\n")
    configfile.write("# \n")
    configfile.write("# Game options \n")
    configfile.write("# \n")
    if autosave==1:
      configfile.write("Autosave:on \n")
    if autosave==0:
      configfile.write("Autosave:off \n")
    if fog==1:
      configfile.write("Fog:on")
    if fog==0:
      configfile.write("Fog:off")

def crawl():
  """
  Main crawling function. Displays the map, keys and different statistics.
  """
  global flcounter
  global fl
  fl=1 #Initialize floor to 1

  #Dungeon and player creation
  while 1:
    purge()
    tempxs=int(raw_input("Horizontal size: "))
    tempys=int(raw_input("Vertical size: "))
    if tempxs<40 or tempys<20:
      print "Minimum size 40x20"
    elif tempxs>=40 and tempys>=20:
      break
  dung=dungeon.dungeon(tempxs,tempys)
  hero=player.player(dung)
  hero.name=raw_input("What is your name? ")

  #Main crawling menu and interface
  crawlmen=-1
  while 1:
    #Move all the mobs
    for i in range(len(dung.mobarray)):
      dung.mobarray[i].trandmove(dung)

    #If any of the mobs has locked on the player and the player is in range, attack
    for j in range(len(dung.mobarray)):
      if dung.mobarray[j].lock:
        if hero.ypos<=dung.mobarray[j].ypos+1 and hero.ypos>=dung.mobarray[j].ypos-1 and hero.xpos<=dung.mobarray[j].xpos+1 and hero.xpos>=dung.mobarray[j].xpos-1:
          dung.mobarray[j].attack(hero,dung)
        else:
          dung.mobarray[j].lock=0
        
    #If any of the mobs are near the player, lock them
    for k in range(len(dung.mobarray)):
      if hero.ypos<=dung.mobarray[k].ypos+1 and hero.ypos>=dung.mobarray[k].ypos-1 and hero.xpos<=dung.mobarray[k].xpos+1 and hero.xpos>=dung.mobarray[k].xpos-1:
        dung.mobarray[k].lock=1

    #Action if player has reached a money loot tile
    if dung.dungarray[hero.ypos][hero.xpos]=="$":
      monies=random.randrange(1,5)
      hero.pocket+=monies
      dung.dungarray[hero.ypos][hero.xpos]="."

    #Action if player has reached a gear loot tile
    if dung.dungarray[hero.ypos][hero.xpos]=="/":
      loot=item.item(random.randrange(1,11))
      if hero.pickobject(loot):
        dung.dungarray[hero.ypos][hero.xpos]="."

    #Crawling loop
    os.system('clear')
    common.version()
    print ""
    dung.fill(hero,fog)
    dung.minimap(hero,fog)
    print "Floor",fl,(hero.xpos,hero.ypos)
    print "Lv",hero.lv,hero.race,hero.charclass
    if hero.lv==1:
      print str(hero.exp)+"/5 xp, "+str(hero.pocket)+" gold"
    if hero.lv>1:
      print str(hero.exp)+"/"+str(3*hero.lv+(2*(hero.lv-1)))+" xp, "+str(hero.pocket)+" gold"
    print ""
    hero.getatr()
    print ""
    print north+south+east+west+" - move"
    print charsh+" - character sheet"
    print opt+" - options"
    print quit+" - go back to menu"
    print report+" - report dungeon"
    #Show an extra "go down" option if player has reached the exit
    if dung.dungarray[hero.ypos][hero.xpos]=="X":
      print nextf+" - next floor"
    print "-> "
    crawlmen=common.getch()
    if crawlmen==charsh: #Character sheet menu
      hero.charsheet()
    elif crawlmen==north:
      hero.move(dung,1) 
    elif crawlmen==south: 
      hero.move(dung,3)
    elif crawlmen==east:
      hero.move(dung,4)
    elif crawlmen==west:
      hero.move(dung,2)
    elif crawlmen==opt: #Game option menu
      options(1)
    elif crawlmen==nextf: #Next floor
      #Double check if the player is in the exit tile
      if dung.dungarray[hero.ypos][hero.xpos]=="X":
        flcounter+=1
        fl+=1
        lsave(hero) 
        if autosave==1:
          hero.save()
        dung=dungeon.dungeon(tempxs,tempys)
        lload(hero)
        for i in range(len(dung.dungarray)):
          for j in range(len(dung.dungarray[i])):
            if dung.dungarray[i][j]=="A":
              hero.ypos=i
              hero.xpos=j
              hero.zpos=0 

    elif crawlmen==quit:
      print "Exit to menu (y/n)?"
      print "All unsaved progress will be lost?"
      confv=common.getch()
      if confv=="y":
        purge()
        break
    elif crawlmen==report:
      rc=-1
      print "Report dungeon? (y/n)"
      print "This will add the current floor to the ./logs/report file"
      print "Please consider sending this file when you are done playing"
      print "-> "
      rc=common.getch()
      if rc=="y":
        dung.report()
        raw_input("Dungeon saved in log file")

    #If the player health is EL0, game over
    if hero.hp2<=0:
      raw_input("Game over")
      break
  pass

def newchar():
  """
  This function displays the menu to create a new character.
  Not yet implemented.
  """
  pass

def purge():
  """
  Sets to zero all the global temporal variables used to store player data.
  Used when exiting a game so the data is not carried to the next one.
  """
  global dex
  global intv
  global con
  global per
  global wil
  global strv
  global cha
  global xp
  global pocket 
  global name
  global lv
  global hp2
  global mp2
  global tempinventory
  global tempequiparr
  global points
  dex=0
  intv=0 
  con=0
  per=0
  wil=0 
  strv=0
  cha=0
  xp=0
  pocket=0
  name="_"
  lv=0  
  hp2=0
  mp2=0
  tempinventory=[]
  for i in range (len(tempequiparr)):
    tempequiparr[i]=item.item(0)
  points=0

def lsave(playa):
  """
  Takes a player object and saves all its attributes into global variables. 
  """
  global dex
  global intv
  global con
  global per
  global wil
  global strv
  global cha
  global xp
  global pocket 
  global name
  global lv
  global hp2
  global mp2
  global tempinventory
  global tempequiparr
  global points
  dex=playa.DEX
  intv=playa.INT 
  con=playa.CON
  per=playa.PER
  wil=playa.WIL 
  strv=playa.STR
  cha=playa.CHA
  xp=playa.exp
  pocket=playa.pocket
  name=playa.name
  lv=playa.lv
  hp2=playa.hp2
  mp2=playa.mp2
  tempinventory=playa.inventory
  tempequiparr=playa.equiparr
  points=playa.points

def lload(playa):
  """
  Loads all the global variables into a player object and then purges the temporal variables.
  """
  global flcounter
  global lv
  playa.DEX=dex
  playa.INT=intv
  playa.CON=con
  playa.PER=per
  playa.WIL=wil 
  playa.STR=strv
  playa.CHA=cha
  playa.pocket=pocket
  playa.name=name
  playa.hp2=hp2
  playa.mp2=mp2
  playa.inventory=tempinventory
  playa.equiparr=tempequiparr
  playa.points=points
  #Adds 1 xp for every 5 floors
  if flcounter==5:
    playa.exp=xp+1
    flcounter-=5
  elif flcounter<5:
    playa.exp+=1
  if playa.lv==1:
    if playa.exp>=5:
      playa.lv+=1
      playa.exp-=5
      playa.points+=2
  lvlimit=3*playa.lv+(2*(playa.lv-1))
  if playa.lv>1:
    while playa.exp>=lvlimit:
      playa.lv+=1
      playa.exp-=lvlimit
      playa.points+=2

menu()