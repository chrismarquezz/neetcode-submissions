class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        accumulator = 0
        for n in nums:
            accumulator ^= n
        return accumulator