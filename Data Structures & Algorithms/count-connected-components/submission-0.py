class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        res = 0

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res
        

