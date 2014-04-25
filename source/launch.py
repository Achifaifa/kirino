#!/usr/bin/env pyton
"""
Main procedure file.

All the crawl and configuration implementation are in this module.
"""

import copy, os, random, sys, time
import dungeon, item, mob, parser, player
import common, config, help

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
xsize=0
ysize=0

#Main menu
def menu():
  """
  Main menu function. Loads the configuration file and enters the menu loop.
  """ 

  #Changes the directory to where the source files are
  try:
    os.chdir(os.path.dirname(__file__))
  except OSError: 
  #OSError is generated when os.path.dirname(__file__) is empty string. 
  #That is, when the path is already where the source files are.
    pass #No changes are needed.
    
  #loads configuration
  cfg=config.config()
  #Main menu
  while 1:
    sys.stdout.flush()
    sys.stdout.flush() 
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
      cfg.options(0)
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
  parsemsg=""
  hitmsg=""

  hero,dung=copy.copy(newgame())

  #Main crawling menu and interface
  crawlmen=-1
  while 1:
    #Reset message strings
    atkmsg=""
    pickmsg=""
    lootmsg=""

    #Move all the mobs, delete dead mobs from array
    for i in range(len(dung.mobarray)):
      try:
        if dung.mobarray[i].HP<=0:
          del dung.mobarray[i]
        else:
          dung.mobarray[i].trandmove(dung)
      except IndexError:
        pass

    #If any of the remaining mobs has locked on the player and the player is in range, attack
    for j in range(len(dung.mobarray)):
      if dung.mobarray[j].lock:
        if (dung.mobarray[j].ypos-1<=hero.ypos<=dung.mobarray[j].ypos+1 and 
            dung.mobarray[j].xpos-1<=hero.xpos<=dung.mobarray[j].xpos+1 ):
          atkmsg=dung.mobarray[j].attack(hero,dung)
        else:
          dung.mobarray[j].lock=0

    #After attacking, reset the hit parameter
    for a in dung.mobarray:
      a.hit=0
        
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
      lootmsg=("You find "+str(monies)+" gold\n")

    #Action if player has reached a gear loot tile
    if dung.dungarray[hero.ypos][hero.xpos]=="/":
      loot=item.item(random.randrange(1,11))
      picked,pickmsg=hero.pickobject(loot)
      if picked:
        dung.dungarray[hero.ypos][hero.xpos]="."

    #Print block
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
    print cfg.showkeys+" key mapping help"
    print""
    print lootmsg+atkmsg+hitmsg+pickmsg+str(parsemsg)
    print "->",

    #Reset message strings after display
    action=0
    parsemsg=""
    hitmsg=""
    crawlmen=common.getch()
    
    #Action choice block

    #Input mode
    if crawlmen==cfg.console:
      try:
        action,parsemsg=parser.parse(raw_input(">>>"),hero,dung,cfg)
      except:
        pass
    #Character sheet menu
    if crawlmen==cfg.charsh: 
      hero.charsheet()

    #Show key help
    elif crawlmen==cfg.showkeys or action==61:
      help.keyhelp() 

    #Movement
    #Check if there are mobs. 
    #If there are attack them, if there are not move.
    elif crawlmen==cfg.north or action==11: 
      if hero.move(dung,1)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos and a.ypos==hero.ypos-1):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.south or action==12: 
      if hero.move(dung,3)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos and a.ypos==hero.ypos+1):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.east or action==13:
      if hero.move(dung,4)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.west or action==14:
      if hero.move(dung,2)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.northeast or action==15:
      if hero.move(dung,6)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos-1):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.northwest or action==16: 
      if hero.move(dung,5)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos-1):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.southeast or action==17:
      if hero.move(dung,8)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos+1):
            hitmsg=hero.attack(a)

    elif crawlmen==cfg.southwest or action==18:
      if hero.move(dung,7)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos+1):
            hitmsg=hero.attack(a)


    #Game option menu
    elif crawlmen==cfg.opt or action==5: #Game option menu
      cfg.options(1)

    #Next floor
    elif crawlmen==cfg.nextf or action==19 or action==31: 
      #Double check if the player is in the exit tile
      if dung.dungarray[hero.ypos][hero.xpos]=="X":
        flcounter+=1
        hero.totalfl+=1
        fl+=1
        lsave(hero) 
        if cfg.autosave==1:
          hero.save()
        allowvendor=0
        randomvendor=random.randrange(5,9)
        if hero.totalfl%randomvendor==0:
          allowvendor=1
        dung=dungeon.dungeon(len(dung.dungarray[0]),len(dung.dungarray),allowvendor)
        lload(hero)
        for i in range(len(dung.dungarray)):
          for j in range(len(dung.dungarray[i])):
            if dung.dungarray[i][j]=="A":
              hero.ypos=i
              hero.xpos=j
              hero.zpos=0 

    #quit to menu
    elif crawlmen==cfg.quit or action==9:
      print "Exit to menu (y/n)?"
      print "All unsaved progress will be lost"
      confv=common.getch()
      if confv=="y":
        purge()
        break

    #Report dungeon
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
      hero.bury()
      try:
        with open ("../player/save","w+") as youdied:
          youdied.write("No character saved")
      except IOError:
        pass
      raw_input("Game over")
      break
  pass

