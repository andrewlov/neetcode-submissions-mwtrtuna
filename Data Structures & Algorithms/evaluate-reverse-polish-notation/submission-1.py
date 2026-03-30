class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    res = val1 + val2
                    stack.append(res)
                elif token == '-':
                    res = val1 - val2
                    stack.append(res)
                elif token == '*':
                    res = val1 * val2
                    stack.append(res)
                elif token == '/':
                    res = int(val1 / val2)
                    stack.append(res)
        return stack.pop()