class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(combination.copy())
                return
            if curr_sum > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                combination.append(candidates[j])
                backtrack(j + 1, curr_sum + candidates[j])
                combination.pop()
        
        backtrack(0, 0)
        return res