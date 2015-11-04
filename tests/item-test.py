import unittest, os, sys

scriptpath = "../source/"
sys.path.append(os.path.abspath(scriptpath))
import item

class TestConsumables(unittest.TestCase):
  """
  Test the consumable class items 
  """

  def boostzero(self,item):
    """
    Checks that all the boosters in an item are zero
    """

    self.assertTrue(item.strbst==0)
    self.assertTrue(item.intbst==0)
    self.assertTrue(item.chabst==0)
    self.assertTrue(item.conbst==0)
    self.assertTrue(item.dexbst==0)
    self.assertTrue(item.perbst==0)
    self.assertTrue(item.wilbst==0)

  def test_HP_potions(self):
    """
    Checks HP potion proprieties

    Specific tests: HPR, MPR and subtype
    """
    ti=item.consumable(0,subtype=1)
    self.assertTrue(ti.type==0)
    self.assertTrue(ti.price>0)
    self.assertTrue(ti.name!="--EMPTY--")
    self.assertIsInstance(ti.name,basestring)
    self.assertTrue(ti.hpr>0)
    self.assertTrue(ti.mpr==0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==1)
    self.boostzero(ti)
    

  def test_MP_potions(self):
    """
    Checks MP potion proprieties

    Specific tests: HPR, MPR and subtype
    """
    ti=item.consumable(0,subtype=2)
    self.assertTrue(ti.type==0)
    self.assertTrue(ti.price>0)
    self.assertTrue(ti.name!="--EMPTY--")
    self.assertIsInstance(ti.name,basestring)
    self.assertTrue(ti.hpr==0)
    self.assertTrue(ti.mpr>0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==2)
    self.boostzero(ti)

  def test_recovery_potions(self):
    """
    Checks recovery potion proprieties

    Specific tests: HPR, MPR and subtype
    """
    ti=item.consumable(0,subtype=3)
    self.assertTrue(ti.type==0)
    self.assertTrue(ti.price>0)
    self.assertTrue(ti.name!="--EMPTY--")
    self.assertIsInstance(ti.name,basestring)
    self.assertTrue(ti.hpr>0)
    self.assertTrue(ti.mpr>0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==3)
    self.boostzero(ti)

  def test_status_potions(self):
    """
    Status potions not implemented
    """

    pass

  def test_tomes(self):
    """
    Checks tome proprieties
    """

    ti=item.consumable(1)
    self.assertTrue(ti.type==1)
    self.assertTrue(ti.price>0)
    self.assertTrue(ti.name!="--EMPTY--")
    self.assertIsInstance(ti.name,basestring)
    self.assertTrue(ti.hpr==0)
    self.assertTrue(ti.mpr==0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==0)
    self.assertIsInstance(ti.strbst,int)
    self.assertIsInstance(ti.intbst,int)
    self.assertIsInstance(ti.chabst,int)
    self.assertIsInstance(ti.conbst,int)
    self.assertIsInstance(ti.dexbst,int)
    self.assertIsInstance(ti.perbst,int)
    self.assertIsInstance(ti.wilbst,int)

  def test_attack(self):
    """
    Attack consumable class not implemented.
    """

    pass

  def test_food(self):
    """
    Tests attributes in unidentified/food type consumables
    """

    ti=item.consumable(3)
    self.assertTrue(ti.type==3)
    self.assertTrue(ti.price>0)
    self.assertTrue(ti.name!="--EMPTY--")
    self.assertIsInstance(ti.name,basestring)
    self.assertIsInstance(ti.hungrec, int)
    self.assertIsInstance(ti.chance, int)
    self.assertIsInstance(ti.statusr, int)
    self.assertIsInstance(ti.subtype, int)
    self.boostzero(ti)

  def test_empty(self):
    """
    Tests the generation of empty items
    """

    ti=item.consumable(4)
    self.assertTrue(ti.type==4)
    self.assertTrue(ti.price==0)
    self.assertTrue(ti.name=="--EMPTY--")
    self.assertIsInstance(ti.name,basestring)
    self.assertTrue(ti.hungrec==0)
    self.assertTrue(ti.chance==0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==0)
    self.boostzero(ti)

class TestItems(unittest.TestCase):
  """
  Tests the regular items
  """

  def test_head(self):
    pass

  def test_face(self):
    pass

  def test_neck(self):
    pass

  def test_shoulders(self):
    pass

  def test_chest(self):
    pass

  def test_onehand(self):
    pass

  def test_twohands(self):
    pass

  def test_ring(self):
    pass

  def test_belt(self):
    pass

  def test_legs(self):
    pass

  def test_feet(self):
    pass

  def test_empty(self):
    pass

class TestFunctions(unittest.TestCase):
  """
  Test functions in the item module, such as reset and enchant
  """

  def test_reset_consumable(self):
    """
    Checks if the consumable reset function resets an objecct
    """

    ti=item.consumable(0)
    ti.reset()
    self.assertTrue(ti.type==4)
    self.assertTrue(ti.price==0)
    self.assertTrue(ti.name=="--EMPTY--")
    self.assertTrue(ti.hpr==0)
    self.assertTrue(ti.mpr==0)
    self.assertIsInstance(ti.name,basestring)
    self.assertTrue(ti.hungrec==0)
    self.assertTrue(ti.chance==0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==0)
    self.assertTrue(ti.strbst==0)
    self.assertTrue(ti.intbst==0)
    self.assertTrue(ti.chabst==0)
    self.assertTrue(ti.conbst==0)
    self.assertTrue(ti.dexbst==0)
    self.assertTrue(ti.perbst==0)
    self.assertTrue(ti.wilbst==0)


  def test_reset_item(self):
    pass

  def test_enchant(self):
    pass

def main():
  unittest.main()

if __name__ == "__main__":
  main()
