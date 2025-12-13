from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        

        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            
        queue=deque([(0,0)])
        grid[0][0]=1
        path=1

        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                if r==n-1 and c==m-1:
                    return path
                
                for i,j in directions:
                    nr,nc=r+i,c+j
                    if 0<= nr<n and 0<=nc<m and grid[nr][nc]==0:
                        
                        grid[nr][nc]=1
                        queue.append((nr,nc))
            path+=1
        return -1
                        




        

    