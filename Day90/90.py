class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        grid=[[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1: 
                break
            grid[i][0]=1
      
        for j in range(n):
            if obstacleGrid[0][j]==1: 
                break
            grid[0][j]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    grid[i][j]+=grid[i-1][j]+grid[i][j-1]
        print(grid)
        return grid[m-1][n-1]


        