class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        g=[0]*(n+1)
        
        for i,j in trust:
            g[i]-=1
            g[j]+=1
        print(g)
        for k in range(1,len(g)):
            if g[k]==n-1:
                return k
        return -1