class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            if c not in counts:
                return False
            counts[c] -= 1
            if counts[c] == 0:
                del counts[c]
        return len(counts) == 0 
        