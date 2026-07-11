class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col_has_zero = False
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_col_has_zero = True
        for r in range(len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for cell in range(len(matrix[0])):
                matrix[0][cell] = 0
        if first_col_has_zero:
            for cell in range(len(matrix)):
                matrix[cell][0] = 0
