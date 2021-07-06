"""
BottomUp iterative approach - Memoization
Time complexity: O(k^2)
Space complexity: O(n)
"""
def generate(self, numRows: int) -> List[List[int]]:
    table = []

    for i in range(1,numRows+1):
        table.append([1]*i)

    for row in range(2,len(table)):
        for col in range(1,row):
            table[row][col] = table[row-1][col-1] + table[row-1][col]

    return table
