import unittest
import random
from SeparateChainingHashTable import SeparateChainingHashTable
from LinearProbingHashTable import LinearProbingHashTable

random.seed(658)

class TestHashTableFactory(unittest.TestCase):
    def setUp(self):
        """
        Set up the hash tables for testing.
        """
        self.setup_separate_chaining()
        self.setup_linear_probing()

    def setup_separate_chaining(self):
        """
        Set up the Separate Chaining Hash Table
        """
        self.hash_table_separate = SeparateChainingHashTable()

        # Add items to separate chaining hash table
        for i in range(10):
            self.hash_table_separate[i] = str(i)

    def setup_linear_probing(self):
        """
        Set up the Linear Probing Hash Table
        """
        self.hash_table_linear = LinearProbingHashTable()

        # Add items to linear probing hash table
        for i in range(10):
            self.hash_table_linear[i] = str(i)

    def test_put_get_sequential_separate(self):
        """
        Test adding items one by one and checking if they can be retrieved, counted, and found
        """
        for i in range(10):
            self.assertEqual(self.hash_table_separate[i], str(i))
            self.assertEqual(len(self.hash_table_separate), i + 1)
            self.assertTrue(i in self.hash_table_separate)
            load_factor = self.hash_table_separate.get_loadfactor()
            self.assertGreaterEqual(load_factor, 0.5)
            self.assertLessEqual(load_factor, 1.5)

        for i in range(10):
            self.assertTrue(i in self.hash_table_separate)

    def test_put_get_remove_sequential_linear(self):
        """
        Test adding items one by one, checking if they can be retrieved, counted, and found
        """
        for i in range(10):
            self.assertEqual(self.hash_table_linear[i], str(i))
            self.assertEqual(len(self.hash_table_linear), i + 1)
            self.assertTrue(i in self.hash_table_linear)
            load_factor = self.hash_table_linear.get_loadfactor()
            self.assertGreaterEqual(load_factor, 0.1)
            self.assertLessEqual(load_factor, 0.9)

        for i in range(10):
            value = self.hash_table_linear.pop(i)
            self.assertEqual(value, str(i))
            self.assertFalse(i in self.hash_table_linear)


class TestSeparateChainingHashTable(unittest.TestCase):
    def setUp(self):
        """Set up for Separate Chaining Hash Table for testing."""
        super().setUp()
        self.factory = TestHashTableFactory()
        self.factory.setup_separate_chaining()

    def test_put_get_sequential_separate(self):
        """Test adding items one by one and checking if they can be retrieved, counted, and found."""
        self.factory.test_put_get_sequential_separate()


class TestLinearProbingHashTable(unittest.TestCase):
    def setUp(self):
        """Set up for Linear Probing Hash Table for testing."""
        super().setUp()
        self.factory = TestHashTableFactory()
        self.factory.setup_linear_probing()

    def test_put_get_remove_sequential_linear(self):
        """Test adding items one by one, checking if they can be retrieved, counted, and found."""
        self.factory.test_put_get_remove_sequential_linear()


if __name__ == "__main__":
    unittest.main()
