class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        char = list(s)
        if len(char) == 0:
            return 0

        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(char)):
            freq[char[right]] += 1

            while freq[char[right]] > 1:
                freq[char[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len