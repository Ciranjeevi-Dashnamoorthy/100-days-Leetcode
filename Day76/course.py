class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        visit=[0]*numCourses

        def dfs(node):
            if visit[node]==1:
                return False  
            if visit[node]==2:
                return True
            visit[node]=1         
            for cur in graph[node]:
                if not dfs(cur):
                    return False
            visit[node]=2
                 
            return True
        for i in range(numCourses):
            # if visit[i]==0:
             if not dfs(i):
                return False
        return True
        