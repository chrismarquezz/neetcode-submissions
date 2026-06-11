class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        max_mid = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target >= matrix[mid][0]:
                max_mid = mid
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                break
                
        return self.searchRow(matrix[max_mid], target)

    def searchRow(self, row, target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False