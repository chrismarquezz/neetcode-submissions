class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        curr_sum = 0

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(combination.copy())
                return
            if curr_sum > target:
                return
            for j in range(i, len(nums)):
                combination.append(nums[j])
                backtrack(j, curr_sum + nums[j])
                combination.pop()
        
        backtrack(0, curr_sum)
        return res