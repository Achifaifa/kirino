#!/usr/bin/env pyton
"""
Parser functions.

Processes a given string and performs the action the string is asking for

The parser, error and other data is located in ../data/parser/
The data is loaded by default in this module, so it is also loaded automagically when importing it.
To modify the data files, please read the instructions in these files.
"""
import os, random, sys
import common, config, help

dictionary={} #Dictionary with the verbs and action groups
errors=[] #Array with error messages
insistor={} #Dictionary with non-recognised inputs and number of repetitions

def parse(words,player,dungeon,config):
  """
  Main parsing function. 

  Splits the string and identifies action, target and options

  Needs a string to be parsed.

  Returns and action code and a message if needed.

  0) No action
    Look sentences only return a description of the place
    Empty, weird or non-interpretable sentences return an error string

  1) Move
    11 north
    12 south
    13 east
    14 west
    15 northeast
    16 northwest
    17 southeast
    18 southwest

    19 down (next floor)

  3) "use" actions
    31 use stairs (next floor)

  4) Combat actions
    Pending

  5) Configuration

  6) Help
    61 Help keys (Show key mapping)
    62 General help (Brings the help menu up)

  It evaluates the verb in the first position and the options next
  e.g.: go north, hit zombie, run southeast, walk nw, equip itemname, etc.
  If the first word of the string is not a verb (i.e. I want to walk north) a random generic error message will be returned.
  """

  #puts all the words from the input in a list
  keyw=words.split()
  if len(words)==0:
    return 0, random.choice(errors)+"\n"
  
  #Look for the first word (Verb) in the dictionary
  while 1:
    action=""
    for key,value in dictionary.iteritems():
      for a in value:
        if keyw[0]==a:
          action=key
          break
    break

  #Process the verb
  try:
    if len(action)==0:
      try:
        insistor[keyw[0]]+=1
      except KeyError:
        insistor[keyw[0]]=1
      if insistor[keyw[0]]<=2:
        return 0,random.choice(errors)+" \n"
      if 2<insistor[keyw[0]]<=5:
        return 0,"Still trying to do that? \n"
      if insistor[keyw[0]]>5:
        return 0,"Can't you stop talking about this "+keyw[0]+" thing? \n"
    else:
      #Identified movement command, process rest of the string
      if action=="move":
        if keyw[1]=="north" or keyw[1]=="n":
          return 11,""
        if keyw[1]=="south" or keyw[1]=="s":
          return 12,""
        if keyw[1]=="east" or keyw[1]=="e":
          return 13,""
        if keyw[1]=="west" or keyw[1]=="w":
          return 14,""
        if keyw[1]=="northeast" or keyw[1]=="north-east" or keyw[1]=="ne":
          return 15,""
        if keyw[1]=="northwest" or keyw[1]=="north-west" or keyw[1]=="nw":
          return 16,""
        if keyw[1]=="southeast" or keyw[1]=="south-east" or keyw[1]=="se":
          return 17,""
        if keyw[1]=="southwest" or keyw[1]=="south-west" or keyw[1]=="sw":
          return 18,""
        if keyw[1]=="down":
          return 19,""
      if action=="look":
        return look(dungeon,player)
      if action=="use":
        return use()
      if action=="equip":
        return equip()
      if action=="unequip":
        return equip()
      if action=="fight":
        return fight()
      if action=="cfg":
        return 5,""
      if action=="help":
        try:
          if keyw[1]=="keys":
            return 61,""
        except IndexError:
          help.help()
          return 62,""
      if action=="quit":
        return 9,""
  except IndexError:
    return 0,random.choice(errors)+"\n"

