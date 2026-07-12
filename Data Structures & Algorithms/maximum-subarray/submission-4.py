class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            running_sum = max(running_sum + nums[i], nums[i])
            global_max = max(global_max, running_sum)
        return global_max