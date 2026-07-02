class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = defaultdict(list)
        grey = set()
        black = set()

        for i, j in prerequisites:
            adj[i].append(j)
        
        def dfs(course):
            if course in grey:
                return False
            if course in black:
                return True
            grey.add(course)
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            black.add(course)
            grey.remove(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res