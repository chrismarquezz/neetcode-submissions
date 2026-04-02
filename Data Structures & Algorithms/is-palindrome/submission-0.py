class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""

        for i in range(len(s)):
            if s[i].isalnum():
                clean_s += s[i].lower()
        
        for i in range(len(clean_s)):
            if clean_s[i] != clean_s[len(clean_s) - 1 - i]:
                return False

        return True