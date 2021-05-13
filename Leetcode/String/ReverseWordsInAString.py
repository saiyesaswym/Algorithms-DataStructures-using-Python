"""
First approach:
Split the string into list of words and Join them in reverse order
Runtime: 32ms
Time complexity: O(n)
"""
def reverseWords(s: str) -> str:
    lis = s.split()
    return ' '.join(lis[::-1])
