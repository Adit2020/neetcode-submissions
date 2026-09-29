class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        result = []
        for key in islice(sorted_dict, k):
            result.append(key)
        return result

