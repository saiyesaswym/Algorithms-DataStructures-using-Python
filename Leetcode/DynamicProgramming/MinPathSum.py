"""
BottomUp - Iterative approach - Tabulation - Optimized approach
minsum(i,j) = min(minsum(i-1,j), minsum(i,j-1)) + value(i,j)
Time complexity: O(m*n)
Space complexity: O(1)
"""
def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    for i in range(1,m):
        grid[i][0] += grid[i-1][0]

    for j in range(1,n):
        grid[0][j] += grid[0][j-1]

    for row in range(1,m):
        for col in range(1,n):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])

    return grid[m-1][n-1]
