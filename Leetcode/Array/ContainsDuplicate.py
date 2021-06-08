"""
Hashset Approach 1
Lookup for duplicates in hashset
Time complexity: O(n)
Space complexity: O(n)
"""
def containsDuplicate(self, nums: List[int]) -> bool:
    vals = set()
    for i in nums:
        if i in vals:
            return True
        else:
            vals.add(i)
    return False

"""
Hashset Approach 2
Since hashset can't have duplicates, compare the lengths
Time complexity: O(n)
Space complexity: O(n)
"""
def containsDuplicate(nums: List[int]) -> bool:
    vals = set(nums)
    if len(vals)==len(nums):
        return False
    else:
        return True

"""
Sorting Approach
Sort the array and look for same consecutive values
Time complexity: O(nlogn)
Space complexity: O(1)
"""
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
