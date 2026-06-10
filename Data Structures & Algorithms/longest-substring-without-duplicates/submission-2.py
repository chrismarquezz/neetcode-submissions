class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest_len = 0
        left = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[i])
            longest_len = max(longest_len, i - left + 1)
        return longest_len