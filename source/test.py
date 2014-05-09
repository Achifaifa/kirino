#! /usr/bin/env python
"""
Test module

The functions here allow the plyaer to test certain aspects of the game without having to go through dungeons to find it.
"""

import copy, os, random, sys
import dungeon, item, mob, npc, parser, player
import common, config, help

def testm():
  """
  Test menu
  """

  while 1:
    common.version()
    print "Test utilities\n"
    print "1.- Test character sheet"
    print "2.- Test combat system"
    print "3.- Test vendor"
    print "4.- Test parser"
    print "5.- Test chat" 
    print "6.- Test generator"
    print "---"
    print "0.- Go back"
    testmen=common.getch()

    if testmen=="1":
      testcharsh()
    if testmen=="2":
      testfight()
    if testmen=="3":
      testvend()
    if testmen=="4":
      testparse()
    if testmen=="5":
      testchat()
    if testmen=="6":
      testgen()
    if testmen=="0":
      break

def testcharsh():
  """
  Test environment for the character sheet.
  """

  dung=dungeon.dungeon(0,0,0)
  test=player.player(dung,1)
  test.charsheet()

def testfight():
  """
  Test environment for the combat system.

  Generates a ring in which different mobs can be generated
  """

  print "Not available"
  common.getch()

def testvend():
  """
  Test environment for vendors and sellers
  """

  dung=dungeon.dungeon(0,0,0)
  hero=player.player(dung,1)
  seller=npc.vendor()
  seller.commerce(hero)

def testchat():
  """
  Test environment for seller chat

  Starts a chat with a random vendor, giving extra information for testing purposes.
  """

  dung=dungeon.dungeon(0,0,0)
  hero=player.player(dung,1)
  seller=npc.vendor()
  parser.chat(seller.keeper,hero)

def testparse():
  """
  Test environment for the parser

  Starts a text interface and identifies the actions and options passed
  """

  print "Not available"
  common.getch()

def testgen():
  """
  Test environment for the dungeon generator.

  It generates a dungeon and displayes the full map in the screen
  """

  while 1:
    os.system('clear')
    common.version()
    print "Dungeon generator test. 0 to exit, other key to generate dungeon"
    try:
      new=dungeon.dungeon(40,40,1)
      new.map()
    except:
      print "\n\nError"
    bla=common.getch()
    if bla=="0":
      break

