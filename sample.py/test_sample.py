import unittest
from sample import add

class SampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(""), "0")
        self.assertEqual(add("1"), "1")
        self.assertEqual(add("10"), "10")
        self.assertEqual(add("1,2"), "3")



if __name__ == "__main__":
    unittest.main()