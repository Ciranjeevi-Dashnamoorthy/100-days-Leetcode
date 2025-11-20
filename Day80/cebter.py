class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g=collections.defaultdict(int)
        for i,j in edges:
            g[i]+=1
            g[j]+=1
        for k in g:
            if g[k]==len(edges):
                return k
        

        