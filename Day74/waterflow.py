from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pseen=set()
        aseen=set()
        pque=deque()
        aque=deque()

        for i in range(0,m):
            pseen.add((i,0))
            pque.append((i,0))
        for j in range(1,n):
            pseen.add((0,j))
            pque.append((0,j))

        for i in range(0,n):
            aseen.add((m-1,i))
            aque.append((m-1,i))
        for j in range(0,m):
            aseen.add((j,n-1))
            aque.append((j,n-1))
        
        def bfs(que,seen):
            coords=set()
            while que:
                i,j=que.popleft()
                coords.add((i,j))
                for i_off,j_off in [[0,1],[1,0],[0,-1],[-1,0]]:
                    r,c=i+i_off,j+j_off
                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
            return coords
        p_coords=bfs(pque,pseen)
        a_coords=bfs(aque,aseen)
        return list(p_coords & a_coords)
            

        