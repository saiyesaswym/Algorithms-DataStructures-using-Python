"""
BottomUp iterative approach - Tabulation
Time complexity: O(n)
Space complexity: O(n)
"""
def minCost(self, costs: List[List[int]]) -> int:
    if len(costs)==0:
        return 0

    table = [[0]*3 for _ in range(len(costs))]

    #BaseCase
    table[0] = costs[0]

    #RecursiveCase
    for i in range(1,len(costs)):
        table[i][0] = costs[i][0] + min(table[i-1][1], table[i-1][2])
        table[i][1] = costs[i][1] + min(table[i-1][0], table[i-1][2])
        table[i][2] = costs[i][2] + min(table[i-1][0], table[i-1][1])

    return min(table[-1])



"""
BottomUp iterative approach - Tabulation - Optimized
Time complexity: O(n)
Space complexity: O(1)
"""
def minCost(self, costs: List[List[int]]) -> int:
    if len(costs)==0:
        return 0

    #table = [[0]*3 for _ in range(len(costs))]

    #BaseCase
    #table[0] = costs[0]

    #RecursiveCase
    for i in range(1,len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])

    return min(costs[-1])
