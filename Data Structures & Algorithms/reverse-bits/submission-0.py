class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            shift = n & 1
            new_slot = shift << 31 - i
            res = res | new_slot
            n >>= 1
        return res