#usr/bin/env python
import os
import common

class config:
  """
  Configuration class. When instancing it it takes the variables from the configuration files and stores them in the instance.

  """ 

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
  nextf="m"

  def __init__(self):
    #Environment variables
    self.autosave=0
    self.fog=1

    #Key mapping variables
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
    self.nextf="m"

    #Checks if there is a config file. If it exists, loads the option variables from it
    if os.path.isfile("../player/config"):
      with open("../player/config","r") as configfile:
        for line in configfile:
          if not line.startswith('#'):
            if line.partition(':')[0]=="North":
              self.north=(line.partition(':')[2]).strip()          
            if line.partition(':')[0]=="South":
              self.south=(line.partition(':')[2]).strip()          
            if line.partition(':')[0]=="East":
              self.east=(line.partition(':')[2]).strip()         
            if line.partition(':')[0]=="West":
              self.west=(line.partition(':')[2]).strip()  
            if line.partition(':')[0]=="Northeast":
              self.northeast=(line.partition(':')[2]).strip() 
            if line.partition(':')[0]=="Northwest":
              self.northwest=(line.partition(':')[2]).strip() 
            if line.partition(':')[0]=="Southeast":
              self.southeast=(line.partition(':')[2]).strip() 
            if line.partition(':')[0]=="Southwest":
              self.southwest=(line.partition(':')[2]).strip()         
            if line.partition(':')[0]=="Sheet":
              self.charsh=(line.partition(':')[2]).strip()         
            if line.partition(':')[0]=="Options":
              self.opt=(line.partition(':')[2]).strip()          
            if line.partition(':')[0]=="Quit":
              self.quit=(line.partition(':')[2]).strip()   
            if line.partition(':')[0]=="Report":
              self.report=(line.partition(':')[2]).strip()          
            if line.partition(':')[0]=="Autosave":
              if line.partition(':')[2].strip()=="on":
                self.autosave=1
            if line.partition(':')[0]=="Fog":
              if line.partition(':')[2].strip()=="off":
                self.fog=0
            if line.partition(':')[0]=="Next floor":
              self.nextf=(line.partition(':')[2]).strip()

  def options(self,restricted):
    """
    Game options menu. This allows modification of the general options, such as key mappings, autosave, etc.
    If the restricted parameter is 1, it hides the options that should not be changed during the game (fog, etc)

    """
    global autosave
    global fog
    while 1:
      os.system('clear')
      common.version()
      print "Options"
      print ""
      if self.autosave==0:
        print "1.- Autosave [off]"
      if self.autosave==1:
        print "1.- Autosave [on]"
      print "    Saves the character between floors"
      if not self.fog and not restricted:
        print "2.- Fog [off]"
      if self.fog and not restricted:
        print "2.- Fog [on]"
      if restricted and self.fog:
        print "2.- Fog [on] [Locked]"
      if restricted and not self.fog:
        print "2.- Fog [off] [Locked]"
      print "    Hides the dungeon out of view range"
      print ""
      print "3.- Key mapping"
      print ""
      print "--"
      print "9.- Help"
      print "0.- Go back"
      print "->",
      opmen=common.getch()
      if opmen=="1":
        self.autosave=not self.autosave
      if opmen=="3":
        self.keymap()
      if opmen=="2" and not restricted:
        self.fog=not self.fog
      if opmen=="9":
        help.help()
      if opmen=="0":
        saveoptions(self)
        break

  #Keyboard mapping options menu. Saves the configuration to file at exit
  def keymap(self):
    """
    Key mapping configuration menu.
    """
    while 1:
      os.system('clear')
      common.version()
      print "Options - Keyboard mapping"
      print ""
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
      print ""
      print "->",
      keymenu=common.getch()
      if keymenu=="0":
        saveoptions(self)
        break
      if keymenu=="9":
        while 1:
          os.system('clear')
          common.version()
          print "Options - Keyboard mapping"
          print ""
          print "1.- Character sheet : "+self.charsh
          print "2.- Option menu: "+self.opt
          print "3.- Report dungeon: "+self.report
          print "4.- Quit dungeon: "+self.quit
          print "---"
          print "9.- More keys"
          print "0.- Go back"
          print ""
          print "->",
          keymenu2=common.getch()
          if keymenu2=="1":
            print "New key for 'Character sheet' "
            tempk=raw_input()
            if len(tempk)!=1:
              raw_input("Invalid key")
            if len(tempk)==1:
              self.charsh=tempk
          if keymenu2=="2":
            print "New key for 'Option menu' "
            tempk=raw_input()
            if len(tempk)!=1:
              raw_input("Invalid key")
            if len(tempk)==1:
              self.opt=tempk
          if keymenu2=="3":
            print "New key for 'Report dungeon' "
            tempk=raw_input()
            if len(tempk)!=1:
              raw_input("Invalid key")
            if len(tempk)==1:
              self.report=tempk
          if keymenu2=="4":
            print "New key for 'Quit dungeon' "
            tempk=raw_input()
            if len(tempk)!=1:
              raw_input("Invalid key")
            if len(tempk)==1:
              self.quit=tempk
          if keymenu2=="9":
            saveoptions(self)
            break
          if keymenu2=="0":
            saveoptions(self)
            menu()
      
      if keymenu=="1":
        print "New key for 'go north' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.north=tempk
      if keymenu=="2":
        print "New key for 'go south' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.south=tempk
      if keymenu=="3":
        print "New key for 'go east' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.east=tempk
      if keymenu=="4":
        print "New key for 'go west' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.west=tempk
      if keymenu=="5":
        print "New key for 'go northeast' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.northeast=tempk
      if keymenu=="6":
        print "New key for 'go northwest' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.northwest=tempk
      if keymenu=="7":
        print "New key for 'go southeast' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.southeast=tempk
      if keymenu=="8":
        print "New key for 'go southwest' "
        tempk=raw_input()
        if len(tempk)!=1:
          raw_input("Invalid key")
        if len(tempk)==1:
          self.southwest=tempk

def saveoptions(self):
  """
  Option saving function. Takes all the configuration variables and writes them into a file.
  The file is located in ../player/, if the directory does not exist this creates the directory and the file.
  """
  if not os.path.exists("../player/"):
    os.makedirs("../player/")
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
    configfile.write("Sheet:"+self.charsh+"\n")
    configfile.write("Options:"+self.opt+"\n")
    configfile.write("Quit:"+self.quit+"\n")
    configfile.write("Report:"+self.report+"\n")
    configfile.write("Next floor:"+self.nextf+"\n")
    configfile.write("# \n")
    configfile.write("# Game options \n")
    configfile.write("# \n")
    if self.autosave==1:
      configfile.write("Autosave:on \n")
    if self.autosave==0:
      configfile.write("Autosave:off \n")
    if self.fog==1:
      configfile.write("Fog:on")
    if self.fog==0:
      configfile.write("Fog:off")

# cfg=config()
# cfg.options(0)