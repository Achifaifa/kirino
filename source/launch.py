#!/usr/bin/env pyton
import os
import sys
import random
import player
import dungeon
import mob

#load/save global variables
dex=0
int=0
con=0
per=0
wil=0
str=0
cha=0
xp=0
points=0
pocket=0
lv=1
hp2=0
mp2=0
name="empty"
tempx=0
tempy=0
flcounter=1 #Floor counter
fl=1#Actual floor (Displayed)
tempinventory=[]
tempequiparr=[]

#Environment variables
autosave=0

#Main menu
def menu():
  dungcreated=0
  while 1==1:
    os.system('clear')
    print "Kirino test"
    print "1.- Play"
    print "2.- Options"
    print ""
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
    print ""
    print "--"
    print "0.- Go back"
    opmen=raw_input("->")
    if opmen=="1":
      autosave=not autosave
    if opmen=="0":
      break

#Dungeon crawling, main function
def crawl():
  global flcounter
  global fl
  fl=1 #Initialize floor to 1
  ok=0

  #Dungeon and player creation
  while ok!=1:
    purge()
    tempx=input("Horizontal size: ")
    tempy=input("Vertical size: ")
    if tempx<40 or tempy<20:
      print "Minimum size 40x20"
    elif tempx>=40 and tempy>=20:
      ok=1
  dung=dungeon.dungeon(tempx,tempy)
  hero=player.player(dung)
  hero.name=raw_input("What is your name?")

  #Main crawling menu and interface
  crawlmen=-1
  while 1==1:
    if dung.dungarray[hero.ypos][hero.xpos]=="X":
      flcounter+=1
      fl+=1
      lsave(hero) 
      if autosave==1:
        hero.save()
      dung=dungeon.dungeon(tempx,tempy)
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
    print "c - character sheet"
    print "o - options"
    print "q - exit to menu"
    crawlmen=raw_input("-> ")
    if crawlmen=="c":
      hero.charsheet()
    elif crawlmen=="n" or crawlmen=="s" or crawlmen=="e" or crawlmen=="w":
      hero.move(dung,crawlmen)
    elif crawlmen=="o":
      options()
    elif crawlmen=="q":
      break
  pass

#New character menu (pass)
def newchar():
  pass

#resets all the temporary variables
def purge():
  global dex
  global int
  global con
  global per
  global wil
  global str
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
  int=0 
  con=0
  per=0
  wil=0 
  str=0
  cha=0
  xp=0
  pocket=0
  name="_"
  lv=0  
  hp2=0
  mp2=0
  tempinventory=[]
  tempequiparr=[]
  points=0


#Grab all the stats from the player and store them in the temporary variables
def lsave(playa):
  global dex
  global int
  global con
  global per
  global wil
  global str
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
  int=playa.INT 
  con=playa.CON
  per=playa.PER
  wil=playa.WIL 
  str=playa.STR
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
  playa.INT=int 
  playa.CON=con
  playa.PER=per
  playa.WIL=wil 
  playa.STR=str
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