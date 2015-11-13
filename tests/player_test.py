import unittest, os, sys

scriptpath = "../source/"
sys.path.append(os.path.abspath(scriptpath))
import player

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

    # Examine amount of objects (TO-DO: Types)
    self.assertEqual(len(tp.belt), 6)
    self.assertEqual(len(tp.equiparr), 11)
    self.assertEqual(len(tp.inventory), 2)

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

  def test_pick_itemp(self):
    pass

  def test_pick_consumable(self):
    pass

  def test_hunger_processing(self):
    pass

  def test_player_movement(self):
    pass

  def test_secondary_attrs(self):
    pass

  def test_will_test_pass(self):
    """
    Test the player's willpower test (pass)
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
    Test the player's willpower test (pass)
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
    Tests player increasing levels once
    """

    tp=player.player()
    tp.exp=5
    self.assertEqual(tp.lv, 1)
    tp.levelup()
    self.assertEqual(tp.lv, 2)

  def test_levelup_multiple(self):
    """
    Tests player increasing levels three times in a single call
    """

    tp=player.player()
    tp.exp=67
    self.assertEqual(tp.lv, 1)
    tp.levelup()
    self.assertEqual(tp.lv, 6)

  def test_levelup_none(self):
    """
    Tests player increasing zero levels without exp
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
