"""
Using MIN Heap
n1 - Initial array
n2 - Append array
O(n1) - build heap
O((n1-k)*logn1)) - Pop n-k elements
O(n2*logk)
Time complexity: O(n1+(n1-k)*logn1+n2*logk)
Space complexity: O(k)
"""
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heap=nums
        heapq.heapify(heap)

        while len(heap)>k:
            heapq.heappop(heap)

    def add(self, val: int) -> int:
        if len(heap)<k:
            heapq.heappush(heap,val)
        elif heap[0]<val:
            heapq.heappushpop(heap,val)
        return(heap[0])


"""
Using MIN Heap
n1 - Initial array
n2 - Append array
O(n1*logk) - Push/pop on max n1 elements
O(n2*logk) - Push/pop on max n2 elements
Time Complexity: O((n1+n2)*logk)
Space complexity: O(k)
"""


import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        heapq.heapify(self.heap)

        for i in nums:
            if not heapq:
                heapq.heappush(self.heap,i)
            elif len(self.heap)>=k:
                if i>self.heap[0]:
                    heapq.heappushpop(self.heap,i)
            elif len(self.heap)<k:
                heapq.heappush(self.heap,i)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif self.heap[0]<val:
            heapq.heappushpop(self.heap,val)
        return(self.heap[0])
