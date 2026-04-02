class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_sum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr_sum = 0
            else:
                curr_sum += 1

                max_ones = max(max_ones, curr_sum)

        return max_ones