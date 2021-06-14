"""
Recursion approach - General template
Time Complexity - O(2^n * n)
Space Complexity - O(2^n)
"""
class Solution:
    def __init__(self):
        self.result=[]

    def letterCasePermutation(self, s: str) -> List[str]:
        self.lettercaseHelper(s,0,[])
        return self.result

    def lettercaseHelper(self, s, i, slate):
        #base case
        if i==len(s):
            self.result.append("".join(slate))
            return self.result
        #recursive case
        else:
            if s[i].isdigit():
                slate.append(s[i])
                self.lettercaseHelper(s,i+1,slate)
                slate.pop()
            else:
                slate.append(s[i].lower())
                self.lettercaseHelper(s,i+1,slate)
                slate.pop()
                slate.append(s[i].upper())
                self.lettercaseHelper(s,i+1,slate)
                slate.pop()
