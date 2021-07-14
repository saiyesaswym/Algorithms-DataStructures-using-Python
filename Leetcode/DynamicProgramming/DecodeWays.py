"""
BottomUp iterative approach - Tabulation
f(n) = f(n-1) (if digit is not 0) + f(n-2) (if first digit is 1-2 and second digit is 0-6)
Time complexity: O(n) -> n - length of the string
Space complexity: O(n)
"""
class Solution:
    def numDecodings(self, s: str) -> int:

        table = [0 for _ in range(len(s)+1)]

        if s[0]=="0":
            return 0

        table[0]=1
        table[1]=1

        for i in range(2,len(s)+1):
            if s[i-1] != "0":
                table[i] += table[i-1]
            if s[i-2] == "1" or (s[i-2] == "2" and s[i-1] in ["0","1","2","3","4","5","6"]):
                table[i] += table[i-2]

        return table[len(s)]
