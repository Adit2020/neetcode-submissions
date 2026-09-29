class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Stores indices
        result = [0] * len(temperatures)
       
        for i in range(len(temperatures)):
            # While stack is not empty and current element is GREATER than stack's top element
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped_index = stack.pop()
            # The current element nums[i] is the NEXT GREATER element for nums[popped_index]
                result[popped_index] = i - popped_index
              
            
        # If the loop finishes, the element at stack[-1] is the PREVIOUS GREATER element
            
            
            stack.append(i)  # Push current index onto the stack
        
        return result