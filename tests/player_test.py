import unittest, os, sys

scriptpath = "../source/"
sys.path.append(os.path.abspath(scriptpath))
import player

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

    



if __name__ == "__main__":
  unittest.main()
