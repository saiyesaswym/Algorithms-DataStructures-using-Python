"""
Idea:
area = min(left,right)*(distance between left and right)
"""

"""
Brute force Approach
Time complexity: O(n^2)
Space complexity: O(1)
"""
def maxArea(self, height: List[int]) -> int:
    n = len(height)
    max_area=0
    for i in range(n):
        for j in range(i,n):
            max_area = max(max_area, min(height[i],height[j])*(j-i))

    return max_area


"""
Two pointer Approach
Time complexity: O(n)
Space complexity: O(1)
"""
def maxArea(self, height: List[int]) -> int:
    i = 0
    j = len(height)-1

    max_area = 0

    while i<j:
        max_area = max(max_area, min(height[i],height[j])*(j-i))
        if height[i]>height[j]:
            j-=1
        else:
            i+=1

    return max_area
