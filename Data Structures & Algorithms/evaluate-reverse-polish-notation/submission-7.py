class Solution:

    """
        1 2 3 4 + -

        

    """

    def solve(self, val1, val2, operator): 
        match operator:
            case '+':
                return val1 + val2
            case '-':
                return val1 - val2
            case '*':
                return val1 * val2
            case '/':
                return int(val1 / val2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        operators = ['+', '-', '*', '/']
        result = 0
        for token in tokens:
            #if operator, pop two numbers and apply operation
            if token in operators:
                val2 = stack.pop()
                val1 = stack.pop()

                res = self.solve(val1, val2, token)

                #update stack with resulting value
                stack.append(res)
            #if not operator
            else: 
                val = int(token)
                stack.append(val)
        return stack.pop()
