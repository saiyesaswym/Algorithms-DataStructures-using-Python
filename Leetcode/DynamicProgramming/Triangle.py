"""
BottomUp iterative approach - Memoization
Time complexity: O(k^2) - k-> # of rows in the given triangle
Space complexity: O(1)
"""
def minimumTotal(self, triangle: List[List[int]]) -> int:

    for row in range(1,len(triangle)):
        triangle[row][0]+=triangle[row-1][0]
        triangle[row][len(triangle[row])-1]+=triangle[row-1][len(triangle[row])-2]

    for row in range(2,len(triangle)):
        for col in range(1,len(triangle[row])-1):
            triangle[row][col] = min(triangle[row-1][col], triangle[row-1][col-1]) + triangle[row][col]

    return min(triangle[-1])
