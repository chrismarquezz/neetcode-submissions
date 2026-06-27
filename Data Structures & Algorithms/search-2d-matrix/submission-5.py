class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        target_row = -1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target:
                target_row = mid
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                break
        return self.binarySearch(matrix[target_row], target)

    def binarySearch(self, row, target):
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