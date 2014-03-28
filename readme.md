#Kirino v0.0.4
  
Basic console based dungeon crawler. 

##Release notes

v0.0.3 Required a major code re-structuring. Some of the minor functions may have been missed some changes and the game may crash under some circumstances. If this happens, please submit a message/issue/twitter mention with the crash message so it can be fixed ASAP (The error type, file and line number are enough). 
(This message will remain here until v0.0.5)

##How to use

run launch.py

Grab loot, run from zombies, explore dungeons. Help provided in game via the help menu (In the main menu and in the options menu during the game)

If you experience a crash, bug or any weird or unexpected behaviour that is not in the bugs file (./info/bugs), please consider reporting it.

**Note**: All the files in the `./player` folder are just examples to show how are those files structured and formatted. When starting a new game, it's safe (And recommended) to delete them.

##List of files/folders:

* data:               Files containing data for generators
  * inventory:          Inventory files
    * `atk_def_mod`:      List of attack/def modifiers
    * `attr_mod`:         List of basic attribute modifiers
    * `items_XX`          List of items and basic stats    
  * player:             Player files
    * `classes`:          List of player classes
    * `names`:            List of names
    * `races`:            List of player races
  * tutorial:           Files for the tutorial (Maps, etc)
    * `tutorial_1`
* docs:               Documentation folder (pydoc generated html files)
* info:               Information files
  * `bugs`:             List of bugs and weird behaviours to fix
  * `notes`:            Temporary notes on feature implementation
  * `todo`:             Ideas and stuff
* player:             Player files
  * `cemetery`:         Example cemetery file
  * `config`:           Example configuration file
  * `save`:             Example save file
* source:             Source file folder
  * `common.py`:        Common functions and procedures
  * `config.py`:        Configuration class
  * `dungeon.py`:       Dungeon class
  * `help.py`:          Help and tutorial
  * `item.py`:          Item class
  * `launch.py`:        Main menus and procedures.
  * `mob.py`:           Giant enemy class
  * `parser.py`:        Word parser (Empty)
  * `player.py`:        Player class
* `readme.md`:        This file

##Changelog

####**v0.0.4** (2014-03-28):
* New features:
  * Dead characters are now saved in a cemetery file
  * Added key mapping help screen
* Bugs fixed:
  * Fixed crash when executing `launch.py` from another directory
* Others:
  * A random name is now chosen if it's left empty when asked
  * Items can be saved and loaded with the player
  * The total number of floors explored is now saved with the character
  * When reporting a dungeon, the user is prompted for a message

####**v0.0.3** (2014-03-21):
* New features: 
  * Tutorial
* Bugs fixed
  * [0.0.3b] Fixed typo in error handling causing crashes
* Others:
  * Added diagonal movement
  * Restructured configuration code
  * Added config.py

####**v0.0.2** (2014-03-14):
* New features:
  * Keyboard events
  * Fog
  * Item enchanting
  * In-game help
  * Zombies
* Bugs fixed:
  * Minimap showing phantom halls
  * Various list index out of range errors in inventory and menus
  * Price of non-boosted items being zero
  * `nwse` being showed as the movement keys despite the configuration
  * Player stats remaining boosted after unequipping items
  * Objects being removed from the ground even if they were not picked up
  * Equipped items not modifying player's secondary attributes
  * Unequipped objects being destroyed
  * Total attack and defense stats stacking when switching items
  * [0.0.2b] Zombies attacking from a long distance
  * [0.0.2c] Non-standard keys (Arrows etc) being accepted in options
  * [0.0.2c] Fixed input errors with empty strings
  * [0.0.2c] Mob movement causing indexErrors
* Others:
  * Cleaned code
  * Increased feedback in less obvious functions
  * Going to the next floor now levels the player up as many times as possible (Not just one)
  * Added more items, races and classes
  * Attribute boost from items now showing in crawl screen and character sheet
  * Going to the next floor now requires user input
  * Items in the inventory can be destroyed
  * [0.0.2c] Other visual adjustments

####**v0.0.1** (2014-03-07):
  First versioned release.