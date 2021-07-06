"""
BottomUp iterative approach - Memoization
Time complexity: O(k^2)
Space complexity: O(n)
"""
def getRow(self, rowIndex: int) -> List[int]:
    table = []

    for i in range(1,rowIndex+2):
        table.append([1]*i)

    for row in range(2,len(table)):
        for col in range(1,row):
            table[row][col] = table[row-1][col-1] + table[row-1][col]

    return table[rowIndex]
