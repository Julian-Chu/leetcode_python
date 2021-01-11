class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        table = {}

        for n in num:
            table[n] = True

        max_length = 0
        for x in table:
            if table[x] == False:
                continue
            length = 1
            table[x] = False
            lo = x - 1
            hi = x + 1
            while lo in table and table[lo] == True:
                length += 1
                table[lo] = False
                lo = lo - 1
            while hi in table and table[hi] == True:
                length += 1
                table[hi] = False
                hi = hi + 1

            max_length = max(max_length, length)

        return max_length

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        max_len, table = 0, {num: True for num in num}

        for lo in num:
            if lo - 1 not in table:
                hi = lo + 1
                while hi in table:
                    hi += 1
                max_len = max(max_len, hi - lo)
        return max_len


"""
timeout
when 數字間差距太大
"""
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        hashset = set()
        min_val = float('inf')
        max_val = -float('inf')
        for n in num:
            hashset.add(n)
            max_val = max(max_val, n)
            min_val = min(min_val, n)

        length = 0
        max_length = 0

        for n in range(min_val, max_val + 1):
            if n in hashset:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0
        return max_length