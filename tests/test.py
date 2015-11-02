import unittest

class TestSuite(unittest.TestCase):

  def test(self):
    self.assertRaises(IndexError,[][1])

  def test2(self):
    self.assertEqual(range(10),range(10))

  def test3(self):
    self.assertEqual(1,1)     

def main():
  unittest.main()

if __name__ == "__main__":
  main()
