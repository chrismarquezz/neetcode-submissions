class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in operands:
                stack.append(t)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if t == "+": res = num1 + num2; stack.append(res)
                if t == "-": res = -num1 + num2; stack.append(res)
                if t == "*": res = num1 * num2; stack.append(res)
                if t == "/": res = num2 / num1; stack.append(res)
        return int(stack[-1])