import unittest, sys

scriptpath = "../source/common.py"
sys.path.append(os.path.abspath(scriptpath))
import common

class testcommon(unittest.TestCase):

  def test_vern(self):
    """
    Test that the version string is actually a string
    """

    self.assertTrue(common.vern().isalpha())
    self.assertFalse(common.vern().isnum())
 
if __name__=="__main__":
  main() 
