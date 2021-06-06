"""
One pass swap - Bubblesort type Approach
Boolean value depends on whether the index is odd or even.
So, as we iterate the array, we compare each element to its next based on its index.
Time complexity: O(n)
Space complexity: O(1)
"""
def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i=1
    while i<len(nums):
        if (i%2==0 and nums[i-1]<nums[i]) or (i%2==1 and nums[i-1]>nums[i]):
            nums[i-1],nums[i] = nums[i],nums[i-1]
        i+=1

    return nums
