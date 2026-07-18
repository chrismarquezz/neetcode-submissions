class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        accumulator = 0
        for i in range(len(nums)):
            accumulator ^= nums[i]
        return accumulator