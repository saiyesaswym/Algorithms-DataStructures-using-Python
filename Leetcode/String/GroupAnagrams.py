"""
Sort and compare
Time complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. 
The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

"""

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hmap = collections.defaultdict(list)
    for s in strs:
        hmap[tuple(sorted(s))].append(s)

    return hmap.values()
