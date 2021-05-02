"""
First approach: Join array into string and compare
Time complexity: O(n)
Space complexity: O(n)
Run time: 32ms
Faster than 58.85%
"""
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)
