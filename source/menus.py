#! /usr/bin/env python

import common, config, dungeon, launch, player

def mainmenu():
  """
  Main menu function. Loads the configuration file and enters the menu loop.
  """ 

  #Main menu
  while 1:
    common.version()
    print "Main menu\n"
    print "%i.- Play"               %(1)
    print "%s.- Quick play\n"       %(2)
    print "%s.- Credits"            %(4)
    print "%s.- Help"               %(9)
    print "%s.- Exit\n->"           %(0)
    menu=common.getch()
    if menu in ["1","2"]: 
      launch.setup(int(menu)-1)
      launch.crawl()
    if menu=="4": scroll(15)
    if menu=="9": help()
    if menu=="0":
      print "Close kirino (y/n)?"
      if common.getch()=="y": 
        os.system('clear')
        exit()

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

def showachievements(player):
  """
  Shows a list of completed achievements.
  """

  common.version()
  print "%s - Character sheet - Achievements\n" %(player.name)

  print "Exploration"
  tfl=player.totalfl
  floors=4 if tfl>=500 else 3 if tfl>=250 else 2 if tfl>=100 else 1 if tfl>=10 else 0
  print "Elevator",["0/4", "1/4", "2/4", "3/4", "4/4"][floors]
  tst=player.steps
  steps=4 if tst>=10000 else 3 if tst>=5000 else 2 if tst>=1000 else 1 if tst>=500 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][steps]

  print "\nCombat"
  kills=4 if tst>=500 else 3 if tst>=250 else 2 if tst>=100 else 1 if tst>=10 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][kills]
  traps=4 if tst>=100 else 3 if tst>=50 else 2 if tst>=20 else 1 if tst>=5 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][traps]

  print "\nItems"
  picks=4 if tst>=100 else 3 if tst>=50 else 2 if tst>=20 else 1 if tst>=5 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][picks]
  destroys=4 if tst>=100 else 3 if tst>=50 else 2 if tst>=20 else 1 if tst>=5 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][destroys]
  enchants=4 if tst>=100 else 3 if tst>=50 else 2 if tst>=20 else 1 if tst>=5 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][enchants]

  print "\nEconomy"
  gold=4 if tst>=10000 else 3 if tst>=5000 else 2 if tst>=2500 else 1 if tst>=1000 else 0
  print ["0/4", "1/4", "2/4", "3/4", "4/4"][gold]

  common.getch()

def showstats(player):
  """
  Displays character stats on screen
  """

  avgdmg=round(player.totaldmg/player.totalhits) if player.totalhits else 0
  hitrate=str(int(round((100*player.totalhits)/player.totalatks))) if player.totalatks else "--"

  common.version()
  print "%s - Character sheet - Stats\n"  %(player.name)

  print "Exploration"
  print "Floors explored:     %i"       %player.totalfl
  print "Steps:               %i"       %player.steps

  print "\nCombat"
  print "Attacks launched:    %i"       %player.totalatks
  print "Hits:                %i (%i%%)"%(player.totalhits, hitrate)
  print "Total damage:        %i"       %(layer.totaldmg)
  print "Average damage:      %i"       %avgdmg
  print "Total damage taken:  %i"       %player.totalrcv
  print "Traps stepped on:    %i"       %player.totaltrp
  print "Mobs killed:         %i"       %player.kills
  print "Max hit damage:      %i"       %player.maxdmg

  print "\nItems"
  print "Items picked:        %i"       %player.itemspck
  print "Items destroyed:     %i"       %player.itemsdst
  print "Items enchanted:     %i"       %player.itemsenc
  print "Maximum enchant lv:  %i"       %player.maxench
  print "Potions taken:       %i"       %player.totalpot

  print "\nEconomy"
  print "Gold earned:         %i"       %player.totalgld
  print "Gold spent:          %i"       %player.totalspn
  print "Items sold:          %i"       %player.totalsll
  print "Items bought:        %i"       %player.totalbuy
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

      try: choice=int(buymenuc)
      except: pass
      itemprice=round(vendor.pricecalc(player)*vendor.forsale[choice-1].price)
      if player.pocket>itemprice:
        player.pocket-=itemprice
        player.totalspn+=itemprice
        if player.pickobject(vendor.forsale[choice-1]):
          print random.choice(msg.okay)
          vendor.keeper.rel+=1
          del vendor.forsale[choice-1]
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

      try: choice=int(sellmenuc)
      except: pass

      player.pocket+=round(player.inventory[choice-1].price/vendor.pricecalc(player))
      player.totalgld+=round(player.inventory[choice-1].price/vendor.pricecalc(player))
      player.totalsll+=1
      vendor.forsale.append(copy.copy(player.inventory[choice-1]))
      del player.inventory[choice-1]
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
      if len(self.potforsale):
        if player.pocket>=round(self.pricecalc(player)*self.potforsale[int(buypotmenu)-1].price):
          if   player.belt[0].name=="--EMPTY--": player.belt[0]=copy.deepcopy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[1].name=="--EMPTY--": player.belt[1]=copy.deepcopy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[2].name=="--EMPTY--": player.belt[2]=copy.deepcopy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[3].name=="--EMPTY--": player.belt[3]=copy.deepcopy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[4].name=="--EMPTY--": player.belt[4]=copy.deepcopy(self.potforsale[int(buypotmenu)-1])
          elif player.belt[5].name=="--EMPTY--": player.belt[5]=copy.deepcopy(self.potforsale[int(buypotmenu)-1])
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

