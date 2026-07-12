class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        accumulator = 0
        for n in nums:
            accumulator ^= n
        for n in range(len(nums) + 1):
            accumulator ^= n
        return accumulator