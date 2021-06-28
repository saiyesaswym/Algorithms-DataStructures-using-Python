"""
n - nodes
m - edges
Time complexity: O(n+m)
Space complexity: O(n+m)
"""
def validTree(self, n: int, edges: List[List[int]]) -> bool:

    def bfs(s):
        #Mark node as visited
        visited[s] = 1

        q = deque()
        q.append(s)

        while q:
            curr = q.popleft()

            #Iterate through the neighbors of node
            for neighbor in adj_list[curr]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    q.append(neighbor)
                    parent[neighbor]=curr
                else:
                    #Either neighbor is parent or a cross edge
                    if parent[curr]!=neighbor:
                        #It is a crossedge
                        return False
        return True

    def dfs(s):
        visited[s]=1

        for neighbor in adj_list[s]:
            if visited[neighbor]==-1:
                parent[neighbor]=s
                if dfs(neighbor):
                    return True
            else:
                #Backedge exists
                if parent[s]!=neighbor:
                    return True
        return False

    adj_list = [[] for i in range(n)]

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = [-1]*n
    parent = [-1]*n
    components = 0

    for i in range(n):
        if visited[i]==-1:
            components+=1
            if components>1:
                return False
            if not bfs(i):#if dfs(i) 
                return False

    return True
