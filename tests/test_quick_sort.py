import unittest
from quick_sort import QuickSortMedio, QuickSortAchaPivo

class TestMergeSort(unittest.TestCase):

    def test_quick_sort_medio_success(self):
        arr = [4, 8, 7, 2, 11, 1, 3]
        quick_sort = QuickSortMedio(arr)
        quick_sort.sort()

        self.assertEqual(arr, [1, 2, 3, 4, 7, 8, 11])

    def test_quick_sort_medio_failure(self):
        arr = [4, 8, 7, 2, 11, 1, 3]
        quick_sort = QuickSortMedio(arr)
        quick_sort.sort()

        self.assertNotEqual(arr, [1, 2, 3, 11, 4, 7, 8])

    def test_quick_sort_acha_pivo_success(self):
        arr = [4, 8, 7, 2, 11, 1, 3]
        quick_sort = QuickSortAchaPivo(arr)
        quick_sort.sort()

        self.assertEqual(arr, [1, 2, 3, 4, 7, 8, 11])

    def test_quick_sort_acha_pivo_failure(self):
        arr = [4, 8, 7, 2, 11, 1, 3]
        quick_sort = QuickSortAchaPivo(arr)
        quick_sort.sort()

        self.assertNotEqual(arr, [1, 2, 3, 11, 4, 7, 8])
