"""
Time Complexity: O(n)
"""
def lengthOfLastWord(self, s: str) -> int:
    return 0 if not s or s.isspace() else len(s.split()[-1])
