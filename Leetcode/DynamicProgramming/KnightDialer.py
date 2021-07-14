"""
BottomUp - Iterative approach - Tabulation
f(i,d) = # of valid phone numbers of length i ending in d
Time complexity: O(n)
Space complexity: O(n)
"""
def knightDialer(self, n: int) -> int:

    table = [[0 for _ in range(10)] for _ in range(n+1)]

    #BaseCase
    for i in range(10):
        table[1][i]=1

    #RecursiveCase
    for i in range(2,n+1):
        table[i][0] = table[i-1][4] + table[i-1][6]
        table[i][1] = table[i-1][6] + table[i-1][8]
        table[i][2] = table[i-1][7] + table[i-1][9]
        table[i][3] = table[i-1][4] + table[i-1][8]
        table[i][4] = table[i-1][0] + table[i-1][3] + table[i-1][9]
        table[i][5] = 0
        table[i][6] = table[i-1][0] + table[i-1][1] + table[i-1][7]
        table[i][7] = table[i-1][2] + table[i-1][6]
        table[i][8] = table[i-1][1] + table[i-1][3]
        table[i][9] = table[i-1][2] + table[i-1][4]

    return sum(table[-1]) % (10**9 + 7)
