class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_all = {}
        for i, string in enumerate(strs):
            count = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)  # <-- convert list to tuple here
            count_all[key] = count_all.get(key, []) + [strs[i]]

        result = []
        for key, value in count_all.items():
            result.append(value)
        return result