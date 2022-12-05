from enum import Enum

class SortMode(Enum):
    MERGESORT = 1
    QUICKSORT = 2
    HEAPSORT = 3

    def __str__(self):
        if self == SortMode.MERGESORT:
            return 'MergeSort'
        elif self == SortMode.QUICKSORT:
            return 'QuickSort'
        elif self == SortMode.HEAPSORT:
            return 'HeapSort'
