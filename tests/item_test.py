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
    self.assertIsInstance(ti.name, str)
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
    self.assertIsInstance(ti.name, str)
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
    self.assertIsInstance(ti.name, str)
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
    self.assertIsInstance(ti.name, str)
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
    self.assertIsInstance(ti.name, str)
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
    self.assertIsInstance(ti.name, str)
    self.assertTrue(ti.hungrec==0)
    self.assertTrue(ti.chance==0)
    self.assertTrue(ti.statusr==0)
    self.assertTrue(ti.subtype==0)
    self.boostzero(ti)

class TestItems(unittest.TestCase):
  """
  Tests the regular items
  """

  def itemtest(self,ti):
    self.assertTrue(ti.name!=" ")
    self.assertIsInstance(ti.name, str)
    self.assertTrue(ti.enchantlv==0)
    self.assertIsInstance(ti.enchantlv, int)
    self.assertTrue(ti.equip==0)
    self.assertIsInstance(ti.equip, int)
    self.assertIsInstance(ti.atk, int)
    self.assertIsInstance(ti.defn, int)
    self.assertTrue(ti.price>=0)
    self.assertIsInstance(ti.price, int)
    self.assertTrue(len(ti.bonuses)==7)
    for i in ti.bonuses:
      self.assertTrue(len(i)==8)
      self.assertIsInstance(i, str)
      self.assertTrue(getattr(ti,i)>=0)
      self.assertIsInstance(getattr(ti,i), int)

  def test_item_generation(self):
    """
    Tests the item generation. 
      -Creates a item in a random category
      -Checks the type 
      -Runs itemtest on it
    
    Since there is random generation involved, each category is tested 100 times
    """

    for j in range(100):
      for i in range(12):
        ti=item.item(i)
        self.assertTrue(ti.type==i)
        self.itemtest(ti)

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
    self.assertIsInstance(ti.name, str)
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
    """
    Tests item resetting with every item type
    """

    for i in range(11):
      ti=item.item(i+1)
      ti.reset()
      self.assertTrue(ti.name==" ")
      self.assertIsInstance(ti.name, str)
      self.assertTrue(ti.enchantlv==0)
      self.assertIsInstance(ti.enchantlv, int)
      self.assertTrue(ti.equip==0)
      self.assertIsInstance(ti.equip, int)
      self.assertTrue(ti.atk==0)
      self.assertIsInstance(ti.atk, int)
      self.assertTrue(ti.defn==0)
      self.assertIsInstance(ti.defn, int)
      self.assertTrue(ti.price==0)
      self.assertIsInstance(ti.price, int)
      self.assertTrue(len(ti.bonuses)==7)
      for i in ti.bonuses:
        self.assertTrue(len(i)==8)
        self.assertIsInstance(i, str)
        self.assertTrue(getattr(ti,i)==0)
        self.assertIsInstance(getattr(ti,i), int)


  def test_enchant_naming(self):
    """
    Tests item enchanting name modifier. 
    """
    
    ti=item.item(1)
    ti.name="test +1"
    ti.enchant()
    self.assertIn(ti.name,["test +2"," "])
  
  def test_enchant_atk_def(self):
    """
    Tests item enchanting attack and bonus raises
    """

    ti=item.item(1)
    ti.atk=ti.defn=0
    ti.enchant()
    self.assertTrue(ti.atk+ti.defn>=0)

  def test_enchant_pricing_fromzero(self):
    """
    Tests item enchanting price raises from 0 to 2
    """

    ti=item.item(1)
    ti.price=0
    ti.enchant()
    self.assertTrue(ti.price==1)

  def test_enchant_pricing_nonzero(self):
    """
    Tests item enchanting price raises from non-zero situations
    """

    ti=item.item(1)
    ti.price=100
    ti.enchant()
    self.assertTrue(ti.price==200)

  def test_enchant_level(self):
    """
    Checks if the enchantlv attribute is raised
    """

    for i in range(10):
      ti=item.item(1)
      ti.enchantlv=i
      ti.enchant()
      self.assertIn(ti.enchantlv,[i+1,0])

if __name__ == "__main__":
  unittest.main()
