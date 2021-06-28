from collections import deque
"""
Using BFS
"""
def numIslands(self, grid: List[List[str]]) -> int:

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

        visited[x][y]=1
        q = deque()
        q.append((x,y))

        while q:
            row,col = q.popleft()
            neighbors = get_neighbors(row,col)
            for i,j in neighbors:
                if visited[i][j]==-1 and grid[i][j]=="1":
                    visited[i][j]=1
                    q.append((i,j))

    #Given grid is the adj matrix
    rows = len(grid)
    cols = len(grid[0])

    visited = [[-1 for i in range(cols)] for j in range(rows)]
    islands = 0

    for i in range(rows):
        for j in range(cols):
            #If it is land and not yet visited
            if visited[i][j]==-1 and grid[i][j]=="1":
                islands+=1
                bfs(i,j)
    return islands


"""
BFS - Optimized Approach
Use grid to mark visited nodes, saves visited array space
"""
def numIslands(self, grid: List[List[str]]) -> int:

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
        q = deque()
        q.append((x,y))
        grid[x][y]="0"

        while q:
            row,col = q.popleft()
            neighbors = get_neighbors(row,col)
            for i,j in neighbors:
                if grid[i][j]!="0":
                    q.append((i,j))
                    grid[i][j]="0"

    #Given grid is the adj matrix
    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    for i in range(rows):
        for j in range(cols):
            #If it is land and not yet visited
            if grid[i][j]!="0":
                islands+=1
                bfs(i,j)
    return islands



"""
Using DFS
"""
def numIslands(self, grid: List[List[str]]) -> int:

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

    def dfs(x,y):
        grid[x][y]="0"

        neighbors = get_neighbors(x,y)
        for i,j in neighbors:
            if grid[i][j]!="0":
                grid[i][j]="0"
                dfs(i,j)

    #Given grid is the adj matrix
    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    for i in range(rows):
        for j in range(cols):
            #If it is land and not yet visited
            if grid[i][j]!="0":
                islands+=1
                dfs(i,j)
    return islands
