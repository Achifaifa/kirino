#usr/bin/env python

import os
import random

class dungeon:
  "Dungeon generator"
  xsize=0
  ysize=0
  dungarray=[]
  
  def __init__(self,x,y):
    xsize=x
    ysize=y
    dungarray=[]
    for i in range (0,xsize):
      secondary=[]
      for j in range (0,ysize):
	secondary.append("0")
      self.dungarray.append(secondary)
  
  def dumpdung(self):
    for i in range (0,10):
      for j in range (0,10):
	print "Tile:",(i,j),"Terrain:",self.dungarray[i][j]
  def show(self):
    for i in range (0,10):
      print ''.join(map(str,self.dungarray[i]))
      
      
    
new=dungeon(10,10)
new.dumpdung()
new.show()