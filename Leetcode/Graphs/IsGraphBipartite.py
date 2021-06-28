"""
DFS Approach
Adjacent nodes have different colors - using two colors - Alternative labeling
Color array - 0 and 1 to label every alternative nodes
Time complexity: O(n+m)
Space complexity: O(n) - Color, Visited and Parent arrays
"""
def isBipartite(self, graph: List[List[int]]) -> bool:

    #Odd cycle detection
    def dfs(s):
        visited[s]=1

        for neighbor in graph[s]:
            if visited[neighbor] == -1:
                parent[neighbor] = s
                #Opposite to the color of its parent
                color[neighbor] = 1 - color[s]
                if not dfs(neighbor):
                    return False
            else:
                if color[s] == color[neighbor]:
                    return False
        return True

    #Given graph is adj list
    n = len(graph)

    visited = [-1]*n
    parent = [-1]*n
    color = [-1]*n

    for i in range(n):
        if visited[i] == -1:
            #Initialize to a color
            color[i]=0
            if not dfs(i):
                return False

    return True



"""
BFS approach
CrossEdge between same levels - Odd count cycle - No Bipartite possible
Distance array - Track the level of each vertex
Time complexity: O(n+m)
Space complexity: O(n) - Distance, Visited and Parent arrays
"""
def isBipartite(self, graph: List[List[int]]) -> bool:

    #Odd cycle detection
    def bfs(s):
        visited[s]=1
        distance[s]=0

        q = deque()
        q.append(s)

        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if visited[neighbor]==-1:
                    visited[neighbor]=1
                    parent[neighbor]=node
                    distance[neighbor]=1+distance[node]
                    q.append(neighbor)
                else:
                    if parent[node]!=neighbor:
                        #CrossEdge in same level - odd cycle possible
                        if distance[neighbor]==distance[node]:
                            return False

        return True

    #Given graph is adj list
    n = len(graph)

    visited = [-1]*n
    parent = [-1]*n
    distance = [-1]*n

    for i in range(n):
        if visited[i] == -1:
            if not bfs(i):
                return False

    return True
