class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = Counter(s1)
        window = Counter(s2[:len(s1)])
        left = 0
        right = len(s1)
        while left < right and right < len(s2):
            print(window)
            if sub == window:
                return True
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]] 
            right += 1
            left += 1
        return sub == window
            
            