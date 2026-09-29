class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            
        # Step 1: Frequency map
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

    # Step 2: Buckets (index = frequency)
        bucket = [[] for _ in range(len(nums) + 1)]

    # Step 3: Fill buckets
        for num, count in freq.items():
            bucket[count].append(num)

    # Step 4: Collect top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # iterate from highest freq
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result


