class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        chrs = {}

        for ch in str:
            chrs[ch] = chrs.get(ch, 0) + 1

        for ch in str:
            if chrs[ch] == 1:
                return ch

        return None