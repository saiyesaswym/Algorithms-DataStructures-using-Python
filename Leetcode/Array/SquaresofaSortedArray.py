"""
Brute Force Approach
Square the list and sort it
"""
def sortedSquares(self, nums: list[int]) -> list[int]:
    return sorted([i*i for i in nums])

"""
Two pointer Approach
Two pointers from both ends of the array
Time Complexity: O(n)
"""
def sortedSquares2(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result


"""
Two pointer Approach - version 2
One pointer at beginning of negative numbers, another at start of positive numbers
Time complexity: O(n)
"""
def sortedSquares3(arr):
    r=0
    while r<len(arr) and arr[r]<0:
        r+=1
    l=r-1

    out=[]

    while l>=0 and r<len(arr):
        if arr[l]**2 > arr[r]**2:
            out.append(arr[r]**2)
            r+=1
        else:
            out.append(arr[l]**2)
            l-=1

    while l>=0:
        out.append(arr[l]**2)
        l-=1

    while r<len(arr):
        out.append(arr[r]**2)
        r+=1

    return out
