class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindrome = []

        def backtrack(i):
            if i == len(s):
                res.append(palindrome.copy())
            for j in range(i, len(s)):
                if not self.is_pal(s[i:j + 1]):
                    continue
                palindrome.append(s[i:j + 1])
                backtrack(j + 1)
                palindrome.pop()
                
        backtrack(0)
        return res

    def is_pal(self, sub):
        return sub == sub[::-1]