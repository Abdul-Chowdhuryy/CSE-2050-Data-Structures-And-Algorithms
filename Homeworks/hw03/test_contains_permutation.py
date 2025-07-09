import unittest
from contains_permutation import contains_permutation

class Test_contains_permutation(unittest.TestCase):
    '''Test cases for contains_permutation'''
    def test_contains_permutation(self):
        self.assertTrue(contains_permutation("abcdef", "def"))
        self.assertTrue(contains_permutation("mnbdef", "mnb"))
        self.assertFalse(contains_permutation("patties", "set"))
        self.assertFalse(contains_permutation("catriots", "sit"))
    
    if __name__ == "__main__":
        unittest.Main()