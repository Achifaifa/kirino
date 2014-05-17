#usr/bin/env python
import os, sys
import common, help

class config:
  """
  Configuration class. When instancing it it takes the variables from the configuration files and stores them in the instance.
  If there is no data on the file with a parameter, the default is taken
  
  #Environment variables
  autosave=0
  fog=1

  #Key mapping variables
  north="n"
  south="s"
  east="e"
  west="w"
  northeast=""
  northwest=""
  southeast=""
  southwest=""
  charsh="c"
  opt="o"
  quit="q"
  report="z"
  nextf="b"
  showkeys="k"
  showmap="m"
  console="/"
  quick1="1"
  quick2="2"
  quick3="3"
  """ 

  def __init__(self):
    #Environment variables
    self.autosave=0
    self.fog=1

    #Key mapping variables, initializing at default
    self.north="n"
    self.south="s"
    self.east="e"
    self.west="w"
    self.northeast=""
    self.northwest=""
    self.southeast=""
    self.southwest=""
    self.charsh="c"
    self.opt="o"
    self.quit="q"
    self.report="z"
    self.nextf="b"
    self.showkeys="k"
    self.showmap="m"
    self.console="/"
    self.quick1="1"
    self.quick2="2"
    self.quick3="3"

    #Checks if there is a config file. If it exists, loads the option variables from it
    if os.path.isfile("../player/config"):
      with open("../player/config","r") as configfile:
        for line in configfile:
          if not line.startswith('#'):
            parA=line.partition(':')[0]
            parB=line.strip().partition(':')[2]
            if parA=="North":         self.north=     parB          
            if parA=="South":         self.south=     parB          
            if parA=="East":          self.east=      parB         
            if parA=="West":          self.west=      parB  
            if parA=="Northeast":     self.northeast= parB 
            if parA=="Northwest":     self.northwest= parB 
            if parA=="Southeast":     self.southeast= parB 
            if parA=="Southwest":     self.southwest= parB         
            if parA=="Sheet":         self.charsh=    parB         
            if parA=="Options":       self.opt=       parB          
            if parA=="Quit":          self.quit=      parB 
            if parA=="Show keys:":    self.showkeys=  parB 
            if parA=="Show map:":     self.showmap=   parB  
            if parA=="Input mode":    self.console=   parB
            if parA=="Next floor":    self.nextf=     parB
            if parA=="Quick slot 1":  self.quick1=    parB
            if parA=="Quick slot 2":  self.quick2=    parB
            if parA=="Quick slot 3":  self.quick3=    parB 
            if parA=="Report":        self.report=    parB          
            if parA=="Autosave":
              if parB=="on":  self.autosave=1
            if parA=="Fog":
              if parB=="off": self.fog=0
            

  def options(self,restricted):
    """
    Game options menu. 

    This allows modification of the general options, such as key mappings, autosave, etc.

    If the restricted parameter is 1, it hides the options that should not be changed during the game (fog, etc)
    """

    global autosave
    global fog
    while 1: 
      os.system('clear')
      common.version()
      print "Options"
      print ""
      if self.autosave==0:  print "1.- Autosave [off]"
      if self.autosave==1:  print "1.- Autosave [on]"
      print "    Saves the character between floors"
      if not self.fog and not restricted:   print "2.- Fog [off]"
      if     self.fog and not restricted:   print "2.- Fog [on]"
      if restricted   and     self.fog:     print "2.- Fog [on] [Locked]"
      if restricted   and not self.fog:     print "2.- Fog [off] [Locked]"
      print "    Hides the dungeon out of view range\n"
      print "3.- Key mapping\n"
      print "--"
      print "9.- Help"
      print "0.- Go back"
      print "->",
      opmen=common.getch()
      if opmen=="1": self.autosave=not self.autosave
      if opmen=="3": self.keymap(restricted)
      if opmen=="2" and not restricted: self.fog=not self.fog
      if opmen=="9": help.help()
      if opmen=="0":
        saveoptions(self)
        break

  #Keyboard mapping options menu. Saves the configuration to file at exit
  def keymap(self,restricted):
    """
    Key mapping configuration menu.
    """
    while 1: 
      os.system('clear')
      common.version()
      print "Options - Keyboard mapping 1/3\n"
      print "1.- Go north: "+self.north
      print "2.- Go south: "+self.south
      print "3.- Go east: "+self.east
      print "4.- Go west: "+self.west
      print "5.- Go northeast: "+self.northeast
      print "6.- Go northwest: "+self.northwest
      print "7.- Go southeast: "+self.southeast
      print "8.- Go southwest: "+self.southwest
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
        saveoptions(self)
        break

      if keymenu=="9":
        while 1:
          sys.stdout.flush() 
          os.system('clear')
          common.version()
          print "Options - Keyboard mapping 2/3\n"
          print "1.- Character sheet : "+self.charsh
          print "2.- Option menu: "+self.opt
          print "3.- Report dungeon: "+self.report
          print "4.- Quit dungeon: "+self.quit
          print "5.- Show keys: "+self.showkeys
          print "6.- Input mode: "+self.console
          print "7.- Quick slot 1: "+self.quick1
          print "8.- Quick slot 2: "+self.quick2
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
            saveoptions(self)
            break

          if keymenu2=="9":
            while 1:
              os.system('clear')
              common.version()
              print "Options - Keyboard mapping 3/3"
              print "1.- Quick slot 3: "+self.quick3
              print "2.- Show map: "+self.showmap
              print "3.- Next floor: "+self.nextf
              print "---"
              print "9.- More keys"
              print "0.- Go back"
              print "\n->",
              keymenu3=common.getch()

              if keymenu3=="1": self.quick3=newkey("quick slot 3")
              if keymenu3=="2": self.showmap=newkey("show map")
              if keymenu3=="3": self.nextf=newkey("next floor")
              if keymenu3=="0":
                saveoptions(self)
                break
              if keymenu3=="9":
                saveoptions(self)
                break
          
def newkey(msg):
  """
  Changes a key.

  Needs a message with the long name of the key (e.g. 'go northwest' for the option variable northwest)
  returns the new value of the option variable (e.g. "New key for 'go northwest'" ->4 -> returns 4)
  If the lenght of the key is not 1, returns an error message.
  """

  tempk=raw_input("New key for '"+msg+"': ")
  if len(tempk)==1: return tempk 
  else: raw_input("Invalid key")

def saveoptions(self):
  """
  Option saving function. 

  Takes all the configuration variables and writes them into a file.

  The file is ../player/config, if the directory does not exist this creates the directory and the file.
  """
  
  if not os.path.exists("../player/"): os.makedirs("../player/")
  with open("../player/config","w+") as configfile:
    configfile.write("# \n")
    configfile.write("# Keyboard options \n")
    configfile.write("# \n")
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
    configfile.write("# \n# Game options \n# \n")
    if self.autosave==1: configfile.write("Autosave:on \n")
    if self.autosave==0: configfile.write("Autosave:off \n")
    if self.fog==1: configfile.write("Fog:on")
    if self.fog==0: configfile.write("Fog:off")