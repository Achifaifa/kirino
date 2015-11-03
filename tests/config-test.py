import unittest, os, sys

scriptpath = "../source/"
sys.path.append(os.path.abspath(scriptpath))
import config

class testcommon(unittest.TestCase):

  def setup(self):
    """
    Creates the config class for tests
    """

    cfg=config.config 

  def test_class(self):
    """
    Tests that the class variables don't have weird stuff
    """
    
    cfg=config.config 

    self.assertIn(cfg.autosave,[0,1])
    self.assertIn(cfg.fog,[0,1])
    self.assertIsInstance(cfg.gomsg,basestring)

    # Assert that the key mappings are 1 digit alnumnumeric strings

    self.assertIsInstance(cfg.northeast, basestring)
    self.assertIsInstance(cfg.nortwest, basestring)
    self.assertIsInstance(cfg.southeast, basestring)
    self.assertIsInstance(cfg.southwest, basestring)
    self.assertIsInstance(cfg.north, basestring)
    self.assertIsInstance(cfg.south, basestring) 
    self.assertIsInstance(cfg.east, basestring) 
    self.assertIsInstance(cfg.west, basestring) 
    self.assertIn(len(cfg.northeast),[0,1])
    self.assertIn(len(cfg.nortwest),[0,1])
    self.assertIn(len(cfg.southeast),[0,1])
    self.assertIn(len(cfg.southwest),[0,1])
    self.assertIn(len(cfg.north),[0,1])
    self.assertIn(len(cfg.south),[0,1])
    self.assertIn(len(cfg.east),[0,1])
    self.assertIn(len(cfg.west),[0,1])
    self.assertIsInstance(cfg.charsh, basestring)
    self.assertIn(len(cfg.charsh,[0,1]))
    self.assertIsInstance(cfg.opt, basestring)
    self.assertIn(len(cfg.opt,[0,1]))
    self.assertIsInstance(cfg.quit, basestring)
    self.assertIn(len(cfg.quit,[0,1]))
    self.assertIsInstance(cfg.report, basestring)
    self.assertIn(len(cfg.report,[0,1]))
    self.assertIsInstance(cfg.nextf, basestring)
    self.assertIn(len(cfg.nextf,[0,1]))
    self.assertIsInstance(cfg.showkeys, basestring)
    self.assertIn(len(cfg.showkeys,[0,1]))
    self.assertIsInstance(cfg.showmap, basestring)
    self.assertIn(len(cfg.showmap,[0,1]))
    self.assertIsInstance(cfg.console, basestring)
    self.assertIn(len(cfg.console,[0,1]))
    self.assertIsInstance(cfg.quick1, basestring)
    self.assertIn(len(cfg.quick1,[0,1]))
    self.assertIsInstance(cfg.quick2, basestring)
    self.assertIn(len(cfg.quick2,[0,1]))
    self.assertIsInstance(cfg.quick3, basestring) 
    self.assertIn(len(cfg.quick3,[0,1]))
    self.assertIsInstance(cfg.quick4, basestring)
    self.assertIn(len(cfg.quick4,[0,1]))
    self.assertIsInstance(cfg.quick5, basestring)
    self.assertIn(len(cfg.quick5,[0,1]))
    self.assertIsInstance(cfg.quick6, basestring)
    self.assertIn(len(cfg.quick6,[0,1]))

if __name__=="__main__":
  unittest.main  
