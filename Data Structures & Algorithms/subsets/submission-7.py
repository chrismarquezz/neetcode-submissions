class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        
        res = []
        subset = []
        backtrack(0)
        return res