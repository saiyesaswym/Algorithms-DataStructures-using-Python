"""
InsertionSort
It always maintains a sorted sublist in the lower positions of list.
Each item is inserted into sublist one by one.
Time complexity: O(n2)
Space complexity: O(1)
"""

def insertionSort(arr):
    for i in range(1,len(arr)):
        pos=i
        next_val = arr[pos]
        while pos>0 and arr[pos-1]>next_val:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = next_val
    return arr


n = int(input("Enter number of elements: "))
lis = []

for i in range(n):
    lis.append(int(input()))

print(insertionSort(lis))
