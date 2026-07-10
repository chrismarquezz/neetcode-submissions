class Solution:
    def isHappy(self, n: int) -> bool:
        running_total = 0
        seen = set()
        while True:
            running_total = 0

            while n > 0:
                last_digit = n % 10
                n = n // 10
                running_total += last_digit ** 2
            if running_total in seen:
                return False
            if running_total == 1:
                return True
            seen.add(running_total)
            n = running_total