class Solution:
    def validTree(self, n: int, edges: List[List[int]]) :
        graph=[[] for _ in range(n)]
        for i ,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        
        def dfs(node,par):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited or nei==par:
                    
                    dfs(nei,node)
                else:
                    return False
            return True

        
        return dfs(0,-1) and len(edges)<n and len(visited)==n
        

        