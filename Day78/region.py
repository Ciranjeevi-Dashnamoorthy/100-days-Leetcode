class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row,col):
            if row<0 or col<0 or row>=n or col>=m or board[row][col]=="X" or board[row][col]=="*":
                return False
            
            board[row][col]="*"
            p=dfs(row+1,col) or dfs(row,col+1) or dfs(row,col-1) or dfs(row-1,col)

        n,m=len(board),len(board[0])
        for i in range(0,m):
            if board[0][i]=="O":
                dfs(0,i)
            if board[n-1][i]=="O":
                dfs(n-1,i)
        for j in range(1,n-1):
            if board[j][0]=="O":
                dfs(j,0)
            if board[j][m-1]=="O":
                dfs(j,m-1)
        for i in range(n):
            for j in range(m):
                if board[i][j]!="*":
                    board[i][j]="X"
                else:
                    board[i][j]="O"
        return board

                

        