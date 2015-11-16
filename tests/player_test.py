import unittest, os, sys

sys.path.append(os.path.abspath("../source/"))
import player
# Importing these just to test item instances
# Do not use to generate actual items for tests
# Use the mock classes for that
from item import consumable as realconsumable
from item import item as realitem

#
# Mock classes for testing
#

class testdungeon:
  """
  Mock dungeon for some player functions
  """

  dungarray=[["#", "#", "#"], ["#", "A", "#"], ["#", ".", "#"], ["#", "#", "#"]]

class testmob:
  """
  Mock mob
  """

  def __init__(self):

    self.marker="i"
    self.name="mob"
    self.defn=0
    self.zpos=0
    self.HP=0
    self.hit=0
    self.exp=1
    self.pres=1
    self.lv=0

class walldungeon:
  """
  Mock dungeon for testing wall detection
  """

  dungarray=[["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]
  filled=dungarray
  mobarray=[testmob()]

class mobdungeon:
  """
  Mock dungeon for testing mob detection
  """

  dungarray=[["i", "i", "i"], ["i", ".", "i"], ["i", "i", "i"]]
  filled=dungarray
  mobarray=[testmob()]

class emptydungeon:
  """
  Mock dungeon for testing movement
  """

  dungarray=[[".", ".", "."], [".", ".", "."], [".", ".", "."]]
  filled=dungarray
  mobarray=[testmob()]

class testitem:
  """
  Mock item for player testing
  """

  strbonus=1
  intbonus=1
  dexbonus=1
  perbonus=1
  conbonus=1
  wilbonus=1
  chabonus=1

  name="test_item"

  # Not used in tests, but necessary so it works
  atk=0
  defn=0

class testemptypotion:
  """
  Empty potion
  """

  @staticmethod
  def reset(): pass

  type=0
  subtype=1
  name="empty"
  hpr=0
  mpr=0

class testhppotion:
  """
  Mock HP potion
  """

  @staticmethod
  def reset(): pass

  type=0
  subtype=1
  name="hp"
  hpr=1
  mpr=0

class testmppotion:
  """
  Mock HP potion
  """

  @staticmethod
  def reset(): pass

  type=0
  subtype=2
  name="mp"
  hpr=0
  mpr=1

class testrecpotion:
  """
  Mock HP potion
  """

  @staticmethod
  def reset(): pass

  type=0
  subtype=3
  name="rec"
  hpr=1
  mpr=1

class testtome:
  """
  Mock HP potion
  """

  @staticmethod
  def reset(): pass

  type=1
  name=   "tome"
  strbst= 1
  intbst= 1
  dexbst= 1
  perbst= 1
  conbst= 1
  wilbst= 1
  chabst= 1

#
# Actual tests
#

class TestPlayer(unittest.TestCase):
  """
  Test the player class
  """

  def test_constructor(self):
    """
    Makes sure the player is generated correctly
    """

    tp=player.player()
    #Check Main characteristics
    self.assertIsInstance(tp.name, str)
    self.assertEqual(tp.pocket, 0)
    self.assertEqual(tp.exp,0)
    self.assertEqual(tp.lv,1)
    self.assertIsInstance(tp.race, str)
    self.assertIsInstance(tp.charclass, str)
    self.assertEqual(tp.status, 0)
    self.assertEqual(tp.prestige, 0)
    self.assertEqual(tp.prestigelv, 1)
    self.assertEqual(tp.stomach, 100)
    self.assertEqual(tp.hungsteps, 0)

    # Stat variables
    self.assertEqual(tp.totalfl, 0)
    self.assertEqual(tp.steps, 0)
    self.assertEqual(tp.totalatks, 0)
    self.assertEqual(tp.totalgld, 0)
    self.assertEqual(tp.totalhits, 0)
    self.assertEqual(tp.totaldmg, 0)
    self.assertEqual(tp.totalrcv, 0)
    self.assertEqual(tp.kills, 0)
    self.assertEqual(tp.totaltrp, 0)
    self.assertEqual(tp.itemspck, 0)
    self.assertEqual(tp.itemsdst, 0)
    self.assertEqual(tp.itemsenc, 0)
    self.assertEqual(tp.totalpot, 0)
    self.assertEqual(tp.totalsll, 0)
    self.assertEqual(tp.totalbuy, 0)
    self.assertEqual(tp.totalspn, 0)
    self.assertEqual(tp.maxdmg, 0)
    self.assertEqual(tp.maxench, 0)

    # Examine amount and types of objects
    self.assertEqual(len(tp.belt), 6)
    self.assertEqual(len(tp.equiparr), 11)
    self.assertEqual(len(tp.inventory), 2)
    for i in tp.belt:
      self.assertIsInstance(i, realconsumable)
    for i in tp.equiparr:
      self.assertIsInstance(i, realitem)
    for i in tp.inventory:
      self.assertIsInstance(i, realitem)

    #Set attribute boosters to 0
    self.assertEqual(tp.strboost, 0)
    self.assertEqual(tp.intboost, 0)
    self.assertEqual(tp.conboost, 0)
    self.assertEqual(tp.wilboost, 0)
    self.assertEqual(tp.perboost, 0)
    self.assertEqual(tp.dexboost, 0)
    self.assertEqual(tp.chaboost, 0)

    self.assertGreater(tp.hp2,1)
    self.assertGreater(tp.mp2,1)
    
    self.assertEqual(tp.ypos, 0)
    self.assertEqual(tp.xpos, 0)
    self.assertEqual(tp.zpos, 0)

    self.assertIsInstance(tp.name, str)
    self.assertIsInstance(tp.charclass, str)

    self.assertGreater(tp.STR,0)
    self.assertGreater(tp.INT,0)
    self.assertGreater(tp.DEX,0)
    self.assertGreater(tp.PER,0)
    self.assertGreater(tp.CON,0)
    self.assertGreater(tp.WIL,0)
    self.assertGreater(tp.CHA,0)

  def test_player_normal_enter(self):
    """
    Tests if a player can correctly enter a dungeon normally
    """

    td=testdungeon
    tp=player.player()

    # Test normal entering
    tp.enter(td)
    self.assertEqual(tp.xpos, 1)
    self.assertEqual(tp.ypos, 1)
    

  def test_player_spec_enter(self):
    """
    Tests if a player can correctly enter a dungeon specifying normally
    """

    td=testdungeon
    tp=player.player()
    tp.enter(td, 0)
    self.assertEqual(tp.xpos, 1)
    self.assertEqual(tp.ypos, 1)

  def test_player_fall_enter(self):
    """
    Tests if a player can correctly enter a dungeon falling
    """

    td=testdungeon
    tp=player.player()
    tp.enter(td, 1)
    self.assertEqual(tp.xpos, 1)
    self.assertEqual(tp.ypos, 2)

  def test_pick_itemp_pass(self):
    """
    Tests if the player can successfully pick an item
    """

    tp=player.player()
    ti=testitem
    ans=tp.pickobject(ti)
    self.assertEqual(ans, (0, "You picked test_item\n"))
    self.assertEqual(tp.itemspck, 1)

  def test_pick_itemp_fail(self):
    """
    Tests if the player doesn't pick the item with the inventory full
    """

    tp=player.player()
    tp.inventory=["item" for i in range(10)]
    self.assertEqual(len(tp.inventory), 10)
    ti=testitem
    ans=tp.pickobject(ti)
    self.assertEqual(ans, (1, "Your inventory is full!\n"))
    self.assertEqual(tp.itemspck, 0)

  def test_pick_consumable_pass(self):
    """
    Tests if the player can pick a consumable
    """

    tp=player.player()
    ti=testhppotion
    ans=tp.pickconsumable(ti)
    self.assertEqual(ans, (1, "You picked hp."))

  def test_pick_consumable_fail(self):
    """
    Tests if the consumable picking fails when inv is epmty
    """

    tp=player.player()
    tp.belt=[testhppotion for i in range(4)]
    ti=testhppotion
    ans=tp.pickconsumable(ti)
    self.assertEqual(ans, (0, "Your belt is full"))

  def test_hunger_processing_pass(self):
    """
    Tests the hunger stat modification
    A new player should not return anything
    """

    tp=player.player()
    ans=tp.hunger()
    tp.hp2=1
    self.assertIsNone(ans)
    self.assertEqual(tp.stomach, 100)
    self.assertEqual(tp.hp2, 1)

  def test_hunger_processing_decrease(self):
    """
    Sets the steps to a high value so the stomach decreases
    """

    tp=player.player()
    tp.hungsteps=10
    tp.hp2=1
    ans=tp.hunger()
    self.assertIsNone(ans)
    self.assertEqual(tp.stomach, 99)
    self.assertEqual(tp.hp2, 1)

  def test_hunger_processing_message(self):
    """
    Tests if the hunger processing returns warning messages
    """

    tp=player.player()
    tp.hungsteps=10
    tp.stomach=10
    tp.hp2=1
    ans=tp.hunger()
    self.assertEqual(ans, "Your stomach growls...\n")
    self.assertEqual(tp.stomach, 9)
    self.assertEqual(tp.hp2, 1)

  def test_hunger_processing_decrease(self):
    """
    Tests if the hunger function decreases HP
    """

    tp=player.player()
    tp.hungsteps=10
    tp.stomach=0
    tp.hp2=1
    ans=tp.hunger()
    self.assertEqual(ans, "You feel hungry and weak\n")
    self.assertEqual(tp.stomach, -1)
    self.assertEqual(tp.hp2, 0)

  def test_player_movement_detect_walls(self):
    """
    Tests wall detection in the player movement
    """

    tp=player.player()
    td=walldungeon
    for i in range(8):
      tp.xpos=tp.ypos=1
      ans=tp.move(td, i+1)
      self.assertEqual(ans, 0)
      self.assertEqual(tp.xpos, 1)
      self.assertEqual(tp.ypos, 1)


  def test_player_movement_detect_mobs(self):
    """
    Tests mob detection in the player movement
    """

    tp=player.player()
    td=mobdungeon
    for i in range(8):
      tp.xpos=tp.ypos=1
      ans=tp.move(td, i+1)
      self.assertEqual(ans, 2)
      self.assertEqual(tp.xpos, 1)
      self.assertEqual(tp.ypos, 1)

  def test_player_movement_straight(self):
    """
    Tests normal player movement
    """

    tp=player.player()
    td=emptydungeon
    for i in range(1,9):
      tp.xpos=tp.ypos=1
      ans=tp.move(td, i)
      self.assertEqual(ans, 1)
      if i==1: fxpos, fypos=1, 0
      if i==2: fxpos, fypos=0, 1
      if i==3: fxpos, fypos=1, 2
      if i==4: fxpos, fypos=2, 1

      if i==5: fxpos, fypos=0, 0
      if i==6: fxpos, fypos=2, 0
      if i==7: fxpos, fypos=0, 2
      if i==8: fxpos, fypos=2, 2

      self.assertEqual(tp.xpos, fxpos)
      self.assertEqual(tp.ypos, fypos)

  def test_secondary_attrs(self):
    """
    Sets the player's primary attributes to known values
    Calls the secondary attribute calculator and checks output
    """

    tp=player.player()
    tp.STR=1
    tp.INT=1
    tp.DEX=1
    tp.PER=1
    tp.CON=1
    tp.WIL=1
    tp.CHA=1
    tp.secondary()
    self.assertEqual(tp.HP, 18)
    self.assertEqual(tp.MP, 2)
    self.assertEqual(tp.END, 14)
    self.assertEqual(tp.SPD, 6)

  def test_will_test_pass(self):
    """
    Test the player's willpower test
    Sets the total will to -40 so it automatically fails rolls
    HP is over 5, so it should pass despite that
    """

    tp=player.player()
    tp.hp2=6
    tp.WIL=-20
    tp.wilboost=-20
    success,msg=tp.willtest()
    self.assertEqual(success, 1)
    self.assertIsInstance(msg, str)

  def test_will_test_fail(self):
    """
    Same as test_will_test_pass, except the HP is set to 1 
    The roll must execute and fail
    """

    tp=player.player()
    tp.hp2=1
    tp.WIL=-20
    tp.wilboost=-20
    success,msg=tp.willtest()
    self.assertEqual(success, 0)
    self.assertIsInstance(msg, str)

  def test_use_hp_potion(self):
    """
    Tests hp potion usage
    """

    tp=player.player()
    ti=testhppotion
    tp.hp2=0
    tp.mp2=0
    ans=tp.use(ti)    
    self.assertEqual(tp.hp2, 1)
    self.assertEqual(tp.mp2, 0)
    self.assertEqual(ans, "You drank hp. You recovered 1 HP.")

  def test_use_mp_potion(self):
    """
    Tests mp potion usage
    """

    tp=player.player()
    ti=testmppotion
    tp.hp2=0
    tp.mp2=0
    ans=tp.use(ti)
    self.assertEqual(tp.hp2, 0)
    self.assertEqual(tp.mp2, 1)
    self.assertEqual(ans, "You drank mp. You recovered 1 MP.")

  def test_use_rec_potion(self):
    """
    Tests recovery potions
    """

    tp=player.player()
    ti=testrecpotion
    tp.hp2=0
    tp.mp2=0
    ans=tp.use(ti)
    self.assertEqual(tp.hp2, 1)
    self.assertEqual(tp.mp2, 1)
    self.assertEqual(ans, "You drank rec. You recovered 1 HP and 1 MP.")

  def test_use_empty_potion(self):
    """
    Tests recovery potions
    """

    tp=player.player()
    ti=testemptypotion
    tp.hp2=0
    tp.mp2=0
    ans=tp.use(ti)
    self.assertEqual(tp.hp2, 0)
    self.assertEqual(tp.mp2, 0)
    self.assertEqual(ans, "You drank empty. ")

  def test_use_tome(self):
    """
    Tests tome usage
    """

    tp=player.player()
    ti=testtome
    tp.INT=0
    tp.DEX=0
    tp.PER=0
    tp.STR=0
    tp.CON=0
    tp.WIL=0
    tp.CHA=0
    msg=tp.use(ti)
    self.assertEqual(tp.INT, 1)
    self.assertEqual(tp.DEX, 1)
    self.assertEqual(tp.STR, 1)
    self.assertEqual(tp.PER, 1)
    self.assertEqual(tp.CON, 1)
    self.assertEqual(tp.WIL, 1)
    self.assertEqual(tp.CHA, 1)
    self.assertEqual(msg, "You used tome. INT +1 DEX +1 PER +1 CON +1 WIL +1 CHA +1 STR +1 \n")

  def test_add_bonuses(self):
    """
    Tests the addition of bonuses from a mock object
    """

    tp=player.player()
    ti=testitem
    tp.strboost=0
    tp.intboost=0
    tp.dexboost=0
    tp.perboost=0
    tp.conboost=0
    tp.wilboost=0
    tp.chaboost=0
    tp.addbonuses(ti)
    self.assertEqual(tp.strboost, 1)
    self.assertEqual(tp.intboost, 1)
    self.assertEqual(tp.dexboost, 1)
    self.assertEqual(tp.perboost, 1)
    self.assertEqual(tp.conboost, 1)
    self.assertEqual(tp.wilboost, 1)
    self.assertEqual(tp.chaboost, 1)

  def test_remove_bonuses(self):
    """
    Tests the removal of bonuses from a mock object
    """

    tp=player.player()
    ti=testitem
    tp.strboost=1
    tp.intboost=1
    tp.dexboost=1
    tp.perboost=1
    tp.conboost=1
    tp.wilboost=1
    tp.chaboost=1
    tp.rembonuses(ti)
    self.assertEqual(tp.strboost, 0)
    self.assertEqual(tp.intboost, 0)
    self.assertEqual(tp.dexboost, 0)
    self.assertEqual(tp.perboost, 0)
    self.assertEqual(tp.conboost, 0)
    self.assertEqual(tp.wilboost, 0)
    self.assertEqual(tp.chaboost, 0)

  def test_levelup_once(self):
    """
    Tests player increasing levels
    Set the experience to 5 
    Expects the player to level up just once
    """

    tp=player.player()
    tp.exp=5
    self.assertEqual(tp.lv, 1)
    tp.levelup()
    self.assertEqual(tp.lv, 2)

  def test_levelup_multiple(self):
    """
    Same as test_levelup_once, except it sets the exp to 67
    With that exp the player should get to level 6 with a single call
    """

    tp=player.player()
    tp.exp=67
    self.assertEqual(tp.lv, 1)
    tp.levelup()
    self.assertEqual(tp.lv, 6)

  def test_levelup_none(self):
    """
    Same as the other test_levelup functions, except it sets the exp to 4
    At level 1 with less than 5 exp, the player should not level up at all
    """

    tp=player.player()
    tp.exp=4
    self.assertEqual(tp.lv, 1)
    tp.levelup()
    self.assertEqual(tp.lv, 1)

  def test_player_attack_pass_roll_no_prestige(self):
    """
    Tests player attack in a mock mob object
    """

    tp=player.player()
    tp.DEX=5
    tp.STR=1
    tp.totatk=1
    tp.lv=5
    tm=testmob()
    tm.exp=1

    for i in range(1,101):
      tp.attack(tm)
      self.assertEqual(tm.HP, -i)
      self.assertEqual(tm.hit, 1)
      self.assertEqual(tp.prestige, 0)
      self.assertEqual(tp.totalhits, i)
      self.assertEqual(tp.totalatks, i)
      self.assertEqual(tp.totaldmg, i)
      self.assertEqual(tp.maxdmg, 1)
      self.assertEqual(tp.kills, i)
      self.assertEqual(tp.exp, i)


  def test_player_attack_pass_roll_prestige(self):
    """
    Tests player attack in a mock mob object
    """

    tp=player.player()
    tp.DEX=5
    tp.STR=1
    tp.totatk=1
    tp.lv=0
    tm=testmob()
    tm.exp=1
    tm.pres=1

    for i in range(1,101):
      tp.attack(tm)
      self.assertEqual(tm.HP, -i)
      self.assertEqual(tm.hit, 1)
      self.assertEqual(tp.prestige, i)
      self.assertEqual(tp.totalhits, i)
      self.assertEqual(tp.totalatks, i)
      self.assertEqual(tp.totaldmg, i)
      self.assertEqual(tp.maxdmg, 1)
      self.assertEqual(tp.kills, i)
      self.assertEqual(tp.exp, i)

  def test_player_attack_fail_roll(self):
    """
    Tests player attack in a mock mob object
    """

    tp=player.player()
    tp.DEX=-10
    tm=testmob()

    for i in range(1,101):
      tp.attack(tm)
      self.assertEqual(tm.HP, 0)
      self.assertEqual(tm.hit, 0)
      self.assertEqual(tp.prestige, 0)
      self.assertEqual(tp.totalhits, 0)
      self.assertEqual(tp.totalatks, i)
      self.assertEqual(tp.totaldmg, 0)
      self.assertEqual(tp.maxdmg, 0)
      self.assertEqual(tp.kills, 0)
      self.assertEqual(tp.exp, 0)

  def test_player_reset(self):
    """
    Tests if the player resets correctly
    """

    tp=player.player()
    tp.reset()

    self.assertEqual(tp.name, "_")
    self.assertEqual(tp.pocket, 0)
    self.assertEqual(tp.exp, 0)
    self.assertEqual(tp.lv, 1)
    self.assertEqual(tp.points, 0)
    self.assertEqual(tp.race, "_")
    self.assertEqual(tp.charclass, "_")
    self.assertEqual(tp.stomach, 100)
    self.assertEqual(tp.inventory, [])
    self.assertEqual(tp.belt, [])
    self.assertEqual(len(tp.equiparr), 11)
    self.assertEqual(tp.totalfl, 0)
    self.assertEqual(tp.prestige, 0)
    self.assertEqual(tp.prestigelv, 1)
    self.assertEqual(tp.totalfl, 0)
    self.assertEqual(tp.steps, 0)
    self.assertEqual(tp.totalatks, 0)
    self.assertEqual(tp.totalhits, 0)
    self.assertEqual(tp.totaldmg, 0)
    self.assertEqual(tp.totalhit, 0)
    self.assertEqual(tp.kills, 0)
    self.assertEqual(tp.totalgld, 0)
    self.assertEqual(tp.totaltrp, 0)
    self.assertEqual(tp.itemspck, 0)
    self.assertEqual(tp.itemsenc, 0)
    self.assertEqual(tp.itemsdst, 0)
    self.assertEqual(tp.totalpot, 0)
    self.assertEqual(tp.totalsll, 0)
    self.assertEqual(tp.totalbuy, 0)
    self.assertEqual(tp.totalspn, 0)
    self.assertEqual(tp.maxdmg, 0)
    self.assertEqual(tp.maxench, 0)
    self.assertEqual(tp.INT, 1)
    self.assertEqual(tp.DEX, 1)
    self.assertEqual(tp.PER, 1)
    self.assertEqual(tp.WIL, 1)
    self.assertEqual(tp.STR, 1)
    self.assertEqual(tp.CON, 1)
    self.assertEqual(tp.CHA, 1)
    self.assertEqual(tp.intboost, 0)
    self.assertEqual(tp.dexboost, 0)
    self.assertEqual(tp.perboost, 0)
    self.assertEqual(tp.wilboost, 0)
    self.assertEqual(tp.strboost, 0)
    self.assertEqual(tp.conboost, 0)
    self.assertEqual(tp.chaboost, 0)
    self.assertEqual(tp.totatk, 0)
    self.assertEqual(tp.totdefn, 0)
    self.assertEqual(tp.HP, 0)
    self.assertEqual(tp.hp2, 0)
    self.assertEqual(tp.MP, 0)
    self.assertEqual(tp.mp2, 0)
    self.assertEqual(tp.END, 0)
    self.assertEqual(tp.SPD, 0)
    self.assertEqual(tp.xpos, 0)
    self.assertEqual(tp.ypos, 0)
    self.assertEqual(tp.zpos, 0)

if __name__ == "__main__":
  unittest.main()
