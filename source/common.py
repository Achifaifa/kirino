#! /usr/bin/env python 
"""
Common procedure file. Contains all the code used by most of the other modules.
"""

import os, sys, tty, termios

def vern():
  """
  Returns a string with the version number
  """

  return "v0.1.4" 

def version():
  """
  Prints the program name and the version in one line
  """

  os.system('clear')
  print "Kirino - %s"%(vern())

def getch():
  """
  Reads a single key from the console input*. Code by Joeyespo:
  https://github.com/joeyespo/py-getch

  *I can't fucking believe this is not in the os library
  """

  fd=sys.stdin.fileno()
  old=termios.tcgetattr(fd)
  try:
    tty.setraw(fd)
    return sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old) 

if __name__=="__main__":
  version()
  print "Common module test. Press any key to exit."
  getch()