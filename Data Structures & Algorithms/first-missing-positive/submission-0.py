class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            val = abs(nums[i])
            if val <= len(nums):
                nums[val - 1] = -abs(nums[val - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1