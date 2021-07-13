"""
BottomUp - Iterative approach - Tabulation
edits(i,j) = min(edits(i-1,j)+1 , edits(i,j-1))+1 , edits(i-1,j-1)+(0,1))
Time complexity: O(m*n)
Space complexity: O(m*n)
"""
def minDistance(self, word1: str, word2: str) -> int:

    m = len(word1)
    n = len(word2)

    #2d array of size (m+1)*(n+1)
    table = [[0 for i in range(n+1)] for j in range(m+1)]

    #baseCase
    for i in range(1,m+1):
        table[i][0]=i

    for j in range(1,n+1):
        table[0][j]=j

    for row in range(1,m+1):
        for col in range(1,n+1):
            s=1
            if word1[row-1]==word2[col-1]:
                s=0
            table[row][col] = min(table[row-1][col]+1, table[row][col-1]+1, table[row-1][col-1]+s)

    return table[-1][-1]
