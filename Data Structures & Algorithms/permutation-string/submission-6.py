class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_window = Counter(s1)
        s2_window = Counter(s2[:len(s1)])
        left = 0
        for right in range(len(s1), len(s2)):
            print(s2_window)
            print(s2[right])
            if s1_window == s2_window:
                return True
            if s2[right] in s2_window:
                s2_window[s2[right]] += 1
            else:
                s2_window[s2[right]] = 1
            s2_window[s2[left]] -= 1
            if s2_window[s2[left]] == 0:
                del s2_window[s2[left]]
            left += 1
        if s1_window == s2_window:
                return True
        return False