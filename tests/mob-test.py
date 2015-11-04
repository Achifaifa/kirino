import os, sys, unittest
sys.path.append(os.path.abspath("../source/"))
import mob


class Mobtestsuit(unittest.TestCase):
  """
  tests mob class
  """

  def test_mob_constructor(self):
    """
    Tests the mob constructor through existing levels
    """

    tm=mob.mob()
    self.assertTrue(tm.lock==0)
    self.assertTrue(tm.hit==0)

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
