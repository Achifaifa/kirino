#! /usr/bin/env python

import common

def enchant(item,player):
  """
  Menu for enchanting items

  It needs a player and item objects to check if the player has enough money. 
  All the success/error messages are returned in this function. The enchant function in item.py doesn't do that.
  """

  oldname=item.name
  enchantprice=item.price

  # Player doesn't have money
  if player.pocket<enchantprice:
    print "You don't have enough money"
    common.getch()
  # Item already at max level
  elif self.enchantlv>=10:
    print "Maximum enchant level reached"
    common.getch()
  # Everything is OK
  else:
    player.pocket-=enchantprice
    player.totalspn+=enchantprice

    #Call the enchant function, report result
    if item.enchant():
      player.itemsenc+=1
      raw_input("%s enchanted successfully"%(oldname))

      # Increase maximum enchanted level in the stats
    if item.enchantlv>player.maxench: player.maxench=item.enchantlv
    else: 
      raw_input("%s broke during enchanting"%(oldname))

def playerattrs(player):
  """
  Prints the player attributes on screen.
  """

  print "HP: %i/%i, MP: %i/%i      "  %(player.hp2,player.HP,player.mp2,player.MP)
  print "STR: %i(+%i)  DEX: %i(+%i)"  %(player.STR,player.strboost,player.DEX,player.dexboost)
  print "INT: %i(+%i)  CON: %i(+%i)"  %(player.INT,player.intboost,player.CON,player.conboost)
  print "WIL: %i(+%i)  PER: %i(+%i)"  %(player.WIL,player.wilboost,player.PER,player.perboost)
  print "CHA: %i(+%i)              "  %(player.CHA,player.chaboost)
  print "END: %i SPD: %i           "  %(player.END,player.SPD)

def achievements(player):
  """
  Shows a list of completed achievements.
  """

  common.version()
  print "%s - Character sheet - Achievements\n" %(player.name)

  print "Exploration"
  if      player.totalfl>=500:    print "Elevator 4/4"
  elif    player.totalfl>=250:    print "Elevator 3/4"
  elif    player.totalfl>=100:    print "Elevator 2/4"
  elif    player.totalfl>=10:     print "Elevator 1/4"
  elif    player.totalfl<10:      print "????     0/4"

  if      player.steps>=10000:    print "Explorer 4/4"
  elif    player.steps>=5000:     print "Explorer 3/4"
  elif    player.steps>=1000:     print "Explorer 2/4"
  elif    player.steps>=500:      print "Explorer 1/4"
  elif    player.steps<500:       print "????     0/4"

  print "\nCombat"
  if      player.kills>=500:      print "Warrior  4/4"
  elif    player.kills>=250:      print "Warrior  3/4"
  elif    player.kills>=100:      print "Warrior  2/4"
  elif    player.kills>=10:       print "Warrior  1/4"
  elif    player.kills<10:        print "????     0/4"

  if      player.totaltrp>=100:   print "Bad luck 4/4"
  elif    player.totaltrp>=50:    print "Bad luck 3/4"
  elif    player.totaltrp>=20:    print "Bad luck 2/4"
  elif    player.totaltrp>=5:     print "Bad luck 1/4"
  elif    player.totaltrp<5:      print "????     0/4"

  print "\nItems"
  if      player.itemspck>=100:   print "Hoarder  4/4"
  elif    player.itemspck>=50:    print "Hoarder  3/4"
  elif    player.itemspck>=20:    print "Hoarder  2/4"
  elif    player.itemspck>=5:     print "Hoarder  1/4"
  elif    player.itemspck<5:      print "????     0/4"

  if      player.itemsdst>=100:   print "Cleaning 4/4"
  elif    player.itemsdst>=50:    print "Cleaning 3/4"
  elif    player.itemsdst>=20:    print "Cleaning 2/4"
  elif    player.itemsdst>=5:     print "Cleaning 1/4"
  elif    player.itemsdst<5:      print "????     0/4"

  if      player.itemsenc>=100:   print "Wizard   4/4"
  elif    player.itemsenc>=50:    print "Wizard   3/4"
  elif    player.itemsenc>=20:    print "Wizard   2/4"
  elif    player.itemsenc>=5:     print "Wizard   1/4"
  elif    player.itemsenc<5:      print "????     0/4"

  print "\nEconomy"
  if      player.totalgld>=10000: print "Gold!!   4/4"
  elif    player.totalgld>=5000:  print "Gold!!   3/4"
  elif    player.totalgld>=2500:  print "Gold!!   2/4"
  elif    player.totalgld>=1000:  print "Gold!!   1/4"
  elif    player.totalgld<1000:   print "????     0/4"

  common.getch()

