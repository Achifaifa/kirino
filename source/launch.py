#!usr/bin/env pyton
"""
Main procedure file.
All the crawl and configuration implementation are in this module.
"""
import copy, os, sys, random
import player, dungeon, mob, item, parser
import common, help, config

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
  except OSError: #OSError generated when os.path.dirname(__file__) is empty string
    pass
    
  #loads configuration
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
      cfg.options(0)
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

  hero,dung=copy.copy(newgame())

  #Main crawling menu and interface
  crawlmen=-1
  while 1:
    atkmsg=""
    #Move all the mobs
    for i in range(len(dung.mobarray)):
      dung.mobarray[i].trandmove(dung)

    #If any of the mobs has locked on the player and the player is in range, attack
    for j in range(len(dung.mobarray)):
      if dung.mobarray[j].lock:
        if (dung.mobarray[j].ypos-1<=hero.ypos<=dung.mobarray[j].ypos+1 and 
            dung.mobarray[j].xpos-1<=hero.xpos<=dung.mobarray[j].xpos+1 ):
          atkmsg=dung.mobarray[j].attack(hero,dung)
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
    print cfg.showkeys+" key mapping help"
    print""
    print atkmsg
    print "->",
    crawlmen=common.getch()
    if crawlmen==cfg.console:
      raw_input(">>>")
    if crawlmen==cfg.charsh: #Character sheet menu
      hero.charsheet()
    elif crawlmen==cfg.north: #Check if there are mobs. if 1 attack if 0 move
      hero.move(dung,1)
    elif crawlmen==cfg.showkeys:
      help.keyhelp() 
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
        hero.totalfl+=1
        fl+=1
        lsave(hero) 
        if cfg.autosave==1:
          hero.save()
        dung=dungeon.dungeon(len(dung.dungarray[0]),len(dung.dungarray))
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
      hero.bury()
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
    try:
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
  os.system('clear')
  dung=dungeon.dungeon(xsize,ysize)
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
        if not line.startswith('#'):
          racesarray.append(line.rstrip('\n').partition(':')[0])
          strarray.append(line.rstrip('\n').partition(':')[2].partition(':')[0])
          intarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[0])
          dexarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          perarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          conarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
          chaarray.append(line.rstrip('\n').partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[2].partition(':')[0])
  selected=0
  while 1:
    try:
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
    try:
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