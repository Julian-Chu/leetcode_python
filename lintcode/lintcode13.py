"""
Rabin-Karp
log(n+m)
"""
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        if target == "":
            return 0
        if source == "":
            return -1

        seed = 31
        mod = 10000007
        n = len(source)
        m = len(target)
        if n < m:
            return -1
        base = pow(seed, m - 1, mod)
        source_win_hash = 0
        target_hash = 0
        for i in range(m):
            source_win_hash = (source_win_hash * seed + ord(source[i])) % mod
            target_hash = (target_hash * seed + ord(target[i])) % mod

        for i in range(n - m + 1):
            if source_win_hash == target_hash:
                if source[i:i + m] == target:
                    return i
            elif i + m < n:
                source_win_hash = source_win_hash - ord(source[i])*base
                source_win_hash = (source_win_hash + mod) %mod  # corner case when source_win_hash < 0
                source_win_hash = (source_win_hash * seed + ord(source[i + m])) % mod
        return -1


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if target == "":
            return 0
        if source == "":
            return -1

        target_size = len(target)
        source_size = len(source)

        for i in range(source_size - target_size):
            if source[i:i+target_size] == target:
                return i
        return -1


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        if target == "":
            return 0
        if source == "":
            return -1

        len_t = len(target)
        len_s = len(source)

        for i in range(len_s - len_t + 1):
            j = 0
            while j < len_t:
                if source[i+j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1