def showstats(player):
  """
  Displays character stats on screen
  """

  common.version()
  print "%s - Character sheet - Stats\n"  %(player.name)

  print "Exploration"
  print "Floors explored:     %i"       %(player.totalfl)
  print "Steps:               %i"       %(player.steps)

  print "\nCombat"
  print "Attacks launched:    %i"       %(player.totalatks)
  try:     print "Hits:                %i (%i%%)"   %(player.totalhits,int(round((100*player.totalhits)/player.totalatks)))
  except : print "Hits:                %i (--%%)"   %(player.totalhits)
  print "Total damage:        %i"       %(player.totaldmg)
  try:     print "Average damage:      %i"          %(round(player.totaldmg/player.totalhits))
  except : print "Average damage:      0"
  print "Total damage taken:  %i"       %(player.totalrcv)
  print "Traps stepped on:    %i"       %(player.totaltrp)
  print "Mobs killed:         %i"       %(player.kills)
  print "Max hit damage:      %i"       %(player.maxdmg)

  print "\nItems"
  print "Items picked:        %i"       %(player.itemspck)
  print "Items destroyed:     %i"       %(player.itemsdst)
  print "Items enchanted:     %i"       %(player.itemsenc)
  print "Maximum enchant lv:  %i"       %(player.maxench)    
  print "Potions taken:       %i"       %(player.totalpot)

  print "\nEconomy"
  print "Gold earned:         %i"       %(player.totalgld)
  print "Gold spent:          %i"       %(player.totalspn)
  print "Items sold:          %i"       %(player.totalsll)
  print "Items bought:        %i"       %(player.totalbuy)
  common.getch()

def buyitem(vendor,player):
  """
  Display the list of items available for buying from the vendor
  """

  while 1:
    common.version()
    print "Shop - Buy items (%iG)\n" %player.pocket
    for i in range(len(vendor.forsale)): print str(i+1)+".- "+vendor.forsale[i].name+" ("+str(round(vendor.pricecalc(player)*vendor.forsale[i].price))+"G)"
    print "--"
    print "0.- Back"
    print "\n->",

    try:
      buymenuc=common.getch()
      if buymenuc=="0":
        print "Nice doing business with you!"
        common.getch()
        break

      itemprice==round(vendor.pricecalc(player)*vendor.forsale[int(buymenuc)-1].price)
      if player.pocket>itemprice:
        player.pocket-=itemprice
        player.totalspn+=itemprice
        if player.pickobject(vendor.forsale[int(buymenuc)-1]):
          print random.choice(msg.okay)
          vendor.keeper.rel+=1
          del vendor.forsale[int(buymenuc)-1]
          player.totalbuy+=1
          common.getch()
        else:
          print random.choice(msg.fail)
          common.getch()
      else:
        print random.choice(msg.fail)
        common.getch()
    except (ValueError, IndexError): pass

