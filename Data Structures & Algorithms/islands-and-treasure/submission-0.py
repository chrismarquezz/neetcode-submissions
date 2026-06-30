class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        while queue:
            row, column = queue.popleft()
            for delta_row, delta_column in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                neighbor_row, neighbor_column = row + delta_row, column + delta_column
                if neighbor_row < 0 or neighbor_row >= len(grid) or neighbor_column < 0 or neighbor_column >= len(grid[0]):
                    continue
                if grid[neighbor_row][neighbor_column] != 2147483647:
                    continue
                grid[neighbor_row][neighbor_column] = grid[row][column] + 1
                queue.append((neighbor_row, neighbor_column))