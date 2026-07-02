class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        if len(edges) == n - 1:
            dfs(0)
            
        return len(visited) == n