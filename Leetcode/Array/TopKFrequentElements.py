"""
Hashmap and one pass
Time complexity: O(nlogn)
Space complexity O(n+k)
"""
def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashmap={}
    for i in arr:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    res=[]
    for i in sorted(hashmap,key=hashmap.get,reverse=True):
        res.append(i)
        if len(res)==k:
            break
    return res



"""
Using Heap
Time complexity: O(nlogk)
Space complexity O(n+k)
"""
def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashmap={}
    for i in arr:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    return heapq.nlargest(k, hashmap.keys(), key=hashmap.get)
