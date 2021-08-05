"""
Layer by layer - Four pointers
Time complexity: O(N) - O(row*col)
Space complexity: O(1)
https://www.youtube.com/watch?v=1ZGJzvkcLsA
"""
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])

    top=0
    down=m-1
    left=0
    right=n-1

    res=[]
    d=0

    while top<=down and left<=right:
        if d==0:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
        elif d==1:
            for i in range(top,down+1):
                res.append(matrix[i][right])
            right-=1
        elif d==2:
            for i in range(right,left-1,-1):
                res.append(matrix[down][i])
            down-=1
        else:
            for i in range(down,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        d=(d+1)%4

    return res
