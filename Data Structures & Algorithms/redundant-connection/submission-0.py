class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1, len(edges) + 1)}

        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node
        
        def union(node1, node2):
            n1_root = find(node1)
            n2_root = find(node2)
            if n1_root == n2_root:
                return False
            parent[n2_root] = n1_root
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        