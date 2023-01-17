import time

class QuickSortMedio:
    
    def __init__(self, array):
        self.array = array
    
    def sort(self):
        # print(self.array)
        start_time = time.time()
        self.__sort(self.array, 0, len(self.array), True)
        self.final_time = time.time() - start_time
        # print(self.array)

    def median_of_three(self, arr, low, high):
        mid = (low + high - 1) // 2
        a = arr[low]
        b = arr[mid]
        c = arr[high-1]

        if a <= b <= c:
            return b, mid
        if c <= b <= a:
            return b, mid
        if a <= c <= b:
            return c, high-1
        if b <= c <= a:
            return c, high-1
        
        return a, low

    def __sort(self, L, low, high, ascending=True):
        result = 0
        if low < high:
            pivot_location, result = self.__partition(L, low, high, ascending)
            result += self.__sort(L, low, pivot_location, ascending)
            result += self.__sort(L, pivot_location + 1, high, ascending)
        return result


    def __partition(self, L, low, high, ascending=True):
        result = 0
        pivot, pidx = self.median_of_three(L, low, high)
        L[low], L[pidx] = L[pidx], L[low]
        i = low + 1
        
        for j in range(low+1, high, 1):
            result += 1
            if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
                L[i], L[j] = L[j], L[i]
                i += 1
        
        L[low], L[i-1] = L[i-1], L[low]

        return i - 1, result

class QuickSortAchaPivo:

    def __init__(self, array):
        self.array = array
    
    def sort(self):
        print(self.array)
        start_time = time.time()
        self.__sort(self.array, 0, len(self.array) - 1)
        self.final_time = time.time() - start_time
        print(self.array)

    def _acha_pivo(self, arr, esq, dir):
        pos = esq + 1
        pivo = 0

        while pos <= dir:
            if arr[pos] >= arr[pos - 1]:
                pos = pos + 1
            else:
                pivo = pos
                break
        
        return pivo

    def particao_acha_pivo(self, arr, esq, dir):
        pivo = arr[esq]
        i = esq
        j = dir

        while i <= j:
            while arr[i] <= pivo:
                i += 1
                if i == dir:
                    break
            while pivo <= arr[j]:
                j -= 1
                if j == esq:
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        arr[esq], arr[j] = arr[j], arr[esq]

        return j

    def __sort(self, arr, esq, dir):
        if esq >= dir:
            return

        pivo = self._acha_pivo(arr, esq, dir)

        if(pivo != 0):
            arr[pivo], arr[esq] = arr[esq], arr[pivo]
            p = self.particao_acha_pivo(arr, esq, dir)
            self.__sort(arr, esq, p - 1)
            self.__sort(arr, p + 1, dir)
