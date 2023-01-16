from enum import Enum

class SortMode(Enum):
    MERGESORT = 1
    QUICKSORT_MEDIO = 2
    QUICKSORT_ACHA_PIVO = 3
    HEAPSORT = 4

    def __str__(self):
        if self == SortMode.MERGESORT:
            return 'MergeSort'
        elif self == SortMode.QUICKSORT_MEDIO:
            return 'QuickSort Médio'
        elif self == SortMode.QUICKSORT_ACHA_PIVO:
            return 'QuickSort Acha Pivô'
        elif self == SortMode.HEAPSORT:
            return 'HeapSort'
