"""
MergeSort
Divide and Conquer approach
List is recursively split into smaller parts and then merged in order
Time complexity: O(nlogn) - for all cases
Space complexity: O(n) - Cannot be done in place, needs auxiliary space
"""
def mergeSort(arr):
    print('Splitting: ', arr)
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1

n = int(input("Enter number of elements: "))
lis = []

for i in range(n):
    lis.append(int(input()))

print(mergeSort(lis))
