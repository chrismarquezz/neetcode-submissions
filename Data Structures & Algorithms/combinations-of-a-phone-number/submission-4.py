class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i, curr_string):
            if i == len(digits):
                res.append(curr_string)
                return
            for c in letters[digits[i]]:
                backtrack(i + 1, curr_string + c)
                
        backtrack(0, "")
        return res