def sell(vendor,player):
  """
  Display the list of items in the inventory to sell
  """

  while 1:
    common.version()
    print "Shop - Sell items (%iG)\n"%player.pocket
    for i,j in enumerate(player.inventory):
      print "%i.- %s (%iG)"%(i, j.name, round(player.inventory[i].price/vendor.pricecalc(player)))
    print "--\n0.- Back\n->",

    try:
        sellmenuc=common.getch()
        if sellmenuc=="0":
          print "Nothing else? I can pay you with roaches!"
          common.getch()
          break
        player.pocket+=round(player.inventory[int(sellmenuc)-1].price/vendor.pricecalc(player))
        player.totalgld+=round(player.inventory[int(sellmenuc)-1].price/vendor.pricecalc(player))
        player.totalsll+=1
        vendor.forsale.append(copy.copy(player.inventory[int(sellmenuc)-1]))
        del player.inventory[int(sellmenuc)-1]
        vendor.keeper.rel+=1
        print random.choice(msg.okay)
        common.getch()
    except (ValueError, IndexError): pass

def buypot(self,player):
  """
  Sells potions to the player. Three random potions are generated by the vendor.
  """
  
  while 1:
    common.version()
    print "Shop - Buy potions (%iG)\n"%player.pocket
    for i,j in enumerate(self.potforsale): 
      print "%i.- %s (%iG)"%(i, j.name, round(self.pricecalc(player)*self.potforsale[i].price))
    print "--"
    print "0.- Back"
    print "\n->",
    buypotmenu=common.getch()

    if buypotmenu=="0":
      print "Nice doing business with you!"
      common.getch()
      break

    try:
     
      if len(self.potforsale)!=0:
        if player.pocket>=round(self.pricecalc(player)*self.potforsale[int(buypotmenu)-1].price):
          if player.belt[0].name=="--EMPTY--": player.belt[0]=copy.copy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[1].name=="--EMPTY--": player.belt[1]=copy.copy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[2].name=="--EMPTY--": player.belt[2]=copy.copy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[3].name=="--EMPTY--": player.belt[3]=copy.copy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[3].name=="--EMPTY--": player.belt[3]=copy.copy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[3].name=="--EMPTY--": player.belt[3]=copy.copy(self.potforsale[int(buypotmenu)-1])
          player.pocket-=self.potforsale[int(buypotmenu)-1].price
          player.totalspn+=self.potforsale[int(buypotmenu)-1].price
          del self.potforsale[int(buypotmenu)-1]
          self.keeper.rel+=1
          print random.choice(msg.success)
          player.totalbuy+=1
          common.getch()

        else:
          print random.choice(msg.fail)
          common.getch()

    except (ValueError,IndexError): pass

def commerce(self,player):
  while 1:
    common.version()
    print "Shop\n"
    print random.choice(msg.welcome)
    print "\n1.- Sell"
    print "2.- Buy items"
    print "3.- Buy food/potions"
    print "4.- Chat"
    print "--"
    print "0.- Back"
    print "\n->",
    commenu=common.getch()

    if commenu=="1":self.sell(player)
    if commenu=="2":self.buyit(player)
    if commenu=="3":self.buypot(player)
    if commenu=="4":parser.chat(self.keeper,player)
    if commenu=="0":
      print random.choice(msg.goodbye)
      common.getch()
      break
    else: pass

def mainmenu():
  """
  Main menu function. Loads the configuration file and enters the menu loop.
  """ 

  #Main menu
  while 1:
    common.version()
    print "Main menu\n"
    print "%i.- Play"               %(1)
    print "%s.- Quick play"         %(2)
    print "%s.- Options"            %(3)
    print "%s.- Credits"            %(4)
    print "%s.- Test utilities\n--" %(5)
    print "%s.- Help"               %(9)
    print "%s.- Exit\n->"           %(0)
    menu=common.getch()
    if menu=="1": crawl(0)
    if menu=="2": crawl(1)
    if menu=="3": cfg.options(0)
    if menu=="4": scroll(15)
    if menu=="5": test.testm()
    if menu=="9": help.help()
    if menu=="0":
      print "Close kirino (y/n)?"
      if common.getch()=="y": 
        os.system('clear')
        exit()

