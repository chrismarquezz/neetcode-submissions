class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            for neighbor in adj.get(course, []):
                if not dfs(neighbor):
                    return False    
            black.add(course)
            grey.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True