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


if __name__=="__main__": pass