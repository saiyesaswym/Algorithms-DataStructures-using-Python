"""
Standard Recursive approach
Time complexity: O(2^n)
Space complexity: O(1)
"""
def fib(self, n: int) -> int:
    if n==0 or n==1:
        return n
    else:
        return self.fib(n-1)+self.fib(n-2)


"""
BottomUp approach - Memoization (Dynamic programming)
Time complexity: O(n)
Space complexity: O(n)
"""
def fib(self, n: int) -> int:
    if n<=1:
        return n
    self.memo = {0:0, 1:1}
    return self.memoize(n)

def memoize(self, n):
    if n in self.memo:
        return self.memo[n]

    self.memo[n] = self.memoize(n-1) + self.memoize(n-2)

    return self.memo[n]


"""
BottomUp approach - Memoization (Dynamic programming)
Time complexity: O(n)
Space complexity: O(n)
"""
def fib(self, n: int) -> int:
    res=[]
    for i in range(0,n+1):
        if i==0 or i==1:
            res.append(i)
        else:
            res.append(res[i-1]+res[i-2])

    return res[n]


"""
Optimized Recursive approach
Time complexity: O(n)
Space complexity: O(1)
"""
def fib(self, n: int) -> int:
    return self.anyseq(n, 0, 1)

def anyseq(self, n, b1, b2):
    if n==0:
        return b1
    else:
        return self.anyseq(n-1, b2, b1+b2)
