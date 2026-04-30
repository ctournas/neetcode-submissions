class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators: 
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    total = (num1) + num2
                elif token == '-':
                    total = num2 - num1
                elif token == '/':
                    total = int(num2 / num1)
                else:
                    total = num1 * num2
                stack.append(total)
            else:
                stack.append(int(token))
        return stack[-1]
        