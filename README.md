# OOP-Sorting-algorithms
A generic sorting algorithm with different other algorithms as subclasses

## Introduction

The goal is to make a collection of sorting algorithms that can easily be imported and used or using the menu in the main code be able to read and write the sorted lists to .txt files

To run the program simply copy the code and put it in environment that can comile and run python from there ***follow the written instructions in the terminal***

To use the program there are 2 ways:
1. importing the desired algorithms `from Course_Work import (sort name)` and then using `.get_sorted_list` to sort the given list and assign it or using `.print_sorted_list` to print the sorted list in the terminal
2. copying the code to an environment that can run it and ***following the steps given in the terminal***. If the given list contains numbers ***it must be written in a line seperated by spaces***. If the given list contains words ***they must be seperated by commas ","***

## Analysis:

This code follows the 4 object-oriented programming pillars:
1. **Polymorphism** - Same operation differently performed.

Each sorting algorithm gives the same result - a sorted list, but each one does it differently. Using polymorphism we can have each algorithm override only the `_sort_list` function to reduce the code size.

- The original `_sort_list`
<img width="486" height="176" alt="image" src="https://github.com/user-attachments/assets/baf7ffa9-3d60-4a4b-84a2-ca77e5da4360" />


- BubbleSort's `_sort_list`
<img width="1034" height="266" alt="image" src="https://github.com/user-attachments/assets/e156f262-af15-475a-bc18-8310a816ae21" />


- MergeSort's `_sort_list`
<img width="404" height="208" alt="image" src="https://github.com/user-attachments/assets/28144690-d19b-4fc6-b129-5c64dffffbd4" />


- Quicksort's `_sort_list`
<img width="420" height="188" alt="image" src="https://github.com/user-attachments/assets/e4a959e7-d1b8-40ae-81a2-e85da02c3589" />



- Bogosort's `_sort_list`
<img width="1096" height="298" alt="image" src="https://github.com/user-attachments/assets/3bdbc1de-1378-4ccc-8360-aa8301c7c4fa" />


- Heapsort's `_sort_list`
<img width="912" height="388" alt="image" src="https://github.com/user-attachments/assets/939d0bd0-f75b-424f-9d88-f26a3d2a0368" />


---
2. **Abstraction** - a simple interface

As mentioned above there are 2 simple ways to use this code - using the terminal to let the code do everything for you or using `.get_sorted_list` and `.print_sorted_list` after importing the desired algorithms

- Terminal interface example and code:
<img width="1028" height="732" alt="image" src="https://github.com/user-attachments/assets/ef0f77cb-2a7d-4086-a2f2-11028756a895" />

<img width="584" height="272" alt="image" src="https://github.com/user-attachments/assets/5a3ef215-b0f8-473c-a329-a63bc6f9b609" />


---
3. **Inheritance**

---
4. **Encapsulation**

This code uses the Strategy pattern as it is more suitable to keep the program versatile. Instead of being able to use only the most efficient sorting algorithm, the user is able to choose whichever one they want which could differ from user to user.

This code mainly uses the composition principle because it makes the code more structured and the aggregation principle does not fit in this case.

## Results:
- A working program that has multiple different sorting algorithms that can be imported to be used seperately or used as a program to read from and write to .txt files  
- Knowledge on how sorting algorithms like Heap Sort or Merge Sort work  
- Knowledge on how to use self referencing.

## Conclusion:
