#! /usr/bin/env python

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

if __name__=="__main__": pass