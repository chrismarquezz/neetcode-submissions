class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        boundary = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == boundary:
                jumps += 1
                boundary = farthest
        
        return jumps