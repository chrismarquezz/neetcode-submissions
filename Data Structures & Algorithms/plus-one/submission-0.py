class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''

        for i in range(len(digits)):
            s += str(digits[i])

        return list(str(int(s) + 1))




        