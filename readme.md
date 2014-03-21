#Kirino v0.0.2d
  
Basic console based dungeon crawler. 

##How to use

Run launch.py, grab loot, run from zombies. Don't die or you will die (People die if they are killed).

Help provided in game via the help menu (In the main menu and in the options menu during the game)

If you experience a crash, bug or any weird or unexpected behaviour that is not in the bugs file (./info/bugs), please consider reporting it.

##List of files/folders:

* data:               Files containing data for generators
  * inventory:          Inventory files
    * `items`             List of items and basic stats
    * `attr_mod`:         List of basic attribute modifiers
    * `atk_def_mod`:      List of attack/def modifiers
  * player:             Player files
    * `races`:            List of player races
    * `classes`:          List of player classes
* docs:               Documentation folder (pydoc generated html files)
* info:               Information files
  * `bugs`:             List of bugs and weird behaviours to fix
  * `todo`:             Ideas and stuff
  * `notes`:            Temporary notes on feature implementation
* player:             Player files
  * `save`:             Example save file
  * `config`:           Example configuration file
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

####**v0.0.3** (2014-03-21):
* New features: 
  * Tutorial
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