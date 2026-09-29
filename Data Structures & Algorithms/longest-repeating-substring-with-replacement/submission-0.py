class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        left = 0
        freq = defaultdict(int)
        max_freq = -float('inf')
        max_window = -float('inf')

        for right, char in enumerate(s):
            freq[char] += 1
            
            max_freq = max(max_freq, freq[char])
            window_size = right - left + 1
            while right - left + 1 - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return max_window
