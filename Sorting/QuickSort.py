"""
QuickSort
Divide and Conquer approach
Similar to MergeSort, but instead of dividing array based on position, it is divided by value.
Time complexity: Best/Avg - O(nlogn); Worst - O(n2)
Space complexity: O(n) - Cannot be done in place, needs auxiliary space
"""
import random

def partition(arr, start, end):
    randindex = random.randrange(start, end)

    arr[start],arr[randindex] = arr[randindex],arr[start]

    pivot = arr[start]
    left = start
    right = start

    for right in range(start+1,end):
        if arr[right] < pivot:
            left+=1
            arr[left],arr[right] = arr[right],arr[left]

    arr[start],arr[left] = arr[left],arr[start]

    return left

def quickSortHelper(arr, start, end):
    if start < end:
        pointer = partition(arr, start, end)

        quickSortHelper(arr, start, pointer)
        quickSortHelper(arr, pointer+1, end)

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr))


n = int(input("Enter number of elements: "))
lis = []

for i in range(n):
    lis.append(int(input()))

print(quickSort(lis))
