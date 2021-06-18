def solveNQueens(self, n: int) -> List[List[str]]:
    final_result=[]

    def nqueensHelper(n,i,slate):
        if i==n:
            sol=[]
            result=[]
            for i in range(n):
                sol.append(['.']*n)
            for i,j in enumerate(slate):
                sol[i][j]='Q'
                result.append(''.join(sol[i]))
            final_result.append(result)
            return
        for j in range(n):
            if hasnoconflict(slate,j):
                slate.append(j)
                nqueensHelper(n,i+1,slate)
                slate.pop()

    def hasnoconflict(slate,col):
        for row in range(len(slate)):
            if slate[row]==col:
                return False
            rowdiff = abs(len(slate) - row)
            coldiff = abs(col - slate[row])
            if rowdiff == coldiff:
                return False
        return True

    nqueensHelper(n,0,[])

    return final_result
