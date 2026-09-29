class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxW = 0
    
        while i < j:
            h_left = heights[i]
            h_right = heights[j]
        
            # Calculate current area
            height = h_left if h_left < h_right else h_right
            water = (j - i) * height
            if water > maxW:
                maxW = water
            
        # Optimization: Skip heights that are shorter than the current boundaries
            if h_left < h_right:
                while i < j and heights[i] <= h_left:
                    i += 1
            else:
                while i < j and heights[j] <= h_right:
                    j -= 1
                
        return maxW