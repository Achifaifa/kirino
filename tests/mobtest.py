import os, sys, unittest
sys.path.append(os.path.abspath("../source/"))
import mob


class Mobtestsuit(unittest.TestCase):
  """
  tests mob class
  """

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

  def test_mob_constructor_secondary(self):
    """
    """

    pass

  def test_mob_movement(self):
    """
    """

    pass

  def test_mob_movement_random(self):
    """
    """

    pass

  def test_mob_movement_trandom(self):
    """
    """

    pass

  def test_mob_search(self):
    """
    """

    pass

  def test_mob_attack(self):
    """
    """

    pass

if __name__ == "__main__":
  unittest.main()
