class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel=image[sr][sc]
        rows,columns=len(image),len(image[0])
        visited=set()
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=columns or image[r][c]!=pixel or (r,c) in visited:
                return False
            visited.add((r,c))
          
            image[r][c]=color
            poss=(dfs(r-1,c) or dfs(r+1,c) or dfs(r,c-1) or dfs(r,c+1))
            return 
        
        dfs(sr,sc)
        return image
        