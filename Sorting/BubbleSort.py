def bubbleSort(lis):
    for i in range(len(lis)-1,0,-1):
        for j in range(i):
            if lis[j]>lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]

    return lis


n = int(input("Enter number of elements: "))
lis = []

for i in range(n):
    lis.append(int(input())

print(bubbleSort(lis))
