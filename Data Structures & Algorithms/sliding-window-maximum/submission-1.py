class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        right = k
        while left < right and right <= len(nums):
            window = nums[left:right]
            res.append(max(window))
            left += 1
            right += 1
        return res