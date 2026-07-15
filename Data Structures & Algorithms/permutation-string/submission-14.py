class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        left = 0
        for i in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0: del s2_count[s2[left]]
            left += 1
        if s1_count == s2_count:
            return True
        return False