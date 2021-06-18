

def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    result=[]
    candidates.sort()

    def subsetsHelper(arr, i, slate):
        if target==sum(slate):
            result.append(slate[:])
            return
        elif target<sum(slate) or i==len(arr):
            return
        else:
            count=1
            j=i+1
            while j<len(arr) and arr[j]==arr[i]:
                count+=1
                j+=1
            #For each choice how many copies to include (with exclusion case)
            for copies in range(0,count+1):
                for c in range(copies):
                    slate.append(arr[i])
                subsetsHelper(arr, i+count, slate)
                for c in range(copies):
                    slate.pop()

    subsetsHelper(candidates, 0, [])

    return result



def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    results = []

    def backtrack(remain, slate, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(slate[:])
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            if i==start or candidates[i]!=candidates[i-1]:
                # add the number into the combination
                slate.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], slate, i+1)
                # backtrack, remove the number from the combination
                slate.pop()

    backtrack(target, [], 0)

    return results
