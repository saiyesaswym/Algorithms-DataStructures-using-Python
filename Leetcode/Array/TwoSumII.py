"""
Two Pointer Approach
Since the input array is Sorted
Time complexity: O(n)
Space complexity: O(1)
"""
def twoSum(numbers: List[int], target: int) -> List[int]:
    l=0
    r=len(numbers)-1
    while l<r:
        total = numbers[l]+numbers[r]
        if(total<target):
            l+=1
        elif total>target:
            r-=1
        else:
            return [l+1,r+1]
