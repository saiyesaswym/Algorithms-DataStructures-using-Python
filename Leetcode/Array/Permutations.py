"""
First approach: Using Recursion
Time complexity: O(n2)
Space complexity: O(1)
"""

def permute(nums: list[int]) -> list[list[int]]:
    result=[]

    if(len(nums)==0):
        return []

    if(len(nums)==1):
        return [nums]

    for i in range(len(nums)):
        currentnum = nums[i]
        remainingnums = nums[:i] + nums[i+1:]
        remainingnumspermute = permute(remainingnums)

        for j in range(len(remainingnumspermute)):
            if(type(remainingnumspermute[j])==list):
                permutedArray = [currentnum] + remainingnumspermute[j]
            else:
                permutedArray = [currentnum] + [remainingnumspermute[j]]
            result.append(permutedArray)

    return result

nums=[1,2,3]
print(permute(nums))
