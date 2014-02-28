#!/usr/bin/env pyton
import os
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
xp=0
pocket=0
lv=1
name="empty"
tempx=0
tempy=0
flcounter=1 #Floor counter
fl=1#Actual floor (Displayed)

#Main menu
def menu():
  dungcreated=0
  while 1==1:
    os.system('clear')
    print "Kirino test"
    print "1.- Play"
    print "2.- Options"
    print "s"
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

#Options menu
def options():
  os.system('clear')
  print "Kirino test"
  print "Options"
  print "--"
  print "0.- Go back"
  opmen=raw_input("->")
  if opmen==0:
    pass

#Dungeon crawling, main function
def crawl():
  global flcounter
  global fl
  ok=0
  while ok!=1:
    tempx=input("Horizontal size: ")
    tempy=input("Vertical size: ")
    if tempx<40 or tempy<20:
      print "Minimum size 40x2y"
    elif tempx>=40 and tempy>=20:
      ok=1
  dung=dungeon.dungeon(tempx,tempy)
  hero=player.player(dung)
  crawlmen=-1
  while 1==1:
    if dung.dungarray[hero.ypos][hero.xpos]=="X":
      flcounter+=1
      fl+=1
      lsave(hero) 
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
    print "Lv",hero.lv,"(",hero.exp,"exp)",hero.pocket,"gold"
    print ""
    hero.getatr()
    print ""
    print "nwse - move"
    print "c - character sheet"
    print "q - exit to menu"
    crawlmen=raw_input("->")
    if crawlmen=="c":
      hero.charsheet()
    elif crawlmen=="n" or crawlmen=="s" or crawlmen=="e" or crawlmen=="w":
      hero.move(dung,crawlmen)
    elif crawlmen=="q":
      break
  pass

#Grab all the stats from the player and store them in the temp variables
def lsave(playa):
  global dex
  global int
  global con
  global per
  global wil
  global str
  global xp
  global pocket 
  global name
  global lv
  dex=playa.DEX
  int=playa.INT 
  con=playa.CON
  per=playa.PER
  wil=playa.WIL 
  str=playa.STR
  xp=playa.exp
  pocket=playa.pocket
  name=playa.name
  lv=playa.lv

#Reassign previous values to new character
def lload(playa):
  global flcounter
  global lv
  playa.DEX=dex
  playa.INT=int 
  playa.CON=con
  playa.PER=per
  playa.WIL=wil 
  playa.STR=str
  playa.pocket=pocket
  playa.name=name
  #Adds 1 xp for every 5 floors
  if flcounter==5:
    playa.exp=xp+1
    playa.lv=lv+1
    flcounter-=5
  elif flcounter<5:
    playa.exp=xp
  else:
    pass

menu()