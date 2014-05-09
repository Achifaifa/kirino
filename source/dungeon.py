#usr/bin/env python
import math, os, random
import common, mob, npc, player

class dungeon:
  """
  Creates and manages dungeons and dungeon displaying features

  #Size variables
  xsize=0       #Horizontal dungeon size
  ysize=0       #Vertical dungeon size

  #Dungeon arrays
  dungarray=[]  #Contains rock, empty, loot, etc
  filled=[]     #This is what will be displayed to the player
  explored=[]   #No use
  traps=[]      #Array with the traps on that floor

  #Mob and peddler data
  mobarray=[]   #Array of mobs walking through the dungeon
  vendorvar=0   #If 1, a vendor is generated in the floor
  """
  
  def __init__(self,x,y,vendor):
    """
    Class constructor. 

    Receives two integers (x,y) that define the horizontal and vertical size.

    It also receives a vendor variable. If set to 1 it generates a shop in a random position inside the dungeon.

    Minimum size is 40x20. If something smaller is given, defaults at the minimum.
    """

    if x<40:
      x=40
    if y<20:
      y=20
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
        roomstarty=random.randrange(1,self.ysize-roomy)
        roomstartx=random.randrange(1,self.xsize-roomx)
        for a in range(roomstarty,roomstarty+roomy):
          for b in range(roomstartx,roomstartx+roomx):
            self.dungarray[a][b]="."
        #Mark each room with a D on a random spot inside it
        self.dungarray[random.randrange(roomstarty,roomstarty+roomy)][random.randrange(roomstartx,roomstartx+roomx)]="D"
            
      #Adds three small rooms (minimum 2*2) per 20x20 space
      for v in range(self.xsize*self.ysize/400):
        roomy=random.randrange(self.ysize/5)+2
        roomx=random.randrange(self.xsize/5)+2
        roomstarty=random.randrange(1,self.ysize-roomy)
        roomstartx=random.randrange(1,self.xsize-roomx)
        for a in range(roomstarty,roomstarty+roomy):
          for b in range(roomstartx,roomstartx+roomx):
            self.dungarray[a][b]="."
        #Mark each room with a D on a random spot inside it
        self.dungarray[random.randrange(roomstarty,roomstarty+roomy)][random.randrange(roomstartx,roomstartx+roomx)]="D"
            
      #Random halls: add some random halls.
      for t in range (self.ysize*self.xsize/800):      #Pending to be fixed
        randomy=random.randrange(1,self.ysize-1)
        randomx=random.randrange(1,self.xsize-1)
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

      #Fill the borders of the dungeon so the player does not fall out
      for i in range(len(self.dungarray)):
        for j in range(len(self.dungarray[i])):
          if i==0:
            self.dungarray[i][j]="#"
          if i==len(self.dungarray):
            self.dungarray[i][j]="#"
          if j==0:
            self.dungarray[i][j]="#"
          if j==len(self.dungarray[i]):
            self.dungarray[i][j]="#"

      #Generate random halls (Up to 1/3 the total size from an empty tile in a random direction)
      #Vertical halls
      for i in range(self.xsize/20):
        count=0
        #Calculate lenght of the hall
        lenght=random.randrange(int(round(self.ysize/3)))
        while count<1000:
          tempx=random.randrange(self.xsize)
          tempy=random.randrange(self.ysize)
          #Make sure this is a horizontal hall
          try:
            if self.dungarray[tempy+1][tempx]=="#" and self.dungarray[tempy-1][tempx]=="#" and self.dungarray[tempy][tempx]==".":
              #Add the tiles upwards and/ord downwards one by one
              upycoord=downycoord=tempy
              while lenght>0:
                uod=random.choice([0,1])
                if uod:
                  try:
                    if upycoord>0:
                      upycoord-=1
                      self.dungarray[upycoord][tempx]="."
                      lenght-=1
                  except:
                    pass
                else:
                  try:
                    if downycoord<self.ysize-1:
                      downycoord+=1
                      self.dungarray[downycoord][tempx]="."
                      lenght-=1
                  except:
                    pass
            if lenght==0:
              break
          except IndexError:
            pass
          count+=1

      #Horizontal halls
      for i in range(self.ysize/10):
        count=0
        lenght=random.randrange(self.xsize)
        while 1:
          tempx=random.randrange(self.xsize)
          tempy=random.randrange(self.ysize)
          try:
            if self.dungarray[tempy][tempx+1]=="#" and self.dungarray[tempy][tempx+1]=="#" and self.dungarray[tempy][tempx]==".":
              leftxcoord=rightxcoord=tempx
              while lenght>0:
                lor=random.choice([0,1])
                if lor:
                  try:
                    if leftxcoord>0:
                      leftxcoord-=1
                      self.dungarray[tempy][leftxcoord]="."
                      lenght-=1
                  except:
                    pass
                else:
                  try:
                    if rightxcoord<self.xsize-1:
                      rightxcoord+=1
                      self.dungarray[tempy][rightxcoord]="."
                      lenght-=1
                  except:
                    pass
            if lenght==0:
              break
          except IndexError:
            pass
          count+=1
                
          
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

      #Adds a mob for every 60 free spaces:
      self.mobarray=[]
      spacecounter=0
      for i in range(self.ysize):
        for j in range(self.xsize):
          if self.dungarray[i][j]==".":
            spacecounter+=1
      for i in range(spacecounter/60):
        self.mobarray.append(mob.mob(self))

      #Adds the vendor
      #First, look for a pattern in which the shop can fit
      #The shop looks like this
      #
      # A) ####  B) ####
      #    #p|.     .|q#
      #    ####     ####
      #
      #so it needs a 3x3 block near a room or a vertical hall.

      #Randomize iterator:
      pairs=[]
      for i in range (len(self.dungarray)-3):
        for j in range (len(self.dungarray[0])-3):
          pairs.append([i,j])
      random.shuffle(pairs)

      if vendor==1:
        self.vendorvar=npc.vendor()
        for i in pairs:
          #Check surroundings
          if (self.dungarray[i[0]][i[1]]=="#" and
              self.dungarray[i[0]][i[1]+1]=="#" and
              self.dungarray[i[0]][i[1]+2]=="#" and
              self.dungarray[i[0]+1][i[1]]=="#" and
              self.dungarray[i[0]+1][i[1]+1]=="#" and
              self.dungarray[i[0]+1][i[1]+2]=="#" and
              self.dungarray[i[0]+2][i[1]]=="#" and
              self.dungarray[i[0]+2][i[1]+1]=="#" and
              self.dungarray[i[0]+2][i[1]+2]=="#" and
              self.dungarray[i[0]+1][i[1]+3]=="."):
            #Place the shop in the first available place and exit the loop
            self.dungarray[i[0]+1][i[1]+1]="p"
            self.dungarray[i[0]+1][i[1]+2]="|"
            break
         
      #Adds spaces in random positions with rocks, one for every 3x3 zone.
      # for i in range(0,self.xsize*self.ysize/9):
      #   randx=random.randrange(self.xsize)
      #  	randy=random.randrange(self.ysize)
      #  	if self.dungarray[randy][randx]=="#":
      #     self.dungarray[random.randrange(self.ysize)][random.randrange(self.xsize)]="."
      #  	else: pass

      #Add money (loot) in random places in the ground. 1 drop per 50 floor tiles
      counter=0
      tempx=0
      tempy=0
      for i in range(self.ysize):
        for j in range(self.xsize):
          if self.dungarray[i][j]==".":
            counter+=1
      for i in range(1,counter/75):
        while self.dungarray[tempy][tempx]!=".":
          tempx=random.randrange(1,self.xsize)
          tempy=random.randrange(1,self.ysize)
        self.dungarray[tempy][tempx]="$"

      #Add objects (loot) in random places. 1 drop per 100 floor tiles
      for i in range (1,counter/100):
        while self.dungarray[tempy][tempx]!=".":
          tempx=random.randrange(1,self.xsize)
          tempy=random.randrange(1,self.ysize)
        self.dungarray[tempy][tempx]="/"        

      #Dungeon should be done

      #Initializes the filled array so it has the same sizent content as the dungarray
      self.filled=[]
      for i in range (self.ysize):
        secondary=[]
        for j in range (self.xsize):
          secondary.append("~")
        self.filled.append(secondary)
      #Fills the filled array with the dungarray data
      for i in range (self.ysize):
        for j in range (self.xsize):
          self.filled[i][j]=self.dungarray[i][j]

      #Initialize explored array
      self.explored=[]
      for i in range(self.ysize):
        temp=[]
        for j in range(self.xsize):
          temp.append("~")
        self.explored.append(temp)

      #Add traps
      self.traps=[]
      for i in range(int(round((self.xsize*self.ysize)/600))):
        while 1:
          randx=random.randrange(len(self.dungarray[0]))
          randy=random.randrange(len(self.dungarray))
          if self.dungarray[randy][randx]==".":
            #Generate random type of trap
            # 10%: Trap to next floor
            # 90%: HP or MP trap
            randtrap=random.randrange(10)
            if randtrap==0:
              self.traps.append([randx,randy,3])
              break
            else:
              self.traps.append([randx,randy,random.randint(1,2)])
              break
      
  def dumpdung(self,place): 
    """
    Generates a list of coordinates and tile type.

    Needs a Place parameter indicatis where. 0 is return to console, anything else dumps it to a file

    Avoid dumping to console with big dungeons, output turns out unreadable
    """

    if place==0:
      #Dump to file mode.
      if not os.path.exists("../logs/"):
        os.makedirs("../logs/")
      with open("../logs/kirino.dump","a+") as dump:
        dump.write ("\n ###################### \n")
      	for i in range (0,len(self.dungarray)):
      	  for j in range (0,len(self.dungarray[i])):
            dump.write("("+str(i+1)+", "+str(j+1)+")")
      	    if self.dungarray[i][j]=="#":
              dump.write (" Rock \n")
      	    elif self.dungarray[i][j]=="A":
              dump.write (" Entrance \n")
      	    elif self.dungarray[i][j]=="X":
              dump.write (" Exit \n")
      	    elif self.dungarray[i][j]==".":
              dump.write (" Hallway \n")
      	    elif self.dungarray[i][j]=="D":
              dump.write (" Undeleted room marker \n")
      	    else:
              dump.write (" Unrecognised value ("+self.dungarray[i][j]+")")
    else:
      #Dump to console
      for i in range (len(self.dungarray)):
        for j in range (len(self.dungarray[i])):
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

  def report(self):
    """
    Appends a map of the dungeon and a report message into a text file.

    File is ../logs/report
    """

    if not os.path.exists("../logs/"):
      os.makedirs("../logs/")
    with open("../logs/report","a+") as dump:
      for i in range (0,len(self.dungarray)):
        dump.write(''.join(map(str,self.dungarray[i]))+"\n")
      dump.write(raw_input("report message?"))
      dump.write("\n ---------- \n")
	   
  def map(self):
    """
    Map generator. 

    Creates a map of the dungeon on screen.
    This shows the entire dungarray[][], so dungeons with a horizontal size larger than the horizontal console size will look weird.
    """

    for i in range (0,len(self.dungarray)):
      print ''.join(map(str,self.dungarray[i]))
      
  def advmap(self,x,y,xmapsize,ymapsize):
    """
    Advanced map function. 

    Displays a small area of the map. 

    x and y are the coordinates of the dungeon array in which the advanced map is centered.
    xmapsize and ymapsize are the horizontal and vertical size of the map. 

    minimum size is 20x10. If something smaller is entered, it defaults at the smallest value. 
    If the coordinates are too close to the edge, they are replaced so the map does not show anything outside the dungeon array.   
    """

    if xmapsize<20:
      xmapsize=20
    if ymapsize<10:
      ymapsize=10
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
        mapstring[counter].append(self.filled[i][j])
         
    #Print loop
    for i in range(len(mapstring)):
      print ''.join(map(str,mapstring[i]))
     
  def advmapcoords(self,x,y):
    """
    Generates an advanced map (20x10) centered on the position (x,y)
    """

    self.advmap(x,y,20,10)

  def minimap(self,player,fog):
    """
    Generates a minimap (advmap centered on the player object passed)

    Uses the function fill(), so it needs the fog parameter too.
    1=fog enabled, anything else fog disabled.
    """

    self.fill(player,fog)
    self.advmapcoords(player.xpos,player.ypos)
    
  def debug(self):
    """
    Debug dungeon 

    Returns an integer as error condition code:
      EC0: (Not actually an error, everything is fine)
      EC1: There is no entrance or exit
      EC2: It's below the minimum size
      EC3: Can't reach the exit from the entrance (pending)
      EC4: There are halls unconnected or unreachable (pending)

    Used in the constructor on this class, although it can be invoked anytime.
    """

    #Making sure the dungeon is over the minimum size
    if self.xsize<40 or self.ysize<20:
      return(2)
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
        return 1
      else:
      #Checks if X is reachable from A (pending)
        pass
        return 0

  def remember(self,player):
    """
    Processes the explored array.

    For every intelligence point, a player can "memorize" up to 100 tiles.
    If the explored map has more explored tiles than that, deletes random tiles until numbers fix.

    This function should only be called when the fog is on
    """

    exploredtiles=0
    for i in range(len(self.explored)):
      for j in range(len(self.explored[0])):
        if self.explored[i][j]!="~":
          exploredtiles+=1
    extra=exploredtiles-((player.INT+player.intboost)*100)
    while extra>0:
      while 1:
        randx=random.randrange(len(self.explored[0]))
        randy=random.randrange(len(self.explored))
        if self.explored[randy][randx]!="~":
          self.explored[randy][randx]="~"
          extra-=1
          break


  def fill(self,player,fog):
    """
    Fills the dungeon temporarily with PC and NPC object and mob markers. 

    Needs a player and the fog parameter

    Does not return anything, but modifies the filled array
    if the parameter fog is 1, it displays a fogged minimap. 
    """

    #Initialize filled array with fog
    for i in range (self.ysize):
      secondary=[]
      for j in range (self.xsize):
        secondary.append("~")
      self.filled.append(secondary)

    #Calculate how many tiles the player is allowed to see
    totper=player.PER+player.perboost   
    
    #Fills the filled array with the dungarray data
    #Only in the places the player is allowed to see
    for i in range (self.ysize):
      for j in range (self.xsize):
        if fog==1:
          viewx=(totper-(abs(i-player.ypos))+2)
          if viewx<0:
            viewx=2
          viewy=(totper-(abs(j-player.xpos))+1)
          if viewy<0:
            viewy=1
          if player.ypos-viewy<i<player.ypos+viewy:
            if player.xpos-viewx<j<player.xpos+viewx:
              self.filled[i][j]=self.dungarray[i][j]
              self.explored[i][j]=self.dungarray[i][j]
            else:
              self.filled[i][j]="~"
          else:
            self.filled[i][j]="~"
          #Add mobs
          for k in self.mobarray:
            if player.ypos-viewy<k.ypos<player.ypos+viewy:
              if player.xpos-viewx<k.xpos<player.xpos+viewx:
                self.filled[k.ypos][k.xpos]="i"

        #If fog is not on, just generate a regular minimap
        if fog!=1:
          for k in range(len(self.mobarray)):
            if self.mobarray[k].ypos==i and self.mobarray[k].xpos==j:
              self.filled[self.mobarray[k].ypos][self.mobarray[k].xpos]="i"
            else:
              self.filled[i][j]=self.dungarray[i][j]

    #Places the player marker in the filled array
    self.filled[player.ypos][player.xpos]="8"