def newgame():
  """
  This function displays the menu to create a new character.
  Not yet implemented.
  """
  global xsize
  global ysize
  cfg=config.config()
  while 1:
    purge()
    try:time before
      os.system('clear')
      common.version()
      print "New game [1/5] Size"
      print""
      xsize=int(raw_input("Horizontal size: "))
      ysize=int(raw_input("Vertical size: "))
      if xsize<40 or ysize<20:
        print "Minimum size 40x20"
      elif xsize>=40 and ysize>=20:
        print str(xsize)+"x"+str(ysize)+" dungeon created",
        common.getch()
        break
    except ValueError:
      pass
  sys.stdout.flush() 
  os.system('clear')
  dung=dungeon.dungeon(xsize,ysize,1)
  hero=player.player(dung)
  common.version()
  print "New game [2/5] Name"
  print ""
  hero.name=raw_input("What is your name? ")
  #If name was left empty, pick a random one
  if len(hero.name)==0:
    namearray=[]
    with open("../data/player/names","r") as names:
      for line in names:
        namearray.append(line.strip())
    hero.name=random.choice(namearray)
  with open("../data/player/races","r") as file:
      racesarray=[]
      strarray=[]
      intarray=[]
      dexarray=[]
      perarray=[]
      conarray=[]
      chaarray=[]
      for line in file:
        if not line.startswith('#'): #There must be a better way to do this
          racesarray.append(line.rstrip('\n').partition(':')[0])
          strarray.append(line.rstrip('\n').partition(':')[2].partition(':')[0])
          intarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[0])
          dexarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          perarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          conarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          chaarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
  selected=0
  while 1:
    try:time before
      os.system('clear')
      common.version()
      print "New game [3/5] Race"
      print ""
      print "Select your race"
      print "<["+cfg.west+"] "+racesarray[selected]+" ["+cfg.east+"]>"
      print "STR +"+str(strarray[selected])+" INT +"+str(intarray[selected])+" DEX +"+str(dexarray[selected])
      print "PER +"+str(perarray[selected])+" CON +"+str(conarray[selected])+" CHA +"+str(chaarray[selected])
      print cfg.quit+": select"
      np=common.getch()
      if np==cfg.west:
        selected-=1
      if np==cfg.east:
        selected+=1
      if np==cfg.quit:
        hero.race=racesarray[selected]
        if not strarray[selected]=="":
          hero.STR+=int(strarray[selected])
        if not strarray[selected]=="":
          hero.INT+=int(intarray[selected])
        if not strarray[selected]=="":
          hero.DEX+=int(dexarray[selected])
        if not strarray[selected]=="":
          hero.PER+=int(perarray[selected])
        if not strarray[selected]=="":
          hero.CON+=int(conarray[selected])
        if not strarray[selected]=="":
          hero.CHA+=int(chaarray[selected])
        break
    except IndexError:
      if np==cfg.west:
        selected +=1
      if np==cfg.east:
        selected-=1
  with open("../data/player/classes","r") as file:
    classesarray=[]
    for line in file:
        classesarray.append(line.rstrip('\n'))
  selected=0
  while 1:
    try:time before
      os.system('clear')
      common.version()
      print "New game [4/5] Class"
      print ""
      print "Select your class"
      print "<["+cfg.west+"] "+classesarray[selected]+" ["+cfg.east+"]>"
      print cfg.quit+": select"
      np=common.getch()
      if np==cfg.west:
        selected-=1
      if np==cfg.east:
        selected+=1
      if np==cfg.quit:
        hero.charclass=classesarray[selected]
        break
    except IndexError:
      if np==cfg.west:
        selected +=1
      if np==cfg.east:
        selected-=1

  return hero,dung

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
  for i in tempequiparr:
    i.reset()
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

  This is used when going to the next floor, so it also adds one experience and levels up if possible.
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

  #Adds 1 xp 
  playa.exp+=1

  #Levels the player up
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