class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
    
        for char in s:
            if char in mapping:
            # Pop the topmost element from the stack, if it's empty use a dummy value
                top_element = stack.pop() if stack else '#'
            # If the mapping for this closing bracket doesn't match the stack top
                if mapping[char] != top_element:
                    return False
            else:
            # It's an opening bracket, push onto the stack
                stack.append(char)
            
    # If the stack is empty, all brackets were matched perfectly
        return not stack