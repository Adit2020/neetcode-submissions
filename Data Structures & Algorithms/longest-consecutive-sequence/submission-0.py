class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #go through the array, put the samallest into another array, and then when youy find the next smallest
        # you then check if it is only one more 
        count = set(nums)
        longest = 0
        for num in count:
            if num - 1 not in count:
                current = num
                length = 1

                while current + 1 in count:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest