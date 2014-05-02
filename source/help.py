#usr/bin/env python 
"""
Help function. Contains help menus and text for the functions in the game.
"""
import os, sys
import dungeon, item, parser,player
import common, config

def help():
  """
  Help main menu. Gives access to the tutorial, descriptions and such
  """
  while 1:
    sys.stdout.flush() 
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

def keyhelp():
  """
  Displays all the keys that can be used while crawling and their function.
  """

  cfg=config.config()
  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Key help\n"
  print "Movement\n"
  print "  "+cfg.northwest+" "+cfg.north+" "+cfg.northeast
  print "   \|/"
  print "  "+cfg.west+"-X-"+cfg.east
  print "   /|\ "
  print "  "+cfg.southwest+" "+cfg.south+" "+cfg.southeast
  print "Next floor:      "+cfg.nextf+"\n"

  print "Inventory\n"
  print "Belt item 1:     "+cfg.quick1
  print "Belt item 2:     "+cfg.quick2
  print "Belt item 3:     "+cfg.quick3+"\n"

  print "Actions\n"
  print "Input mode:      "+cfg.console
  print "Character sheet: "+cfg.charsh
  print "Options menu:    "+cfg.opt
  print "Quit:            "+cfg.quit
  print "Report dungeon:  "+cfg.report+"\n"
  print "Press any key to continue"
  common.getch()

def about():
  """
  Gives information about the game
  """

  sys.stdout.flush() 
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
    sys.stdout.flush() 
    os.system('clear')
    common.version()
    print "Help - Using kirino"
    print ""
    print "1.- General introduction"
    print "2.- Crawling screen"
    print "3.- Character sheet"
    print "4.- Items and inventory"
    print "5.- Saving and loading"
    print "6.- Word parser"
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
    if fhmen=="6":
      parserh()
    if fhmen=="0":
      break

def introh():
  """
  Small introduction to the game and basic controls
  """

  sys.stdout.flush() 
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

  sys.stdout.flush() 
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
  sys.stdout.flush() 
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

def parserh():
  """
  Information about the word parser
  """

  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Help - Using kirino - Word parser"
  print ""
  print "Kirino has a very simple word parser that processes basic instructions, such as move, look, hit and such"
  print "The parser needs, however, certain syntax requirements in the sentences that are passed to it"
  print ""
  print "First, the first word must be a verb. 'Go north' is an accepted expression, while 'I want to go north' it's not."
  print "Second, the simpler the sentences are, the better. 'Drop sword' will have the same effect as 'Drop sword from inventory to the ground'."
  print "Third, some of the words in a sentence can be ignored. The parser does not analyze the full sentence, it only examines the first word and processes the rest accordingly."
  print ""
  raw_input("Go back")

def saveh():
  """
  Information about saving and loading characters and configuration
  """

  sys.stdout.flush() 
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

  sys.stdout.flush() 
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

  sys.stdout.flush() 
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

  cfg=config.config()

  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Help - Using kirino - Tutorial - Introduction"
  print ""
  print "Hello there! Welcome to Kirino"
  print "This is a console-based dungeon crawler. In this tutorial you will learn the basic controls and game mechanics."
  print ""
  print "press any key to continue",
  common.getch()

  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Help - Using kirino - Tutorial - Basic dungeons"
  print ""
  new=dungeon.dungeon(40,20)
  new.map()
  print ""
  print "This is a dungeon. It's a labrynth made of rooms and halls. Every dungeon is randomly generated at the start of each level."
  print "You can see the entrance tile (A) and the exit tile (X) in it."
  print "Your objective is to reach the exit tile."
  print ""
  print "press any key to continue",
  common.getch()

  new.dungarray=[]
  with open("../data/tutorial/tutorial_1","r") as tuto1:
    for line in tuto1:
      line=line.strip()
      secondary=[]
      if line.startswith("#"):
        for char in line:
          secondary.append(char)
      new.dungarray.append(secondary)
  play=player.player(new)
  new.mobarray=[]
  new.fill(play,0)
  while 1:
    sys.stdout.flush()
    os.system('clear')
    common.version()
    print "Help - Using kirino - Tutorial - Basic dungeons"
    print ""
    print "Go ahead, give it a go!"
    print "use "+cfg.north+cfg.south+cfg.east+cfg.west+" to move horizontally"
    print "use "+cfg.northeast+cfg.northwest+cfg.southeast+cfg.southwest+" to move diagonally"
    print "When you reach the exit tile, press "+cfg.nextf
    print "You can change the key mapping in the option menu ("+cfg.opt+")"
    print "If you want to skip this part of the tutorial, press "+cfg.quit
    new.map()
    print ""
    print "-> ",
    tut1ch=common.getch()
    if tut1ch==cfg.north:
      play.move(new,1)
    if tut1ch==cfg.south:
      play.move(new,3)
    if tut1ch==cfg.east:
      play.move(new,4)
    if tut1ch==cfg.west:
      play.move(new,2)
    if tut1ch==cfg.northeast:
      play.move(new,6)
    if tut1ch==cfg.northwest:
      play.move(new,5)
    if tut1ch==cfg.southeast:
      play.move(new,8)
    if tut1ch==cfg.southwest:
      play.move(new,7)
    if tut1ch==cfg.quit:
      break
    if tut1ch==cfg.opt:
      cfg.options(1)
    if new.dungarray[play.ypos][play.xpos]=="X":
      if tut1ch==cfg.nextf:
        break

  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Help - Using kirino - Tutorial - Items"
  print ""
  print "You will find some things throughout the dungeons. Here is a brief summary."
  print "/ <- This is an object. It can be a weapon, clothing or something else. You won't know until you pick it up!"
  print "$ <- This is money! Pick it up, and you'll be able to use it to enchant weapons and buy things"
  print ""
  print "More things will be added on the future, make sure to check them out"
  print ""
  print "press any key to continue",
  common.getch()

  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Help - Using kirino - Tutorial - Enemies"
  print ""
  print "Of course, you will not be alone in the dungeons. Enemies will be around! Here is a small list:"
  print ""
  print "i - Zombie"
  print ""
  print "You can see the complete descriptions in the help menu"
  print ""
  print "press any key to continue",
  common.getch()

  sys.stdout.flush() 
  os.system('clear')
  common.version()
  print "Help - Using kirino - Tutorial - Parser"
  print ""
  print "You can use more than key presses to control your character. Kirino has a word parser that allows you to write small commands, IF style"
  print "If you have never played Interactive Fiction, playing games like adventure or zork for a few minutes will give you an idea"
  print "For example, you can use 'go north' to move north, or 'help' to access the help menu."
  print "Go ahead, try writing something and see if it works!"
  print ""
  print "press any key to continue"
  #Interactive tutorial goes here
  common.getch()