from collections import Counter


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = [0] * 26, [0] * 26
        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
        return dic1 == dic2

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c, d = Counter(s), Counter(t)
        if len(c - d) == 0:
            return True
        else:
            return False
