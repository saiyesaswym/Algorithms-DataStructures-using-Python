"""
BottomUp - Iterative approach - Tabulationt
No. of ways he can reach nth step: f(n-1)+f(n-2) -> Fibonacci sequence
Time complexity: O(n)
Space complexity: O(n)
"""
def climbStairs(self, n: int) -> int:
    memo = {1:1,2:2}

    for i in range(3,n+1):
        memo[i]=memo[i-1]+memo[i-2]

    return memo[n]


"""
BottomUp - Iterative approach - Tabulation - Optimized approach
No. of ways he can reach nth step: f(n-1)+f(n-2) -> Fibonacci sequence
Time complexity: O(n)
Space complexity: O(1)
"""
def climbStairs(self, n: int) -> int:
    if n<=2:
        return n

    first=1
    second=2

    for i in range(3,n+1):
        third = first+second
        first = second
        second = third

    return second
