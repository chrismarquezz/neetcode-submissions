class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr_string, open_count, closed_count):
            if len(curr_string) == 2 * n:
                res.append(curr_string)
                return
            if open_count < n:
                backtrack(curr_string + "(", open_count + 1, closed_count)
            if open_count > closed_count:
                backtrack(curr_string + ")", open_count, closed_count + 1)

        res = []
        backtrack("", 0, 0)
        return res
