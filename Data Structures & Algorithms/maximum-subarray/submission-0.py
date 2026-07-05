class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        running_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i] + running_sum:
                running_sum = nums[i]
            else:
                running_sum += nums[i]
            global_max = max(global_max, running_sum)
        
        return global_max