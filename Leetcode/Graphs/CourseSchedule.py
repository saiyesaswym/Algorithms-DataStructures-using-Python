"""
Time complexity: O(n+m)
Space complexity: O(n) - Visited, Arrival and Departure arrays
"""
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    #Build a graph
    adj_list = [[] for i in range(numCourses)]

    for src,dest in prerequisites:
        adj_list[dest].append(src)

    arrival = [0]*numCourses
    visited = [-1]*numCourses
    departure = [0]*numCourses
    timestamp = [0]

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
        return False

    for i in range(numCourses):
        if visited[i]==-1:
            if dfs(i):
                return False

    return True
