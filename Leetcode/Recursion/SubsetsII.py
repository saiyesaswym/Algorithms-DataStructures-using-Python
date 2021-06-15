"""

"""
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    result=[]
    nums.sort()

    def subsetsHelper(arr, i, slate):
        if i==len(arr):
            result.append(slate[:])
            return
        else:
            count=1
            j=i+1
            while j<len(arr) and arr[j]==arr[i]:
                count+=1
                j+=1
            #For each choice how many copies to include (with exclusion case)
            for copies in range(0,count+1):
                #Add those copies to our partial solution
                for c in range(copies):
                    slate.append(arr[i])
                subsetsHelper(arr, i+count, slate)
                for c in range(copies):
                    slate.pop()

    subsetsHelper(nums, 0, [])

    return result
