import random
from merge_sort import MergeSort
from heap_sort import HeapSort
from quick_sort import QuickSortMedio, QuickSortAchaPivo
from utils.sort_mode import SortMode
from utils.color import color

def generate_instance(n):
    return [i + 1 for i in range(n)]

def __sort(mode, arr, f, len_little_disordered, len_very_disorderly):
    print(color.BOLD + u'\u2794' + f' {str(mode)} ({len(arr)})' + color.END)

    f.write(f'\n====== {str(mode)} ======\n')

    f.write('=> Pouco desordenada:\n')

    little_disordered_arr = arr.copy()
    for _ in range(int(len_little_disordered)):
        index_a = random.randint(0, len(arr) - 1)
        index_b = random.randint(0, len(arr) - 1)
        little_disordered_arr[index_a], little_disordered_arr[index_b] = little_disordered_arr[index_b], little_disordered_arr[index_a]

    if mode == SortMode.MERGESORT:
        sort = MergeSort(little_disordered_arr)
        sort.sort()
    elif mode == SortMode.QUICKSORT_MEDIO:
        sort = QuickSortMedio(little_disordered_arr)
        sort.sort()
    elif mode == SortMode.QUICKSORT_ACHA_PIVO:
        sort = QuickSortAchaPivo(little_disordered_arr)
        sort.sort()
    elif mode == SortMode.HEAPSORT:
        sort = HeapSort(little_disordered_arr)
        sort.sort()

    f.write(f'\tNumber of swaps: {int(len_little_disordered)}\n')
    f.write(f'\tTime: {sort.final_time}s\n')

    print('   ' + color.GREEN + u'\u2713' + ' Pouco desordenada' + color.END)

    ######################################

    f.write('=> Muito desordenada:\n')

    very_disorderly_arr = arr.copy()
    for _ in range(int(len_very_disorderly)):
        index_a = random.randint(0, len(arr) - 1)
        index_b = random.randint(0, len(arr) - 1)
        very_disorderly_arr[index_a], very_disorderly_arr[index_b] = very_disorderly_arr[index_b], very_disorderly_arr[index_a]

    if mode == SortMode.MERGESORT:
        sort = MergeSort(very_disorderly_arr)
        sort.sort()
    elif mode == SortMode.QUICKSORT_MEDIO:
        sort = QuickSortMedio(very_disorderly_arr)
        sort.sort()
    elif mode == SortMode.QUICKSORT_ACHA_PIVO:
        sort = QuickSortAchaPivo(very_disorderly_arr)
        sort.sort()
    elif mode == SortMode.HEAPSORT:
        sort = HeapSort(very_disorderly_arr)
        sort.sort()

    f.write(f'\tNumber of swaps: {int(len_very_disorderly)}\n')
    f.write(f'\tTime: {sort.final_time}s\n')

    print('   ' + color.GREEN + u'\u2713' + ' Muito desordenada' + color.END)

    
def main():
    cases = [100, 1000, 5000, 10000, 50000, 100000]
    # cases = [10]

    for case in cases:
        f = open(f'output/result{case}.txt', 'w')
        f.write(f'n = {case}\n')
        
        arr = generate_instance(case)

        len_little_disordered = len(arr) * 0.1
        len_very_disorderly = len(arr) * 0.5

        __sort(SortMode.MERGESORT, arr.copy(), f, len_little_disordered, len_very_disorderly)
        __sort(SortMode.QUICKSORT_MEDIO, arr.copy(), f, len_little_disordered, len_very_disorderly)
        __sort(SortMode.QUICKSORT_ACHA_PIVO, arr.copy(), f, len_little_disordered, len_very_disorderly)
        __sort(SortMode.HEAPSORT, arr.copy(), f, len_little_disordered, len_very_disorderly)
        
        f.close()

if __name__ == "__main__":
    main()
