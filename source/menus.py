#! /usr/bin/env python

def enchant(item,player):
  """
  Menu for enchanting items

  Enchanting an item costs the current item price, and doubles its price.
  If the player has no money to pay for the enchant or the item is lv10, enchant() returns a message and passes.

  If the item is destroyed all its attributes are set to 0. 
  Deleting the resetted item from the inventory is done in the player module after calling the enchant() function.
  """

  

  oldname=item.name
  enchantprice=item.price

  if player.pocket<enchantprice:
    print "You don't have enough money"
    common.getch()
  elif self.enchantlv>=10:
    print "Maximum enchant level reached"
    common.getch()
  elif player.pocket>=enchantprice and self.enchantlv<10:
    player.pocket-=enchantprice
    player.totalspn+=enchantprice

    if item.enchant():
      player.itemsenc+=1
      raw_input("%s enchanted successfully"%(oldname))
    else: 
      raw_input("%s broke during enchanting"%(oldname))
  else: pass


if __name__=="__main__": pass