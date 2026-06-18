class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        potential_row = -1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target:
                potential_row = mid
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                break
        return self.search_row(matrix[potential_row], target)

    def search_row(self, row, target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False