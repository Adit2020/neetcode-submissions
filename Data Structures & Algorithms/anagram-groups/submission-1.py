from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        freq = []
        m = len(strs)
        for i in range(m):
            freq = defaultdict(int)
            n = len(strs[i])
            string = strs[i]
            for j in range(n):
                freq[string[j]] += 1
            key = tuple(sorted(freq.items()))
            hash[key].append(string)
        return list(hash.values())
