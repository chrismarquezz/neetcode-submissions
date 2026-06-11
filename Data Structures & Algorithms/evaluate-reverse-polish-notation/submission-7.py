class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        res = 0
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if tokens[i] == '+':
                    res = num1 + num2
                    stack.append(res)
                elif tokens[i] == '*':
                    res = num1 * num2
                    stack.append(res)
                elif tokens[i] == '-':
                    res = -num1 + num2
                    stack.append(res)
                elif tokens[i] == '/':
                    res = num2 / num1
                    stack.append(res)
            print(stack)

        return int(stack[-1])