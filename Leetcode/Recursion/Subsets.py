"""
Recursion - General template
Time complexity: O(2^n * n)
Space complexity: O(2^n * n)
"""
def subsets(self, nums: List[int]) -> List[List[int]]:
    result=[]

    def subsetHelper(nums, i, slate):
        if i==len(nums):
            result.append(slate[:])
        else:
            subsetHelper(nums, i+1, slate)
            slate.append(nums[i])
            subsetHelper(nums, i+1, slate)
            slate.pop()
    subsetHelper(nums, 0, [])
    return result
