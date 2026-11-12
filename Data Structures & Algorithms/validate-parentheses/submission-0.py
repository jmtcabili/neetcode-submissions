class Solution:
    def isValid(self, s: str) -> bool:
        """
        Signs of valid: 
        1. same count and pair and ending on [ ( {
        2. close in correct order
            - distance between has to be even 
            
        How to check for pair
        - for each char: 
            - push to stack if opening
            - if closing variant, if not equal to head of stack not valid
        """
        starting = ['(', '{', '[']
        ending = [')', '}', ']']

        stack = [] 
        for ch in s:
            #check immediately if ch is not paired with head
            if ch in ending:
                if len(stack) == 0:
                    return False
                idx = ending.index(ch)
                if stack[-1] != starting[idx]: 
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        
        #if it reaches this point and stack is not empty, return true
        return len(stack) == 0


