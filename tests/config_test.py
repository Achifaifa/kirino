import unittest, os, sys
sys.path.append(os.path.abspath("../source/"))
import config

class testcommon(unittest.TestCase):

  def setup(self):
    """
    Creates the config class for tests
    """

    cfg=config.config()

  def test_class(self):
    """
    Tests that the class variables don't have weird stuff
    """
    
    cfg=config.config()

    self.assertIn(cfg.autosave,[0,1])
    self.assertIn(cfg.fog,[0,1])
    self.assertIsInstance(cfg.gomsg,str)

    # Assert that the key mappings are 1 digit alnumnumeric strings

    self.assertIsInstance(cfg.northeast, str)
    self.assertIsInstance(cfg.northwest, str)
    self.assertIsInstance(cfg.southeast, str)
    self.assertIsInstance(cfg.southwest, str)
    self.assertIsInstance(cfg.north, str)
    self.assertIsInstance(cfg.south, str) 
    self.assertIsInstance(cfg.east, str) 
    self.assertIsInstance(cfg.west, str) 
    self.assertIn(len(cfg.northeast),[0,1])
    self.assertIn(len(cfg.northwest),[0,1])
    self.assertIn(len(cfg.southeast),[0,1])
    self.assertIn(len(cfg.southwest),[0,1])
    self.assertIn(len(cfg.north),[0,1])
    self.assertIn(len(cfg.south),[0,1])
    self.assertIn(len(cfg.east),[0,1])
    self.assertIn(len(cfg.west),[0,1])
    self.assertIsInstance(cfg.charsh, str)
    self.assertIn(len(cfg.charsh),[0,1])
    self.assertIsInstance(cfg.opt, str)
    self.assertIn(len(cfg.opt),[0,1])
    self.assertIsInstance(cfg.quit, str)
    self.assertIn(len(cfg.quit),[0,1])
    self.assertIsInstance(cfg.report, str)
    self.assertIn(len(cfg.report),[0,1])
    self.assertIsInstance(cfg.nextf, str)
    self.assertIn(len(cfg.nextf),[0,1])
    self.assertIsInstance(cfg.showkeys, str)
    self.assertIn(len(cfg.showkeys),[0,1])
    self.assertIsInstance(cfg.showmap, str)
    self.assertIn(len(cfg.showmap),[0,1])
    self.assertIsInstance(cfg.console, str)
    self.assertIn(len(cfg.console),[0,1])
    self.assertIsInstance(cfg.quick1, str)
    self.assertIn(len(cfg.quick1),[0,1])
    self.assertIsInstance(cfg.quick2, str)
    self.assertIn(len(cfg.quick2),[0,1])
    self.assertIsInstance(cfg.quick3, str) 
    self.assertIn(len(cfg.quick3),[0,1])
    self.assertIsInstance(cfg.quick4, str)
    self.assertIn(len(cfg.quick4),[0,1])
    self.assertIsInstance(cfg.quick5, str)
    self.assertIn(len(cfg.quick5),[0,1])
    self.assertIsInstance(cfg.quick6, str)
    self.assertIn(len(cfg.quick6),[0,1])

if __name__=="__main__":
  unittest.main() 
