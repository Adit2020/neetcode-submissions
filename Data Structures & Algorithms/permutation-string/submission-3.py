class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # sliding window question. where I would use defaultdict to count the frequency of characters
        s1_list = defaultdict(int)
        for i in range(len(s1)):
            s1_list[s1[i]] += 1
        # now do a sliding window across s2
        left = 0
        s2_list = defaultdict(int)
        for right in range(len(s2)):
            s2_list[s2[right]] += 1
            if right - left + 1 > len(s1):
                s2_list[s2[left]] -= 1
                if s2_list[s2[left]] == 0:
                    del s2_list[s2[left]]
                left += 1
            if right - left + 1 == len(s1):
                if s2_list == s1_list:
                    return True
            
            
        return False
            

