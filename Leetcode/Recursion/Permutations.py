"""
Recursive approach - General template
"""
class Solution:
    def __init__(self):
        self.result=[]

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.permHelper([],nums)
        return self.result

    def permHelper(self, slate, bag):
        if len(bag)==0:
            self.result.append(slate[:])
        else:
            for i in range(0,len(bag)):
                slate.append(bag[i])
                self.permHelper(slate, bag[:i]+bag[i+1:])
                slate.pop()


sol = Solution()
print(sol.permute([1,2,3]))


"""
Recursive approach - Size of subproblem is represented by index
"""
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def permHelper(arr, i, slate):
            if i==len(arr):
                result.append(slate[:])
                return
            else:
                for p in range(i,len(arr)):
                    arr[p],arr[i] = arr[i],arr[p]
                    slate.append(arr[i])
                    permHelper(arr, i+1, slate)
                    slate.pop()
                    arr[p],arr[i] = arr[i],arr[p]

        permHelper(nums,0,[])
        return result


"""
Backtracking approach
"""
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def permHelper(arr, i):
            if i==len(arr):
                result.append(arr[:])
                return
            else:
                for p in range(i,len(arr)):
                    arr[p],arr[i] = arr[i],arr[p]
                    permHelper(arr, i+1)
                    arr[p],arr[i] = arr[i],arr[p]

        permHelper(nums,0)
        return result
