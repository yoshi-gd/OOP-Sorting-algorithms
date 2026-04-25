# OOP-Sorting-algorithms
A generic sorting algorithm with different other algorithms as subclasses

## Introduction

The goal is to make a collection of sorting algorithms that can easily be imported and used or using the menu in the main code be able to read and write the sorted lists to .txt files

To run the program simply copy the code and put it in environment that can comile and run python from there **follow the written instructions in the terminal**

To use the program there are 2 ways:
1. importing the desired algorithms from Course_Work import (sort name) and then using .get_sorted_list to sort the given list and assign it or using .print_sorted_list to print the sorted list in the terminal
2. copying the code to an environment that can run it and **following the steps given in the terminal**. If the given list contains numbers **it must be written in a line seperated by spaces**. If the given list contains words **they must be seperated by commas ","**

## Analysis:

This code follows the 4 object-oriented programming pillars:
1. **Polymorphism**
2. **Abstraction**
3. **Inheritance**
4. **Encapsulation**

This code uses the Strategy pattern as it is more suitable to keep the program versatile. Instead of being able to use only the most efficient sorting algorithm, the user is able to choose whichever one they want which could differ from user to user.

This code mainly uses the composition principle because it makes the code more structured and the aggregation principle does not fit in this case.

## Results:
● A working program that has multiple different sorting algorithms that can be imported to be used seperately or used as a program to read from and write to .txt files  
● Knowledge on how sorting algorithms like Heap Sort or Merge Sort work  
● Knowledge on how to use self referencing.

## Conclusion:
