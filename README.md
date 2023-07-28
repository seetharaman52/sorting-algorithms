This repository contains a single .py file that contains 5 basic sorting techniques

## Bubble Sort : (In place - sorting)
Best case : O(n) <br>
Worst case : O(n^2) <br>
Inefficient for Large Datasets. <br>
Bubble sort is three times slower than QuickSort for n = 100 <br>

## Selection Sort : (In place - sorting)
Worst case, Best case : O(n^2) <br>
Inefficient for Large Datasets.

## Insertion Sort : (In place - sorting)
Best case : O(n) <br>
Worst case : O(n^2) <br>
Efficient for small datasets and partially sorted arrays.

## Merge Sort : (Comparison and recursive based)
All cases : O(n log n) <br>
Efficient, stable, suitable for large datasets (Divide and Conquer).

## Quick Sort : (Recursion based)
Average case : O(n log n) <br>
Worst case : O(n^2) <br>
Efficient, widely used and reduces space usage.

## Heap Sort : (In place - sorting)
All cases : O(n log n) <br>
Efficient but not stable. <br>

## Counting Sort : (Not in place)
All cases : O(n + k) ; K is the range of input. <br>
Efficient for sorting non-negative integers with a small range but requires extra memory

## Radix Sort : (Not in place)
All cases : O(d * (n + k)) ; d → number of digits in max number, k is range of input.<br>
Suitable for sorting integers with fixed number of digits.

## Bucket Sort : (Not in place)
Worst case : O(n^2), but can be linear with good choice of hash func.<br>
Efficient when data is uniformly distributed across buckets.

## Tim Sort : (Not in place)
All cases : O(n log n)<br>
A hybrid sorting algorithm derived from Merge sort and Insertion sort. In python it is "sorted()".