def printpldata(w,gl):
  """
  Displays the player data on screen
  """

  print "HP: %i/%i, MP: %i/%i"%(w.hero.hp2,w.hero.HP,w.hero.mp2,w.hero.MP)
  print "FL %i Lv %i"%(gl.fl,w.hero.lv),
  if w.hero.lv==1: print "(%i/5 xp)"%(w.hero.exp)
  if w.hero.lv>1:  print "%i/%i xp"%(w.hero.exp,3*w.hero.lv+(2*(w.hero.lv-1)))
  for i in range(6): print "(%s) %s" %(eval("w.cfg.quick%i"%(i+1)),w.hero.belt[i].name)

def newgame(quick=0):
  """
  This function displays the menu to create a new character.

  Receives an optionanl quick parameter. if 1, it generates a 40x40 dungeon and a random player.
  """

  cfg=config.config()

  #If quick is 1, generate everything randomly
  if quick:
    dung=dungeon.dungeon(50,50,1)
    hero=player.player()
    hero.enter(dung)

  #If not, go through the usual process
  elif not quick:
    while 1:
      #purge()
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
    hero=player.player()
    hero.enter(dung)
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

def charsheet(self):
    """
    Character sheet. 

    Main menu to edit, view and configure characters and player options
    """

    menu=0
    while 1:
      self.secondary()
      common.version()
      print "%s - Character sheet\n"              %(self.name)
      print "Level %i %s %s"                      %(self.lv,self.race,self.charclass)
      if self.lv==1: print "%i/5 xp, %i points"   %(self.exp,self.points)
      if self.lv>1:  print "%i/%i xp, %i points"  %(self.exp,3*self.lv+(2*(self.lv-1)),self.points)
      print "%i floors explored"                  %(self.totalfl)
      print "Stomach is %i%% full\n"              %(self.stomach)
      self.getatr()
      print "\n1.- Spend points"
      print "2.- Inventory"
      print "3.- Character options"
      print "4.- Stats"
      print "5.- Achievements"
      print "\n8.- Save"
      print "9.- Load"
      print "\n0.- Exit"
      print "->",
      menu=common.getch()
      if   menu=="1": spend()
      elif menu=="2": invmenu()
      elif menu=="3": optmenu()
      elif menu=="4": statmenu()
      elif menu=="5": achievements()
      elif menu=="8":
        print "saving... "+self.save()
        common.getch()
      elif menu=="9":
        print "loading... "+self.load()
        common.getch()
      elif menu=="0": break
      pass

def spend(self):
  """
  Point spending menu.
  """

  choice=-1
  while choice!="0": 
    self.secondary()
    common.version()
    print "%s - Character sheet \n"%(self.name)
    print "Spend points"
    if self.points==0:  print "No points left! \n"
    else:               print "%i points left \n"%(self.points)

    #Determining cost of improving attributes (Based on AFMBE rules, sort of)  
    coststr=5 if self.STR<5 else ((self.STR/5)+1)*5
    costint=5 if self.INT<5 else ((self.INT/5)+1)*5
    costdex=5 if self.DEX<5 else ((self.DEX/5)+1)*5
    costper=5 if self.PER<5 else ((self.PER/5)+1)*5
    costcon=5 if self.CON<5 else ((self.CON/5)+1)*5
    costwil=5 if self.WIL<5 else ((self.WIL/5)+1)*5
    costcha=5 if self.CHA<5 else ((self.CHA/5)+1)*5

    #printing menu
    print "1.- [%i] STR %i (+%i)"%(coststr,self.STR,self.strboost)
    print "2.- [%i] INT %i (+%i)"%(costint,self.INT,self.intboost)
    print "3.- [%i] DEX %i (+%i)"%(costdex,self.DEX,self.dexboost)
    print "4.- [%i] CON %i (+%i)"%(costcon,self.CON,self.conboost)
    print "5.- [%i] PER %i (+%i)"%(costper,self.PER,self.perboost)
    print "6.- [%i] WIL %i (+%i)"%(costwil,self.WIL,self.wilboost)
    print "7.- [%i] CHA %i (+%i)"%(costcha,self.CHA,self.chaboost)
    print "\nSecondary attributes:"
    print 'END:', self.END, '     SPD:', self.SPD
    print "Max. HP: %i"%(self.HP)
    print "Max. MP: %i"%(self.MP)
    print "---"
    print "0.- Exit"
    print "\n->",
    choice=common.getch()

    #Choice cases
    if self.points==0: pass
    else:
      if choice=="1":
        if self.points>=coststr:
          self.STR+=1
          self.points-=coststr
      elif choice=="2":
        if self.points>=costint:
          self.INT+=1
          self.points-=costint
      elif choice=="3":
        if self.points>=costdex:
          self.DEX+=1
          self.points-=costdex
      elif choice=="4":
        if self.points>=costcon:
          self.CON+=1
          self.points-=costcon
      elif choice=="5":
        if self.points>=costper:
          self.PER+=1
          self.points-=costper
      elif choice=="6":
        if self.points>=costwil:
          self.WIL+=1
          self.points-=costwil
      elif choice=="7":
        if self.points>=costcha:
          self.CHA+=1
          self.points-=costcha
      elif choice=="0": pass
      else: pass

