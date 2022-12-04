import unittest
from merge_sort import MergeSort

class TestMergeSort(unittest.TestCase):

    def test_merge_sort_success(self):
        arr = [4, 8, 7, 2, 11, 1, 3]
        merge_sort = MergeSort(arr)
        merge_sort.sort()

        self.assertEqual(arr, [1, 2, 3, 4, 7, 8, 11])

    def test_merge_sort_failure(self):
        arr = [4, 8, 7, 2, 11, 1, 3]
        merge_sort = MergeSort(arr)
        merge_sort.sort()

        self.assertNotEqual(arr, [1, 2, 3, 11, 4, 7, 8])
