"""
Sort
Time complexity: O(nlogn)
Space complexity: O(1)
"""
def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums,reverse=True)[k-1]


"""
Using MIN Heap
Build heap for n elemnts - Remove n-k values - kth value will be minimum
Time complexity: O(n+(n-k)logn) (O(n) to build heap and (n-k)*logn to pop n-k elements from heap of size n)
Space complexity: O(n)
"""
import heapq

def findKthLargest(self, nums: List[int], k: int) -> int:
    heap=nums
    heapq.heapify(heap)

    while len(heap)>k:
        heapq.heappop(heap)

    return heap[0]

"""
Using MIN Heap
Build heap for first k elemnts - Insert any of remaining n-k if it's greater than heap minimum
Time complexity: O(k+(n-k)logk) (O(k) to build heap and (n-k)*logk to push/pop n-k elements on heap of size k)
Space complexity: O(n)
"""
def findKthLargest(self, nums: List[int], k: int) -> int:
    heap=nums[:k]
    heapq.heapify(heap)

    for i in range(k,len(nums)):
        if nums[i]>heap[0]:
            heapq.heappushpop(heap, nums[i])

    return heap[0]


"""
Using MAX Heap
nlargest method - Returns list of n largest elements
Time complexity: O(nlogk)
Space complexity: O(k)
"""
import heapq

def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


"""
QuickSelect Algorithm
Time complexity: O(n); O(n2)->worst case
Space complexity: O(1)
"""
import random

def findKthLargest(self, nums: List[int], k: int) -> int:
    return quickselect(nums, 0, len(nums), len(nums)-k)

def quickselect(self, arr, start, end, k):
    pointer = partition(arr, start, end)

    if end-start<=0:
        return arr[start]

    if pointer==k:
        return arr[pointer]
    elif pointer>k:
        return quickselect(arr, start, pointer, k)
    else:
        return quickselect(arr, pointer+1, end, k)

def partition(arr, start, end):
    randindex = random.randrange(start, end)

    arr[randindex], arr[start] = arr[start], arr[randindex]

    pivot = arr[start]
    i = start

    for j in range(start+1, end):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[start],arr[i] = arr[i],arr[start]

    return i
