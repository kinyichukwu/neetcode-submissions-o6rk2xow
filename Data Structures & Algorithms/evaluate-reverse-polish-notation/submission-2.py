class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
                continue

            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if t == "+":
                    result = a + b
                    stack.append(result)
                
                if t == "-":
                    result = a - b
                    stack.append(result)
                
                if t == "*":
                    result = a * b
                    stack.append(result)
                
                if t == "/":
                    result = int(a / b)
                    stack.append(result)

        return int(stack.pop())