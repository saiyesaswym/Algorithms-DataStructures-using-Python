"""
Brute force Approach
Time complexity: O(n^3)
Space complexity: O(1)
"""
def longestPalindrome(self, s: str) -> str:
    maxx=0
    ss=''
    if len(s)==1:
        return s
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if self.is_palindrome(s[i:j]):
                if maxx<len(s[i:j]):
                    maxx=len(s[i:j])
                    ss=s[i:j]
    return ss

def is_palindrome(self,s):
    return s==s[::-1]



"""
Two Pointer Approach
Time complexity: O(n^2)
Space complexity: O(1)
"""
class Solution:
    res = ""
    lres = 0

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            #Odd length
            l,r = i,i
            self.isPalindrome(l,r,s)

            #Even length
            l,r = i,i+1
            self.isPalindrome(l,r,s)

        return self.res

    def isPalindrome(self, l, r, s):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1 > self.lres:
                self.lres = r-l+1
                self.res = s[l:r+1]
            l -= 1
            r += 1
