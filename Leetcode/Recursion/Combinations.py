"""
Time complexity - O(k * nCk)
Space complexity - O(k * nCk)
"""
def combine(self, n: int, k: int) -> List[List[int]]:
    result=[]
    def combHelper(i,slate):
        if len(slate)==k:
            result.append(slate[:])
        else:
            for j in range(i,n+1):
                slate.append(j)
                combHelper(j+1,slate)
                slate.pop()

    combHelper(1,[])
    return result
