class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxW = 0

        while i < j:
            height_i = heights[i]
            height_j = heights[j]
            width = j - i
            height = min(height_i, height_j)
            water = width * height

            maxW = max(maxW, water)

            if height_i < height_j:
                i += 1
            else:
                j -= 1

        return maxW