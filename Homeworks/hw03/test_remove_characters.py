import unittest
from remove_characters import remove_characters

class Test_remove_characters(unittest.TestCase):
    def test_remove_characters(self):
        '''Test cases for remove_characters'''
        self.assertEqual(remove_characters("back", "ck"), "ba")
        self.assertEqual(remove_characters("back", ""), "back")
        self.assertNotEqual(remove_characters("back", "rack"), "back")
        self.assertNotEqual(remove_characters("back", "tack"), "back")

if __name__ == '__main__':
    unittest.main()
