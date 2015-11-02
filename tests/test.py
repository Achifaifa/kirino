import unittest

class TestSuite(unittest.TestCase):

    def test(self):
        self.failIf(1==0)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
