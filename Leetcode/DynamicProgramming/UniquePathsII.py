"""
BottomUp - Iterative approach - Memoization
ways(i,j) = ways(i-1,j) + ways(i,j-1))
Time complexity: O(m*n)
Space complexity: O(1)
"""
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0]==1:
        return 0

    obstacleGrid[0][0]=1

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    for i in range(1,m):
        obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

    for j in range(1,n):
        obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

    for row in range(1,m):
        for col in range(1,n):
            if obstacleGrid[row][col]==1:
                obstacleGrid[row][col]=0
            else:
                obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]

    print(obstacleGrid)

    return obstacleGrid[m-1][n-1]
