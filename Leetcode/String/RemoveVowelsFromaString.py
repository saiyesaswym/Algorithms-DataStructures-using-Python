"""
First approach: Brute force approach
Looping through the string and finding for vowels
Time complexity: O(n) ("in" operator for SET takes O(1))
Run time: 28ms
Faster than 78.99%
"""
def removeVowels(s: str) -> str:
    vowels = {'a','e','i','o','u'}
    ans=[]
    for i in s:
        if i not in vowels:
            ans.append(i)
    return ''.join(ans)

s = "leetcodeisacommunityforcoders"
print(removeVowels(s))
