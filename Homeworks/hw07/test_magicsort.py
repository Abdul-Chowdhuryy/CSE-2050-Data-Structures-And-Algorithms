import unittest
from magicsort import MagicCase, INVERSION_BOUND
from magicsort import linear_scan, reverse_list, magic_insertionsort, magic_mergesort, magic_quicksort, magicsort

class TestMagicSort(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [1, 2, 3, 4, 5]
        self.reverse_sorted_list = [5, 4, 3, 2, 1]
        self.constant_num_inversions_list = [1, 2, 4, 3, 5]
        self.general_list = [5, 3, 2, 4, 1]

    def test_linear_scan_sorted_list(self):
        result = linear_scan(self.sorted_list)
        self.assertEqual(result, MagicCase.SORTED)

    def test_linear_scan_reverse_sorted_list(self):
        result = linear_scan(self.reverse_sorted_list)
        self.assertEqual(result, MagicCase.REVERSE_SORTED)

    def test_linear_scan_constant_num_inversions_list(self):
        result = linear_scan(self.constant_num_inversions_list)
        self.assertEqual(result, MagicCase.CONSTANT_NUM_INVERSIONS)

    def test_linear_scan_general_list(self):
        result = linear_scan(self.general_list)
        self.assertEqual(result, MagicCase.GENERAL)

    def test_reverse_list_even_length_list(self):
        L = [1, 2, 3, 4]
        reverse_list(L)
        self.assertEqual(L, [4, 3, 2, 1])

    def test_reverse_list_odd_length_list(self):
        L = [1, 2, 3, 4, 5]
        reverse_list(L)
        self.assertEqual(L, [5, 4, 3, 2, 1])

    def test_magic_insertionsort(self):
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        magic_insertionsort(L, left=2, right=5)
        self.assertEqual(L, [9, 8, 5, 6, 7, 4, 3, 2, 1, 0])

    def test_magic_mergesort(self):
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        magic_mergesort(L, left=2, right=5)
        self.assertEqual(L, [9, 8, 5, 6, 7, 4, 3, 2, 1, 0])

    def test_magic_quicksort(self):
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        magic_quicksort(L, left=2, right=5)
        self.assertEqual(L, [9, 8, 5, 6, 7, 4, 3, 2, 1, 0])

    def test_magicsort_sorted_list(self):
        result = magicsort(self.sorted_list)
        self.assertEqual(result, set())

    def test_magicsort_constant_num_inversions_list(self):
        result = magicsort(self.constant_num_inversions_list)
        self.assertEqual(result, {'magic_insertionsort'})

    def test_magicsort_general_list(self):
        result = magicsort(self.general_list)
        self.assertEqual(result, {'magic_quicksort'})

if __name__ == '__main__':
    unittest.main()
