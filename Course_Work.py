import random


class Sort:
    def __init__(self, lst):
        if lst:
            self._list = lst.copy()
        else:
            raise ValueError("Please provide a non empty list")

        self._counter = 0

    @property
    def isSorted(self):
        return (all(self._list[i] <= self._list[i+1] for i in range(len(self._list)-1)))

    @property
    def _sort_list(self):
        self._counter = 0
        self._list = sorted(self._list)
        return self._list

    @property
    def print_sorted_list(self):
        print(f"Sorted list: {self._sort_list}")
        print(f"Comparisons: {self._counter}")

    @property
    def get_sorted_list(self):
        return (self._sort_list)
    
    @property
    def get_reverse_sorted_list(self):
        reverse = self._sort_list
        reverse.reverse()
        return (reverse)


class BubbleSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def _sort_list(self):
        while not self.isSorted:
            for i in range(0, len(self._list)-1):
                self._counter += 1
                if self._list[i] > self._list[i+1]:
                    self._list[i], self._list[i+1] = self._list[i+1], self._list[i]
        return self._list


class MergeSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def _sort_list(self):
        left = 0
        right = len(self._list)-1
        self.split(left, right)
        return self._list

    def split(self, left, right):
        if left < right:
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

        i = 0
        j = 0
        k = left

        while i < len1 and j < len2:
            self._counter += 1
            if Left_side[i] <= Right_side[j]:
                self._list[k] = Left_side[i]
                i += 1
            else:
                self._list[k] = Right_side[j]
                j += 1
            k += 1

        while i < len1:
            self._list[k] = Left_side[i]
            i += 1
            k += 1

        while j < len2:
            self._list[k] = Right_side[j]
            j += 1
            k += 1


class QuickSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def _sort_list(self):
        low = 0
        high = len(self._list) - 1
        self.quicksort(low, high)
        return self._list

    def quicksort(self, low, high):
        if low < high:
            pivot = self.part_sort(low, high)

            self.quicksort(low, pivot-1)
            self.quicksort(pivot+1, high)

    def part_sort(self, low, high):
        pivot = self._list[high]

        i = low-1

        for j in range(low, high):
            self._counter += 1
            if self._list[j] < pivot:
                i += 1
                self._list[i], self._list[j] = self._list[j], self._list[i]

        self._list[i+1], self._list[high] = self._list[high], self._list[i+1]
        return (i+1)


class BogoSort(Sort):
    def __init__(self, lst):
        super().__init__(lst)

    @property
    def _sort_list(self):
        while not self.isSorted:
            num1 = random.randrange(0, len(self._list))
            num2 = random.randrange(0, len(self._list))
            if num1 is not num2:
                self._list[num1], self._list[num2] = self._list[num2], self._list[num1]
                self._counter += 1
        return self._list


class HeapSort(Sort):

    def __init__(self, lst):
        super().__init__(lst)

    @property
    def _sort_list(self):
        length = len(self._list)

        for i in range(length//2, -1, -1):
            self.max_heap(length, i)

        for i in range(length - 1, 0, -1):
            self._list[0], self._list[i] = self._list[i], self._list[0]
            self.max_heap(i, 0)

        return self._list

    def max_heap(self, length, i):
        largest = i

        left = 2*i+1
        right = 2*i+2

        if left < length and self._list[left] > self._list[largest]:
            largest = left
            self._counter += 1

        if right < length and self._list[right] > self._list[largest]:
            largest = right
            self._counter += 1

        if largest != i:
            self._list[i], self._list[largest] = self._list[largest], self._list[i]
            self.max_heap(length, largest)

print("Welcome! What kind of list are you sorting? (Enter corresponding number)")
print("1. Numbers")
print("2. Words")
s1 = int(input("Option: ").strip())
if s1 != 1 and s1 !=2:
    raise Exception("Option does not exist, please try again")
print()

print("What type of sorting algorithm would you like to use? (Enter corresponding number)")
print("1. Bubble Sort")
print("2. Merge Sort")
print("3. Quick Sort")
print("4. Bogo Sort")
print("5. Heap Sort")
print("6. Python sorting")
s2 = int(input("Option: ").strip())
if s2 not in range(1,7):
    raise Exception("Option does not exist, please try again")
print()

print("Do you want the list to be reversed? (lowest to highest -> highest to lowest)")
s4 = input("Y/N: ").strip().upper()
if s4 != "Y" and s4 != "N":
    raise Exception("Option does not exist, please try again")

print("Do you want a new file with the unsorted and sorted list")
print("Or the sorted list added to current file")
print("Or rewrite the file with the sorted list?")
print("1. New")
print("2. Add")
print("3. Rewrite")
s3 = int(input("Option: ").strip())
if s3 not in range(1, 4):
    raise Exception("Option does not exist, please try again")
print()

print("Enter file name/file path")
f_name = input("Name: ")

if s3 == 1:
    print("New file name")
    f_new = input("Name:")

if s1 == 1:
    with open(f_name, 'r') as file:
        text = file.read().split()
   
    if not text:
        raise ValueError("File is empty")

    try:
        List=[float(number) for number in text]
    except ValueError:
        raise ValueError("File must contain only numbers")
    
        

else:
    with open(f_name, 'r') as file:
        text = file.read().strip()

    if not text:
        raise ValueError("File is empty")
    if ',' not in text:
        raise ValueError("Words must be separated by commas")
    
    List = [word.strip() for word in text.split(',')]
    
    if any(word == '' for word in List):
        raise ValueError("Empty words are not allowed. Check your comma placements")

algorithms = {
    1: BubbleSort(List),
    2: MergeSort(List),
    3: QuickSort(List),
    4: BogoSort(List),
    5: HeapSort(List),
    6: Sort(List)
}

S=algorithms[s2]


if s4 == "N":
    if s3 == 1:
        f = open(f_new, "x")
        with open(f_new, "w") as file:
            file.write(f"Unsorted list: {List}\n")
            file.write(f"Sorted list: {S.get_sorted_list}\n")
    elif s3 == 2:
        with open(f_name, "a") as file:
            file.write("\n")
            file.write(f"Sorted list: {S.get_sorted_list}")
    else:
        with open(f_name, "w") as file:
            file.write(f"Sorted list: {S.get_sorted_list}")
else:
    if s3 == 1:
        f = open(f_new, "x")
        with open(f_new, "w") as file:
            file.write(f"Unsorted list: {List}\n")
            file.write(f"Sorted list: {S.get_reverse_sorted_list}\n")
    elif s3 == 2:
        with open(f_name, "a") as file:
            file.write("\n")
            file.write(f"Sorted list: {S.get_reverse_sorted_list}")
    else:
        with open(f_name, "w") as file:
            file.write(f"Sorted list: {S.get_reverse_sorted_list}")
