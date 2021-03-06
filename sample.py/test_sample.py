import unittest
from sample import add

class SampleTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(""), "0")
        self.assertEqual(add("1"), "1")
        self.assertEqual(add("10"), "10")
        self.assertEqual(add("1,2"), "3")
        self.assertEqual(add("1,2,3,4"), "10")
        self.assertEqual(add("4,5,6,7,8,9"), "39")
        self.assertEqual(add("21,5\n4,7"), "37")
        self.assertEqual(add("2,59\n1004"), "61")



if __name__ == "__main__":
    unittest.main()