def printpldata(player):
  """
  Displays the player data on screen
  """

  print "HP: %i/%i, MP: %i/%i"%(player.hp2,player.HP,player.mp2,player.MP)
  print "FL %i Lv %i"%(fl,player.lv),
  if player.lv==1: print "(%i/5 xp)"%(player.exp)
  if player.lv>1:  print "%i/%i xp"%(player.exp,3*player.lv+(2*(player.lv-1)))
  for i in range(6): print "(%c) %s" %(quick[i],player.belt[i].name)

def newgame(quick=0):
  """
  This function displays the menu to create a new character.

  Receives an optionanl quick parameter. if 1, it generates a 40x40 dungeon and a random player.
  """

  global xsize
  global ysize
  cfg=config.config()

  #If quick is 1, generate everything randomly
  if quick:
    dung=dungeon.dungeon(50,50,1)
    hero=player.player(1)
    hero.enter(dung)

  #If not, go through the usual process
  elif not quick:
    while 1:
      purge()
      try:
        common.version()
        print "New game [1/5] Dungeon size\n~40x40 recommended\n"
        xsize=int(raw_input("Horizontal size: "))
        ysize=int(raw_input("Vertical size: "))
        if xsize<40 or ysize<20: print "Minimum size 40x20"
        else:
          print "%ix%i dungeon created"%(xsize,ysize)
          common.getch()
          break
      except ValueError: pass

    os.system('clear')
    dung=dungeon.dungeon(xsize,ysize,1)
    hero=player.player(0)
    hero.enter(dung,0)
    common.version()
    print "New game [2/5] Name\n"
    hero.name=raw_input("What is your name? ")
    #If name was left empty, pick a random one
    if len(hero.name)==0:
      with open("../data/player/names","r") as names:
        hero.name=random.choice(names.readlines()).strip()

    # setup stats arrays from dict saved in file
    racesarray=[]
    strarray=[]
    intarray=[]
    dexarray=[]
    perarray=[]
    conarray=[]
    chaarray=[]
    sys.path.insert(0, "../data/player")
    from races import stats
    for race in stats: racesarray.append(race)
    
    selected=0
    while 1:
      try:
        common.version()
        race = racesarray[selected]
        print "New game [3/5] Race\n"
        print "Select your race"
        print "<[%s] %s [%s]>"           %(cfg.west,race,cfg.east)
        print "STR %s \tINT %s \tDEX %s" %(stats[race]["STR"],stats[race]["INT"],stats[race]["DEX"])
        print "PER %s \tCON %s \tCHA %s" %(stats[race]["PER"],stats[race]["CON"],stats[race]["CHA"])
        print "%s: select"               %(cfg.quit)
        np=common.getch()
        if np==cfg.west and selected>0: selected-=1
        if np==cfg.east: selected+=1
        if np==cfg.quit:
          hero.race=racesarray[selected]
          hero.STR+=int(stats[race]["STR"])
          hero.INT+=int(stats[race]["INT"])
          hero.DEX+=int(stats[race]["DEX"])
          hero.PER+=int(stats[race]["PER"])
          hero.CON+=int(stats[race]["CON"])
          hero.CHA+=int(stats[race]["STR"])
          break
      except IndexError:
        if np==cfg.west: selected+=1
        if np==cfg.east: selected-=1
    
    with open("../data/player/classes","r") as file:
      classesarray=[i.rstrip() for i in file]
    selected=0
    
    while 1:
      try:
        common.version()
        print "New game [4/5] Class\n"
        print "Select your class"
        print "<[%s] %s [%s]>"  %(cfg.west,classesarray[selected],cfg.east)
        print "%s: select"      %cfg.quit
        np=common.getch()
        if np==cfg.west and selected>0: selected-=1
        if np==cfg.east: selected+=1
        if np==cfg.quit:
          hero.charclass=classesarray[selected]
          break
      except IndexError:
        if np==cfg.west: selected +=1
        if np==cfg.east: selected-=1
  return hero,dung

if __name__=="__main__": pass