def optmenu(self):
  """
  Player options menu
  """

  coptmen=-1
  while coptmen!="0": 
    common.version()
    print "%s - Character sheet \n"%(self.name)
    print "1.- Change name"
    print "---"
    print "0.- Back"
    print "->",
    coptmen=common.getch()
    if coptmen=="1": self.name=raw_input("New name? ")
    if coptmen=="0": break

def invmenu(self):
    """
    Inventory menu and managing. 
    """

    while 1: 
      common.version()
      print "%s - Character sheet"%(self.name)

      #Print equipped items
      print "\nEquipped"
      parts=["Head","Face","Neck","Back","Chest","L hand","R hand","Ring","Belt","Legs","Feet"]
      for i,it in enumerate(parts): print "%02i [+%i/+%i] %s:  %s %s" %(i+1,self.equiparr[i].atk,self.equiparr[i].defn,it,self.equiparr[i].name,self.calcbonus(self.equiparr[i]))
      print "   [+%i/+%i] Total"                 %(self.totatk,self.totdefn)

      #Print everything in the inventory array
      print "\nInventory (%i G)" %(self.pocket)
      for i in range(len(self.inventory)): print "0%i [+%i/+%i] %s (%iG)[%i]" %(i+1,self.inventory[i].atk,self.inventory[i].defn,self.inventory[i].name,self.inventory[i].price,self.inventory[i].type)

      #Print the belt items
      print "\nBelt"
      parts=["B1","B2","B3"]
      for i in range(3): print "%s - %s"%(parts[i],self.belt[i].name)

      #Print the inventory action menu
      print "\nq - destroy item"
      print "w - enchant item"
      print "a - unequip item"
      print "b - use belt item"
      print "0 - Back"
      print "\n->",
      invmenu=common.getch()

      #Belt using menu
      if invmenu=="b":
        try:
          print "Which item? ",
          beltmen=common.getch
          self.use(self.belt[int(beltmen)-1])
        except IndexError: pass

      #Destroy an item from inventory
      elif invmenu=="q":
        print "Which item? "
        itdst=common.getch()
        if "0"<itdst<=str(len(self.inventory)):
          itemdestroyed=self.inventory[int(itdst)-1].name
          print "Destroy "+itemdestroyed+"? (y/n)"
          confirm=common.getch()
          if confirm=="y":
            self.itemsdst+=1
            del self.inventory[int(itdst)-1]
            raw_input(itemdestroyed+" destroyed")

      #Enchanting menu
      elif invmenu=="w":
        try:
          print "Which item? "
          itech=int(common.getch())
          if 0<itech<=len(self.inventory):
            self.inventory[int(itech)-1].enchant(self)
            if self.inventory[int(itech)-1].name==" ": del self.inventory[int(itech)-1]
        except ValueError: pass

      #Unequip menu
      elif invmenu=="a":
        try:
          unitem=int(raw_input("which item? "))
          if 0<int(unitem)<=len(self.equiparr) and self.equiparr[int(unitem)-1].name!=" ":
            temp=copy.copy(self.equiparr[int(unitem)-1])
            self.rembonuses(self.equiparr[int(unitem)-1])
            self.inventory.append(temp)
            self.equiparr[int(unitem)-1].reset()
            for i in self.equiparr: 
              if i.name=="--": i.reset()
        except ValueError: print "Invalid choice"

      #Exit from inventory menu
      elif invmenu=="0": break

      #Item flipping
      else:
        try:
          if 0<int(invmenu)<=len(self.inventory):
            #Flip only if the item is not a weapon
            if self.inventory[int(invmenu)-1].type not in [6,7]:

              #Transform the menu choice in an actual index
              invmenu=int(invmenu)-1

              #If swapping to a non-empty slot     
              if not self.equiparr[self.inventory[invmenu].type-1].name==" ":
                #Store the item in the equipped array in temp
                temp=self.equiparr[self.inventory[invmenu].type-1]
                #Remove bonuses
                self.rembonuses(temp)

              #If swapping to an empty space, just assign an empty object to temp
              else: temp=item.item(0)

              #Flip equip variables
              self.inventory[invmenu].equip=1
              temp.equip=0
              #Add bonuses
              self.addbonuses(self.inventory[invmenu])
              #Move the item to the equip and delete the inventory reference
              self.equiparr[self.inventory[invmenu].type-1]=self.inventory[invmenu]
              del self.inventory[invmenu]
              #Return the temp item to the inventory if it's not empty
              if temp.name!=" ": self.inventory.append(temp)

            #If it's a weapon, evaluate cases. 
            #1H goes to either left or right hand (Unequips left first if both full)
            elif self.inventory[int(invmenu)-1].type==6:
              
              #Case 1: Slot 6 empty
              if self.equiparr[5].name in [" ","--"]:

                #Flip equip variables
                self.inventory[int(invmenu)-1].equip=1
                #Add bonuses
                self.addbonuses(self.inventory[int(invmenu)-1])
                #Move the item to the equip and delete the inventory reference
                self.equiparr[5] = self.inventory[int(invmenu)-1]
                del self.inventory[int(invmenu)-1]

                #Remove any equipped 2H weapon
                if self.equiparr[6].name not in [" ","--"]:
                  self.rembonuses(self.equiparr[6])
                  self.equiparr[6].equip=0
                  self.inventory.append(copy.copy(self.equiparr[6]))
                  self.equiparr[6].reset()

              #Case 2: Slot 7 empty
              elif self.equiparr[6].name in [" ","--"]:

                #Flip equip variables
                self.inventory[int(invmenu)-1].equip=1
                #Add bonuses
                self.addbonuses(self.inventory[int(invmenu)-1])
                #Move the item to the equip and delete the inventory reference
                self.equiparr[6] = self.inventory[int(invmenu)-1]
                del self.inventory[int(invmenu)-1]

              #Case 3: Both slots used (Input slot)
              else: 
                while 1:
                  print "Where? (6-L hand; 7-R hand; 0-cancel)"
                  place=common.getch()
                  if place in ["6","7","0"]: break

                if place=="6":
                  #Remove equipment in slot 5
                  self.rembonuses(self.equiparr[5])
                  self.equiparr[5].equip=0
                  self.inventory.append(copy.copy(self.equiparr[5]))
                  self.equiparr[5].reset()
                  #Flip equip variables
                  self.inventory[int(invmenu)-1].equip=1
                  #Add bonuses
                  self.addbonuses(self.inventory[int(invmenu)-1])
                  #Move the item to the equip and delete the inventory reference
                  self.equiparr[5] = self.inventory[int(invmenu)-1]
                  del self.inventory[int(invmenu)-1]

                elif place=="7":
                  #Remove equipment in slot 6
                  self.rembonuses(self.equiparr[6])
                  self.equiparr[6].equip=0
                  self.inventory.append(copy.copy(self.equiparr[6]))
                  self.equiparr[6].reset()
                  #Flip equip variables
                  self.inventory[int(invmenu)-1].equip=1
                  #Add bonuses
                  self.addbonuses(self.inventory[int(invmenu)-1])
                  #Move the item to the equip and delete the inventory reference
                  self.equiparr[6] = self.inventory[int(invmenu)-1]
                  del self.inventory[int(invmenu)-1]

                elif place=="0": pass
              
            #2H unequips both hands first
            elif self.inventory[int(invmenu)-1].type==7:

              #Return elements 5 and 6 to inventory
              for i in [5,6]:

                #If swapping to a non-empty slot     
                if not self.equiparr[i].name in [" ","--"]:
                  #Store the item in the equipped array in temp
                  temp=self.equiparr[i]
                  #Remove bonuses
                  self.rembonuses(temp)

                #If swapping to an empty space, just assign an empty object to temp
                else: temp=item.item(0)
                #Flip equip variables
                temp.equip=0                
                #Return the temp item to the inventory if it's not empty
                if temp.name!=" ": self.inventory.append(copy.copy(temp))

              invmenu=int(invmenu)-1
              #Flip equip
              self.inventory[invmenu].equip=1
              #Add bonuses
              self.addbonuses(self.inventory[invmenu])
              #Move the item to the equip and delete the inventory reference
              self.equiparr[6]=copy.copy(self.inventory[invmenu])
              del self.inventory[invmenu]
              #Remove weapon bonus indicators in slot 5
              self.equiparr[5].reset()
              #Show that the weapon is 2H
              self.equiparr[5].name="--"

        except: pass

if __name__=="__main__": pass