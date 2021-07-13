"""
BottomUp iterative approach - Tabulation
Time complexity: O(n)
Space complexity: O(n)
"""
def maxSubArray(self, nums: List[int]) -> int:

    n = len(nums)

    #1D Array of size n+1
    table = [0 for i in range(n)]

    #BaseCase
    table[0]=nums[0]

    #RecursiveCase
    #Either extend the subarray from i-1 or start new subarray from i
    for i in range(1,n):
        table[i] = max(table[i-1]+nums[i], nums[i])

    return max(table)


"""
BottomUp iterative approach - Tabulation - Optimized
Time complexity: O(n)
Space complexity: O(1)
"""
def maxSubArray(self, nums: List[int]) -> int:

    n = len(nums)

    #BaseCase
    prev_subarray=nums[0]
    max_subarray=nums[0]

    #RecursiveCase
    #Either extend the subarray from i-1 or start new subarray from i
    for i in range(1,n):
        prev_subarray = max(prev_subarray+nums[i], nums[i])
        max_subarray = max(max_subarray, prev_subarray)

    return max_subarray
