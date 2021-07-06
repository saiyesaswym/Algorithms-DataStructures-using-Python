"""
Time complexity: O(n+m)
Space complexity: O(n) - Visited, topSort, Arrival and Departure arrays
"""
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    #Build a graph
    adj_list = [[] for i in range(numCourses)]

    for src,dest in prerequisites:
        adj_list[dest].append(src)

    arrival = [0]*numCourses
    visited = [-1]*numCourses
    departure = [0]*numCourses
    timestamp = [0]
    topSort = []

    def dfs(node):
        arrival[node]=timestamp[0]
        timestamp[0]+=1
        visited[node]=1

        for neighbor in adj_list[node]:
            if visited[neighbor]==-1:
                if dfs(neighbor):
                    return True
            else:
                if departure[neighbor]==0:
                    return True

        departure[node]=timestamp[0]
        timestamp[0]+=1
        #Collect nodes with each DFS closing call stack
        topSort.append(node)
        return False

    for i in range(numCourses):
        if visited[i]==-1:
            if dfs(i):
                return []

    #Return reverse of topsort as we collected them in ascending order
    return topSort[::-1]
