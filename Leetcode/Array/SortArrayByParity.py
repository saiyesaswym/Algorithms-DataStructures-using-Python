"""
Two pointer Approach - In place - Lomuto partition
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
Two pointer approach - Hoare's partition
Time complexity: O(n)
Space complexity: O(1)
"""
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    i=0
    j=len(nums)-1

    while i<j:
        #Swap when left has odd and right has even
        if nums[i]%2!=0 and nums[j]%2==0:
            nums[i],nums[j] = nums[j],nums[i]
        if nums[i]%2==0:
            i+=1
        if nums[j]%2!=0:
            j-=1

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
