class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        target_row = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target:
                target_row = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.search(matrix[target_row], target) if target_row != float('inf') else False

    def search(self, row, target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        return False