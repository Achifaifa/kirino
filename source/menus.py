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


if __name__=="__main__": pass