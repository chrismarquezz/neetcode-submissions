class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.find_pivot(nums)        
        if nums[pivot] <= target <= nums[n - 1]:
            left, right = pivot, n - 1            
        else:
            left, right = 0, pivot - 1           
        while left <= right:                    
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left= mid + 1
            else:
                right= mid - 1
        return -1

    def find_pivot(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return left