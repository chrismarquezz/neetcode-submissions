class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_index = 0
        for i in range(len(nums)):
            if i <= maximum_index:
                maximum_index = max(maximum_index, i + nums[i])
        return maximum_index >= len(nums) - 1