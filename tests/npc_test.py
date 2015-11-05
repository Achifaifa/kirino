import os, sys, unittest
sys.path.append(os.path.abspath("../source/"))
import npc



class npctestsuit(unittest.TestCase):
  """
  Tests for NPC creation and management
  """

  def test_npc_constructor(self):
    """
    Tests that the NPC constructor correctly chooses elements
    """

    pass


if __name__ == "__main__":
  unittest.main()
