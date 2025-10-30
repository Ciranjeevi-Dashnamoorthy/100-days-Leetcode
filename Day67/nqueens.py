class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."] * n for _ in range(n)]
        res=[]
        cols=set()
        posdiag=set()
        negdiag=set()
        def backtrack(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or row+col in posdiag or row-col in negdiag:
                    continue
                board[row][col]="Q"
                cols.add(col) 
                posdiag.add(row+col)
                negdiag.add(row-col)

                backtrack(row+1)

                board[row][col]="."
                cols.remove(col) 
                posdiag.remove(row+col)
                negdiag.remove(row-col)


        backtrack(0)
        return res
        