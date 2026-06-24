class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_window = Counter(s1)
        s2_window = Counter(s2[:len(s1)])
        print(s2_window)
        left = 0
        for right in range(len(s1), len(s2)):
            if s1_window == s2_window:
                return True
            s2_window[s2[right]] = s2_window.get(s2[right], 0) + 1
            s2_window[s2[left]] -= 1
            if s2_window[s2[left]] == 0: del s2_window[s2[left]]
            left += 1
        if s1_window == s2_window:
                return True
        return False