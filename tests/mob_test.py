import os, sys, unittest
sys.path.append(os.path.abspath("../source/"))
import mob

class testdungeon():
  """
  Static dungeon with just a hall
  """

  dungarray=[["#", "#", "#"],
             ["#", ".", "#"],
             ["#", ".", "#"],
             ["#", "#", "#"]]

class testplayer():
  """
  Sample player with just enough attributes for testing
  """

  totdefn=0
  xpos=0
  ypos=0
  hp2=0
  totalrcv=0

class Mobtestsuit(unittest.TestCase):
  """
  tests mob class
  """

  mobattributes=["INT", "DEX", "STR", "PER", "CON", "WIL", "CHA"]

  def test_mob_constructor_primary(self):
    """
    Tests the mob constructor through existing levels
    """

    for j in range(50):
      for i in range(10):
        tm=mob.mob(i)
        self.assertEqual(tm.lock, 0)
        self.assertEqual(tm.hit, 0)
        self.assertEqual(tm.xpos, 0)
        self.assertEqual(tm.ypos, 0)
        self.assertEqual(len(tm.marker), 1)
        self.assertIsInstance(tm.marker, basestring)
        self.assertIsInstance(tm.level, int)
        self.assertIsInstance(tm.prestige, int)
        self.assertIsInstance(tm.exp, int)
        self.assertGreaterEqual(tm.exp, 0)
        self.assertIsInstance(tm.INT, int)
        self.assertIsInstance(tm.DEX, int)
        self.assertIsInstance(tm.PER, int)
        self.assertIsInstance(tm.CON, int)
        self.assertIsInstance(tm.WIL, int)
        self.assertIsInstance(tm.CHA, int)
        self.assertIsInstance(tm.STR, int)
        self.assertIsInstance(tm.atk, int)
        self.assertIsInstance(tm.defn, int)
        self.assertGreaterEqual(tm.atk, 0)
        self.assertGreaterEqual(tm.defn, 0)
        self.assertGreaterEqual(tm.MP, 0)
        self.assertGreaterEqual(tm.HP, 0)
        self.assertGreaterEqual(tm.END, 0)
        self.assertGreater(tm.SPD, 0)


  def test_mob_constructor_secondary(self):
    """
    Tests the secondary attribute generation in the mob constructor
    """

    for j in range(50):
      for q in range(10):
        tm=mob.mob(q)
        for i in self.mobattributes: setattr(tm,i,1)
        tm.secondary()
        for i in self.mobattributes: 
          self.assertIsInstance(eval("tm.%s"%i), int)
        self.assertEqual(tm.HP, 18)
        self.assertEqual(tm.MP, 2)
        self.assertEqual(tm.END, 14)
        self.assertEqual(tm.SPD, 6)

  def test_mob_movement(self):
    """
    Puts the mob in a controlled dungeon and test the movement
    """

    td=testdungeon
    for j in range(50):
      for q in range(10):
        tm=mob.mob(q)
        for i in range(4):
          tm.xpos=1
          tm.ypos=1
          ret=tm.move(td,i+1,1)
          if i+1==3: 
            self.assertEqual(tm.ypos, 2)
            self.assertEqual(ret, 0)
          else:
            self.assertEqual(tm.ypos, 1)
            self.assertEqual(ret, 1)
          self.assertEqual(tm.xpos, 1)

  def test_mob_movement_random(self):
    """
    Runs the mob through the test dungeon and tests its random movement
    """

    td=testdungeon
    tm=mob.mob(0)
    tm.xpos=1
    tm.ypos=1
    for i in range(100):
      tm.move(td,1)
      self.assertEqual(tm.xpos, 1)
      self.assertIn(tm.ypos, [1,2])

  def test_mob_movement_trandom(self):
    """
    Puts the mob in the test dungeon and makes it move randomly through it
    """

    td=testdungeon
    tm=mob.mob(0)
    tm.xpos=1
    tm.ypos=1
    for i in range(100):
      tm.move(td)
      self.assertEqual(tm.xpos, 1)
      self.assertIn(tm.ypos, [1,2])

  def test_mob_search(self):
    """
    Search for player test automation

    Checks that the mob can detect player and determine course correctly
    """

    tp=testplayer
    tm=mob.mob()
    tm.PER=999

    # South (Should return 3)
    tm.xpos, tm.ypos=0, 0
    tp.xpos, tp.ypos=0, 10
    res=tm.search(tp)
    self.assertEqual(res, 3)

    # East (Should return 4)
    tp.xpos, tp.ypos=10, 0
    res=tm.search(tp)
    self.assertEqual(res, 4)

    # North (Should return 1)
    tm.xpos, tm.ypos=0, 10
    tp.xpos, tp.ypos=0, 0
    res=tm.search(tp)
    self.assertEqual(res, 1)

    # West (Should return 2)
    tm.xpos, tm.ypos=10, 0
    res=tm.search(tp)
    self.assertEqual(res, 2)

  def test_mob_search_failure(self):
    """
    Checks if the search function fails properly
    """

    tp=testplayer
    tm=mob.mob()
    tm.PER=0
    tm.xpos, tm.ypos=0, 0
    tp.xpos, tp.ypos=0, 10
    res=tm.search(tp)
    self.assertEqual(res, 0)

  def test_mob_lock(self):
    """
    Tests if the mob successfully locks to a player 
    """

    tp=testplayer
    tm=mob.mob()
    self.assertEqual(tm.lock, 0)
    tm.xpos, tm.ypos=0, 0
    tp.xpos, tp.ypos=0, 10
    tm.flock(tp)
    self.assertEqual(tm.lock, 0)
    tp.xpos, tp.ypos=0, 1
    tm.flock(tp)
    self.assertEqual(tm.lock, 1)

  def test_mob_attack(self):
    """
    # Creates a fakey scenario for attack tests
    """

    tp=testplayer
    tm=mob.mob()
    tm.xpos=1
    tm.ypos=1
    tm.lock=1
    tm.name="##MOB##"
    tp.xpos=1
    tp.ypos=2
    tp.name="##PLAYER##"
    tm.STR=5
    tm.DEX=4 #Makes sure the roll always pass
    tm.atk=5
    tp.totdefn=10
    tp.totalrcv=0
    tp.hp2=100
    out=tm.attack(tp)
    self.assertEqual(tp.totalrcv, 15)
    self.assertIsInstance(tp.totalrcv, int)
    self.assertEqual(tp.hp2, 85)
    self.assertIsInstance(tp.hp2, int)
    self.assertIn("##MOB##", out)
    self.assertIn("##PLAYER##", out)
    self.assertIsInstance(out, basestring)
    self.assertEqual(tm.xpos, 1)
    self.assertEqual(tm.ypos, 1)
    self.assertEqual(tp.xpos, 1)
    self.assertEqual(tp.ypos, 2)
    
if __name__ == "__main__":
  unittest.main()
