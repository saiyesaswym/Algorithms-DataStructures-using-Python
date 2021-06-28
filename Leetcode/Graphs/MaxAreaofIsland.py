
from collections import deque
"""
Time Complexity: O(R*C), where R is the number of rows in the given grid, and C is the number of columns.
We visit every square once.
Space complexity: O(R*C), space used by stack
"""
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

    def get_neighbors(x,y):
        result = []
        if x+1<len(grid):
            result.append((x+1,y))
        if y+1<len(grid[0]):
            result.append((x,y+1))
        if x-1>=0:
            result.append((x-1,y))
        if y-1>=0:
            result.append((x,y-1))
        return result

    def bfs(x,y):
        count=0
        q = deque()
        q.append((x,y))
        grid[x][y]=0
        count+=1

        while q:
            row,col = q.popleft()
            neighbors = get_neighbors(row,col)
            for i,j in neighbors:
                if grid[i][j]!=0:
                    count+=1
                    q.append((i,j))
                    grid[i][j]=0
        return count

    #Given grid is the adj matrix
    rows = len(grid)
    cols = len(grid[0])

    max_count = 0

    for i in range(rows):
        for j in range(cols):
            #If it is land and not yet visited
            if grid[i][j]!=0:
                max_count = max(max_count, bfs(i,j))
    return max_count
