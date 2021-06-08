
def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums,reverse=True)[k-1]




from heapq import heappop, heappush

def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq._heapify_max(nums)
    while k>1:
        heappop(nums)
        heapq._heapify_max(nums)
        k-=1
    return heappop(nums)
