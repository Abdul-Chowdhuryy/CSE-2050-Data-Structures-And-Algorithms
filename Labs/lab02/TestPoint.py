import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(3, 4)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""        
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)
    def test_eq(self):
        """Making sure the points = eachother """
        self.assertTrue(self.p1.__eq__(self.p3))
        self.assertFalse(self.p1.__eq__(self.p2))
       
    def test_equidistant(self):
        """Making sure the distance is equal"""
     
        self.assertTrue(self.p1.equidistant(self.p3))
        self.assertFalse(self.p1.equidistant(self.p2))
       

    def test_within(self):
        """Making sure the distance within is accurate"""
        distance = 1
        self.assertTrue(self.p1.within(distance, self.p3))
        self.assertFalse(self.p1.within(distance, self.p2))


unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects
