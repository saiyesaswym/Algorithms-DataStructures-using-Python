"""
Brute force Approach
Time complexity: O(n^3)
Space complexity: O(1)
"""
def longestConsecutive(self, nums: List[int]) -> int:
    max_streak = 0

    for num in nums:
        cur_num = num
        cur_streak = 1

        while cur_num+1 in nums:
            cur_num += 1
            cur_streak += 1

        max_streak = max(max_streak, cur_streak)

    return max_streak


"""
Sort and compare
Time complexity: O(nlogn)
Space complexity: O(1)
"""
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    nums = sorted(list(set(nums)))

    prev = nums[0]
    count = 1
    maxx = 1

    for i in range(1,len(nums)):
        if prev==nums[i]-1:
            count+=1
        else:
            maxx = max(maxx, count)
            count=1
        prev = nums[i]

    maxx = max(maxx, count)

    return maxx


"""
Hashset and compare
Time complexity: O(n)
Space complexity: O(n)
"""
def longestConsecutive(self, nums: List[int]) -> int:
    max_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num-1 not in num_set:
            cur_num = num
            cur_streak = 1

            while cur_num+1 in num_set:
                cur_num += 1
                cur_streak += 1

            max_streak = max(max_streak, cur_streak)

    return max_streak
