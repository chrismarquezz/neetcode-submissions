class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right                          
        while left <= right:
            mid = left + (right - left) // 2
            if self.calculate_time(piles, mid) <= h:
                answer = mid                    
                right = mid - 1                
            else:
                left = mid + 1
        return answer   
    
    def calculate_time(self, piles, speed):
        time = 0
        for p in piles:
            time += (p + speed - 1) // speed
        return time