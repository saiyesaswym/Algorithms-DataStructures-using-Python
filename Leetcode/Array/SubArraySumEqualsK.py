"""
Brute force approach
For every subarray - find the sum of each subarray
Time complexity: O(n^3)
Space complexity: O(1)
"""
def subarraySum(self, nums: List[int], k: int) -> int:
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n+1):
            print(nums[i:j])
            if sum(nums[i:j])==k:
                count+=1
    return count


"""
Better Brute force approach - Sum on the fly
Time complexity: O(n^2)
Space complexity: O(1)
"""
def subarraySum(self, nums: List[int], k: int) -> int:
    count=0
    n=len(nums)
    for i in range(n):
        total=0
        for j in range(i,n):
            total+=nums[j]
            if total==k:
                count+=1
    return count
