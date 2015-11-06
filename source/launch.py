#! /usr/bin/env python
"""
Main procedure file.

Contains menus and the main crawl procedure
"""

import copy, os, random, sys, time
import dungeon, item, mob, npc, parser, player
import common, config, help, test

class gv():
  """
  Class that stores global variables
  """

  dex=con=per=wil=cha=0
  intv=strv=0
  xp=lv=1
  points=0
  pocket=0
  hp2=mp2=0
  name="empty"
  flcounter=1       #Floor counter
  fl=1              #Actual (total) floor (Displayed)
  tempinventory=[]
  tempequiparr=[]
  xsize=ysize=0

class world():
  """
  Class that stores the current state of the world
  """

  dung=None
  hero=None

def setup(quickvavr=0):
  """
  Creates dungeons, mobs, worlds, etc to be used in game
  """

  cfg=config.config()
  global flcounter
  global fl
  fl=1 #Initialize floor to 1
  parsemsg=hitmsg=usemsg=wilmsg=hungmsg=""
  hungsteps=0
  quick=[cfg.quick1,cfg.quick2,cfg.quick3,cfg.quick4,cfg.quick5,cfg.quick6]
  hero,dung=copy.copy(newgame(quickvar))

  #If there is no fog, load the map
  if not cfg.fog:
    for i in range(len(dung.dungarray)):
      for j in range(len(dung.dungarray[0])):
        dung.explored[i][j]=dung.dungarray[i][j]

