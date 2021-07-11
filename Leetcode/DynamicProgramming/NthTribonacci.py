"""
BottomUp - Iterate approach - Tabulation - Optimzed
Time complexity: O(n)
Space complexity: O(1)
"""
def tribonacci(self, n: int) -> int:
    if n<=1:
        return n

    first=0
    second=1
    third=1

    for i in range(3,n+1):
        fourth = first+second+third
        first = second
        second = third
        third = fourth

    return third
