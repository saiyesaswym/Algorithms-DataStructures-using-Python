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


"""
First approach: Two-pass Hash Table
Time complexity: O(n) - Hashtable has lookup time of O(1)
Space complexity: O(n)
"""

def twoSum_hash1(nums: list[int], target: int):
    hashmap = {}
    for i,j in enumerate(nums):
        hashmap[j]=i

    for i in range(len(nums)):
        complement = target - nums[i]
        if(complement in hashmap.keys() and hashmap[complement]!=i):
            return [i, hashmap[complement]]


nums = [2,7,11,15]
target = 9

print(twoSum_hash1(nums,target))


"""
Third approach: One-pass Hash Table
Time complexity: O(n) - Hashtable has lookup time of O(1)
Space complexity: O(n)
"""

def twoSum_hash2(nums: list[int], target: int):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if(complement in hashmap.keys()):
            return [hashmap[complement], i]
        hashmap[nums[i]] = i

nums = [2,7,11,15]
target = 9

print(twoSum_hash2(nums,target))
