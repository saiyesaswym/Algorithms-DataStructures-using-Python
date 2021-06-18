"""
Backtracking approach
Time complexity: O(2^n)
"""
def generateParenthesis(self, n: int) -> List[str]:
    result=['']*2*n
    final_result=[]

    def helper(arr, i, n, op, cl):
        if cl==n:
            final_result.append("".join(result))
        else:
            if op<n:
                arr[i]='('
                helper(arr, i+1, n, op+1, cl)
            if op>cl:
                arr[i]=')'
                helper(arr, i+1, n, op, cl+1)

    helper(result, 0, n, 0, 0)

    return final_result
