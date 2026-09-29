class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            diffirence = target - num
            if diffirence in numbers:
                # diffirenc ie guaranted to be the smaller index
                return [numbers[diffirence], i]
            numbers[num] = i
            
            