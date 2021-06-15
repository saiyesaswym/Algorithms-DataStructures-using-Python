"""
Recursion - Standard template - Redundant approach
Build the entire tree but avoid duplicates when collecting
Time complexity: O(n! * n)
Space complexity: O(n! * n)
"""
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    result=[]

    def permHelper(arr, i):
        if i==len(arr):
            if arr not in result:
                result.append(arr[:])
            return
        else:
            for p in range(i,len(arr)):
                arr[p],arr[i] = arr[i],arr[p]
                permHelper(arr, i+1)
                arr[p],arr[i] = arr[i],arr[p]

    permHelper(nums,0)
    return result


"""
Recursion - Optimized Approach
Avoiding duplicate choices at every node
Time complexity: O(n! * n)
Space complexity: O(n! * n)
"""
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    result=[]

    def permHelper(arr, i):
        if i==len(arr):
            result.append(arr[:])
            return
        else:
            hashset=set()
            for p in range(i,len(arr)):
                if arr[p] not in hashset:
                    hashset.add(arr[p])
                    arr[p],arr[i] = arr[i],arr[p]
                    permHelper(arr, i+1)
                    arr[p],arr[i] = arr[i],arr[p]

    permHelper(nums,0)
    return result
