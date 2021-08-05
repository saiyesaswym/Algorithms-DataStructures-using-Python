"""
Using BFS
Time complexity: O(m*n)
Space complexity: O(m*n)
""" 

def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

    if not heights or not heights[0]:
        return []

    def get_neighbors(x,y):
        result = []
        if x+1<len(heights):
            result.append((x+1,y))
        if y+1<len(heights[0]):
            result.append((x,y+1))
        if x-1>=0:
            result.append((x-1,y))
        if y-1>=0:
            result.append((x,y-1))
        return result

    m = len(heights)
    n = len(heights[0])

    pac_q = deque()
    atl_q = deque()

    for i in range(m):
        pac_q.append((i,0))
        atl_q.append((i,n-1))

    for j in range(n):
        pac_q.append((0,j))
        atl_q.append((m-1,j))

    def bfs(queue):
        visited = set()
        while queue:
            row,col = queue.popleft()
            visited.add((row,col))

            for i,j in get_neighbors(row,col):
                if (i,j) in visited:
                    continue

                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if heights[i][j] < heights[row][col]:
                    continue

                queue.append((i,j))
        return visited

    # Perform a BFS for each ocean to find all cells accessible by each ocean
    pac_list = bfs(pac_q)
    atl_list = bfs(atl_q)

    # Find all cells that can reach both oceans, and convert to list
    return list(pac_list.intersection(atl_list))
