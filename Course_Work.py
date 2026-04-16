import random

class Sort:
    def __init__(self, lst):
        if lst:
            self._list = lst
        else:
            raise ValueError("Please provide a non empty list")
        
        self._sorted_list = []
        self._counter = 0

    @property
    def isSorted(self):
        return(all(self._list[i] <= self._list[i+1] for i in range(len(self._list)-1)))
    
    @property
    def sort_list(self):
        return sorted(self._list)

    @property
    def print_sorted_list(self):
        print(f"Sorted list: {self.sort_list}")
        print(f"times swapped: {self._counter}")

    @property
    def get_sorted_list(self):
        self._sorted_list = self.sort_list
        return(self._sorted_list)
    
class BubbleSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def sort_list(self):
        while not self.isSorted:
            for i in range(0, len(self._list)-1):
                if self._list[i] > self._list[i+1]:
                    self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
                    self._counter+=1
        return self._list

class MergeSort(Sort):
    pass

class QuickSort(Sort):
    pass

class BogoSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)
    
    @property
    def sort_list(self):
        while not self.isSorted:
            num1=random.randrange(0, len(self._list))
            num2=random.randrange(0, len(self._list))
            if num1 is not num2:
                self._list[num1], self._list[num2] = self._list[num2], self._list[num1]
                self._counter+=1
        return self._list
    
class HeapSort(Sort):
    pass

lst = [100, 4, -5, 3, 7, 1, 6, -1, 3, 7]
lst1 = [5, 3, 2, 4, 1]
random.shuffle(lst1)

sorteD = BubbleSort(lst)

sorteD.print_sorted_list

lst2 = sorteD.get_sorted_list
