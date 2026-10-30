from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for string in strs:
            freq = [0] * 26

            for char in string:
                freq[ord(char) - ord('a')] += 1

            key = tuple(freq)
            hash[key].append(string)

        return list(hash.values())