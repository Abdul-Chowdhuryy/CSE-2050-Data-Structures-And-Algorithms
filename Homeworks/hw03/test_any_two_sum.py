import unittest
from any_two_sum import any_two_sum

class Test_any_two_sum(unittest.TestCase):
    def test_any_two_sum(self):
        '''Test cases for any_two_sum'''
        self.assertTrue(any_two_sum([3, 3, 2, 5], 7))
        self.assertTrue(any_two_sum([1, 3, 4, 3], 7))
        self.assertFalse(any_two_sum([1, 1, 1, 1], 5))
        self.assertFalse(any_two_sum([2, 2, 2, 0], 8))

    if __name__ == "__main__":
        unittest.Main()
