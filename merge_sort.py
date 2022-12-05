import time

class MergeSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        start_time = time.time()
        self.__sort(self.array)
        self.final_time = time.time() - start_time

    def __sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2

            sub_array_left = arr[:mid]
            sub_array_right = arr[mid:]

            self.__sort(sub_array_left)
            self.__sort(sub_array_right)

            i = j = k = 0

            while i < len(sub_array_left) and j < len(sub_array_right):
                if sub_array_left[i] < sub_array_right[j]:
                    arr[k] = sub_array_left[i]
                    i += 1
                else:
                    arr[k] = sub_array_right[j]
                    j += 1
                k += 1

            while i < len(sub_array_left):
                arr[k] = sub_array_left[i]
                i += 1
                k += 1

            while j < len(sub_array_right):
                arr[k] = sub_array_right[j]
                j += 1
                k += 1
