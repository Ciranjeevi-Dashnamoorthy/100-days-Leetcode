class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import defaultdict
        g=defaultdict(list)
        for i in range(len(rooms)):
            for j in rooms[i]:
                g[i].append(j)
        visited=set()
        
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for i in g[node]:
                if i not in visited:
                    dfs(i)
               
        dfs(0)
        return len(visited)==len(rooms)
        