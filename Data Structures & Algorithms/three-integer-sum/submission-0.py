class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

       
        for i in range(len(nums) - 2):
            # Skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    left_val = nums[j]
                    right_val = nums[k]

                    while j < k and left_val == nums[j]:
                        j += 1
                    while j < k and right_val == nums[k]:
                        k -= 1
        return res