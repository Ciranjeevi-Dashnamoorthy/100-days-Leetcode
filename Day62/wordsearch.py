class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=columns or word[i]!=board[r][c]:
                return False
            temp=board[r][c]
            board[r][c]="0"

            found=(dfs(r-1,c,i+1) or
            dfs(r+1,c,i+1) or
            dfs(r,c-1,i+1) or 
            dfs(r,c+1,i+1))

            board[r][c]=temp
            return found

        rows,columns=len(board),len(board[0])

        for r in range(rows):
            for c in range(columns):
                if board[r][c]==word[0] and dfs(r,c,0):
                    return True
        return False

        