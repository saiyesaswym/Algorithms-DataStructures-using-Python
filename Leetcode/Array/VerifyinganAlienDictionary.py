"""
Compare adjacent words
N be the length of order, and M be the total number of characters in words
Time complexity: O(M+N)
Space complexity: O(N)
But N=26 is fixed. So, TC: O(M) and SC: O(1) 
"""
def isAlienSorted(self, words: List[str], order: str) -> bool:
    hmap = {}
    for i,val in enumerate(order):
        hmap[val] = i

    for i in range(len(words)-1):
        for j in range(len(words[i])):
            # If we do not find a mismatch letter between words[i] and words[i + 1],
            # we need to examine the case when words are like ("apple", "app").
            if j>=len(words[i+1]):
                return False
            if words[i][j]!=words[i+1][j]:
                # If character in first word is greater than second word, not sorted
                if hmap[words[i][j]]>hmap[words[i+1][j]]:
                    return False
                # if we find the first different character and they are sorted,
                # then there's no need to check remaining letters
                break
    return True
