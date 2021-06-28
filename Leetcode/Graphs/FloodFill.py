
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

    def get_neighbors(x,y):
        result = []
        if x+1<len(image):
            result.append((x+1,y))
        if y+1<len(image[0]):
            result.append((x,y+1))
        if x-1>=0:
            result.append((x-1,y))
        if y-1>=0:
            result.append((x,y-1))
        return result

    def bfs(x,y,oldColor):
        print(oldColor)
        q = deque()
        q.append((x,y))
        image[x][y]=newColor

        while q:
            row,col = q.popleft()
            neighbors = get_neighbors(row,col)
            for i,j in neighbors:
                if image[i][j]==oldColor:
                    q.append((i,j))
                    image[i][j]=newColor

    oldColor = image[sr][sc]

    #EdgeCase - Gets into infinite loop
    if oldColor==newColor:
        return image

    bfs(sr,sc,oldColor)

    return image
