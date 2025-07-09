import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_empty_list(self):
        """Test sorting an empty list."""
        arr = []
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, [])
        self.assertEqual(num_swaps, 0)

    def test_sorted_list(self):
        """Test sorting a sorted list."""
        arr = [1, 2, 3, 4, 5]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])
        self.assertEqual(num_swaps, 0)

    def test_reverse_sorted_list(self):
        """Test sorting a reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        expected_swaps = len(arr) * (len(arr) - 1) // 2
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])
        self.assertEqual(num_swaps, expected_swaps)

    def test_random_list(self):
        """Test sorting a random list."""
        arr = [7, 3, 2, 3, 4, 9]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertEqual(sorted_arr, [2, 3, 3, 4, 7, 9])
        self.assertEqual(len(sorted_arr), len(arr))
    
      
class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""
    def setUp(self):
        """Set up for bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm."""
    def setUp(self):
        """Set up for insertion sort algorithm for testing."""
        super().setUp(insertion_sort)

class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm."""
    def setUp(self):
        """Set up for selection sort algorithm for testing."""
        super().setUp(selection_sort)

if __name__ == "__main__":
    unittest.main()
