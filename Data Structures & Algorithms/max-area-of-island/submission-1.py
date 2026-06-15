class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    curr_area = self.search(grid, i, j)
                    max_area = max(max_area, curr_area)
        return max_area
    
    def search(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.search(grid, i + 1, j) + self.search(grid, i, j + 1) + self.search(grid, i - 1, j) + self.search(grid, i, j - 1)
