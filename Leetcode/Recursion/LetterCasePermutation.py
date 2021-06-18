"""
Recursion approach - General template
Time Complexity - O(2^n * n)
Space Complexity - O(2^n * n)
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

"""
Recursion approach - Optimized version
Use input string as list - No need of Slate
Time Complexity - O(2^n * n)
Space Complexity - O(2^n * n)
"""
class Solution:
    def __init__(self):
        self.result=[]

    def letterCasePermutation(self, s: str) -> List[str]:
        self.lettercaseHelper(list(s),0)
        return self.result

    def lettercaseHelper(self, s, i):
        #base case
        if i==len(s):
            self.result.append("".join(s))
            return self.result
        #recursive case
        else:
            if s[i].isdigit():
                self.lettercaseHelper(s,i+1)
            else:
                s[i] = s[i].lower()
                self.lettercaseHelper(s,i+1)
                s[i] = s[i].upper()
                self.lettercaseHelper(s,i+1)
