class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == "+":
                    temp = a + b
                    stack.append(temp)
                elif tokens[i] == "*":
                    temp = a * b
                    stack.append(temp)
                elif tokens[i] == "-":
                    temp = a - b
                    stack.append(temp)
                else:
                    temp = int(a / b)
                    stack.append(temp)

        return stack.pop()
                    

                
            