"""
First approach: Brute force approach
Time complexity: O(n2)
Space complexity: O(1)
"""
def bubbleSort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1):
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis


"""
Second approach: ShortBubble approach
If there are no exchanges in a pass, list is already sorted
Best case Time complexity: O(n) - when array is already sorted
Time complexity: O(n2)
Space complexity: O(1)
"""
def shortBubble(lis):
    for i in range(len(lis)-1):
        swapped=False
        for j in range(len(lis)-1):
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
                swapped=True
        if swapped==False:
            break
    return lis


"""
Third approach: Optimized version 2
This approach compares one less comparision in every pass
Time complexity: O(n2)
Space complexity: O(1)
"""
def bubbleSort2(lis):
    for i in range(len(lis)-1,0,-1):
        for j in range(i):
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis


"""
Fourth approach: ShortBubble approach - Optimized way
If there are no exchanges in a pass, list is already sorted
This approach compares one less comparision in every pass
Best case Time complexity: O(n) - when array is already sorted
Time complexity: O(n2)
Space complexity: O(1)
"""
def shortBubble2(lis):
    for i in range(len(lis)-1,0,-1):
        swapped=False
        for j in range(i):
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
                swapped=True
        if swapped==False:
            break
    return lis



n = int(input("Enter number of elements: "))
lis = []

for i in range(n):
    lis.append(int(input()))

print(bubbleSort(lis))
