class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = {"{", "(", "["}
        for c in s:
            if c in opened:
                stack.append(c)
            else:
                if stack:
                    if c == "}":
                        if stack.pop() != "{":
                            return False
                    elif c == ")":
                        if stack.pop() != "(":
                            return False
                    elif c == "]":
                        if stack.pop() != "[":
                            return False
                else:
                    return False
        return True if not stack else False