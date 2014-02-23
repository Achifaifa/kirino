#usr/bin/env python
import os
import random
import dungeon

class mob:
  "Mob class"
  xpos=0
  ypos=0
  
  #Mob generator. It just sets the coordinates to (0,0)
  def __init__(self,dungeon):
    self.xpos=random.randrange(dungeon.xsize)
    self.ypos=random.randrange(dungeon.ysize)
    while dungeon.dungarray[self.ypos][self.xpos]=="#":
      self.xpos=random.randrange(dungeon.xsize)
      self.ypos=random.randrange(dungeon.ysize)
    pass
  
  #Move function. Accepts strings with direction and distance
  def move(self,dungeon,direction,distance):
    direction=''+direction
    if direction=="n":
      if dungeon.dungarray[self.ypos-1][self.xpos]=="#":
        print "There is a wall there!"
      else:
        self.ypos -= distance
    if direction=="w":
      if dungeon.dungarray[self.ypos][self.xpos-1]=="#":
         print "There is a wall there!"
      else:
        self.xpos -= distance  
    if direction=="s":
      if dungeon.dungarray[self.ypos+1][self.xpos]=="#":
        print "There is a wall there!"
      else:     
        self.ypos += distance
    if direction=="e":
      if dungeon.dungarray[self.ypos][self.xpos+1]=="#":
        print "There is a wall there!"
      else:
        self.xpos += distance
  
  #Moves a given distance in a random direction
  def randmove(self,dungeon,dist):
    rand=0
    rand=random.randrange(4)
    if rand==1:
      self.move(dungeon,"n",dist)
    elif rand==2:
      self.move(dungeon,"s",dist)
    elif rand==3:
      self.move(dungeon,"e",dist)
    elif rand==0:
      self.move(dungeon,"w",dist)

  #Twitch plays kirino
  def trandmove(self,dungeon):
    rand=0
    rand=random.randrange(2)+1#Will depend on the mob in the future
    self.randmove(dungeon,rand)
  
  #Store the copypastes here
  def copypaste(self):
    pass
    ###
  
    ###
    


#Test stuff
new=dungeon.dungeon(70,40)
goblin=mob(new)
while 1==1:
  print "Current tile:",new.dungarray[goblin.ypos][goblin.xpos]
  print "Current position:",(goblin.xpos,goblin.ypos)
  goblin.move(new,(raw_input("Direction? ")),1)
  
#step=0
#ite=0
#medi=0
#totstep=0
##while 1==1:
  #print "Current steps:",step,"Iterations:",ite,"Median:",medi
  #os.system('clear')
  #goblin.trandmove()
  #print goblin.xpos,goblin.ypos
  #step+=1
  #if goblin.xpos==0 and goblin.ypos==0:
    #ite += 1
    #totstep += step
    #medi = totstep/ite
    #step=0
    
#print step

