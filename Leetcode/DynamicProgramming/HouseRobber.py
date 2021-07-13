
def rob(self, nums: List[int]) -> int:

    #EdgeCase
    if len(nums)==0:
        return 0

    #BaseCase
    if len(nums)>2:
        nums[2] += nums[0]

    for i in range(3,len(nums)):
        nums[i] += max(nums[i-2], nums[i-3])

    return max(nums)
