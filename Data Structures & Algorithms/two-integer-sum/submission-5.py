from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maps the number value to its index
        num_to_index = {} 
        
        for i, num in enumerate(nums):
            difference = target - num
            
            # If the complement exists in our map, we found the pair
            if difference in num_to_index:
                return [num_to_index[difference], i]
            
            # Otherwise, save the current number and index for future lookups
            num_to_index[num] = i
            
        return []
