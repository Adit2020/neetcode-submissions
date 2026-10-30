class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash = {}
        result = []
        for i in range(n):
            hash[nums[i]] = i
        for i in range(n):
            diffirence = target - nums[i]
            if diffirence in hash:
                if not (hash[diffirence] == i):
                    result.append(i)
                    result.append(hash[diffirence])
                    return result