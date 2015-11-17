#Changelog

##Current work

Current stable release: 0.1.7

####**v0.2** (Progress so far):
* New features:
* Bugs Fixed:
  * Fixed excessive multiple leveling bug
  * Fixed wrong message when hunger decreases HP
  * Fixed item pricing bug
  * Fixed bought consumables not going to the last 2 belt positions
* Others:
  * Code refactoring
  * Shippable CI integration
  * Unit tests
  * Moved user interaction to single module
  * Nerfed mana traps

##Old releases

####**v0.1.7** (2014-11-21):
* New features:
* Bugs fixed:
  * Fixed bug in credit scroll
  * [0.1.7b] Fixed space appearing randomly before title
* Others:
  * Code rewritten
  * Removed useless exit prompt

####**v0.1.6** (2014-11-07):
* New features: 
* Bugs fixed:
  * Fixed mobs respawning in the dungeon
  * Fixed item enchant displaying post-enchanting name
* Others: 
  * Rewrote code
  * [0.1.6b] Balanced mob and object generation
  * [0.1.6b] Updated parsing algorithms and code
  * [0.1.16c] Removed unnecesary sys imports
  * [0.1.16d] Merged a request and fixed crashes from request

####**v0.1.5** (2014-10-24):
* New features:
* Bugs fixed:
  * Fixed bad call to item generator
  * [0.1.5b] Fixed crash when picking money up
* Others:
  * Money dropped now depends on player level
  * Updated code
  * Launch.py is now executable
  * Adjusted will test rolls
  * [0.1.5b] Changed default controls

####**v0.1.4** (2014-10-17):
* New features:
* Bugs fixed:
  * Fixed issue with credit scrolling
  * Fixed crash when generating items
* Others:
  * Depurated code
  * Fixed and updated credits
  * Updated default controls

####**v0.1.3** (2014-09-13):
* New features:
* Bugs Fixed:
  * Fixed crash while launching
* Others:
  * Fixed non-critical syntax issues


####**v0.1.2** (2014-08-08):
* New features:
  * Removed the 110 stomach limit
  * Added more food types
* Bugs fixed:
  * Fixed crash when eating inocuous food
* Others:
  * Removed schedule file
  * Removed logo in main menu

####**v0.1.1** (2014-08-01):
* New features:
* Bugs fixed:
* Others:
  * Removed spanish help file
  * Corrected some code

####**v0.1.0** (2014-07-25):
* New features:
  * Potions now spawn on dungeons
* Bugs fixed:
  * Fixed crash when using items
  * Fixed crash when picking items up
  * Fixed game starting only on quick mode
  * Fixed footwear not generating
* Others:
  * Balanced armour
  * [0.1.1] Corrected layout
  * [0.1.1b] Removed some files

####**v0.0.18** (2014-07-18):
* New features:
* Bugs fixed:
  * Crash in mob individual test
  * Mobs having negative secondaries
* Others:
  * Potions appear (rarely) as drops
  * NPCs sell food
  * Mobs with a random level can be spawned
  * Added food to item individual testing

####**v0.0.17** (2014-07-11):
* New features:
* Bugs fixed:
  * Crash when falling through trap
* Others:
  * Food appears randomly on dungeons

####**v0.0.16** (2014-07-04):
* New features:
  * New mob: Dead dog
  * [0.0.16b] Hunger
* Bugs Fixed:
  * Fixed attribute display showing wrong numbers
  * [0.0.16b] Fixed weapon bonuses not disappearing when equipping 2Hs
* Others:
  * Default dungeon size changed to 50x50

####**v0.0.15** (2014-06-27):
* New features:
* Bugs fixed:
  * --EMPTY-- being shown as name when drinking potions
  * [0.0.15c] Crash when falling through traps
* Others:
  * Level increases whenever experience cap is reached.
  * Changed attribute display layout
  * [0.0.15b] Restructured classes
  * [0.0.15c] Default dungeon size changed to 70x70

