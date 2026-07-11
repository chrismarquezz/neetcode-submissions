class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                box_num = (i // 3) * 3 + (j // 3)
                if num != ".":
                    if num in rows[i] or num in cols[j] or num in boxes[box_num]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_num].add(num)
        return True