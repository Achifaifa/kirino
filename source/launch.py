#! /usr/bin/env python
"""
Main procedure file.

Contains menus and the main crawl procedure
"""

import copy, os, random, sys, time
import dungeon, item, mob, npc, parser, player
import common, config, help, test

class gl():
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
  config=None
  
  def resetmsg():

    parsemsg=hitmsg=usemsg=wilmsg=hungmsg=""

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

  glcfg=config.config()
  gl.fl=1 #Initialize floor to 1
  gl.resetmsg()
  gl.hungsteps=0
  quick=[cfg.quick1,cfg.quick2,cfg.quick3,cfg.quick4,cfg.quick5,cfg.quick6]
  hero,dung=copy.copy(newgame(quickvar))

  #If there is no fog, load the map
  if not cfg.fog:
    for i in range(len(dung.dungarray)):
      for j in range(len(dung.dungarray[0])):
        dung.explored[i][j]=dung.dungarray[i][j]

def pickthings(dungeon,player):
  """
  Makes the player pick whatever is on the floor up and updates stats
  """

  tile=dungeon.dungarray[player.ypos][player.xpos]

  #Action if player has reached a money loot tile
  if tile=="$":
    monies=random.randrange(1,player.lv*5)
    player.pocket+=monies
    player.totalgld+=monies
    dungeon.dungarray[player.ypos][player.xpos]="."
    pickmsg="\nYou find %i gold\n"%monies

  #Action if player has reached a gear loot tile
  elif tile=="/":
    loot=item.item(random.randrange(1,12))
    picked,pickmsg=player.pickobject(loot)
    if picked: dungeon.dungarray[player.ypos][player.xpos]="."

  #Action if player has reached a food tile
  elif tile=="o":
    if random.choice([0,0,0,1]): loot=item.consumable(3,0)
    else: loot=item.consumable(0,0)
    picked,pickmsg=player.pickconsumable(loot)
    if picked: dungeon.dungarray[player.ypos][player.xpos]="."
  return pickmsg

def atrap(dungeon, player):
  """
  Checks if the player has stepped on a trap
  """

  #Action if player stepped on a trap
  for i in dung.traps:
    if (i[0],i[1])==(hero.ypos,hero.xpos):      
      hero.totaltrp+=1

      trapdmg=1+random.randrange(1,5)

      # Normal trap
      if i[2]==1:
        hero.hp2-=trapdmg
        hero.totalrcv+=trapdmg
        dung.dungarray[hero.ypos][hero.xpos]="_"
        return "You stepped on a trap! Lost %i HP\n"%(trapdmg)

      # Mana trap
      elif i[2]==2:
        hero.mp2-=trapdmg
        dung.dungarray[hero.ypos][hero.xpos]="_"
          
        # If there is no mana, drain life instead
        if hero.mp2<0:
          hero.mp2=0
          hero.hp2-=trapdmg
          hero.totalrcv+=trapdmg
          return "You feel your life draining out. Lost %i HP\n"%(trapdmg)
        return "Something is sucking your soul! Lost %i MP\n"%(trapdmg)

      # Trap to next floor
      elif i[2]==3:
         return "A trap door opens under you. \nYou fall to the next floor and lose 5HP"
        hero.hp2-=5
        hero.totalrcv+=5
        gl.flcounter+=1
        hero.totalfl+=1
        gl.fl+=1
        if cfg.autosave==1: hero.save()

        allowvendor=1 if not hero.totalfl%random.randrange(5,9) else 0
        world.dung=dungeon.dungeon(world.dung.xsize,world.dung.ysize,allowvendor)
        if not cfg.fog: world.dung.explored=world.dung.dungarray
        hero.enter(world.dung,1)

def crawl(quickvar=0):
  """
  Main crawling function. Displays the map, keys and different statistics.
  """

  crawlmen=-1
  while 1:

    # Process hunger
    hungmsg=hero.hunger()

    #Reset message strings
    atkmsg=pickmsg=trapmsg=""

    #Update the explored map
    if cfg.fog: dung.remember(hero)

    #Move all the mobs, delete dead mobs from array
    dung.mobarray=[i for i in dung.mobarray if i.HP>0]
    for i in dung.mobarray: i.search(dung,hero)

    #Level the player up
    hero.levelup()

    #Attack with all the mobs. Range/conditoins check in mob.attack()
    atkmsg="".join([j.attack(hero,dung) for j in dung.mobarray])

    #After attacking, reset the hit parameter
    #If any of the mobs are near the player, lock them
    for i in dung.mobarray: 
      i.hit=0
      i.lock()
        
    # Pick things from floor
    pickthings(dung,hero)

    # Check if the player has stepped on a trap
    trapmsg=atrap(dung,hero)

    #Print header and map
    common.version()
    dung.fill(hero,cfg.fog)
    dung.minimap(hero,cfg.fog)
    menus.printpldata(hero)

    print "\n%c: key mapping help"%(cfg.showkeys)
    print hungmsg+atkmsg+hitmsg+pickmsg+str(parsemsg)+trapmsg+wilmsg+usemsg
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
    elif crawlmen in cfg.quick:
      usemsg=hero.use(hero.belt[cfg.quick.index(crawlmen)])

    if wils:
      #Movement
      #Check if there are mobs. 
      #If there are attack them, if there are not move.
      elif (crawlmen==cfg.north or action==11):
        if hero.move(dung,1)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos and a.ypos==hero.ypos-1):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.south or action==12):
        if hero.move(dung,3)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos and a.ypos==hero.ypos+1):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.east or action==13):
        if hero.move(dung,4)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.west or action==14):
        if hero.move(dung,2)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.northeast or action==15):
        if hero.move(dung,6)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos-1):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.northwest or action==16):
        if hero.move(dung,5)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos-1):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.southeast or action==17):
        if hero.move(dung,8)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos+1 and a.ypos==hero.ypos+1):
              hitmsg=hero.attack(a)

      elif (crawlmen==cfg.southwest or action==18):
        if hero.move(dung,7)==2:
          for a in dung.mobarray:
            if (a.xpos==hero.xpos-1 and a.ypos==hero.ypos+1):
              hitmsg=hero.attack(a)

    

      #Next floor
      elif (crawlmen==cfg.nextf or action==19 or action==31): 
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

    #Game option menu
    elif crawlmen==cfg.opt or action==5: cfg.options(1)

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
      print "Report dungeon? (y/[n])"
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
      raw_input(cfg.gomsg)
      break

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