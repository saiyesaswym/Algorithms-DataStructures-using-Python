"""
Time complexity: O(n2)
Space complexity: O(1)
"""
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    res=[]
    for i in nums1:
        if i in nums2 and i not in res:
            res.append(i)
    return res

"""
Time complexity: O(n+m)
Space complexity: O(n+m)
"""
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return set(nums1).intersection(set(nums2))


"""
Time complexity: O(n+m)
Space complexity: O(n+m)
"""
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    s1 = set(nums1)
    s2 = set(nums2)

    return self.set_intersection(s1,s2)

def set_intersection(self, set1, set2):
    return [x for x in set1 if x in set2]