def crawl(quickvar=0):
  """
  Main crawling function. Displays the map, keys and different statistics.
  """

  crawlmen=-1
  while 1:

    #Update hunger stats
    hungsteps+=1
    if hungsteps==10:
      hungsteps=0
      hero.stomach-=1
      if hero.stomach<10:
        hungmsg="Your stomach growls...\n"

    #Act if hungry
    if not hero.stomach:
      hero.hp2-=1
      hungmsg="You feel hungry and weak\n"

    #Reset message strings
    atkmsg=pickmsg=trapmsg=""
    lootmsg="\n"

    #Update the explored map
    if cfg.fog: dung.remember(hero)

    #Move all the mobs, delete dead mobs from array
    dung.mobarray=[i for i in dung.mobarray if i.HP>0]
    for i in dung.mobarray: i.search(dung,hero)

    #Level the player up
    hero.levelup()

    #If any of the remaining mobs has locked on the player and the player is in range, attack
    for j in dung.mobarray:
      if j.lock:
        if (j.ypos-1<=hero.ypos<=j.ypos+1 and j.xpos-1<=hero.xpos<=j.xpos+1 ):
          atkmsg=j.attack(hero,dung)
        else: j.lock=0

    #After attacking, reset the hit parameter
    for a in dung.mobarray: a.hit=0
        
    #If any of the mobs are near the player, lock them
    for k in range(len(dung.mobarray)):
      if (j.ypos-1<=hero.ypos<=j.ypos+1 and 
          j.xpos-1<=hero.xpos<=j.xpos+1 ):
        dung.mobarray[k].lock=1

    #Action if player has reached a money loot tile
    if dung.dungarray[hero.ypos][hero.xpos]=="$":
      monies=random.randrange(1,hero.lv*5)
      hero.pocket+=monies
      hero.totalgld+=monies
      dung.dungarray[hero.ypos][hero.xpos]="."
      lootmsg=("\nYou find %i gold\n"%monies)

    #Action if player has reached a gear loot tile
    if dung.dungarray[hero.ypos][hero.xpos]=="/":
      loot=item.item(random.randrange(1,12))
      picked,pickmsg=hero.pickobject(loot)
      if picked: dung.dungarray[hero.ypos][hero.xpos]="."

    #Action if player has reached a food tile
    if dung.dungarray[hero.ypos][hero.xpos]=="o":
      if random.choice([0,0,0,1]): loot=item.consumable(3,0)
      else: loot=item.consumable(0,0)
      picked,pickmsg=hero.pickconsumable(loot)
      if picked: dung.dungarray[hero.ypos][hero.xpos]="."

    #Action if player stepped on a trap
    for i in dung.traps:
      if i[0]==hero.xpos and i[1]==hero.ypos:      
        hero.totaltrp+=1
        if i[2]==1:
          trapdmg=1+random.randrange(1,5)
          hero.hp2-=trapdmg
          hero.totalrcv+=trapdmg
          dung.dungarray[hero.ypos][hero.xpos]="_"
          trapmsg="You stepped on a trap! Lost %i HP\n"%(trapdmg)
        if i[2]==2:
          trapdmg=int(round(hero.MP/random.randrange(5,10)))+1
          hero.mp2-=trapdmg
          trapmsg="Something is sucking your soul! Lost %i MP\n"%(trapdmg)
          if hero.mp2<0:
            hero.mp2=0
            hero.hp2-=trapdmg
            hero.totalrcv+=trapdmg
            trapmsg="You feel your life draining out. Lost %i HP\n"%(trapdmg)
          dung.dungarray[hero.ypos][hero.xpos]="_"
        if i[2]==3:
          trapmsg="A trap door opens under you. \nYou fall to the next floor and lose 5HP"
          hero.hp2-=5
          hero.totalrcv+=5
          flcounter+=1
          hero.totalfl+=1
          fl+=1
          lsave(hero)
          if cfg.autosave==1: hero.save()
          allowvendor=0
          if hero.totalfl%random.randrange(5,9)==0: allowvendor=1
          dung=dungeon.dungeon(len(dung.dungarray[0]),len(dung.dungarray),allowvendor)
          lload(hero)
          if not cfg.fog: dung.explored=dung.dungarray
          hero.enter(dung,1)

    #Print header and map
    common.version()
    dung.fill(hero,cfg.fog)
    dung.minimap(hero,cfg.fog)

    #Prit data
    print "HP: %i/%i, MP: %i/%i"%(hero.hp2,hero.HP,hero.mp2,hero.MP)
    print "FL %i Lv %i"%(fl,hero.lv),
    if hero.lv==1: print "(%i/5 xp)"%(hero.exp)
    if hero.lv>1:  print "%i/%i xp"%(hero.exp,3*hero.lv+(2*(hero.lv-1)))
    for i in range(6): print "(%c) %s" %(quick[i],hero.belt[i].name)
    print "\n%c: key mapping help"%(cfg.showkeys)
    print hungmsg+lootmsg+atkmsg+hitmsg+pickmsg+str(parsemsg)+trapmsg+wilmsg+usemsg
    print "->",

    #Reset message strings after display
    action=0
    parsemsg=hitmsg=usemsg=wilmsg=hungmsg=""
    crawlmen=common.getch()

    #Willpower test
    wils,wilmsg=hero.willtest()
    
    #Action choice block
    #Input mode
    if crawlmen==cfg.console:
      try: action,parsemsg=parser.parse(raw_input(">>>"),hero,dung,cfg)
      except: pass

    #Explored map
    elif crawlmen==cfg.showmap:
      common.version()
      print "Map"
      for i in dung.explored: print "".join(i)
      common.getch()

    #Character sheet menu
    elif crawlmen==cfg.charsh: hero.charsheet()

    #Show key help
    elif (crawlmen==cfg.showkeys or action==61): help.keyhelp() 

    #Using belt items
    elif crawlmen==cfg.quick1: usemsg=hero.use(hero.belt[0])
    elif crawlmen==cfg.quick2: usemsg=hero.use(hero.belt[1])
    elif crawlmen==cfg.quick3: usemsg=hero.use(hero.belt[2])
    elif crawlmen==cfg.quick4: usemsg=hero.use(hero.belt[3])
    elif crawlmen==cfg.quick5: usemsg=hero.use(hero.belt[4])
    elif crawlmen==cfg.quick6: usemsg=hero.use(hero.belt[5])

    #Movement
    #Check if there are mobs. 
    #If there are attack them, if there are not move.
    elif (crawlmen==cfg.north or action==11) and wils:
      if hero.move(dung,1)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos and a.ypos==hero.ypos-1):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.south or action==12) and wils:
      if hero.move(dung,3)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos and a.ypos==hero.ypos+1):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.east or action==13) and wils:
      if hero.move(dung,4)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.west or action==14) and wils:
      if hero.move(dung,2)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.northeast or action==15) and wils:
      if hero.move(dung,6)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos-1):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.northwest or action==16) and wils:
      if hero.move(dung,5)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos-1):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.southeast or action==17) and wils:
      if hero.move(dung,8)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos+1):
            hitmsg=hero.attack(a)

    elif (crawlmen==cfg.southwest or action==18) and wils:
      if hero.move(dung,7)==2:
        for a in dung.mobarray:
          if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos+1):
            hitmsg=hero.attack(a)

    #Game option menu
    elif crawlmen==cfg.opt or action==5: cfg.options(1)

    #Next floor
    elif (crawlmen==cfg.nextf or action==19 or action==31) and wils: 
      #Double check if the player is in the exit tile
      if dung.dungarray[hero.ypos][hero.xpos]=="X":
        flcounter,hero.totalfl,fl=(i+1 for i in (flcounter,hero.totalfl,fl))
        lsave(hero) 
        if cfg.autosave==1: hero.save()
        allowvendor=0
        if hero.totalfl%random.randrange(5,9)==0: allowvendor=1
        dung=dungeon.dungeon(len(dung.dungarray[0]),len(dung.dungarray),allowvendor)
        # Modify the new dungeon 
        # Add mobs according to the player level
        lload(hero)
        if not cfg.fog: dung.explored=dung.dungarray
        for i in range(len(dung.dungarray)):
          for j in range(len(dung.dungarray[i])):
            if dung.dungarray[i][j]=="A":
              hero.ypos=i
              hero.xpos=j
              hero.zpos=0 

    #quit to menu
    elif crawlmen==cfg.quit or action==9:
      print "Exit to menu (y/n)?\nAll unsaved progress will be lost"
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
      except IOError: pass
      raw_input(cfg.gomsg)
      break

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
  for i in tempequiparr: i.reset()
  points=0

