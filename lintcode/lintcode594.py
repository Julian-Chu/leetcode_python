class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    def strStr2(self, source, target):
        if source is None or target is None:
            return -1
        if source == "":
            if target == "":
                return 0
            return -1

        seed = 31
        mod = 10000007

        n = len(source)
        m = len(target)
        # h = (seed**(m-1))%mod
        # h = pow(seed, m-1, mod)
        # print(h)
        h = 1
        for i in range(m - 1):
            h = (h * seed) % mod
        source_win_hash = 0
        target_hash = 0

        for i in range(m):
            source_win_hash = (source_win_hash * seed + ord(source[i])) % mod
            target_hash = (target_hash * seed + ord(target[i])) % mod

        for i in range(n - m + 1):
            if source_win_hash == target_hash:
                is_match = True
                for j in range(m):
                    if source[i + j] != target[j]:
                        is_match = False
                        break
                if is_match:
                    return i
            if i < n - m:
                source_win_hash = (source_win_hash - ord(source[i]) * h) % mod
                source_win_hash = (source_win_hash * seed + ord(source[i + m])) % mod
                source_win_hash = (source_win_hash + mod) % mod

        return -1