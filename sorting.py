import time
#import sys
class sort():
    @staticmethod
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    @staticmethod
    def selectionSort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertionSort(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    @staticmethod
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = sort.mergeSort(left)
        right = sort.mergeSort(right)
        return sort.merge(left, right)
    
    @staticmethod
    def merge(left, right): # For Mergesort
        merged = []
        left_idx = 0
        right_idx = 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        merged += left[left_idx:]
        merged += right[right_idx:]
        return merged

    #sys.setrecursionlimit(10_000)
    @staticmethod
    def quickSort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sort.quickSort(left) + sort.quickSort(middle) + sort.quickSort(right)

if __name__ == "__main__":
    s = sort()
    arr = [9,8,7,6,5,4,3,2,1]

    start_time = time.time()
    print("Bubble Sort: ", s.bubbleSort(arr))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Execution time in ms: ",execution_time,"\n")

    start_time = time.time()
    print("Quick Sort: ", s.quickSort(arr))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Execution time in ms: ",execution_time,"\n")

    start_time = time.time()
    print("Selection Sort: ", s.selectionSort(arr))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Execution time in ms: ",execution_time,"\n")
    
    start_time = time.time()
    print("Insertion Sort: ", s.insertionSort(arr))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Execution time in ms: ",execution_time,"\n")

    start_time = time.time()
    print("Merge Sort: ", s.mergeSort(arr))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Execution time in ms: ",execution_time,"\n")