####**v0.0.14** (2014-06-20):
* New features:
  * Stats
  * Achievements
  * Attack rolls for mobs and players
  * Added extra mobs (Snakes and bats)
  * [0.0.14b] Mob IA
* Bugs Fixed:
  * Crash when loading characters
  * Fixed NPCs selling empty items
  * Minimap showing terrain outside dungeon
  * Race and class selection menu showing twice
  * Crash when accessing belt from inventory
  * 1H and 2H weapons being used at the same time
  * Crash when generating random characters
  * [0.0.14c] Inventory not updating with 2H weapons
  * [0.0.14c] Mobs not disappearing after dying
* Others:
  * Willpower tests have to be passed to attack
  * Hitting flying enemies is now harder

####**v0.0.13** (2014-06-13):
* New features:
  * Loading mobs from files
* Bugs fixed:
  * [0.0.13b] Fixed crash when managing mobs
* Others:
  * Balanced zombies

####**v0.0.12** (2014-06-06):
* New features:
  * Custom game over message
  * [0.0.12+b] Individual module testing 
* Bugs fixed:
  * Fixed formatting issues
  * Fixed consumable generation crashes
* Others:
  * Cleaned code

####**v0.0.11** (2014-05-16):
* New features:
  * Tomes and scrolls
* Bugs fixed:
  * Crash when playing a small dungeon after a large one
* Others:
  * Peddlers have at least one potion for sale
  * [0.0.11b] Cleaned code

####**v0.0.10** (2014-05-09):
* New features:
  * Prestige system
  * Quick play
  * Traps
  * Test utilities
  * Willpower tests
  * Intelligence dependant explored map
* Bugs fixed:
  * Look instruction not working randomly
  * Crashes in potion buying menu
  * [0.0.10b] Fixed crashes in tutorial
* Others:
  * Cleaned crawling interface
  * Removed non working code
  * Expanded parser
  * Improved random character generator
  * [0.0.10b] Improved dungeon generator
  * [0.0.10b] Balanced trap rate/damage
  * [0.0.10b] Finished tutorial

####**v0.0.9** (2014-05-02):
* New features:
  * Potions
* Bugs fixed:
  * Save file having lots of empty items
  * Player having random starting attributes
  * Crash when launching from external directory
* Others:
  * Expanded parser
  * [0.0.9b] Added credits
  * [0.0.9b] Potion saving and loading
  * [0.0.9c] Fixed help module

####**v0.0.8** (2014-04-25):
* New features:
  * Combat system
  * [0.0.8b] Windows support
* Bugs fixed:
  * Some item messages not showing
  * HP and HP changing when opening sheet and loading characters
* Others:
  * Increased mob information
  * [0.0.8c] Charisma and vendor relationship influences price
  
####**v0.0.7** (2014-04-18):
* New features:
  * Word parser
  * NPC generator
  * Peddlers and vendors 
  * [0.0.7b] buying and selling items
* Bugs fixed:
  * [0.0.7b] Getting stuck at (0,0) when loading character
  * [0.0.7b] Crash when typing some invalid commands
  * [0.0.7c] Buying expensive items and ending with negative balance
  * [0.0.7c] Crash when pressing enter in trade menus
* Others:
  * Depurated code
  * Removed white spaces

####**v0.0.6** (2014-04-11):
* Bugs fixed:
  * Increasing stats also increases MP (Similar to bug fixed in v0.0.5)
* Others:
  * Save file is now deleted when dying
  * Depurated code
  * [0.0.6b] Improved message output

####**v0.0.5** (2014-04-04):
* Bugs fixed:
  * Increasing stats also increases HP
* Others:
  * Increased picked items/loot verbosity
  * Item attribute boost now appears in inventory
  * [v0.0.5b] Enabled white spaces

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
  * [0.0.4b] Race can now be selected
  * [0.0.4c] Class can now be selected

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
