class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        temp_max_right = 0
        temp_max_left = 0
        res = 0
        for i in range(len(max_left) - 1):
            temp_max_left = max(temp_max_left, height[i])
            max_left[i + 1] = temp_max_left
        for i in range(len(max_right) - 1, 0, -1):
            temp_max_right = max(temp_max_right, height[i])
            max_right[i - 1] = temp_max_right
        for i in range(len(height)):
            res += max(0, min(max_left[i], max_right[i]) - height[i])
        return res