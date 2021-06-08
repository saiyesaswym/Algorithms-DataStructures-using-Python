"""
Two pointer Approach - In place
Time complexity: O(n)
Space complexity: O(1)
"""
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    i=0
    for j in range(len(nums)):
        if nums[j]%2==0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums


"""
Two pass approach
Time complexity: O(n)
Space complexity: O(n)
"""
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    res=[]
    for i in nums:
        if i%2==0:
            res.append(i)
    for j in nums:
        if j%2!=0:
            res.append(j)
    return res
