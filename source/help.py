#usr/bin/env python 
"""
Help function. Contains help menus and text for the functions in the game.
"""
import os
import common

def help():
  """
  Help main menu. Gives access to the tutorial, descriptions and such
  """
  while 1:
    os.system('clear')
    common.version()
    print "Help"
    print ""
    print "1.- About this game"
    print "2.- Using kirino"
    print "3.- Tutorial"
    print "---"
    print "0.- Back"
    print ""
    print "->",
    helpmen=common.getch()
    if helpmen=="2":
      funchelp()
    if helpmen=="1":
      about()
    if helpmen=="3":
      tutorial()
    if helpmen=="0":
      break
    else:
      pass

def about():
  """
  Gives information about the game
  """
  os.system('clear')
  common.version()
  print "Help - About kirino"
  print ""
  print "This is kirino, a console-based dungeon crawler"
  print ""
  print "If you have played nethack, you should already be familiar with the mechanics. If you haven't it may look confusing at first due to the text-only nature of it, but you will probably get used to it soon as it is not very different from similar 3D games."
  print ""
  print "The goal of the game is to crawl through as many dungeon floors as possible, collecting loot and money. If your HP reaches zero, you will die and the game will end. As simple as that!"
  print ""
  print "Please note that this is currently in a very early development phase and some basic features may not be implemented yet."
  print "If you have any suggestions or you want to report a bug or weird behaviour, feel free to do it using github issues at https://github.com/Achifaifa/kirino or contacting me at twitter (@Achifaifa) or via email (achi[at]hush[dot]ai)"
  print ""
  raw_input("Go back")

def funchelp():
  """
  Gives information about specific game functions and options
  """
  while 1:
    os.system('clear')
    common.version()
    print "Help - Using kirino"
    print ""
    print "1.- General introduction"
    print "2.- Crawling screen"
    print "3.- Character sheet"
    print "4.- Items and inventory"
    print "5.- Saving and loading"
    print "---"  
    print "0.- Back"
    print "->",
    fhmen=common.getch()
    if fhmen=="1":
      introh()
    if fhmen=="2":
      crawlingh()
    if fhmen=="3":
      charh()
    if fhmen=="4":
      itemh()
    if fhmen=="5":
      saveh()
    if fhmen=="0":
      break

def introh():
  """
  Small introduction to the game and basic controls
  """
  os.system('clear')
  common.version()
  print "Help - Using kirino - General introduction"
  print ""
  print "Welcome to kirino!"
  print "kirino is a basic console-based dungeon crawler. The main goal is to survive for as long as possible while crawling through endless dungeons."
  print ""
  print "To start a game, select 'new game' in the main menu, and then input the size of the dungeon you would like to play in."
  print "After being prompted for your name, the game will begin and you will find yourself in a randomly generated dungeon. Your race and class will be randomly chosen so you don't lose any time thinking about it ;)"
  print "Crawl through the dungeon, grab the loot, kill the monsters (soon) and locate the exit to the next floor!"
  print "If you have played any kind of RPG game before, all the elements in the screen will look familiar to you. If you are totally lost, feel free to try the tutorial out."
  print "For information on specific functions, please check the rest of the help"
  print ""
  raw_input("Go back")

def crawlingh():
  """
  description of the crawling screen elements
  """
  os.system('clear')
  common.version()
  print "Help - Using kirino - crawling screen (1/2)"
  print ""
  print "The crawling screen is where most of the action happens. It gives you information about you and the environment."
  print ""
  print "From top to bottom, you can see:"
  print "minimap; floor and location, level, race and class; experience and gold."
  print "HP, MP, primary and secondary attributes, including the attribute boost from items."
  print "keys available. They can be configured in the option menu"
  print ""
  raw_input("next")
  os.system('clear')
  common.version()
  print "Help - Using kirino - crawling screen (2/2)"
  print ""
  print "The minimap is composed by ascii characters:"
  print ""
  print "8 - your current position"
  print "# - A rock tile. You can't walk through"
  print ". - A floor tile. These are empty"
  print ""
  print "$ - Money. Walk over this tile to pick it up"
  print "/ - Item. Walk over to pick it up"
  print ""
  print "i - Zombie"
  print ""
  print "A - Stairs up. This is where you start on a level"
  print "X - Floor exit. Move here to go to the the next floor"
  print ""
  raw_input("Go back")

def saveh():
  """
  Information about saving and loading characters and configuration
  """
  os.system('clear')
  common.version()
  print "Help - Using kirino - Saving and loading"
  print ""
  print "-Saving and loading characters"
  print "  Once you are done playing, you may want to save your character for the next time. To do that, go to the character sheet and select 'save'."
  print "  All the information will be saved in a file located in ./player/save. This information includes things like your name, level, attributes and gold in your stash, but (at the moment) it does not save your inventory data, so all your items will be lost."
  print "  Saving a character will overwrite anything contained in the save file, so make sure you make a manual backup if you want one."
  print "  To load a previously saved character, simply select 'load' from the character sheet menu. The character will be replaced with the data you previously saved."
  print ""
  print "  kirino also has an autosave function. If enabled, it will automatically save your character every time you progress to the next dungeon. To enable it, simply go to the game options menu and switch it to [on]"
  print ""
  print "-Saving and loading configuration"
  print "Most of the controls can be customised. They are saved automatically to a text file in ./player/config. The configuration from this text file is automatically loaded when kirino starts."
  print "The options will save automatically (overwriting the previous file) whenever you exit an option menu"
  print ""
  raw_input("Go back")

def charh():
  """
  Information about the character sheet and the options in it
  """
  os.system('clear')
  common.version()
  print "Help - Using kirino - Character sheet"
  print ""
  print "The character sheet is where you can manage your character."
  print ""
  print "It shows the same information as the crawl screen, and it gives you options to:"
  print ""
  print "-Spend your points to improve your attributes"
  print "  Simply go to the point spending menu. You will see all your attributes, your attribute levels and how much it will cost you to upgrade a certain attribute."
  print ""
  print "-Manage your inventory"
  print "  See 'inventory' on the menu"
  print ""
  print "-Configure your character"
  print "  Select the characteristic you wish to modify and input the new value"
  print ""
  print "-Save and load your character"
  print "  See 'saving and loading'"
  print ""
  raw_input("Go back")

def itemh():
  """
  Information about items, inventory, enchanting, etc
  """
  os.system('clear')
  common.version()
  print "Help - Using kirino - Items and inventory"
  print ""
  print "Once in the inventory menu, you can equip, unequip, destroy and enchant items"
  print ""
  print "-Equipping, unequipping and destroying items"
  print "  To equip an item, simply write the inventory numbers it is assgined to (1-9) and the item will be equipped, automatically returning to your inventory any item you previously had in the slot it is assigned to"
  print "  To unequip an item, select 'unequip item' (Default a) and then write the equip number it has assigned (1-11). The item will then return to your inventory"
  print "  Destroying items is easy: Select the option in the menu (Default q) and then select the item you wish to destroy. The item must be in your inventory"
  print ""
  print "-Echanting items"
  print "  To enchant an item, select enchant item (Default w) and then select an item in your inventory. Enchanting an item costs the current item price and doubles its price (minimum 1G)"
  print "  Enchanting an item increases its attack or defense rating by 1 and adds random attribute boosts. Items can only be enchanted up to level 10 (item +10)"
  print "  Enchanting an item has a failure rate of 1%. If the enchanting fails, the item is destroyed."
  print ""
  raw_input("Go back")

def tutorial():
  """
  Small tutorial with basic controls and elements.
  Not implemented.
  """
  pass