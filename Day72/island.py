class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,columns=len(grid),len(grid[0])   
        ct=0
        def dfs(r,c):
            if r>=rows or c>=columns or r<0 or c<0 or grid[r][c]=='0':
                return False
            
            if grid[r][c]=="1":
                 grid[r][c]="0"
            poss=(dfs(r-1,c) or dfs(r+1,c) or dfs(r,c-1) or dfs(r,c+1))
            
            return poss
                                
        for row in range(rows):
                for col in range(columns):
                    if grid[row][col]=="1":
                        dfs(row,col)
                        ct+=1

        
        return ct