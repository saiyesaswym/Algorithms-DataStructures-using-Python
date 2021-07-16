"""
Brute force Approach
Time complexity: O(n^2)
Space complexity: O(1)
"""
def trap(self, height: List[int]) -> int:

    max_water=0

    for idx in range(1,len(height)-1):
        left = self.findleftbound(height, idx)
        right = self.findrightbound(height, idx)

        if left!=-1 and right!=-1:
            max_water += min(height[left],height[right]) - height[idx]

    return max_water


def findleftbound(self, height, i):
    temp=i
    while i>0:
        if height[i-1]>height[temp]:
            temp=i-1
        i-=1
    return temp



"""
BottomUp - Iterative approach - Tabulation
Cache left bound and right bound for each bar
Time complexity: O(n)
Space complexity: O(n)
"""
def trap(self, height: List[int]) -> int:

    if len(height)==0:
        return 0

    max_water=0
    size = len(height)

    left_max = [0 for _ in range(size)]
    right_max = [0 for _ in range(size)]

    left_max[0] = height[0]
    for i in range(1,size):
        left_max[i] = max(height[i], left_max[i-1])

    right_max[size-1] = height[size-1]
    for j in range(size-2,-1,-1):
        right_max[j] = max(height[j], right_max[j+1])

    for idx in range(1,len(height)-1):
        max_water += min(left_max[idx],right_max[idx]) - height[idx]

    return max_water
