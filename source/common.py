#usr/bin/env python 
"""
Common procedure file. Contains all the code used by most of the other modules.
"""
import os
import sys
import tty
import termios

def version():
  """
  Prints the program name and the version in one line
  """
  print "Kirino - v0.0.2c"

def getch():
  """
  Reads a single key from the console input*. Code by Joeyespo:
  https://github.com/joeyespo/py-getch

  *I can't fucking believe this is not in the os library
  """
  fd = sys.stdin.fileno()
  old = termios.tcgetattr(fd)
  try:
    tty.setraw(fd)
    return sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old) 