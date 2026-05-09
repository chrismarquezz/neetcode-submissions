class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for _ in height]
        max_right = [0 for _ in height]
        max_from_left = 0
        max_from_right = 0
        res = 0

        for i in range(len(height) - 1):
            max_from_left = max(max_from_left, height[i])
            max_left[i + 1] = max_from_left
        
        for i in range(len(height) - 1, 0, -1):
            max_from_right = max(max_from_right, height[i])
            max_right[i - 1] = max_from_right

        for i in range(len(height)):
            res += max(0, min(max_left[i], max_right[i]) - height[i])
        
        return res

