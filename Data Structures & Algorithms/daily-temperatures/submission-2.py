class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            result = []
            for i in range(len(temperatures)) :
                curr_temp = temperatures[i]
                counter = 0
                found = False
                j = i + 1
                while j < len(temperatures) and not found:
                    if curr_temp < temperatures[j]:
                        found = True
                    counter += 1
                    j+=1
                if found:
                    result.append(counter)
                else: 
                    result.append(0)
            return result
        """
        result = [0] * len(temperatures)
        stack = [] #[temp, idx]; your running stack to store numbers waiting for a warmer day

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #while stack has contents and curr temp is greater than head
                #get head entry from stack
                stackT, stackInd = stack.pop()
                #find distance between indices and store in res
                result[stackInd] = i - stackInd
            #if there's no stack or current is not greater than stack; add the curr along the stack
            stack.append((t,i))
        return result

        
        