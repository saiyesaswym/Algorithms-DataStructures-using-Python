"""
Given a rope, cut it into parts maximizing the product of their lengths.

Example
Input: 4
Output: 4

Length of the rope is 4.

All ways it can be cut into parts: 1+3, 1+1+2, 1+1+1+1, 2+2, 2+1+1.

Among these, 2+2 cut makes for the greatest product: 2*2=4.
"""

"""
BottomUp - Iterative approach - Tabulation
f(n) = max(f(cut)*f(n-cut))
Time complexity: O(n^2)
Space complexity: O(n)
"""

def max_product_from_cut_pieces(n):
    if n<2:
        return 0

    if n==2:
        return 1

    if n==3:
        return 2

    table = [0 for _ in range(n+1)]

    table[0]=0
    table[1]=1
    table[2]=2
    table[3]=3

    for i in range(4,n+1):
        maxx=0
        for j in range(1,(n//2)+1):
            maxx = max(maxx, table[j]*table[i-j])
        table[i] = maxx

    return table[n]
