class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return
            if board[i][j] == "O":
                board[i][j] = "S"
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == len(board) - 1:
                    dfs(i, j)
                if j == 0 or j == len(board[i]) - 1:
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
                