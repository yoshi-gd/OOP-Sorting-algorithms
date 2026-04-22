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
        print(f"Comparisons: {self._counter}")

    @property
    def get_sorted_list(self):
        return(self.sort_list)
    
class BubbleSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def sort_list(self):
        while not self.isSorted:
            for i in range(0, len(self._list)-1):
                self._counter+=1
                if self._list[i] > self._list[i+1]:
                    self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
        return self._list

class MergeSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def sort_list(self):
        left = 0
        right = len(self._list)-1
        self.split(left, right)
        return self._list
        
    def split(self, left, right):
        if left<right:
            middle = (left+right)//2
            self.split(left, middle)
            self.split(middle+1, right)
            self.merge(left, middle, right)
    
    def merge(self, left, middle, right):
        len1 = middle - left + 1
        len2 = right - middle

        Left_side = [0] * len1
        Right_side = [0] * len2

        for i in range(len1):
            Left_side[i] = self._list[left + i]
        for j in range(len2):
            Right_side[j] = self._list[middle + 1 + j]
        
        i=0
        j=0
        k=left

        while i < len1 and j < len2:
            self._counter+=1
            if Left_side[i] <= Right_side[j]:
                self._list[k] = Left_side[i]
                i+=1
            else:
                self._list[k] = Right_side[j]
                j+=1
            k+=1

        while i<len1:
            self._list[k] = Left_side[i]
            i+=1
            k+=1

        while j<len2:
            self._list[k] = Right_side[j]
            j+=1
            k+=1

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
