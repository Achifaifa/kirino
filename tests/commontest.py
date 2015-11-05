import os, sys, unittest
sys.path.append(os.path.abspath("../source/"))
import common

class testcommon(unittest.TestCase):

  def test_vern(self):
    """
    Test that the version string is actually a string
    """

    self.assertIsInstance(common.vern(), basestring)
 
if __name__=="__main__":
  unittest.main() 
