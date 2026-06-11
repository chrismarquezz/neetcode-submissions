class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.calculate_time(piles, mid) <= h:
                right = mid        
            else:
                left = mid + 1
        return left
    
    def calculate_time(self, piles, speed):
        time = 0
        for p in piles:
            time += (p + speed - 1) // speed
        return time