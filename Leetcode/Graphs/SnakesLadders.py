from collections import deque

def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)

    #Build Graph - as array
    flag=1
    count=0
    res=[]
    for row in range(n-1,-1,-1):
        if flag==1:
            for col in range(0,n):
                count+=1
                if board[row][col]!=-1:
                    res.append(board[row][col])
                else:
                    res.append(count)
        else:
            for col in range(n-1,-1,-1):
                count+=1
                if board[row][col]!=-1:
                    res.append(board[row][col])
                else:
                    res.append(count)
        flag = flag*-1

    total=(n*n)+1
    distance = [-1]*total
    visited = [-1]*total
    
    def bfs(s):
        q = deque()
        q.append(s)

        visited[s]=1
        distance[s]=0

        while q:
            curr = q.popleft()
            for j in range(curr+1,curr+7):
                if j<=len(res):
                    i=res[j-1]
                    if visited[i]==-1:
                        visited[i]=1
                        distance[i]=1+distance[curr]
                        q.append(i)

    bfs(1)

    return distance[total-1]
