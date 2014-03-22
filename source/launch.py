#!usr/bin/env pyton
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
import config

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

#Main menu
def menu():
  """
  Main menu function. Loads the configuration file and enters the menu loop.
  """ 
  cfg=config.config()
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
    print "->",
    menu=common.getch()
    if menu=="1":
      crawl()
    if menu=="2":
      config.options(0)
    if menu=="3":
      pass
    if menu=="9":
      help.help()
    if menu=="0":
      print "Close kirino (y/n)?"
      ec=common.getch()
      if ec=="y": 
        exit()

def crawl():
  """
  Main crawling function. Displays the map, keys and different statistics.
  """
  cfg=config.config()
  global flcounter
  global fl
  fl=1 #Initialize floor to 1

  #Dungeon and player creation
  while 1:
    purge()
    try:
      tempxs=int(raw_input("Horizontal size: "))
      tempys=int(raw_input("Vertical size: "))
      if tempxs<40 or tempys<20:
        print "Minimum size 40x20"
      elif tempxs>=40 and tempys>=20:
        break
    except ValueError:
      pass
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
        if (dung.mobarray[j].ypos-1<=hero.ypos<=dung.mobarray[j].ypos+1 and 
            dung.mobarray[j].xpos-1<=hero.xpos<=dung.mobarray[j].xpos+1 ):
          dung.mobarray[j].attack(hero,dung)
        else:
          dung.mobarray[j].lock=0
        
    #If any of the mobs are near the player, lock them
    for k in range(len(dung.mobarray)):
      if (dung.mobarray[j].ypos-1<=hero.ypos<=dung.mobarray[j].ypos+1 and 
          dung.mobarray[j].xpos-1<=hero.xpos<=dung.mobarray[j].xpos+1 ):
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
    dung.fill(hero,cfg.fog)
    dung.minimap(hero,cfg.fog)
    print "Floor",fl,(hero.xpos,hero.ypos)
    print "Lv",hero.lv,hero.race,hero.charclass
    if hero.lv==1:
      print str(hero.exp)+"/5 xp, "+str(hero.pocket)+" gold"
    if hero.lv>1:
      print str(hero.exp)+"/"+str(3*hero.lv+(2*(hero.lv-1)))+" xp, "+str(hero.pocket)+" gold"
    print ""
    hero.getatr()
    print ""
    print cfg.north+cfg.south+cfg.east+cfg.west+" - move (n/s/e/w)"
    print cfg.northeast+cfg.northwest+cfg.southeast+cfg.southwest+" - move (ne/nw/se/sw)"
    print cfg.charsh+" - character sheet"
    print cfg.opt+" - options"
    print cfg.quit+" - go back to menu"
    print cfg.report+" - report dungeon"
    #Show an extra "go down" option if player has reached the exit
    if dung.dungarray[hero.ypos][hero.xpos]=="X":
      print cfg.nextf+" - next floor"
    print "->",
    crawlmen=common.getch()
    if crawlmen==cfg.charsh: #Character sheet menu
      hero.charsheet()
    elif crawlmen==cfg.north:
      hero.move(dung,1) 
    elif crawlmen==cfg.south: 
      hero.move(dung,3)
    elif crawlmen==cfg.east:
      hero.move(dung,4)
    elif crawlmen==cfg.west:
      hero.move(dung,2)
    elif crawlmen==cfg.northeast:
      hero.move(dung,6) 
    elif crawlmen==cfg.northwest: 
      hero.move(dung,5)
    elif crawlmen==cfg.southeast:
      hero.move(dung,8)
    elif crawlmen==cfg.southwest:
      hero.move(dung,7)
    elif crawlmen==cfg.opt: #Game option menu
      cfg.options(1)
    elif crawlmen==cfg.nextf: #Next floor
      #Double check if the player is in the exit tile
      if dung.dungarray[hero.ypos][hero.xpos]=="X":
        flcounter+=1
        fl+=1
        lsave(hero) 
        if cfg.autosave==1:
          hero.save()
        dung=dungeon.dungeon(tempxs,tempys)
        lload(hero)
        for i in range(len(dung.dungarray)):
          for j in range(len(dung.dungarray[i])):
            if dung.dungarray[i][j]=="A":
              hero.ypos=i
              hero.xpos=j
              hero.zpos=0 

    elif crawlmen==cfg.quit:
      print "Exit to menu (y/n)?"
      print "All unsaved progress will be lost?"
      confv=common.getch()
      if confv=="y":
        purge()
        break
    elif crawlmen==cfg.report:
      rc=-1
      print "Report dungeon? (y/n)"
      print "This will add the current floor to the ./logs/report file"
      print "Please consider sending this file when you are done playing"
      print "->",
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