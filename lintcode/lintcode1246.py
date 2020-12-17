"""
timeout
"""
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def characterReplacement(self, s, k):
        if not s:
            return 0

        longest = 0
        n = len(s)

        for i in range(n):
            j = i + 1
            replace = 0
            while j < n and (replace < k or s[j] == s[i]):
                if s[j] != s[i]:
                    replace += 1
                j += 1

            longest = max(longest, j - i)

        return longest


class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """

    def characterReplacement(self, s, k):
        if not s:
            return 0

        # ABAAB => 利用 i - j-1間需要不同的ch 不能用dict記憶，可以換成 replace = 長度 - 最多重複出現的char次數
        max_freq = 0
        counter = {}
        n = len(s)
        j = 0
        longest = 0
        for i in range(n):
            while j < n and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_freq = max(max_freq, counter[s[j]])
                j += 1

            # j可能指向 (ABBACD , 2) 的D
            #                 ^
            if j - i - max_freq > k:
                longest = max(longest, j - 1 - i)
            else:
                longest = max(longest, j - i)

            counter[s[i]] -= 1
            # update max_freq
            max_freq = max(counter.values())

        return longest
