#usr/bin/env python
import os
import random
import player
import mob

class dungeon:
  "Dungeon class"
  xsize=0
  ysize=0
  dungarray=[]
  filled=[]
  
  #Main dungeon generator, terrain only. Absolute minimum 40x20
  def __init__(self,x,y):
    self.xsize=x
    self.ysize=y
    self.dungarray=[]
    while self.debug()!=0: 
      #This fills the dungeon with # (Rock)
      for i in range (0,self.ysize):
        secondary=[]
        for j in range (0,self.xsize):
          secondary.append("#")
        self.dungarray.append(secondary)
            
      #Adds one big room  (minimum 4*4) per 40*40 space
      for v in range(self.xsize*self.ysize/1600):
        roomy=random.randrange(self.ysize/3)+4
        roomx=random.randrange(self.xsize/3)+4
        roomstarty=random.randrange(self.ysize-roomy)
        roomstartx=random.randrange(self.xsize-roomx)
        for a in range(roomstarty,roomstarty+roomy):
          for b in range(roomstartx,roomstartx+roomx):
            self.dungarray[a][b]="."
        #Mark each room with a D on a random spot inside it
        self.dungarray[random.randrange(roomstarty,roomstarty+roomy)][random.randrange(roomstartx,roomstartx+roomx)]="D"
            
      #Adds three small rooms (minimum 2*2) per 20x20 space
      for v in range(self.xsize*self.ysize/400):
        roomy=random.randrange(self.ysize/5)+2
        roomx=random.randrange(self.xsize/5)+2
        roomstarty=random.randrange(self.ysize-roomy)
        roomstartx=random.randrange(self.xsize-roomx)
        for a in range(roomstarty,roomstarty+roomy):
          for b in range(roomstartx,roomstartx+roomx):
            self.dungarray[a][b]="."
        #Mark each room with a D on a random spot inside it
        self.dungarray[random.randrange(roomstarty,roomstarty+roomy)][random.randrange(roomstartx,roomstartx+roomx)]="D"
            
      #Random halls: add some random halls.
      for t in range (self.ysize*self.xsize/800):      #Pending to be fixed
        randomy=random.randrange(self.ysize)
        randomx=random.randrange(self.xsize)
        randleny=random.randrange(self.ysize*2/3)
        randlenx=random.randrange(self.xsize*2/3)
        #I'm not sure what this does
        for a in range (randomy,randomy+randleny):
          if randomy+randleny==self.ysize:
            self.dungarray[a][randomx]="."
          if a==randleny-1:
            self.dungarray[a][randomx]="D"
        for b in range (randomx,randomx+randlenx):
          if randomx+randlenx==self.xsize:
            self.dungarray[randomy][b]="."
          if b==randlenx-1:
            self.dungarray[randomy][b]="D"
                  
      #Connect rooms: create halls between positions with "D" (Rooms)
      #Skip this part, reading it gives cancer.
      #Looks for Ds in the dungeon array
      var=0
      for i in range(self.ysize):
        for j in range(self.xsize):
          if self.dungarray[i][j]=="D":
            for k in range(self.ysize):
              for l in range(self.xsize):
                if self.dungarray[k][l]=="D":
                #Generate hall connecting (i,j) and (k,l), the positions of the last 2 Ds found.
                  if i>k:
                    for m in range(i-k):
                      self.dungarray[i-m][j]="."
                    if j>l:
                      for n in range(j-l):
                        self.dungarray[k][j-n]="."
                    else:
                      for n in range(l-j):
                        self.dungarray[k][l-i-m]="."
                  else:
                    for m in range(k-i):
                      self.dungarray[k-m][l]="."
                      var=m
                    if j>l:
                      for n in range(j-l):
                        self.dungarray[k-var][j-n]="."
                    else:
                      for n in range(l-j):
                        self.dungarray[k-var][l-n]="."
                        #I still don't know how the fuck I made this work
          
      #This generates random coordinates for the entrance tile (A)
      entrancey=random.randrange(self.ysize)
      entrancex=random.randrange(self.xsize)
      while self.dungarray[entrancey][entrancex]!=".":
        entrancey=random.randrange(self.ysize)
        entrancex=random.randrange(self.xsize)
      self.dungarray[entrancey][entrancex]="A"
            
      #This generates random coordinates for the exit tile (X)
      #The conditions are
      # 1)being more than half of the total vertical or horizontal distance apart to avoid making it too easy
      # 2)not being in a tile that has nothing on it (.)
      #The second condition has priority. If after 100 cycles it hasn't found a position that satisifies both, it will be placed on a random empty tile.
      #The loop limit can be adjusted, but it makes no difference (Tried with limits up to a billion)
      exity=entrancey
      exitx=entrancex
      counter=0
      while abs(entrancex-exitx)<self.xsize/2 or abs(entrancey-exity)<self.ysize/2:
        counter += 1
        if counter>100:
          break
        while self.dungarray[exity][exitx]!=".":
      	  exity=random.randrange(self.ysize)
      	  exitx=random.randrange(self.xsize)
      self.dungarray[exity][exitx]="X"
            
      #Removes any D from the rooms previously created
      for i in range (len(self.dungarray)):
      	for j in range (len(self.dungarray[i])):
      	  if self.dungarray[i][j]=="D":
      	    self.dungarray[i][j]="."
      	  
      # Adds spaces in random positions with rocks, one for every 3x3 zone.
      # for i in range(0,self.xsize*self.ysize/9):
      # 	randx=random.randrange(self.xsize)
      # 	randy=random.randrange(self.ysize)
      # 	if self.dungarray[randy][randx]=="#":
      #    self.dungarray[random.randrange(self.ysize)][random.randrange(self.xsize)]="."
      # 	else: pass
            
      #Dungeon should be done

      #Initializes the filled array so it has the same sizent content as the dungarray
      self.filled=[]
      for i in range (0,self.ysize):
        secondary=[]
        for j in range (0,self.xsize):
          secondary.append("#")
        self.filled.append(secondary)
      #Fills the filled array with the dungarray data
      for i in range (0,self.ysize):
        for j in range (0,self.xsize):
          self.filled[i][j]=self.dungarray[i][j]
      
      
  #Dump the dung. Generates a list of coordinates and tile type 
  #place indicates where. 0 is return to console, anything else dumps it to a file
  #Avoid dumping to console with big dungeons, output turns out unreadable
  def dumpdung(self,place): 
    if place==0:
      #Dump to file mode.
      with open("kirino.dump","a") as dump:
        dump.write ("\n ###################### \n")
  	for i in range (0,len(self.dungarray)):
  	  for j in range (0,len(self.dungarray[i])):
  	    if self.dungarray[i][j]=="#":
                dump.write ("(")
                dump.write (str(i+1))
                dump.write (", ")
                dump.write (str(j+1))
                dump.write (")")
                dump.write (" Rock \n")
  	    elif self.dungarray[i][j]=="A":
                dump.write ("(")
                dump.write (str(i+1))
                dump.write (", ")
                dump.write (str(j+1))
                dump.write (")")
                dump.write (" Entrance \n")
  	    elif self.dungarray[i][j]=="X":
                dump.write ("(")
                dump.write (str(i+1))
                dump.write (", ")
                dump.write (str(j+1))
                dump.write (")")
                dump.write (" Exit \n")
  	    elif self.dungarray[i][j]==".":
                dump.write ("(")
                dump.write (str(i+1))
                dump.write (", ")
                dump.write (str(j+1))
                dump.write (")")
                dump.write (" Hallway \n")
  	    elif self.dungarray[i][j]=="D":
                dump.write ("(")
                dump.write (str(i+1))
                dump.write (", ")
                dump.write (str(j+1))
                dump.write (")")
                dump.write (" Undeleted room marker \n")
  	    else:
                dump.write ("(")
                dump.write (str(i+1))
                dump.write (", ")
                dump.write (str(j+1))
                dump.write (")")
                dump.write (" Unrecognised value (")
                dump.write (self.dungarray[i][j])
                dump.write (")")
    else:
      #Dump to console
      for i in range (0,len(self.dungarray)):
	  for j in range (0,len(self.dungarray[i])):
	    if self.dungarray[i][j]=="#":
	      print (i+1,j+1),"Rock"
	    elif self.dungarray[i][j]=="A":
	      print (i+1,j+1),"Entrance"
	    elif self.dungarray[i][j]=="X":
	      print (i+1,j+1),"Exit"
	    elif self.dungarray[i][j]==".":
	      print (i+1,j+1), "Hallway"
	    elif self.dungarray[i][j]=="D":
	      print (i+1,j+1), "Undeleted room marker"
	    else:
	      print (i+1,j+1),"Unrecognised value",(self.dungarray[i][j])
	   
  #Map generator. Creates a map of the dungeon on screen.
  def map(self):
    for i in range (0,len(self.dungarray)):
      print ''.join(map(str,self.dungarray[i]))
      #TO-DO: Use colours in the console to print this, so the map on the console looks better (zero priority)
      
  #Advanced map. Displays an area of the map to be moved and scrolled    
  def advmap(self,x,y,xmapsize,ymapsize):
    mapstring=[]
    for i in range(ymapsize+1):
      mapstring.append([])
    #Adjusting for deviation
    x -= xmapsize/2
    y -= ymapsize/2
    #Replaces the marker if the input is bad
    if x+xmapsize>=self.xsize:
      x=self.xsize-xmapsize
    if y+ymapsize>=self.ysize:
      y=self.ysize-ymapsize
    #Assign loop
    counter=0
    for i in range(y,y+ymapsize):
      counter+=1
      for j in range(x,x+xmapsize):
        mapstring[counter].append(self.filled[i][j]) # Gives out of range errors sometimes.
    # Add the "player" marker (a marker in the middle of the map, not in the actual player position)
    # mapstring[(ymapsize/2)+1][xmapsize/2]="8"
    #Print loop
    for i in range(len(mapstring)):
      print ''.join(map(str,mapstring[i]))
  
  #Generates an advmap (20x10) centered on the position    
  def advmapcoords(self,x,y):
    self.advmap(x,y,20,10)

  #Generates a minimap (advmap centered on the player)
  def minimap(self,player):
    self.advmapcoords(player.xpos,player.ypos)

    
  #Debug dungeon 
  #Returns an integer as error condition code:
  #	EC0: (This is not actually an error, everything is fine)
  #	EC1: There is no entrance or exit
  #	EC2: It's below the minimum size
  #	EC3: Can't reach the exit from the entrance (pending)
  #	EC4: There are halls unconnected or unreachable (pending)
  #Used in the constructor, although it can be invoked anytime.
  def debug(self):
    #Making sure the dungeon is over the minimum size
    if self.xsize<40 or self.ysize<20:
      return(2,"minimum size 40x20")
    else:
    #Checks if the entrance and exit are still there
      entrance=0
      exit=0
      for i in range(len(self.dungarray)):
        for j in range(len(self.dungarray[i])):
          if self.dungarray[i][j]=="A":
            entrance += 1
          if self.dungarray[i][j]=="X":
            exit += 1
      if entrance!=1 or exit!=1:
        return(1,"no entrance or exit found, or more than one entrances or exists ")
      else:
      #Checks if X is reachable from A (Unnecessary, but pending. Low priority)
        pass
        return(0)
  #Fills the dungeon temporarily with PC, NPC, object and mob markers. 
  #Needs a player, the object array (Pending) and the mob array (pending)
  #Does not return anything, but modifies the filled array
  def fill(self,player):
    for i in range (0,self.ysize):
      secondary=[]
      for j in range (0,self.xsize):
        secondary.append("#")
      self.filled.append(secondary)
    #Fills the filled array with the dungarray data
    for i in range (0,self.ysize):
      for j in range (0,self.xsize):
        self.filled[i][j]=self.dungarray[i][j]
    #Places the player marker in the filled array
    self.filled[player.ypos][player.xpos]="8"