def look(dungeon,player):
  """
  Generates a description about what the player can see from its position. 

  It uses the filled array from the dungeon object to look for things.
  Talks about enemies, objects, money and space in a very general sense and without many details. 
  The output, verbosity and content will be improved in future versions.
  """

  #Counter variables
  zombies=piles=objects=0
  exit=entrance=0
  description="You are in a "
  type=-1 #0 is a room, 1 is a hall

  # Map analysis
  for i in range(player.ypos-5, player.ypos+5):
    for j in range(player.xpos-10, player.xpos+10):
      if dungeon.filled[i][j]=="i":
        zombies+=1
      if dungeon.filled[i][j]=="$":
        piles+=1
      if dungeon.filled[i][j]=="/":
        objects+=1
      if dungeon.filled[i][j]=="A":
        entrance=1
      if dungeon.filled[i][j]=="X":
        exit=1
      else:
        pass

  #Working on this
  if (dungeon.filled[player.ypos+1][player.xpos]=="." and dungeon.filled[player.ypos-1][player.xpos]=="." and 
      dungeon.filled[player.ypos][player.xpos+1]=="#" and dungeon.filled[player.ypos][player.xpos-1]=="#" ):
    description=description+"hall."
  if (dungeon.filled[player.ypos+1][player.xpos]=="#"and dungeon.filled[player.ypos-1][player.xpos]=="#"and 
      dungeon.filled[player.ypos][player.xpos+1]=="." and dungeon.filled[player.ypos][player.xpos-1]=="." ):
    description=description+"hall."
  else:
    description=description+"room."

  #Enemies
  if zombies==1:
    description=description+" You can see a zombie from your position."
  if 5>=zombies>1:
    description=description+" There are "+str(zombies)+" zombies around."
  if zombies>5:
    description=description+" You are surrounded by zombies!"

  #Gold  
  if piles>1:
    description=description+" There are also a few piles of gold."
  if piles==1:
    description=description+" There is also a pile of gold."

  #Objects
  if objects>1:
    description=description+" Some things are scattered around."
  if objects==1:
    description=description+" Something is lying on the floor."

  #Entrance and exit
  if not entrance and not exit:
    description=description+" There are no signs of the exit nearby."
  if entrance and exit:
    description=description+" You can see both the entrance and the exit! They are quite close together."
    return 0,description
  if entrance:
    description=description+" You can see the stairs you just used."
  if exit:
    description=description+" You can see the stairs to the next floor."

  return 0,description

def use(words):
  if words[1]=="stairs":
    return 31,""
  else:
    return 3,"you use stuff or do stuff with stuff"

def equip():
  return 3,"you equip or unequip stuff"

def fight():
  return 4,"You miss"

def load():
  """
  Data file loading function.

  Load the data in ../data/parser/words,errors to data structures
  """
  global dictionary
  global errors

  movewords=[]
  lookwords=[]
  usewords=[]
  equipwords=[]
  unequipwords=[]
  fightwords=[]
  cfgwords=[]
  helpwords=[]

  print "Loading dictionaries...    ",
  try:
    with open ("../data/parser/words","r") as wordsfile:
      for line in wordsfile:
        if not line.startswith('#'):
          line=line.strip()
          if line.partition(':')[0]=="movement":
            movewords=line.partition(':')[2].split()
            dictionary["move"]=movewords
          elif line.partition(':')[0]=="look":
            lookwords=line.partition(':')[2].split()
            dictionary["look"]=lookwords
          elif line.partition(':')[0]=="use":
            usewords=line.partition(':')[2].split()
            dictionary["use"]=usewords
          elif line.partition(':')[0]=="equip":
            equipwords=line.partition(':')[2].split()
            dictionary["equip"]=equipwords
          elif line.partition(':')[0]=="unequip":
            unequipwords=line.partition(':')[2].split()
            dictionary["unequip"]=unequipwords
          elif line.partition(':')[0]=="fight":
            fightwords=line.partition(':')[2].split()
            dictionary["fight"]=fightwords
          elif line.partition(':')[0]=="cfg":
            cfgwords=line.partition(':')[2].split()
            dictionary["cfg"]=cfgwords
          elif line.partition(':')[0]=="help":
            helpwords=line.partition(':')[2].split()
            dictionary["help"]=helpwords
          elif line.partition(':')[0]=="quit":
            quitwords=line.partition(':')[2].split()
            dictionary["quit"]=quitwords
    print "done"
  except IOError:
    raw_input("cound not load parser data files")
  try:
    print "Loading messages...        ",
    with open ("../data/parser/errors","r") as errorsfile:
      for line in errorsfile:
        if not line.startswith('#'):
          line=line.strip()
          errors.append(line)
    print "done."
    sys.stdout.flush() 
    os.system('clear')
  except IOError:
    raw_input("cound not load parser data files")
  sys.stdout.flush() 
  os.system('clear')


load()
# sys.stdout.flush() 
os.system('clear')
# print dictionary
# print errors

