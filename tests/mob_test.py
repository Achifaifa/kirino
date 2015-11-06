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
        self.assertTrue(tm.lock==0)
        self.assertTrue(tm.hit==0)
        self.assertTrue(tm.xpos==0)
        self.assertTrue(tm.ypos==0)
        self.assertTrue(len(tm.marker)==1)
        self.assertIsInstance(tm.marker, basestring)
        self.assertIsInstance(tm.level, int)
        self.assertIsInstance(tm.prestige, int)
        self.assertIsInstance(tm.exp, int)
        self.assertTrue(tm.exp>=0)
        self.assertIsInstance(tm.INT, int)
        self.assertIsInstance(tm.DEX, int)
        self.assertIsInstance(tm.PER, int)
        self.assertIsInstance(tm.CON, int)
        self.assertIsInstance(tm.WIL, int)
        self.assertIsInstance(tm.CHA, int)
        self.assertIsInstance(tm.STR, int)
        self.assertIsInstance(tm.atk, int)
        self.assertIsInstance(tm.defn, int)
        self.assertTrue(tm.atk>=0)
        self.assertTrue(tm.defn>=0)
        self.assertTrue(tm.MP>=0)
        self.assertTrue(tm.HP>=0)
        self.assertTrue(tm.END>=0)
        self.assertTrue(tm.SPD>0)


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
        self.assertTrue(tm.HP==18)
        self.assertTrue(tm.MP==2)
        self.assertTrue(tm.END==14)
        self.assertTrue(tm.SPD==6)

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
            self.assertTrue(tm.ypos==2)
            self.assertTrue(ret==0)
          else:
            self.assertTrue(tm.ypos==1)
            self.assertTrue(ret==1)
          self.assertTrue(tm.xpos==1)

  def test_mob_movement_random(self):
    """
    Runs the mob through the test dungeon and tests its random movement
    """

    td=testdungeon
    tm=mob.mob(0)
    tm.xpos=1
    tm.ypos=1
    for i in range(100):
      tm.randmove(td,1)
      self.assertTrue(tm.xpos==1)
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
      tm.trandmove(td)
      self.assertTrue(tm.xpos==1)
      self.assertIn(tm.ypos, [1,2])

  def test_mob_search(self):
    """
    #TO-DO: search for test automation
    """

    pass

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
    self.assertTrue(tp.totalrcv==15)
    self.assertIsInstance(tp.totalrcv, int)
    self.assertTrue(tp.hp2==85)
    self.assertIsInstance(tp.hp2, int)
    self.assertIn("##MOB##", out)
    self.assertIn("##PLAYER##", out)
    self.assertIsInstance(out, basestring)
    self.assertTrue(tm.xpos==1)
    self.assertTrue(tm.ypos==1)
    self.assertTrue(tp.xpos==1)
    self.assertTrue(tp.ypos==2)




if __name__ == "__main__":
  unittest.main()