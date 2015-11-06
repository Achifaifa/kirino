#Kirino v0.2 (BETA)

![](https://api.shippable.com/projects/5637d6041895ca44742262e6/badge/master)  
Basic console based dungeon crawler. 

##Release notes

The current effort is to implement tests and some sort of CI solution, plus refactoring all the bad code and leaving it readable. Until that gets done, there are chances the master branch won't work at all. Check one of the previous versions (0.1.1a for the first presentation of the project, 0.1.7 for the last working version) if you want to play. 

Kirino v0.1.1 was presented at the open game compo at Euskal Encounter 22 and, surprisingly, ended up in the third place. I am very satisfied with myself and very glad someone in the jury understood all the work behind this heap of crap. Thanks to all the testers and people who helped!!

Development will continue at a slower pace; but new features, mobs and other things will be added while fixing bugs and rewriting parts of the code. Needless to say, suggestions and bug reports are still welcome.

##How to use

run launch.py. Grab loot, kill zombies, explore dungeons. Help provided in game via the help menu.

If you experience a crash, bug or any weird or unexpected behaviour, please consider reporting it by opening a github issue. Suggestions and opinions are also welcome.

**Note on player files**: All the files in the `./player` folder are just examples to show how are those files structured and formatted and contain my personal player data, saved games and other files. After downloading or cloning the repo, it's safe (And recommended) to delete that folder (Unless you want to play with my character). Make sure you save your player folder and replace it when you download the next version. If a new feature is added the save file can be updated with the new player things simply by loading and saving.

**Note on controls**: The default controls may not be totally logical for some players since I'm not using a qwerty layout. I tried to make them as 'global' as possible using common keys (zxcv) for movement. If it's the first time you play, go to the options menu and make sure everything is left to your liking. 

##OS specific information

* Unix/Linux: Works as-is as long as python 2.7 is installed.  
  Tested in Debian, Gentoo, OpenBSD, Ubuntu.
* Windows: Kirino can't be used in windows' command prompt. You can play it in this platform using a terminal emulator like putty. Different emulators may have different requirements to run python files, so read their documentation first. If you can't get any emulator working, I recommend using a Linux virtual machine.
* OSX: It's essentially a very expensive FreeBSD, so it should work. Maybe. I don't really care. (Untested)
* SSH: To play via ssh you need a compatible terminal. The default unix/linux one works, and you can use putty in windows.  
  Connect via ssh to achi.se (User `kirino`, pass `kirino`) and the game will launch automagically.  
  Please note that until a ssh-specific fork is developed you can still change the configuration file and other options, so check that out first before playing.

##Testers

@NesuMikuni [v0.0.8]  
@Seldan     [Since v0.0.2]  
Txapel      [Since v0.0.16]  
Valnar      [v0.0.1]  

##Aknowledgements and Thanks

@disassemblyline  
@jdiezlopez  
joeyespo (GH: getch code)  
@klon  
@marcan42  
@Ninji_Folf (Helped a lot with the server) 
@s7age  
stevenbird (GH: nltk source)  

