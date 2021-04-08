"""
First approach: Brute force approach
Looping through the list and adding numbers to counter variable
Time complexity: O(n)
Run time: 40ms
Faster than 62.16%
"""
def runningSum(nums: list[int]) -> list[int]:
    res=[]
    temp=0
    for i in nums:
        temp+=i
        res.append(temp)
    return res


"""
Second approach: Brute force approach
Update the input array without using additional variables
Time complexity: O(n)
Run time: 40ms
Less memory than previous approach
"""
def runningSum2(nums: list[int]) -> list[int]:
    for i in range(1,len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums

print(runningSum2([1,1,1,1,1]))
