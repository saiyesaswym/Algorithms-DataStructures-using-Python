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


"""
Time complexity - O(k * nCk)
Space complexity - O(k * nCk)
"""
def combine(self, n: int, k: int) -> List[List[int]]:
    result=[]
    def combHelper(arr,i,slate):
        if len(slate)==k:
            print(slate)
            result.append(slate[:])
            return

        if i==n:
            return

        combHelper(arr,i+1,slate)
        slate.append(arr[i])
        combHelper(arr,i+1,slate)
        slate.pop()

    arr=[i for i in range(1,n+1)]
    combHelper(arr,0,[])

    return result
