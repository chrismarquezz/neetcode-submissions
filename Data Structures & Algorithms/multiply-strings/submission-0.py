class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0 for _ in range(len(num1) + len(num2))]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
        for k in range(len(res) - 1):
            res[k + 1] += res[k] // 10
            res[k] %= 10
        res = res[::-1]                   
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1                         
        return "".join(map(str, res[i:]))
                