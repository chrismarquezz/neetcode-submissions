class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        pivot = self.find_pivot(nums, target)
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            left = 0
            right = pivot - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def find_pivot(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return left