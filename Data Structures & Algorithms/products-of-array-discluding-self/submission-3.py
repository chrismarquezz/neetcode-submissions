class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        res = [1 for _ in range(len(nums))]
        for i in range(1, len(left)):
            left[i] = nums[i - 1] * left[i - 1]
        for i in range(len(right) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        for i in range(len(res)):
            res[i] = left[i] * right[i]
        return res