class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(i, curr_string):
            if len(curr_string) == len(digits):
                res.append(curr_string)
                return
            for c in letters[digits[i]]:
                backtrack(i + 1, curr_string + c)
        res = []
        letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if not digits:
            return res
        backtrack(0, "")
        return res