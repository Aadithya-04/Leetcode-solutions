class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for token in tokens:
            if token in "+-*/":
            # Pop the last two numbers from the stack
                b = stack.pop()
                a = stack.pop()
            
            # Perform the appropriate operation
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                # Perform integer division that truncates toward zero
                    stack.append(int(a / b))
            else:
            # Push the number onto the stack
                stack.append(int(token))
    
    # The final result will be the only number left in the stack
        return stack[0]
        