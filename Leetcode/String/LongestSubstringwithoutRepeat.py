"""
Sliding window approach 1
Time complexity: O(n2)
"""
def lengthOfLongestSubstring(s: str) -> int:
    i=0
    j=1
    maxx=0
    count=0

    while i<len(s) and j<=len(s):
        if has_duplicates(s[i:j]):
            if count>maxx:
                maxx=count
            count-=1
            i+=1
        else:
            j+=1
            count+=1
    if count>maxx:
        maxx=count
    return maxx

def has_duplicates(self, s):
    temp=set()
    for i in s:
        if i in temp:
            return True
        else:
            temp.add(i)
    return False




"""
Sliding window approach 2
"""

def lengthOfLongestSubstring2(s: str) -> int:
    charSet = set()
    l=0
    max_count=0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        max_count = max(max_count, r-l+1)

    return max_count
