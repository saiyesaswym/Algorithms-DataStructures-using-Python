"""
BFS approach
CrossEdge between same levels - Odd count cycle - No Bipartite possible
Distance array - Track the level of each vertex
Time complexity: O(n+m)
Space complexity: O(n) - Distance, Visited and Parent arrays
"""
def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    #Odd cycle detection
    def bfs(s):
        visited[s]=1
        distance[s]=0

        q = deque()
        q.append(s)

        while q:
            node = q.popleft()
            for neighbor in adj_list[node]:
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

    #Build Graph
    adj_list = [[] for i in range(n)]

    for edge in dislikes:
        adj_list[edge[0]-1].append(edge[1]-1)
        adj_list[edge[1]-1].append(edge[0]-1)

    visited = [-1]*n
    parent = [-1]*n
    distance = [-1]*n

    for i in range(n):
        if visited[i] == -1:
            if not bfs(i):
                return False

    return True
