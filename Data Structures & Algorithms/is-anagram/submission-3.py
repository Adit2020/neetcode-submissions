from collections import defaultdict    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        n = len(s)
        m = len(t)
        for i in range(n):
            freq_s[s[i]] += 1
        for i in range(m):
            freq_t[t[i]] += 1
        return freq_s == freq_t