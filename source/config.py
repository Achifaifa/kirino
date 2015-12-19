#! /usr/bin/env python
import os
import common, help

class config:
  """
  Configuration class. When instancing it it takes the variables from the configuration files and stores them in the instance.
  If there is no data on the file with a parameter, the default is taken
  
  Default variable data:

  #Environment variables
  autosave=0
  fog=1
  gomsg="Game Over"

  #Key mapping variables
  north="c"
  south="x"
  east="v"
  west="z"
  northeast=""
  northwest=""
  southeast=""
  southwest=""
  charsh="q"
  opt="o"
  quit=";"
  report="y"
  nextf="b"
  showkeys="k"
  showmap="m"
  console="/"
  quick1="a"
  quick2="r"
  quick3="s"
  quick4="t"
  quick5="d"
  quick6="b"
  """ 

  def __init__(self):
    #Environment variables
    self.autosave=0
    self.fog=1
    self.gomsg="Game Over"

    #Key mapping variables, initializing at default
    self.northeast=self.northwest=self.southeast=self.southwest=""
    self.north,self.south,self.east,self.west="c","x","v","z"
    self.charsh="q"
    self.opt="y"
    self.quit=";"
    self.report="u"
    self.nextf="b"
    self.showkeys="k"
    self.showmap="m"
    self.console="/"
    self.quick1="a"
    self.quick2="r"
    self.quick3="s"
    self.quick4="t"
    self.quick5="d"
    self.quick6="h"
    self.quick=[self.quick1,self.quick2,self.quick3,self.quick4,self.quick5,self.quick6]

    #Checks if there is a config file. If it exists, loads the option variables from it
    if os.path.isfile("../player/config"):
      with open("../player/config","r") as configfile:
        for line in configfile:
          if not line.startswith('#'):
            parA,parB=line.split(':')
            parB=parB.strip()
            if   parA=="North":         self.north=     parB          
            elif parA=="South":         self.south=     parB          
            elif parA=="East":          self.east=      parB         
            elif parA=="West":          self.west=      parB  
            elif parA=="Northeast":     self.northeast= parB 
            elif parA=="Northwest":     self.northwest= parB 
            elif parA=="Southeast":     self.southeast= parB 
            elif parA=="Southwest":     self.southwest= parB         
            elif parA=="Sheet":         self.charsh=    parB         
            elif parA=="Options":       self.opt=       parB          
            elif parA=="Quit":          self.quit=      parB 
            elif parA=="Show keys:":    self.showkeys=  parB 
            elif parA=="Show map:":     self.showmap=   parB  
            elif parA=="Input mode":    self.console=   parB
            elif parA=="Next floor":    self.nextf=     parB
            elif parA=="Quick slot 1":  self.quick1=    parB
            elif parA=="Quick slot 2":  self.quick2=    parB
            elif parA=="Quick slot 3":  self.quick3=    parB 
            elif parA=="Quick slot 4":  self.quick1=    parB
            elif parA=="Quick slot 5":  self.quick2=    parB
            elif parA=="Quick slot 6":  self.quick3=    parB 
            elif parA=="Report":        self.report=    parB 
            elif parA=="Game over msg": self.gomsg=     parB     
            elif parA=="Autosave" and parB=="on":   self.autosave=1
            elif parA=="Fog"      and parB=="off":  self.fog=0
            

  def options(self,restricted):
    """
    Game options menu. 

    This allows modification of the general options, such as key mappings, autosave, etc.

    If the restricted parameter is 1, it hides the options that should not be changed during the game (fog, etc)
    """

    global autosave
    global fog
    while 1: 
      common.version()
      print "Options \n"
      if not self.autosave: print "1.- Autosave [off]"
      if self.autosave:     print "1.- Autosave [on]"
      print "    Saves the character between floors"
      if not self.fog and not restricted:   print "2.- Fog [off]"
      if     self.fog and not restricted:   print "2.- Fog [on]"
      if restricted   and     self.fog:     print "2.- Fog [on] [Locked]"
      if restricted   and not self.fog:     print "2.- Fog [off] [Locked]"
      print "    Hides the dungeon out of view range"
      print "3.- Game over message: %s"%(self.gomsg)
      print "    Message displayed when the game ends"
      print "4.- Key mapping \n"
      print "--"
      print "9.- Help"
      print "0.- Go back"
      print "->",
      opmen=common.getch()
      if opmen=="1": self.autosave=not self.autosave
      if opmen=="2" and not restricted: self.fog=not self.fog
      if opmen=="3": self.gomsg=raw_input("New message?>")
      if opmen=="4": self.keymap(restricted)
      if opmen=="9": help.help()
      if opmen=="0":
        self.saveoptions()
        break

  #Keyboard mapping options menu. Saves the configuration to file at exit
  def keymap(self,restricted):
    """
    Key mapping configuration menu.
    """
    while 1: 
      common.version()
      print "Options - Keyboard mapping 1/3 \n"
      print "1.- Go north: %c"      %(self.north)
      print "2.- Go south: %c"      %(self.south)
      print "3.- Go east: %c"       %(self.east)
      print "4.- Go west: %c"       %(self.west)
      print "5.- Go northeast: %c"  %(self.northeast)
      print "6.- Go northwest: %c"  %(self.northwest)
      print "7.- Go southeast: %c"  %(self.southeast)
      print "8.- Go southwest: %c"  %(self.southwest)
      print "---"
      print "9.- More keys"
      print "0.- Go back"
      print "\n->",
      keymenu=common.getch()

      if keymenu=="1": self.north=newkey("go north")
      if keymenu=="2": self.south=newkey("go south")
      if keymenu=="3": self.east=newkey("go east")
      if keymenu=="4": self.west=newkey("go west")
      if keymenu=="5": self.northeast=newkey("go northeast")
      if keymenu=="6": self.northwest=newkey("go northwest")
      if keymenu=="7": self.southeast=newkey("go southeast")
      if keymenu=="8": self.southwest=newkey("go southwest")
      if keymenu=="0":
        self.saveoptions()
        break

      if keymenu=="9":
        while 1:
          common.version()
          print "Options - Keyboard mapping 2/3 \n"
          print "1.- Character sheet : %c"  %(self.charsh)
          print "2.- Option menu: %c"       %(self.opt)
          print "3.- Report dungeon: %c"    %(self.report)
          print "4.- Quit dungeon: %c"      %(self.quit)
          print "5.- Show keys: %c"         %(self.showkeys)
          print "6.- Input mode: %c"        %(self.console)
          print "7.- Quick slot 1: %c"      %(self.quick1)
          print "8.- Quick slot 2: %c"      %(self.quick2)
          print "---"
          print "9.- More keys"
          print "0.- Go back"
          print "\n->",
          keymenu2=common.getch()

          if keymenu2=="1": self.charsh=newkey("character sheet")
          if keymenu2=="2": self.opt=newkey("option menu")
          if keymenu2=="3": self.report=newkey("report dungeon")
          if keymenu2=="4": self.quit=newkey("quit")
          if keymenu2=="5": self.showkeys=newkey("show keys")
          if keymenu2=="6": self.console=newkey("input mode")
          if keymenu2=="7": self.quick1=newkey("quick slot 1")
          if keymenu2=="8": self.quick2=newkey("quick slot 2")
          #extra options
          if keymenu2=="0":
            self.saveoptions()
            break

          if keymenu2=="9":
            while 1:
              common.version()
              print "Options - Keyboard mapping 3/3"
              print "1.- Quick slot 3: %c"  %(self.quick3)
              print "2.- Quick slot 4: %c"  %(self.quick4)
              print "3.- Quick slot 5: %c"  %(self.quick5)
              print "4.- Quick slot 6: %c"  %(self.quick6)
              print "5.- Show map: %c"      %(self.showmap)
              print "6.- Next floor: %c"    %(self.nextf)
              print "---"
              print "9.- More keys"
              print "0.- Go back"
              print "\n->",
              keymenu3=common.getch()

              if keymenu3=="1": self.quick3=newkey("quick slot 3")
              if keymenu3=="2": self.quick3=newkey("quick slot 4")
              if keymenu3=="3": self.quick3=newkey("quick slot 5")
              if keymenu3=="4": self.quick3=newkey("quick slot 6")
              if keymenu3=="5": self.showmap=newkey("show map")
              if keymenu3=="6": self.nextf=newkey("next floor")
              if keymenu3=="0":
                self.saveoptions()
                break
              if keymenu3=="9":
                self.saveoptions()
                break

  def saveoptions(self):
    """
    Option saving function. 

    Takes all the configuration variables and writes them into a file.

    The file is ../player/config, if the directory does not exist this creates the directory and the file.
    """
    
    if not os.path.exists("../player/"): os.makedirs("../player/")
    with open("../player/config","w+") as configfile:
      configfile.write("# \n# Keyboard options \n# \n")
      configfile.write("North:"+self.north+"\n")
      configfile.write("South:"+self.south+"\n")
      configfile.write("East:"+self.east+"\n")
      configfile.write("West:"+self.west+"\n")
      configfile.write("Northeast:"+self.northeast+"\n")
      configfile.write("Northwest:"+self.northwest+"\n")
      configfile.write("Southeast:"+self.southeast+"\n")
      configfile.write("Southwest:"+self.southwest+"\n")
      configfile.write("Input mode:"+self.console+"\n")
      configfile.write("Sheet:"+self.charsh+"\n")
      configfile.write("Options:"+self.opt+"\n")
      configfile.write("Quit:"+self.quit+"\n")
      configfile.write("Report:"+self.report+"\n")
      configfile.write("Next floor:"+self.nextf+"\n")
      configfile.write("Show keys:"+self.showkeys+"\n")
      configfile.write("Show map:"+self.showmap+"\n")
      configfile.write("Quick slot 1:"+self.quick1+"\n")
      configfile.write("Quick slot 2:"+self.quick2+"\n")
      configfile.write("Quick slot 3:"+self.quick3+"\n")  
      configfile.write("Quick slot 4:"+self.quick4+"\n")
      configfile.write("Quick slot 5:"+self.quick5+"\n")
      configfile.write("Quick slot 6:"+self.quick6+"\n")    
      configfile.write("# \n# Game options \n# \n")
      configfile.write("Game over msg:"+self.gomsg+"\n")
      if self.autosave: configfile.write("Autosave:on \n")
      if not self.autosave: configfile.write("Autosave:off \n")
      if self.fog: configfile.write("Fog:on")
      if not self.fog: configfile.write("Fog:off")

def newkey(msg):
  """
  Changes a key.

  Needs a message with the long name of the key (e.g. 'go northwest' for the option variable northwest)
  returns the new value of the option variable (e.g. "New key for 'go northwest'" ->4 -> returns 4)
  If the lenght of the key is not 1, returns an error message.
  """

  tempk=raw_input("New key for '%s': "%msg)
  if len(tempk)==1: return tempk 
  else: raw_input("Invalid key")

if __name__=="__main__":
  try: os.chdir(os.path.dirname(__file__))
  except OSError: pass 
  common.version()
  print "Config module test"
  cfg=config()
  cfg.options(0)
