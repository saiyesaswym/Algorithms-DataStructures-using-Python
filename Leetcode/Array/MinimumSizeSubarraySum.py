"""
Two pointer Approach
Time complexity: O(n)
Space complexity: O(1)
"""
def minSubArrayLen(target: int, nums: List[int]) -> int:
    l=0
    r=0
    min_size=10**5
    curr_sum=0
    while r<len(nums):
        curr_sum+=nums[r]
        if curr_sum < target:
            r+=1
        else:
            min_size = min(min_size, r-l+1)
            curr_sum = curr_sum-nums[r]-nums[l]
            l+=1

    return min_size if min_size<10**5 else 0
