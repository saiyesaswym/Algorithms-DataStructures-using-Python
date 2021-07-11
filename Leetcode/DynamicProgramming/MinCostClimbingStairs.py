"""
BottomUp - Iterative approach - Tabulation
No. of ways he can reach nth step: f(n-1)+f(n-2) -> Fibonacci sequence
Time complexity: O(n)
Space complexity: O(n)
"""
def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)
    table = [-1]*(n+2)

    table[0]=0
    table[1]=cost[0]

    cost.append(0)

    for i in range(2,n+2):
        table[i] = min(table[i-1], table[i-2]) + cost[i-1]

    return table[n+1]
