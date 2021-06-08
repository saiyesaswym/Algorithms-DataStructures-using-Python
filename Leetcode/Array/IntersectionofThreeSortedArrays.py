
"""
Using Hashmap
Time complexity: O(N)
Space complexity: O(N)
N -> total length of all the three input arrays
"""
def arraysIntersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    hashmap={}
    res=[]

    for i in arr1:
        hashmap[i]=1
    for j in arr2:
        if j in hashmap:
            hashmap[j]+=1
        else:
            hashmap[j]=1
    for k in arr3:
        if k in hashmap:
            if hashmap[k]==2:
                res.append(k)
    return res


"""
Using Hashset
Time complexity: O(N)
Space complexity: O(N)
"""
def arraysIntersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    return sorted(set(arr1).intersection(set(arr2).intersection(set(arr3))))