def lsave(pl,g):
  """
  Takes a player object and saves all its attributes into the global class 
  """

  g.dex=pl.DEX
  g.intv=pl.INT 
  g.con=pl.CON
  g.per=pl.PER
  g.wil=pl.WIL 
  g.strv=pl.STR
  g.cha=pl.CHA
  g.xp=pl.exp
  g.pocket=pl.pocket
  g.name=pl.name
  g.lv=pl.lv
  g.hp2=pl.hp2
  g.mp2=pl.mp2
  g.tempinventory=pl.inventory
  g.tempequiparr=pl.equiparr
  g.points=pl.points

def lload(pl,g):
  """
  Loads all the global variables into a player object and then purges the temporal variables.

  This is used when going to the next floor, so it also adds one experience and levels up if possible.
  """

  global flcounter
  global lv
  pl.DEX=g.dex
  pl.INT=g.intv
  pl.CON=g.con
  pl.PER=g.per
  pl.WIL=g.wil 
  pl.STR=g.strv
  pl.CHA=g.cha
  pl.pocket=g.pocket
  pl.name=g.name
  pl.hp2=g.hp2
  pl.mp2=g.mp2
  pl.inventory=g.tempinventory
  pl.equiparr=g.tempequiparr
  pl.points=g.points

  #Adds 1 xp 
  pl.exp+=1

  #Levels the player up
  pl.levelup()

def scroll(lines):
  """
  Scrolls the text from the ./data/misc/credits

  lines is the height in lines of the visible text
  """

  #Pending to implement music of some sort
  emptyheight=lines
  count=head=0
  credstr=[]

  with open ("../data/misc/credits","r") as credits:
    credstr=[i.rstrip() for i in credits]

  while 1:
    os.system('clear')
    for i in range(emptyheight): print ""
    for i in credstr[0 if emptyheight>0 else head:lines-emptyheight]: print i
    emptyheight-=1
    if count<=len(credstr)+lines: count+=1
    else: break
    if emptyheight<0: head+=1
    time.sleep(1/1.5)

if __name__=="__main__":
  #Changes the directory to where the source files are
  try: os.chdir(os.path.dirname(__file__))
  except OSError: pass 

  try: menu()
  except KeyboardInterrupt: exit()