"""
SelectionSort
Same as Bubblesort, but only one exchange is made for every pass
So, it is faster than bubbleSort
Time complexity: O(n2)
Space complexity: O(1)
"""
def selectionSort(lis):
    for i in range(len(lis)-1,0,-1):
        max_pos=0
        for j in range(1,i+1):
            if lis[j]>lis[max_pos]:
                max_pos = j
        lis[i], lis[max_pos] = lis[max_pos], lis[i]
    return lis


n = int(input("Enter number of elements: "))
lis = []

for i in range(n):
    lis.append(int(input()))

print(selectionSort(lis))
