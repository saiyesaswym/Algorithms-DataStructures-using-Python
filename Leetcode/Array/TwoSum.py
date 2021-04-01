"""
First approach: Brute force approach
Time complexity: O(n2)
Space complexity: O(1)
"""

def twoSum(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j]


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
