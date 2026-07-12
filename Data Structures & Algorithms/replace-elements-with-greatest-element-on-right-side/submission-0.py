class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        max_from_right = -1
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = max_from_right
            max_from_right = max(arr[i], max_from_right)
        return ans