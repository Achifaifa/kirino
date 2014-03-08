#!/usr/bin/env pyton
import os
import sys
import random
import player
import dungeon
import mob
import item

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

#Key mapping variables
north="n"
south="s"
east="e"
west="w"
charsh="c"
opt="o"
quit="q"
report="z"

#Main menu
def menu():
  global north
  global south
  global east
  global west
  global charsh
  global opt
  global quit
  global report
  global autosave

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


  #Main menu
  while 1:
    os.system('clear')
    print "Kirino test"
    print "1.- Play"
    print "2.- Options"
    print "3.- "
    print "--"
    print "0.- Exit"
    menu=raw_input("->")
    if menu=="1":
      crawl()
    if menu=="2":
      options()
    if menu=="3":
      pass
    if menu=="0":
      exit()

#Game options menu
def options():
  global autosave
  while 1:
    os.system('clear')
    print "Kirino test"
    print "Options"
    print ""
    if autosave==0:
      print "1.- Autosave [off]"
    if autosave==1:
      print "1.- Autosave [on]"
    print "  Saves the character to file between floors"
    print "2.- Key mapping"
    print ""
    print "--"
    print "0.- Go back"
    opmen=raw_input("->")
    if opmen=="1":
      autosave=not autosave
    if opmen=="2":
      keymap()
    if opmen=="0":
      saveoptions()
      break

#Keyboard mapping options menu. Saves the configuration to file at exit
def keymap():
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
    print "Kirino test"
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
    keymenu=raw_input("-> ")
    if keymenu=="0":
      saveoptions()
      break
    if keymenu=="9":
      pass
    if keymenu=="1":
      north=raw_input("New key for 'go north' ")
    if keymenu=="2":
      south=raw_input("New key for 'go south' ")
    if keymenu=="3":
      east=raw_input("New key for 'go east' ")
    if keymenu=="4":
      west=raw_input("New key for 'go west' ")
    if keymenu=="5":
      charsh=raw_input("New key for 'Character sheet' ")
    if keymenu=="6":
      opt=raw_input("New key for 'Option menu' ")
    if keymenu=="7":
      report=raw_input("New key for 'Report dungeon' ")
    if keymenu=="8":
      quit=raw_input("New key for 'Quit dungeon' ")

#Saves the game options to file
def saveoptions():
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
    configfile.write("# \n")
    configfile.write("# Game options \n")
    configfile.write("# \n")
    if autosave==1:
      configfile.write("Autosave:on")
    if autosave==0:
      configfile.write("Autosave:off")

#Dungeon crawling, main function
def crawl():
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
  hero.name=raw_input("What is your name?")

  #Main crawling menu and interface
  crawlmen=-1
  while 1:
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
    os.system('clear')
    print "Kirino test"
    dung.fill(hero)
    dung.minimap(hero)
    print "Floor",fl,(hero.xpos,hero.ypos)
    print "Lv",hero.lv,hero.race,hero.charclass
    if hero.lv==1:
      print hero.exp,"/ 5 xp",hero.pocket,"gold"
    if hero.lv>1:
      print hero.exp,"/",3*hero.lv+(2*(hero.lv-1)),"xp,",hero.pocket,"gold"
    print ""
    hero.getatr()
    print ""
    print "nwse - move"
    print charsh+" - character sheet"
    print opt+" - options"
    print quit+" - go back to menu"
    print report+" - report dungeon"
    crawlmen=raw_input("-> ")
    if crawlmen==charsh:
      hero.charsheet()
    elif crawlmen==north:
      hero.move(dung,1) 
    elif crawlmen==south: 
      hero.move(dung,3)
    elif crawlmen==east:
      hero.move(dung,4)
    elif crawlmen==west:
      hero.move(dung,2)
    elif crawlmen==opt:
      options()
    elif crawlmen==quit:
      purge()
      break
    elif crawlmen==report:
      dung.report()
  pass

#New character menu (pass)
def newchar():
  pass

#resets all the temporary variables
def purge():
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


#Grab all the stats from the player and store them in the temporary variables
def lsave(playa):
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

#Reassign temporary saved values to new character
def lload(playa):
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
    if playa.exp>=lvlimit:
      playa.lv+=1
      playa.exp-=lvlimit
      playa.points+=2

menu()

# for i in range(100):
#   print i,(3*i)+(2*(i-1))