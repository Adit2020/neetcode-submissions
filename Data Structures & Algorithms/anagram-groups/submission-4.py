from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for string in strs:
            key = tuple(sorted(string))
            hash[key].append(string)

        return list(hash.values())