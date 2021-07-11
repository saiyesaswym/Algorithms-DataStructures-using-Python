"""
BottomUp - Iterative approach - Tabulation
Time complexity: O(a*k) - amount * noOfCoins
Space complexity: O(a)
"""
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [math.inf]*(amount+1)

        #basecase
        table[0]=0

        #RecursiveCase
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    table[i] = min(table[i], table[i-c])
            table[i]+=1

        if math.isinf(table[amount]):
            return -1
        return table[amount]
