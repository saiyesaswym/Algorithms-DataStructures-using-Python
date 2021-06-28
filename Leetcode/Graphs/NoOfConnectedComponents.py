
from collections import deque

"""
n - nodes
m - edges
Time complexity: O(n+m)
Space complexity: O(n+m)
"""

def countComponents(self, n: int, edges: List[List[int]]) -> int:

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

    def dfs(s):
        visited[s]=1

        for neighbor in adj_list[s]:
            if visited[neighbor] == -1:
                dfs(neighbor)

    #build the graph - O(n+m)
    adj_list = [[] for i in range(n)]

    #Turn edgelist to adjlist
    for edge in edges:
        #Since the graph is undirected
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    #visited array - O(n)
    visited = [-1] * n

    #Counter to keep track of no. of components - O(1)
    components=0

    #Outerloop to traverse through all nodes - O(n+m)
    for i in range(n):
        if visited[i] == -1:
            components+=1
            #Call bfs or dfs on the node
            bfs(i)

    return components
