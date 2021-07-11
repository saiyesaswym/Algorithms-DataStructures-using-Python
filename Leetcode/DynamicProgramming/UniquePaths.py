"""
BottomUp - Iterative approach - Tabulation
ways(i,j) = ways(i-1,j) + ways(i,j-1))
Time complexity: O(m*n)
Space complexity: O(m*n)
"""
def uniquePaths(self, m: int, n: int) -> int:
    table = [[0 for i in range(n)] for j in range(m)]

    table[0][0]=1

    for i in range(1,m):
        table[i][0]=1

    for j in range(1,n):
        table[0][j]=1

    for row in range(1,m):
        for col in range(1,n):
            table[row][col] = table[row-1][col] + table[row][col-1]

    return table[m-1][n-1]
