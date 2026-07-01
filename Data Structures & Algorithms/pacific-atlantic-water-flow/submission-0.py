class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_visited = set()
        a_visited = set()

        

        def dfs(i, j, visited, prev_height):
            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[i]):
                return
            if heights[i][j] < prev_height:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
        
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if i == 0 or j == 0:
                    dfs(i, j, p_visited, heights[i][j])
                if i == len(heights) - 1 or j == len(heights[i]) - 1:
                    dfs(i, j, a_visited, heights[i][j])

        return [[i, j] for (i, j) in p_visited & a_visited]