
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

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
            # add the number into the combination
            slate.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], slate, i)
            # backtrack, remove the number from the combination
            slate.pop()

    backtrack(target, [], 0)

    return results



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
