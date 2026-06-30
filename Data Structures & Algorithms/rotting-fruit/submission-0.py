class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for delta_r, delta_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    n_r, n_c = r + delta_r, c + delta_c
                    if n_r < 0 or n_r >= len(grid) or n_c < 0 or n_c >= len(grid[0]):
                        continue
                    if grid[n_r][n_c] != 1:
                        continue
                    grid[n_r][n_c] = 2
                    fresh -= 1
                    queue.append((n_r, n_c))
            if queue:
                time += 1
        return time if fresh == 0 else -1