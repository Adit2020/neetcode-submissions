class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {"+", "-", "*", "/"}
        stack = []
    
        for token in tokens:
            if token not in oper:
                stack.append(int(token))
            else:
            # Pop the two most recent operands
                b = stack.pop()
                a = stack.pop()
            
            # Perform the operation
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                # Use int() to truncate toward zero
                    stack.append(int(float(a) / b))
                
        return stack[0]