
def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []
    letters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    arr=[]
    for i in digits:
        arr.append(letters[i])
    result=[]

    def lettersHelper(arr,i,slate):
        if i==len(arr):
            result.append("".join(slate[:]))
        else:
            for j in arr[i]:
                slate.append(j)
                lettersHelper(arr,i+1,slate)
                slate.pop()

    lettersHelper(arr,0,[])
    return result
