#Kirino v0.0.1
  
Basic console based dungeon crawler. 

##How to use

Run launch.py, follow instructions.

##List of files/folders:

* data:                Files containing data for generators
  * inventory:           Inventory files
    * `items`              List of items and basic stats
    * `attr_mod`:          List of basic attribute modifiers
    * `atk_def_mod`:       List of attack/def modifiers
  * player:            Player files
    * `races`:             List of player races
    * `classes`:           List of player classes
* docs:                Documentation folder (html files)
* info:                Information files
  * `bugs`:                List of bugs and weird behaviours to fix
  * `todo`:                Ideas and stuff
  * `notes`:               Temporary notes on feature implementation
* player:              Player files
  * `save`:                Example save file
  * `config`:              Example configuration file
* source:              Source file folder
  * `dungeon.py`:          Dungeon class and generator
  * `item.py`:             Item class
  * `launch.py`:           Main menus and procedures.
  * `mob.py`:              Generates a dude with a position.
  * `parser.py`:           Future word parser (Now empty)
  * `player.py`:           Basic player functionality.
* `readme`:                This file
