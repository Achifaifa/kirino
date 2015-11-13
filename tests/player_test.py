import unittest, os, sys

scriptpath = "../source/"
sys.path.append(os.path.abspath(scriptpath))
import player
# Importing this just to test item instances
# Do not use to generate actual items for tests
# Use the mock classes for that
from item import consumable as realconsumable
from item import item as realitem

class testdungeon:
  """
  Mock dungeon for some player functions
  """

  dungarray=[["#", "#", "#"], ["#", "A", "#"], ["#", ".", "#"], ["#", "#", "#"]]

class testitem:
  """
  Mock item for player testing
  """

  pass

class TestConsumables(unittest.TestCase):
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

    # Examine amount of objects
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
    pass

  def test_pick_itemp_fail(self):
    pass

  def test_pick_consumable_pass(self):
    pass

  def test_pick_consumable_fail(self):
    pass

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

  def test_player_movement(self):
    pass

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

  def test_use_item(self):
    pass

  def test_add_bonuses(self):
    pass

  def test_remove_bonuses(self):
    pass

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

  def test_player_attack(self):
    pass

  def test_player_reset(self):
    pass

if __name__ == "__main__":
  unittest.main()
