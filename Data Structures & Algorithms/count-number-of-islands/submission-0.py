class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.search(grid, i, j)
                    number_of_islands += 1
        return number_of_islands

    def search(self, grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.search(grid, i, j + 1)
        self.search(grid, i + 1, j)
        self.search(grid, i - 1, j)
        self.search(grid, i, j - 1)
        