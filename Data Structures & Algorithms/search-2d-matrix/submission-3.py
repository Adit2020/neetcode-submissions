class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the avg of every row. and do a binary search on that
        # agter you find the value using binary search. go search taht index array
        
        # perform binary search
        left = 0
        right = len(matrix) - 1

        while left < right:
            mid = left + (right - left) // 2

            if matrix[mid][-1] >= target:
                right = mid
            else:
                left = mid + 1

        row = left
        left = 0
        right = len(matrix[row]) - 1
        main_arr = matrix[row]
        while left < right:
            mid = left + (right - left) // 2

            if main_arr[mid] >= target:
                right = mid
            else:
                left = mid + 1 

        return main_arr[left] == target